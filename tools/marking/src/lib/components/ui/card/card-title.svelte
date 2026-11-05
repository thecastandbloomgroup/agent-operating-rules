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
	data-slot="card-title"
	class={cn("text-base leading-snug font-medium group-data-[size=sm]/card:text-sm", className)}
	{...restProps}
>
	{@render children?.()}
</div>