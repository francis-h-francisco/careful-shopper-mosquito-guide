# Careful Shopper — Mosquito Protection Guide

> **Independent test/demo workspace.** This repository is a technical experiment for a WordPress Playground-based preview of a mosquito-protection buyer guide. It is not the official Careful Shopper production website and is not affiliated with or endorsed by Careful Shopper.

## Purpose

Build a polished, accessible, mobile-first, nine-zone educational guide that helps readers understand mosquito-bite protection choices without pressuring them to buy a particular product. The intended business model may include affiliate commissions, disclosed clearly and consistently.

The latest employer direction is to use **SEE EXAMPLE** on Amazon product links—not “BUY NOW” or the older “View on Amazon” label. The guide explains needs, features and trade-offs rather than promoting brands.

## Current status

**Initial Playground proof-of-concept code committed; Pages deployment and browser startup/import are not yet verified.**

- [x] Public repository and source-reconciled documentation scaffold.
- [x] User authorized selecting six Zone 7 example destinations.
- [x] User authorized Pages + Playground first and conventional WordPress hosting as fallback.
- [x] Static entry page, Playground iframe shell, Blueprint and Pages Actions workflow committed.
- [ ] Enable/configure GitHub Pages for GitHub Actions if the repository has not already been configured.
- [ ] Verify Actions deployment and obtain the actual Pages URL.
- [ ] Test first-time Playground startup and prepared-page import in a clean browser.
- [ ] Repeat startup and test a second browser/device.
- [ ] Select and validate six Zone 7 example destinations.
- [ ] Resolve authorized footer destinations; source provides labels but not URLs.
- [ ] Build the complete nine-zone guide after the runtime gate passes.
- [ ] Test responsive layout, accessibility, links, and cache/update behavior.
- [ ] Publish and verify a review URL before sharing it.

## Architecture boundary

GitHub Pages serves static files; it does not run a conventional WordPress PHP/MySQL server. The current proof of concept loads the official WordPress Playground client in an iframe and uses a Blueprint to create a prepared WordPress page. WordPress runs in each visitor's browser through WebAssembly. Each visitor has an isolated instance; edits and database changes are **not shared**.

The official embed is documented as experimental and may change. This is a review/demo architecture, not a shared production WordPress site. See [the Playground proof-of-concept notes](docs/PLAYGROUND-POC.md).

If the official remote runtime or import flow proves unsuitable, the user has authorized a conventional shared WordPress-hosting fallback. Do not switch before testing and documenting the technical reason.

## Repository map

- `index.html` — static project entry page.
- `playground.html` — Playground startup/import test harness.
- `blueprint.json` — prepared WordPress setup and import check page.
- `docs/PLAYGROUND-POC.md` — technical spike and acceptance criteria.
- `QUICKSTART.md` — contributor setup.
- `docs/PROJECT-BRIEF.md` — scope, editorial direction and constraints.
- `docs/ARCHITECTURE.md` — Playground + Pages experiment and limitations.
- `docs/BUILD-CHECKLIST.md` — source decisions, open items and acceptance checks.
- `docs/DECISIONS.md` — decisions and unresolved questions.
- `.github/workflows/pages.yml` — GitHub Pages deployment workflow.

## Source-of-truth boundaries

The supplied mosquito blog brief, Careful Shopper style sheet and rough HTML example are the assignment references. The rough HTML is an example to inspect, not a finished implementation to copy wholesale. Where the source documents omit information, record the gap rather than inventing copy, products or URLs.

Do not commit private correspondence, credentials, payment details, or unrelated career records. Only add assets that may legally be redistributed in this public repository. Do not upload manufacturer product photos. The Style Sheet permits the supplied mosquito-bite demo photo for this test; exclude the flea photo and retain the specified credit.

## License and attribution

No open-source license has been selected. Until one is added, assume the original project content and assets are **all rights reserved**. Confirm rights and attribution for every image and other third-party asset before publishing.
## 2026-11-06 — Nine-zone public guide

**Nine-zone static guide committed; user reports the GitHub Pages URL is live.** Source readback verifies the committed HTML, but no independent visual browser inspection has yet been completed.

Live URL: https://francis-h-francisco.github.io/careful-shopper-mosquito-guide/

The guide includes the nine source-ordered zones, specified Verdana typography and palette, exact disclosure repeated before both product groups, mosquito-bite photo with Dreamstime_216036901 credit, Zone 5 controlling copy, six barrier cards, five pairing cards, comparison table and curated-by/footer. The flea photo is excluded. CTA wording is SEE EXAMPLE per Eve's latest message.

Zone 8 uses the five source-provided Amazon links. Zone 7 currently uses Amazon category-search destinations for the six authorized categories; these are explicitly identified as test links, not verified individual listings or confirmed affiliate-tracked links. Footer and some navigation destinations were not supplied and are flagged rather than invented.

GitHub Pages serves the public static guide. WordPress Playground remains a separate, visitor-isolated experiment at /playground.html; the startup/import test is not yet confirmed. It is not a shared WordPress backend.

Next: user visual QA at desktop and 22.5rem mobile, keyboard/200% zoom checks, Playground startup/import test, individually verified Zone 7 product destinations, and authorized missing navigation/footer URLs. No screenshot has yet been captured and nothing has been sent to Eve.
