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

<p
	bind:this={ref}
	data-slot="card-description"
	class={cn("text-muted-foreground text-sm", className)}
	{...restProps}
>
	{@render children?.()}
</p>