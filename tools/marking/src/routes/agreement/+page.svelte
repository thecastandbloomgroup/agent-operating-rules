<script>
	// @ts-check
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';

	/** @type {{ data: import('./$types').PageData }} */
	let { data } = $props();

	// The Bloom calibration used 0.667 as the floor for a trusted labeller.
	const FLOOR = 0.667;

	/** @param {number | null} k */
	function show(k) {
		return k === null ? 'n/a' : k.toFixed(2);
	}
</script>

<main class="mx-auto flex max-w-3xl flex-col gap-6 p-4 sm:p-8">
	<header class="flex flex-col gap-2">
		<h1 class="text-2xl font-semibold tracking-tight">How the judges compare with your marks</h1>
		<p class="text-sm text-muted-foreground">
			Each row compares one judge with your {data.n} marks on one question. Kappa corrects the agreement
			for chance. A kappa of {FLOOR} or more is the floor for trusting that judge on that question.
		</p>
	</header>

	<Card.Root>
		<Card.Content class="overflow-x-auto">
			<table class="w-full text-sm">
				<thead class="text-left text-muted-foreground">
					<tr>
						<th class="py-2 pr-4 font-medium">Judge</th>
						<th class="py-2 pr-4 font-medium">Question</th>
						<th class="py-2 pr-4 font-medium">Agree</th>
						<th class="py-2 font-medium">Kappa</th>
					</tr>
				</thead>
				<tbody>
					{#each data.rows as row (row.judge + row.column)}
						<tr class="border-t">
							<td class="py-2 pr-4">{row.judge}</td>
							<td class="py-2 pr-4">{row.column}</td>
							<td class="py-2 pr-4">{row.agree} of {row.n}</td>
							<td class="py-2">
								<Badge variant={row.kappa !== null && row.kappa >= FLOOR ? 'default' : 'outline'}>
									{show(row.kappa)}
								</Badge>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</Card.Content>
	</Card.Root>

	<p class="text-sm text-muted-foreground">
		The marks are saved in sheet.csv. Tell Claude the sheet is done, and it will write the judge-trust
		note from these numbers.
	</p>
	<div><Button variant="outline" href="/">Back to the marks</Button></div>
</main>
