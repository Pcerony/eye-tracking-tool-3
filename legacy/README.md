# Legacy Files

`ppt/index.html` is the pre-migration rollback baseline. It is not a source for
new edits and must not be published as the current deck.

`legacy/unsafe-write-scripts/` contains historical scripts that rewrite large
parts of the deck using brittle string replacement. They are retained only for
forensics. Do not run them, import them from tests, or move them back under
`test/` or `scratch/`.

The supported path is: edit modular sources, run validation, run `npm run
build`, and review `dist/index.html`.

`legacy/unreferenced-assets/` contains inactive visual files retained for
forensics. They are not build inputs and may not be reintroduced without a
manifest entry and an explicit use case.
