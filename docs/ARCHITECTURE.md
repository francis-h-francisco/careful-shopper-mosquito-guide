# Architecture Notes

## Current proof of concept

The first static implementation is committed:

- `index.html` — Pages entry page.
- `playground.html` — iframe shell that loads the official Playground JavaScript client.
- `blueprint.json` — creates a named WordPress site and a published “Playground Import Check” page through a Blueprint `runPHP` step.
- `.github/workflows/pages.yml` — deploys the repository root to GitHub Pages on pushes to `main`.

**Code is committed, but the GitHub Pages deployment and real-browser runtime/import are not yet verified.**

## Runtime model

The shell imports the Playground client from `https://playground.wordpress.net/client/index.js` and connects to `https://playground.wordpress.net/remote.html`. WordPress processing happens in the visitor's browser through WebAssembly. GitHub Pages only serves static files; it does not run a conventional PHP application server or shared MySQL database.

Each visitor's browser runs its own Playground instance. Visitors do not share a live database, and one visitor's edits are not automatically visible to another. Treat the preview as a disposable review demo unless a persistence/export design is separately proven. Do not include private data.

The official embed is experimental and may change. Dependence on the public Playground service also introduces availability and third-party-runtime risk.

## Must be tested

1. Pages deployment succeeds and HTTPS URL is reachable.
2. First-time visitor can start Playground without a local server.
3. Blueprint loads and the generated “Playground Import Check” page appears.
4. Clean-browser reload repeats the setup successfully.
5. A second browser/device can repeat startup.
6. Browser storage, export and restoration behavior are understood before relying on persistence.
7. Theme/plugin loading and final media paths work if used in the finished guide.

## Performance and browser support

Playground loads WebAssembly assets and may take longer on mobile or slower networks. The official hosting guide notes larger initial downloads, browser differences and higher mobile memory use. Test at desktop and phone widths; do not promise instant startup or universal mobile performance.

## Release and cache behavior

A stable Pages URL can serve later releases, but browser and intermediary caches may temporarily show older files. No universal forced-refresh guarantee is possible.

Use a visible build identifier, versioned asset names, suitable cache headers where supported, and avoid a service worker unless its update lifecycle is implemented and tested. Check the public URL in a private window, after hard refresh, and on mobile.

## Fallback

The user authorizes conventional shared WordPress hosting if Pages + Playground proves unsuitable. Test the current route first. If fallback is required, verify current hosting limits, PHP/database support, HTTPS, import size, plugin/theme compatibility, persistence, public access and performance before committing to it.

## Acceptance

Do not claim a working Playground-on-Pages site until a first-time visitor can start it from HTTPS without a local server, prepared content loads, a clean browser can repeat startup, isolation is documented, responsive/accessibility checks pass, and a later release can be verified at the same URL.

If this route proves unreliable, use the authorized conventional WordPress-hosting fallback and document the technical reason.