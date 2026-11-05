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
## 2026-11-06 — Public guide and Playground separation

index.html is now the nine-zone public static guide served by GitHub Pages. User reports this URL is live: https://francis-h-francisco.github.io/careful-shopper-mosquito-guide/

GitHub Pages serves static HTML/CSS/JS. The public guide does not rely on a shared WordPress database.

playground.html loads the official Playground client and blueprint.json. The current Blueprint creates a disposable “Playground Import Check” page. Playground is browser-side and isolated per visitor; it is not a shared PHP/MySQL server. Startup/import and clean-browser repeatability remain unverified.

The static guide is the public reader experience. Playground is a separate technical sandbox for testing WordPress authoring/import behavior. Do not describe the site as WordPress-powered until runtime and full guide import are validated.

The guide follows the supplied nine-zone sequence and Style Sheet, uses the supplied mosquito-bite image, excludes the flea photo, and uses text-only product-window placeholders. Zone 7 links currently lead to Amazon category searches, explicitly marked as test destinations; they are not confirmed individual listings or affiliate tracking. Zone 8 uses the five source-provided example links.

Acceptance: user browser checks at desktop and 22.5rem mobile, keyboard/200% zoom/accessibility, Playground startup/import, verified Zone 7 individual product destinations and authorized footer/nav URLs.

## 2026-11-06 — Twenty Twenty-Five child-theme direction

The Blueprint now installs the WordPress.org `twentytwentyfive` theme and activates a Careful Shopper child theme. The child theme keeps the guide-specific templates and imports the source guide content; its stylesheet translates the supplied MHTML's ivory/forest-green/gold palette, 1120px editorial width, rounded panels and muted text into the current nine-zone layout.

The Blueprint disables automatic login (`login: false`). This removes the previous automatic admin-login step from the intended visitor flow. It does not make the Playground service a shared WordPress host: every visitor still receives an isolated browser instance. The Pages launcher and raw Blueprint URL have been updated in source, but runtime startup, theme installation, front-page rendering, CORS, clean-session repeatability and visitor-facing admin visibility remain unverified until real-browser testing.
