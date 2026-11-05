# WordPress Playground proof of concept

## Purpose

This first implementation tests a GitHub Pages-hosted static shell that starts WordPress Playground in an iframe and loads a prepared Blueprint. It is a technical spike, not the finished nine-zone guide.

## Files

- `index.html` — project entry page.
- `playground.html` — browser-side Playground client and status reporting.
- `blueprint.json` — reproducible setup steps and a generated “Playground Import Check” page.
- `.github/workflows/pages.yml` — deploys the repository root to GitHub Pages after pushes to `main`.

## Runtime model and limitations

The static page imports the official Playground client from `https://playground.wordpress.net/client/index.js` and connects to `https://playground.wordpress.net/remote.html`. WordPress processing runs in the visitor's browser through WebAssembly. This is not a PHP/MySQL server hosted by GitHub Pages. Each visitor has an isolated instance and local browser storage; visitor edits are not shared.

The official Playground embed is documented as experimental and may change. The public Playground service is maintained for community use and does not guarantee availability for every traffic level. The first clean-browser run is therefore a required acceptance test.

## Acceptance test

1. Open the Pages URL in a fresh private/incognito browser window.
2. Wait for the Playground status to report that it is ready.
3. Confirm the WordPress frame displays the page titled **Playground Import Check**.
4. Reload the page and confirm startup repeats without manual local-server setup.
5. Repeat on a second browser or device if possible.
6. Record startup time, browser/device, any errors, and whether the generated page appears.

Do not mark the Playground route validated until the user confirms these browser observations. If the remote service, import or repeat startup fails, inspect the failure and decide whether to self-host the Playground static assets or use the authorized conventional WordPress-hosting fallback.

## Source basis

The implementation follows the official WordPress Playground embed/client example and Blueprint documentation. See:

- https://github.com/WordPress/wordpress-playground
- https://wordpress.github.io/wordpress-playground/developers/build-your-first-app/
- https://wordpress.github.io/wordpress-playground/blueprints/steps/
- https://developer.wordpress.org/playground/handbook/guides/import-content-with-blueprints/
- https://developer.wordpress.org/playground/developers/architecture/host-your-own-playground/

Last updated: 2026-11-06.