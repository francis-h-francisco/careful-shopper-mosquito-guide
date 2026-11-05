# Architecture Notes

## Current implementation

- `index.html` — minimal public entry page.
- `playground.html` — minimal WordPress preview entry.
- `blueprint.json` — installs Twenty Twenty-Five, writes/activates the Careful Shopper child theme, enqueues `menu.js`, and imports the bicycle-security guide as the front page.
- `.github/workflows/pages.yml` — deploys the repository root to GitHub Pages on pushes to `main`.

## Runtime model

GitHub Pages serves static files only. WordPress Playground runs in each visitor's browser through WebAssembly. Each visitor has an isolated instance; changes are not shared and do not update the public launcher. The official Playground client is experimental.

## Child theme behavior

The child theme loads after Twenty Twenty-Five. Its `menu.js` script is enqueued in the footer. The script toggles the mobile navigation's `open` class, updates `aria-expanded`, closes after a navigation link is selected, and closes on Escape.

Desktop navigation is a single non-wrapping flex row. Below 60rem it is replaced by the Menu button. Product cards use three columns on wide screens and one column below 48rem; layer cards stack below 40rem. The comparison table is the only horizontally scrollable element.

## Media

The bicycle hero photo is an external Pexels image. Its runtime loading and remote availability are not yet verified. Product windows are intentionally placeholders; no manufacturer product photos are downloaded.

## Acceptance

Do not claim the preview is working until a first-time visitor can start Playground from HTTPS, the Blueprint imports the page, the child theme is active, the photo loads, the mobile menu works, responsive layout and keyboard checks pass, and a clean session can repeat startup.
