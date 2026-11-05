# Marking app

A local web page for the blind marking of judged actions. It shows one action at a time, takes two Yes or No answers, and saves each answer to the sheet at once. The judges' answers stay hidden until every row has both marks.

Run it from the repository root:

```sh
task marking
```

Then open <http://localhost:5173>. The task writes `items.json` from the sheet first. Next it runs `task marking-check`, then it starts the app.

The check clicks the page in headless Chrome against a blank copy of the sheet. Then it reads the copy back from disk. It fails unless each answer reaches the file, so a page that only looks saved never reaches a person. Set `CHROME` to the Chrome binary when it is not in `/Applications`.

The stack is Svelte 5 with runes, SvelteKit 2, Tailwind CSS 4, and shadcn-svelte, with JSDoc types. `pnpm run check` type-checks the app, and `pnpm test` runs its server tests.
