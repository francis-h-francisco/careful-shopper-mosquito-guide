# Architecture Notes

## Intended proof of concept
First experiment with GitHub Pages as static hosting and a browser-based WordPress Playground runtime loaded from those files. Prove first-time HTTPS startup, prepared-content import and clean-browser repeatability before building the full page.

Pages does not run a conventional WordPress PHP application server or shared MySQL database. This is not ordinary shared WordPress hosting.

## Visitor model
Each visitor's browser runs its own Playground instance. Visitors do not share a live database, and one visitor's edits are not automatically visible to another. Treat the preview as a disposable review demo unless a persistence/export design is separately proven. Do not include private data.

## Must be tested
The exact runtime, startup configuration, import/blueprint flow, persistence, theme/plugin loading, media paths and browser support are unverified. First build a minimal proof of concept and repeat it in a clean browser. Inspect exports rather than assuming their contents.

## Release and cache behavior
A stable Pages URL can serve a later deployment, but browser and intermediary caches may temporarily show older files. No universal forced-refresh guarantee is possible.

Use a visible build identifier, versioned asset names, suitable cache headers where supported, and avoid a service worker unless its update lifecycle is implemented and tested. Check the public URL in a private window, after hard refresh, and on mobile.

## Fallback
The user authorizes InfinityFree/conventional shared WordPress hosting if Pages + Playground proves unsuitable. Test the Playground route first; do not switch prematurely. If fallback is required, verify current hosting limits, PHP/database support, HTTPS, import size, plugin/theme compatibility, persistence, public access and performance before committing to it.

## Acceptance
Do not claim a working Playground-on-Pages site until a first-time visitor can start it from HTTPS without a local server, prepared content loads, a clean browser can repeat startup, isolation is documented, responsive/accessibility checks pass, and a later release can be verified at the same URL.

If this route proves unreliable, use the authorized InfinityFree fallback and document the technical reason.