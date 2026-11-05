<script>
	import { cn } from "$lib/utils.js";
	/** @type {import('svelte/elements').HTMLAttributes<HTMLDivElement> & { ref?: HTMLElement | null, children?: import('svelte').Snippet }} */
	let {
		ref = $bindable(null),
		class: className,
		children,
		...restProps
	} = $props();
</script>

<div
	bind:this={ref}
	data-slot="card-action"
	class={cn(
		"col-start-2 row-span-2 row-start-1 self-start justify-self-end",
		className
	)}
	{...restProps}
>
	{@render children?.()}
</div>