# Careful Shopper — Bicycle Security Guide

> Independent test/demo workspace. This repository is not the official Careful Shopper production website.

## Current brief

The latest employer direction (M003, 2026-11-06) supersedes the earlier mosquito-specific assignment: adapt a regular WordPress theme, starting with Twenty Twenty-Five or GeneratePress, use one coherent security theme, and select 3–6 complementary products from third-party Amazon Marketplace sellers. The current demo uses **bicycle security** with three categories: hardened-steel chain lock, hardened-steel U-lock, and motion-alarm lock. The page teaches feature selection and how the layers complement one another. Buttons say **SEE EXAMPLE**.

The earlier Mosquito Blog and Careful Shopper Style Sheet remain available as design references where their layout and presentation rules still apply. Mosquito-specific copy, product categories, and photo are not the current assignment.

## Current implementation

- `index.html` — minimal public entry page.
- `playground.html` — minimal WordPress preview entry.
- `blueprint.json` — installs WordPress.org Twenty Twenty-Five, writes and activates the Careful Shopper child theme, enqueues its menu script, and imports the bicycle-security guide as the front page.
- The child theme uses Verdana/Geneva/Arial, a narrow type scale, 24px-equivalent rounded panels, one-column page zones, a three-card desktop product row, and a one-column product layout below 48rem.
- Zone 4 uses a free Pexels bicycle-and-chain photo by Simon Reza. Product windows remain text placeholders; the earlier Style Sheet says product photos are supplied by Lasso on the live site and must not be downloaded for this test.

## Important status and limitations

- The source files are committed; no clean-browser visual verification of the current Blueprint has yet been completed.
- Amazon links currently open category-search results, not verified individual product detail pages. The exact third-party seller and offer must be checked on the Amazon product page under **Sold by** before selecting a listing. Do not claim seller identity, stock, price, or affiliate tracking is verified.
- The Pexels image URL is external; its loading in the Playground runtime has not yet been verified.
- The Playground is browser-isolated. It is not a shared production WordPress server or shared database.
- The official Playground client is experimental; first-time startup and Blueprint import must be tested in a clean browser.
- The public page is a launcher, not a duplicate static guide.

## Acceptance checks

1. Open the Pages URL in a clean browser.
2. Launch WordPress Playground and confirm the bicycle-security page is the front page.
3. Confirm Twenty Twenty-Five is the parent theme and Careful Shopper child theme is active.
4. Confirm the Zone 4 photo loads.
5. Confirm desktop navigation remains on one row.
6. At phone width, confirm the Menu button opens/closes all navigation items and keyboard Escape closes it.
7. Confirm product cards are three across on desktop and one per row on mobile; layer cards stack below 40rem.
8. Confirm no page-level horizontal overflow; only the comparison table may scroll horizontally.
9. Verify all Amazon destinations and third-party seller details before presenting as product-specific recommendations.
10. Repeat startup in a clean session and another browser/device if possible.

## Repository map

- `docs/PROJECT-BRIEF.md` — latest brief and retained design rules.
- `docs/ARCHITECTURE.md` — Pages + Playground boundaries.
- `docs/BUILD-CHECKLIST.md` — implementation and acceptance status.
- `docs/DECISIONS.md` — source and scope decisions.
- `docs/PLAYGROUND-POC.md` — runtime proof of concept.
- `.github/workflows/pages.yml` — GitHub Pages deployment.
