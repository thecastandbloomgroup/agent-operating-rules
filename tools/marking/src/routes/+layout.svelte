<script>
	// @ts-check
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	/** @type {{ children: import('svelte').Snippet }} */
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Blind marking</title>
</svelte:head>

{@render children()}
