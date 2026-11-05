# WordPress Playground proof of concept

## Purpose

The Pages site keeps the fast static guide available and provides a separate link to a browser-based WordPress preview. The preview is prepared from a public Blueprint hosted in this repository.

## Current implementation

- `index.html` — public nine-zone guide, with a link to the WordPress preview.
- `playground.html` — short launch page explaining the isolated preview.
- `blueprint.json` — installs the WordPress.org Twenty Twenty-Five theme, writes a Careful Shopper child theme and imports the guide as the front page.
- The child theme keeps the supplied editorial content and adapts its visual system from the MHTML reference: ivory canvas, forest-green hero, gold accent, muted green-grey text, fine borders and rounded editorial panels.

The Blueprint sets `login: false`; it does not automatically log a visitor into the WordPress administrator account. The intended visitor path is the front-end preview, not an editing session.

## Runtime model and limitations

WordPress Playground runs in the visitor's browser through WebAssembly. GitHub Pages serves static files only; it is not a conventional PHP/MySQL host. Each visitor receives an isolated WordPress instance. Changes are not shared with other visitors and do not update the public Pages guide.

The Playground remote runtime is experimental and may change. The public service does not guarantee availability at every traffic level. This is a review/demo route, not a shared production WordPress site.

## Acceptance test — still required

1. Open the Pages URL in a fresh private/incognito browser window.
2. Open **WordPress preview** and wait for Playground startup.
3. Confirm the site opens on the mosquito guide, not a generic sample page.
4. Confirm Twenty Twenty-Five is the parent theme and Careful Shopper child theme is active.
5. Confirm no automatic WordPress admin login occurs.
6. Reload in a clean session and repeat.
7. Repeat on a second browser or device if possible.
8. Record browser/device, startup time, errors, page appearance and whether the guide is the front page.

Do not mark the route validated until these observations are confirmed in a real browser. If the runtime, Blueprint import or repeat startup fails, document the failure and assess the already-authorized conventional WordPress-hosting fallback.

## Blueprint hosting requirement

The Blueprint URL is a public raw GitHub URL. It must remain publicly readable and allow cross-origin requests. The launcher uses the official Playground query parameter to load it. If the repository or branch changes, update the launcher URL too.

## Source basis

The MHTML file was parsed as a multipart archive and its complete HTML/CSS parts were extracted. It was not independently browser-rendered in this work. The theme translates the supplied palette and layout direction; it does not copy the WordPress.com toolbar, navigation or unrelated page chrome.
