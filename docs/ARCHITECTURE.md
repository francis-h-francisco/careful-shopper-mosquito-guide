# Architecture Notes

## Intended proof of concept
GitHub Pages serves static files. The experiment is to load a browser-based WordPress Playground runtime from those files and initialize a prepared site.

Pages does not run a conventional PHP application server or shared MySQL database. This is not ordinary shared WordPress hosting.

## Visitor model
Each visitor's browser runs its own Playground instance. Visitors do not share a live database, and one visitor's edits are not automatically visible to another. Treat the preview as a disposable review demo unless a persistence/export design is separately proven. Do not include private data.

## Must be tested
The exact runtime, startup configuration, import/blueprint flow, persistence, theme/plugin loading, media paths and browser support are unverified. First build a minimal proof of concept and repeat it in a clean browser. Inspect exports rather than assuming their contents.

## Release and cache behavior
A stable Pages URL can serve a later deployment, but browser and intermediary caches may temporarily show older files. No universal forced-refresh guarantee is possible.

Use a visible build identifier, versioned asset names, suitable cache headers where supported, and avoid a service worker unless its update lifecycle is implemented and tested. Check the public URL in a private window, after hard refresh, and on mobile.

## Acceptance
Do not claim a working Playground-on-Pages site until a first-time visitor can start it from HTTPS without a local server, prepared content loads, a clean browser can repeat startup, isolation is documented, responsive/accessibility checks pass, and a later release can be verified at the same URL.

If this route proves unreliable, use Pages for a static HTML review or conventional WordPress hosting for a shared site.
