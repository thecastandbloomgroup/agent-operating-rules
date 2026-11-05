// @ts-check
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile, readFile, mkdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { parse, stringify } from '../src/lib/server/csv.js';
import { HEADER, agreement, complete, kappa, loadSheet, marksOf, saveMarks } from '../src/lib/server/marking.js';

test('csv round trip keeps commas, quotes, and line breaks', () => {
	const rows = [{ a: 'x, "y"', b: 'line\nbreak' }];
	assert.deepEqual(parse(stringify(rows, ['a', 'b'])), rows);
});

test('csv reads the quoted note field that Python writes', () => {
	const text = 'executor,note\r\nm,"says ""Clear"", then stops"\r\n';
	assert.deepEqual(parse(text), [{ executor: 'm', note: 'says "Clear", then stops' }]);
});

async function sheetDir() {
	const dir = await mkdtemp(path.join(tmpdir(), 'marking-'));
	const rows = [
		{ run: 'r', file: 'responses/m/A-s1.md', action: '1' },
		{ run: 'r', file: 'responses/m/A-s2.md', action: '2' }
	];
	await writeFile(path.join(dir, 'sheet.csv'), stringify(rows, HEADER));
	return dir;
}

test('saveMarks writes one row and keeps the others', async () => {
	const dir = await sheetDir();
	await saveMarks(1, { domain: 'True', reason: 'False', note: 'a, b' }, dir);
	const marks = marksOf(await loadSheet(dir));
	assert.deepEqual(marks[1], { domain: 'True', reason: 'False', note: 'a, b' });
	assert.deepEqual(marks[0], { domain: '', reason: '', note: '' });
	assert.equal(complete(marks), false);
});

test('saveMarks refuses a value that is not True or False, and a missing row', async () => {
	const dir = await sheetDir();
	await saveMarks(0, { domain: 'maybe', reason: 'True', note: '' }, dir);
	assert.equal(marksOf(await loadSheet(dir))[0].domain, '');
	await assert.rejects(saveMarks(9, { domain: 'True', reason: 'True', note: '' }, dir), RangeError);
});

test('kappa is 1 for full agreement and 0 for chance agreement', () => {
	assert.equal(kappa(['True', 'False'], ['True', 'False']), 1);
	assert.equal(kappa(['True', 'True', 'False', 'False'], ['True', 'False', 'True', 'False']), 0);
});

test('agreement matches judge rows by file and action', async () => {
	const results = await mkdtemp(path.join(tmpdir(), 'results-'));
	await mkdir(path.join(results, 'r'));
	const head = 'file,action,domain_right,reason_cause_effect\n';
	await writeFile(path.join(results, 'r', 'action-checks.csv'), head + 'f.md,1,True,False\n');
	await writeFile(path.join(results, 'r', 'action-checks-argon.csv'), head + 'f.md,1,False,False\n');
	const sheet = [{ run: 'r', file: 'f.md', action: '1', domain_right_human: 'True', reason_cause_effect_human: 'False' }];
	const rows = await agreement(sheet, results);
	const first = rows.find((r) => r.judge === 'First judge' && r.column === 'Domain right');
	const second = rows.find((r) => r.judge === 'Second judge' && r.column === 'Domain right');
	assert.deepEqual([first?.agree, second?.agree], [1, 0]);
});
