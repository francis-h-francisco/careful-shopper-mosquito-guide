# WordPress Playground proof of concept

## Purpose

The Pages site is a minimal entry page to a prepared WordPress preview. The preview uses a public Blueprint in this repository.

## Current implementation

- Twenty Twenty-Five parent theme.
- Careful Shopper child theme.
- Bicycle-security guide imported as the front page.
- Mobile navigation behavior loaded from the child theme's `menu.js`.
- Pexels bicycle-chain photo in Zone 4; product windows remain text placeholders.

## Runtime model and limitations

WordPress Playground runs in the visitor's browser through WebAssembly. GitHub Pages serves static files only. Each visitor gets an isolated instance; edits are not shared. The public Playground client is experimental.

## Acceptance test

1. Open the Pages URL in a clean browser.
2. Open WordPress preview.
3. Confirm the bicycle-security guide is the front page.
4. Confirm Twenty Twenty-Five parent and Careful Shopper child theme.
5. Confirm the hero image loads.
6. Test desktop nav and mobile Menu button.
7. Confirm cards and layer strip follow responsive breakpoints.
8. Repeat in a clean session and another browser/device if possible.

Do not mark the route validated until these observations are made in a real browser. If Playground startup/import is unreliable, document the failure and assess the already-authorized conventional WordPress-hosting fallback.
