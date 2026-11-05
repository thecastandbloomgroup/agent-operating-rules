// @ts-check
import { fail } from '@sveltejs/kit';
import { complete, loadItems, loadSheet, marksOf, saveMarks } from '$lib/server/marking.js';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const [items, sheet] = await Promise.all([loadItems(), loadSheet()]);
	const marks = marksOf(sheet);
	// No judge result leaves the server here, so the marking stays blind.
	return { items, marks, complete: complete(marks) };
}

/** @type {import('./$types').Actions} */
export const actions = {
	save: async ({ request }) => {
		const form = await request.formData();
		const index = Number(form.get('index'));
		try {
			await saveMarks(index, {
				domain: form.get('domain'),
				reason: form.get('reason'),
				note: form.get('note')
			});
		} catch (error) {
			return fail(400, { message: error instanceof Error ? error.message : String(error) });
		}
		// Read the row back from the file, so the page can check what it holds.
		const marks = marksOf(await loadSheet())[index];
		return { saved: index, marks };
	}
};
