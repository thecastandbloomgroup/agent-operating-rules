// @ts-check
// A small CSV reader and writer for the sheet and the judge files. It handles
// quoted fields with commas, quotes, and line breaks, as Python's csv module writes them.

/**
 * @param {string} text
 * @returns {Record<string, string>[]}
 */
export function parse(text) {
	/** @type {string[][]} */
	const rows = [];
	/** @type {string[]} */
	let row = [];
	let field = '';
	let quoted = false;
	for (let i = 0; i < text.length; i++) {
		const c = text[i];
		if (quoted) {
			if (c === '"' && text[i + 1] === '"') {
				field += '"';
				i++;
			} else if (c === '"') {
				quoted = false;
			} else {
				field += c;
			}
		} else if (c === '"') {
			quoted = true;
		} else if (c === ',') {
			row.push(field);
			field = '';
		} else if (c === '\n' || c === '\r') {
			if (c === '\r' && text[i + 1] === '\n') i++;
			row.push(field);
			rows.push(row);
			row = [];
			field = '';
		} else {
			field += c;
		}
	}
	if (field !== '' || row.length) {
		row.push(field);
		rows.push(row);
	}
	const [header = [], ...body] = rows.filter((r) => r.length > 1 || r[0] !== '');
	return body.map((r) => Object.fromEntries(header.map((h, j) => [h, r[j] ?? ''])));
}

/** @param {string} value */
function quote(value) {
	return /[",\r\n]/.test(value) ? `"${value.replaceAll('"', '""')}"` : value;
}

/**
 * @param {Record<string, string>[]} rows
 * @param {string[]} header
 * @returns {string}
 */
export function stringify(rows, header) {
	const lines = [header.map(quote).join(',')];
	for (const row of rows) lines.push(header.map((h) => quote(row[h] ?? '')).join(','));
	return lines.join('\n') + '\n';
}
