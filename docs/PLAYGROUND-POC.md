# WordPress Playground Preview

## Overview

GitHub Pages serves the project entry page and the WordPress Playground launcher. The nine-zone guide is created inside WordPress from the public `blueprint.json` file.

## Files

- `index.html` — project entry page.
- `playground.html` — launch page for the browser-based WordPress preview.
- `blueprint.json` — installs WordPress.org Twenty Twenty-Five, writes and activates the Careful Shopper child theme, and imports the guide as the front page.
- Child theme files in the Blueprint — stylesheet, theme setup and responsive navigation script.

## Runtime model

WordPress Playground runs in each visitor's browser through WebAssembly. GitHub Pages serves static files only; it does not run a conventional PHP/MySQL WordPress server. Each visitor receives an isolated WordPress instance. Visitor edits and database changes are not shared with other visitors.

The preview is for review and demonstration, not a shared production WordPress site. The remote Playground runtime is experimental and may change.

The Blueprint disables automatic administrator login. The intended visitor path is the public front-end guide.

## Acceptance checks

Do not describe the preview as validated until all of the following have been observed in a real browser:

1. Open the HTTPS Pages URL in a clean private/incognito browser session.
2. Launch WordPress Playground and wait for startup.
3. Confirm the guide loads as the WordPress front page.
4. Confirm Twenty Twenty-Five is the parent theme and the Careful Shopper child theme is active.
5. Confirm the guide image loads and the responsive navigation works.
6. Repeat startup/import in a fresh session and, if available, a second browser or device.
7. Test desktop and 22.5rem phone widths, keyboard navigation, visible focus, Escape-to-close, 200% zoom and page-level overflow.
8. Confirm only the comparison table scrolls horizontally.
9. Record browser/device, startup result, errors and screenshot evidence.

If startup, import or repeatability fails, document the specific failure and assess the authorized conventional WordPress-hosting fallback.

## Source and asset boundary

The supplied Mosquito Blog and Careful Shopper Style Sheet control content and design. The MHTML is a visual reference only where compatible with those documents. The current Zone 4 image still needs replacement with the specifically permitted source image; see `docs/BUILD-CHECKLIST.md`.

Product links are demonstration destinations. They are not confirmed affiliate-tracked links or verified current listings. Unprovided navigation/footer destinations remain unresolved rather than being invented.
