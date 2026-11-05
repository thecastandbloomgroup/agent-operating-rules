// @ts-check
import { readFile, writeFile, rename } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { parse, stringify } from './csv.js';

/**
 * @typedef {object} Item
 * @property {string} run
 * @property {string} file
 * @property {number} action
 * @property {string} prompt_id
 * @property {string} prompt
 * @property {string} label
 * @property {string} action_text
 * @property {string} end
 */

/**
 * @typedef {'True' | 'False' | ''} Mark
 * @typedef {{ domain: Mark, reason: Mark, note: string }} Marks
 */

export const HEADER = [
	'run',
	'file',
	'action',
	'domain_right_human',
	'reason_cause_effect_human',
	'note'
];

/** The repository root. The app runs from tools/marking, two folders down. */
export const ROOT = process.env.MARKING_REPO ?? path.resolve(process.cwd(), '../..');
export const RESULTS = path.join(ROOT, 'tests/evaluation/results');
export const SHEET_DIR = path.join(RESULTS, process.env.MARKING_SHEET ?? '2026-11-05-human-marking');

/** @returns {Promise<Item[]>} */
export async function loadItems(dir = SHEET_DIR) {
	return JSON.parse(await readFile(path.join(dir, 'items.json'), 'utf8'));
}

/** @returns {Promise<Record<string, string>[]>} */
export async function loadSheet(dir = SHEET_DIR) {
	return parse(await readFile(path.join(dir, 'sheet.csv'), 'utf8'));
}

/**
 * The marks of each row, in sheet order.
 * @param {Record<string, string>[]} rows
 * @returns {Marks[]}
 */
export function marksOf(rows) {
	return rows.map((r) => ({
		domain: /** @type {Mark} */ (r.domain_right_human ?? ''),
		reason: /** @type {Mark} */ (r.reason_cause_effect_human ?? ''),
		note: r.note ?? ''
	}));
}

/** @param {unknown} value @returns {Mark} */
function asMark(value) {
	return value === 'True' || value === 'False' ? value : '';
}

/**
 * Write the marks of one row. The write goes to a temporary file first, so a
 * crash never leaves a half-written sheet.
 * @param {number} index
 * @param {{ domain: unknown, reason: unknown, note: unknown }} marks
 */
export async function saveMarks(index, marks, dir = SHEET_DIR) {
	const rows = await loadSheet(dir);
	if (!Number.isInteger(index) || index < 0 || index >= rows.length) {
		throw new RangeError(`no row ${index}`);
	}
	rows[index].domain_right_human = asMark(marks.domain);
	rows[index].reason_cause_effect_human = asMark(marks.reason);
	rows[index].note = String(marks.note ?? '').slice(0, 2000);
	const target = path.join(dir, 'sheet.csv');
	await writeFile(`${target}.tmp`, stringify(rows, HEADER));
	await rename(`${target}.tmp`, target);
}

/** @param {Marks[]} marks */
export function complete(marks) {
	return marks.length > 0 && marks.every((m) => m.domain && m.reason);
}

/**
 * Cohen's kappa for two lists of 'True' and 'False' marks.
 * @param {string[]} a
 * @param {string[]} b
 */
export function kappa(a, b) {
	const n = a.length;
	if (!n) return null;
	const agree = a.filter((x, i) => x === b[i]).length / n;
	const pa = a.filter((x) => x === 'True').length / n;
	const pb = b.filter((x) => x === 'True').length / n;
	const chance = pa * pb + (1 - pa) * (1 - pb);
	return chance === 1 ? null : (agree - chance) / (1 - chance);
}

/**
 * @typedef {object} Agreement
 * @property {string} judge
 * @property {string} column
 * @property {number} agree
 * @property {number} n
 * @property {number | null} kappa
 */

/**
 * The agreement of each judge file with the human marks, per column.
 * @param {Record<string, string>[]} sheet
 * @returns {Promise<Agreement[]>}
 */
export async function agreement(sheet, results = RESULTS) {
	const judges = [
		{ name: 'First judge', file: 'action-checks.csv' },
		{ name: 'Second judge', file: 'action-checks-argon.csv' }
	];
	const columns = [
		{ name: 'Domain right', human: 'domain_right_human', judge: 'domain_right' },
		{ name: 'Reason states cause and effect', human: 'reason_cause_effect_human', judge: 'reason_cause_effect' }
	];
	/** @type {Map<string, Map<string, Record<string, string>>>} */
	const cache = new Map();
	/** @param {string} run @param {string} file */
	async function judgeRows(run, file) {
		const key = `${run}/${file}`;
		if (!cache.has(key)) {
			const p = path.join(results, run, file);
			const rows = existsSync(p) ? parse(await readFile(p, 'utf8')) : [];
			cache.set(key, new Map(rows.map((r) => [`${r.file}#${r.action}`, r])));
		}
		return /** @type {Map<string, Record<string, string>>} */ (cache.get(key));
	}
	/** @type {Agreement[]} */
	const out = [];
	for (const judge of judges) {
		for (const column of columns) {
			/** @type {string[]} */ const human = [];
			/** @type {string[]} */ const model = [];
			for (const row of sheet) {
				const found = (await judgeRows(row.run, judge.file)).get(`${row.file}#${row.action}`);
				if (!found || !row[column.human]) continue;
				human.push(row[column.human]);
				model.push(found[column.judge]);
			}
			out.push({
				judge: judge.name,
				column: column.name,
				agree: human.filter((x, i) => x === model[i]).length,
				n: human.length,
				kappa: kappa(human, model)
			});
		}
	}
	return out;
}
