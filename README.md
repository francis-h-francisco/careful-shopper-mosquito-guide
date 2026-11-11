# Careful Shopper — Mosquito Protection Guide

A nine-zone educational guide about mosquito barriers and the products that complement them.

**Version chooser:** [Open the landing page](https://francis-h-francisco.github.io/careful-shopper-mosquito-guide/)

## Available design versions

- **Version 1 — Strict:** [Open in WordPress Playground](https://playground.wordpress.net/?blueprint-url=https%3A%2F%2Fraw.githubusercontent.com%2Ffrancis-h-francisco%2Fcareful-shopper-mosquito-guide%2Fmain%2Fblueprint-v1-strict.json). Follows the Careful Shopper Style Sheet value by value: Verdana only, the listed colors only, rem sizes, nine zones in order, "See Example" buttons, the exact disclosure above every group of product links.
- **Version 2 — Creative:** [Open in WordPress Playground](https://playground.wordpress.net/?blueprint-url=https%3A%2F%2Fraw.githubusercontent.com%2Ffrancis-h-francisco%2Fcareful-shopper-mosquito-guide%2Fmain%2Fblueprint-v2-creative.json). Same words and content rules, a new field-guide design: serif display type, pine and amber palette, a sticky contents rail, specimen product cards with "See example on Amazon", and a comparison table that becomes cards on a phone.

Each link launches an independent WordPress Playground instance in the visitor browser. The two previews do not share a WordPress database, and edits in one do not update the other. The older blueprint.json and blueprint-v2.*.json files are kept as history and are no longer linked from the landing page.

## How the versions are built

The blueprints are generated, not hand-edited:

- tools/guide_content.py holds every word of the guide, so both versions say the same thing.
- versions/v1-strict/ and versions/v2-creative/ each hold render.py (markup), theme/ (a Twenty Twenty-Five child theme: style.css, functions.php, menu.js, templates, parts) and version.json.
- tools/build-blueprints.py renders each version and writes blueprint-v1-strict.json and blueprint-v2-creative.json. The blueprint installs Twenty Twenty-Five, writes the child theme, and adds a must-use plugin that uploads the Zone 4 photo and creates the guide as the static front page.
- tools/preview.py assembles each version locally and audits it in Chromium at 1440, 1024, 768, 600 and 360 px (fonts, sizes, colors, overflow, cards per row). It needs Playwright.

```
python3 tools/build-blueprints.py          # both versions
python3 tools/preview.py v1-strict v2-creative
```

## What the guide covers

- Why mosquitoes bite and the risks associated with bites
- Three complementary protection layers: block, reduce and relieve
- A comparison of six mosquito barriers
- Six barrier categories and five complementary product categories
- Clear product-link disclosure and practical pairing guidance

The page follows the supplied Mosquito Blog and Careful Shopper Style Sheet. Product buttons say **See Example** (Version 1) or **See example on Amazon** (Version 2), both wordings Eve approved.

## Preview architecture

GitHub Pages serves the version chooser and the two Blueprint files. WordPress Playground runs as an isolated instance in each visitor browser. It is not a shared WordPress database, and visitor changes are not published to a common site.

## Important limitations

This repository is a review/demo, not a production storefront. Product links are demonstration destinations; affiliate tracking, product availability and current listing details are not verified. Some navigation and footer destinations were not supplied in the assignment and remain placeholders rather than pointing to invented pages.

The Zone 4 image is the permitted watermarked mosquito-bite image embedded in the original rough-draft HTML. The flea image is excluded. Product windows are placeholders for Lasso-style displays; product images are not downloaded.

A successful source build does not prove that a Playground preview has started or rendered correctly. Browser checks, responsive checks, keyboard/zoom checks and a final screenshot remain required before this is presented as complete.

## Project files

- blueprint-v1-strict.json, blueprint-v2-creative.json — generated Playground setups linked from the landing page.
- versions/, tools/ — the sources and scripts that generate them.
- blueprint.json, blueprint-v2.0.0.json, blueprint-v2-preview-*.json — earlier builds, kept as history.
- index.html — landing page with two version links.
- playground.html — direct original preview launcher.
- docs/PROJECT-BRIEF.md — content and acceptance requirements.
- docs/BUILD-CHECKLIST.md — remaining acceptance checks.
- docs/PLAYGROUND-POC.md — preview architecture and runtime limitations.
