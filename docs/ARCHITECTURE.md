# Architecture

## Public entry and preview

- `index.html` — GitHub Pages project entry page.
- `playground.html` — launcher for the official WordPress Playground client.
- `blueprint.json` — installs Twenty Twenty-Five, writes and activates the Careful Shopper child theme, and imports the nine-zone guide as the WordPress front page.
- `.github/workflows/pages.yml` — deploys the repository root to GitHub Pages on pushes to `main`.

The entry page is not the nine-zone guide itself. The guide is imported into the visitor's WordPress Playground instance from the Blueprint.

## Runtime model

GitHub Pages serves static files; it does not provide a conventional PHP application server or shared MySQL database. WordPress Playground runs through WebAssembly in each visitor's browser. Each visitor has an isolated instance; visitor edits are not shared with other visitors.

The preview is a demonstration/review route, not a shared production WordPress site. The public Playground service is experimental and may change.

## Theme and interaction

The Blueprint installs WordPress.org Twenty Twenty-Five and activates the Careful Shopper child theme. The child theme supplies the guide layout and stylesheet. Its menu script supports open/close, close-on-link, outside-click close and Escape with focus return.

The source layout defines three product cards per desktop row, two only at intermediate widths and one per row below 40rem. Layer cards stack below 40rem. The comparison table is the only intended horizontal scroller.

## Acceptance requirements

The source build alone does not prove deployment or runtime success. Before release, verify:

1. GitHub Pages deployment and HTTPS reachability.
2. First-time Playground startup and Blueprint import.
3. Correct guide front page and active child theme.
4. Repeat startup in a clean session and a second browser/device where possible.
5. Image rendering, responsive layout, navigation behavior and all destinations.
6. Keyboard access, visible focus, 200% zoom and no page-level horizontal overflow.
7. Final screenshot evidence.

See `docs/BUILD-CHECKLIST.md` for the current pass/fail list.

## Fallback

Conventional shared WordPress hosting is an authorized fallback if Pages + Playground proves unsuitable. Do not switch until the current route has been tested and the reason for failure is recorded.
