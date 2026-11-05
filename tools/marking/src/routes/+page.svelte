<script>
	// @ts-check
	import { untrack } from 'svelte';
	import { enhance } from '$app/forms';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { Progress } from '$lib/components/ui/progress/index.js';
	import { Textarea } from '$lib/components/ui/textarea/index.js';
	import { Separator } from '$lib/components/ui/separator/index.js';

	/** @type {{ data: import('./$types').PageData }} */
	let { data } = $props();

	/** @typedef {import('$lib/server/marking.js').Mark} Mark */

	// The page keeps its own copy of the marks; each change saves one row.
	let marks = $state(untrack(() => data.marks.map((m) => ({ ...m }))));
	let index = $state(
		untrack(() => Math.max(0, data.marks.findIndex((m) => !m.domain || !m.reason)))
	);
	let status = $state('');
	/** @type {HTMLFormElement | undefined} */
	let form = $state();

	let item = $derived(data.items[index]);
	let mark = $derived(marks[index]);
	let done = $derived(marks.filter((m) => m.domain && m.reason).length);
	let complete = $derived(done === marks.length);

	const DOMAINS = [
		['Clear', 'Cause and effect are known to everyone. A best practice exists. One step.'],
		['Complicated', 'Cause and effect are knowable with analysis or expertise. The action names the analysis.'],
		['Complex', 'Cause and effect are visible only afterward. The action is a small, safe-to-fail probe.'],
		['Chaotic', 'No cause and effect are visible. The action stabilises first.'],
		['Confused', 'The domain cannot be told. The action gathers what is needed to classify.']
	];

	/** @param {'domain' | 'reason'} field @param {Mark} value */
	function choose(field, value) {
		marks[index][field] = marks[index][field] === value ? '' : value;
		save();
	}

	function save() {
		status = 'Saving';
		form?.requestSubmit();
	}

	/** @param {number} to */
	function go(to) {
		index = Math.min(data.items.length - 1, Math.max(0, to));
	}

	function next() {
		const later = marks.findIndex((m, i) => i > index && (!m.domain || !m.reason));
		go(later === -1 ? index + 1 : later);
	}

	/** @param {KeyboardEvent} event */
	function onkeydown(event) {
		if (event.target instanceof HTMLTextAreaElement) return;
		const keys = /** @type {Record<string, () => void>} */ ({
			'1': () => choose('domain', 'True'),
			'2': () => choose('domain', 'False'),
			'3': () => choose('reason', 'True'),
			'4': () => choose('reason', 'False'),
			ArrowRight: () => go(index + 1),
			ArrowLeft: () => go(index - 1),
			Enter: next
		});
		const run = keys[event.key];
		if (run) {
			event.preventDefault();
			run();
		}
	}
</script>

<svelte:window {onkeydown} />

<main class="mx-auto flex max-w-5xl flex-col gap-6 p-4 sm:p-8">
	<header class="flex flex-col gap-3">
		<div class="flex flex-wrap items-baseline justify-between gap-2">
			<h1 class="text-2xl font-semibold tracking-tight">Blind marking</h1>
			<p class="text-sm text-muted-foreground">{done} of {marks.length} marked · {status}</p>
		</div>
		<Progress value={done} max={marks.length} />
		<p class="text-sm text-muted-foreground">
			Read one action of a model's answer. Answer two questions about it. The judges' answers stay
			hidden until all {marks.length} are marked.
		</p>
		<nav class="flex flex-wrap gap-1.5" aria-label="Rows">
			{#each marks as m, i (i)}
				<button
					type="button"
					onclick={() => go(i)}
					aria-current={i === index ? 'true' : undefined}
					class="size-8 rounded-md border text-xs font-medium transition-colors
						{i === index ? 'border-foreground ring-2 ring-ring/50' : 'border-border'}
						{m.domain && m.reason ? 'bg-primary text-primary-foreground' : m.domain || m.reason ? 'bg-muted' : 'bg-background'}"
				>
					{i + 1}
				</button>
			{/each}
		</nav>
	</header>

	<div class="grid gap-6 lg:grid-cols-[1fr_18rem]">
		<Card.Root>
			<Card.Header>
				<Card.Title>Row {index + 1}: action {item.action} of prompt {item.prompt_id}</Card.Title>
				<Card.Description class="break-all">{item.run} / {item.file}</Card.Description>
			</Card.Header>
			<Card.Content class="flex flex-col gap-5">
				<details class="rounded-lg border p-3 text-sm">
					<summary class="cursor-pointer font-medium">The prompt the model answered</summary>
					<p class="mt-2 whitespace-pre-wrap text-muted-foreground">{item.prompt}</p>
				</details>

				<section class="flex flex-col gap-2">
					<div class="flex items-center gap-2">
						<h2 class="text-sm font-medium">The action</h2>
						{#if item.label}<Badge variant="secondary">labelled {item.label}</Badge>{/if}
					</div>
					<pre
						class="max-h-96 overflow-auto rounded-lg bg-muted p-4 text-sm leading-relaxed whitespace-pre-wrap">{item.action_text}</pre>
				</section>

				<details class="rounded-lg border p-3 text-sm">
					<summary class="cursor-pointer font-medium">The whole End section, for context</summary>
					<pre class="mt-2 max-h-96 overflow-auto text-xs whitespace-pre-wrap text-muted-foreground">{item.end}</pre>
				</details>

				<Separator />

				<form
					bind:this={form}
					method="POST"
					action="?/save"
					class="flex flex-col gap-5"
					use:enhance={() => {
						return async ({ result }) => {
							status = result.type === 'success' ? 'Saved' : 'Not saved, try again';
						};
					}}
				>
					<input type="hidden" name="index" value={index} />
					<input type="hidden" name="domain" value={mark.domain} />
					<input type="hidden" name="reason" value={mark.reason} />

					<fieldset class="flex flex-col gap-2">
						<legend class="mb-1 font-medium">1. Does the Cynefin label fit the work of this action?</legend>
						<div class="flex gap-2">
							<Button
								type="button"
								variant={mark.domain === 'True' ? 'default' : 'outline'}
								aria-pressed={mark.domain === 'True'}
								onclick={() => choose('domain', 'True')}>Yes <kbd class="opacity-60">1</kbd></Button
							>
							<Button
								type="button"
								variant={mark.domain === 'False' ? 'default' : 'outline'}
								aria-pressed={mark.domain === 'False'}
								onclick={() => choose('domain', 'False')}>No <kbd class="opacity-60">2</kbd></Button
							>
						</div>
					</fieldset>

					<fieldset class="flex flex-col gap-2">
						<legend class="mb-1 font-medium">
							2. Does the reason say how cause and effect relate, that is, what it takes to know the effect?
						</legend>
						<div class="flex gap-2">
							<Button
								type="button"
								variant={mark.reason === 'True' ? 'default' : 'outline'}
								aria-pressed={mark.reason === 'True'}
								onclick={() => choose('reason', 'True')}>Yes <kbd class="opacity-60">3</kbd></Button
							>
							<Button
								type="button"
								variant={mark.reason === 'False' ? 'default' : 'outline'}
								aria-pressed={mark.reason === 'False'}
								onclick={() => choose('reason', 'False')}>No <kbd class="opacity-60">4</kbd></Button
							>
						</div>
					</fieldset>

					<label class="flex flex-col gap-2">
						<span class="text-sm font-medium">Note, if a judge would miss something (optional)</span>
						<Textarea name="note" bind:value={marks[index].note} onblur={save} rows={2} />
					</label>
				</form>
			</Card.Content>
			<Card.Footer class="flex justify-between gap-2">
				<Button variant="outline" onclick={() => go(index - 1)} disabled={index === 0}>Back</Button>
				{#if complete}
					<Button href="/agreement">See how the judges compare</Button>
				{:else}
					<Button onclick={next}>Next unmarked <kbd class="opacity-60">Enter</kbd></Button>
				{/if}
			</Card.Footer>
		</Card.Root>

		<aside class="flex flex-col gap-4 text-sm">
			<Card.Root>
				<Card.Header><Card.Title class="text-base">The five domains</Card.Title></Card.Header>
				<Card.Content class="flex flex-col gap-3">
					{#each DOMAINS as [name, text] (name)}
						<div>
							<p class="font-medium">{name}</p>
							<p class="text-muted-foreground">{text}</p>
						</div>
					{/each}
				</Card.Content>
			</Card.Root>
			<p class="text-muted-foreground">
				Keys: 1 and 2 answer question 1, 3 and 4 answer question 2, arrows move, Enter jumps to the next
				unmarked row. Each answer saves at once.
			</p>
		</aside>
	</div>
</main>
