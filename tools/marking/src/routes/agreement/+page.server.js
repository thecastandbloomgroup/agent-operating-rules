// @ts-check
import { redirect } from '@sveltejs/kit';
import { agreement, complete, loadSheet, marksOf } from '$lib/server/marking.js';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const sheet = await loadSheet();
	// The judges stay hidden until every row has both marks.
	if (!complete(marksOf(sheet))) redirect(303, '/');
	return { rows: await agreement(sheet), n: sheet.length };
}
