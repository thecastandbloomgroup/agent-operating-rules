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
	data-slot="card-footer"
	class={cn("bg-muted/50 rounded-b-xl border-t p-(--card-spacing) flex items-center", className)}
	{...restProps}
>
	{@render children?.()}
</div>