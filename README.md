# Careful Shopper — Mosquito Protection Guide

> **Independent test/demo workspace.** This repository is a technical experiment for a WordPress Playground-based preview of a mosquito-protection buyer guide. It is not the official Careful Shopper production website and is not affiliated with or endorsed by Careful Shopper.

## Purpose

Build a polished, accessible, mobile-first, nine-zone educational guide that helps readers understand mosquito-bite protection choices without pressuring them to buy a particular product. The intended business model may include affiliate commissions, disclosed clearly and consistently.

The latest employer direction is to use **SEE EXAMPLE** on Amazon product links—not “BUY NOW” or the older “View on Amazon” label. The guide explains needs, features and trade-offs rather than promoting brands.

## Project status

**Documentation scaffold — implementation and deployment have not yet been validated.**

- [x] Public repository created.
- [x] Source documents reviewed; project brief, checklist and decisions reconciled against them.
- [x] User authorized example-link selection for the six Zone 7 card categories.
- [x] User authorized the Pages + Playground experiment first and InfinityFree as fallback if needed.
- [ ] Select and validate six suitable Zone 7 example destinations.
- [ ] Resolve authorized destinations for the footer links; source provides labels but not URLs.
- [ ] Prove the Playground packaging/startup/import approach.
- [ ] Build the nine-zone page to the supplied specifications.
- [ ] Test accessibility, responsive layouts, links and cache/update behavior.
- [ ] Publish and verify a review URL before sharing it.

## Important architecture note

GitHub Pages is a static host. It does not run a conventional WordPress PHP/MySQL server. A browser-based WordPress Playground experiment may load WordPress inside each visitor's browser using WebAssembly and browser storage. Each visitor has a separate local instance; edits and database changes are **not shared** between visitors.

This is an experimental review/demo architecture, not a replacement for a conventional shared WordPress website. Test the preconfigured Playground startup/import flow in real browsers first. The user has authorized InfinityFree/conventional shared WordPress hosting as a fallback if the experiment is not viable.

## Repository map

- `README.md` — project overview and current status.
- [`QUICKSTART.md`](QUICKSTART.md) — contributor setup and first-run checklist.
- [`docs/PROJECT-BRIEF.md`](docs/PROJECT-BRIEF.md) — scope, editorial direction and constraints.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — Playground + Pages experiment and limitations.
- [`docs/BUILD-CHECKLIST.md`](docs/BUILD-CHECKLIST.md) — confirmed instructions, unresolved destinations and acceptance checks.
- [`docs/DECISIONS.md`](docs/DECISIONS.md) — decisions and unresolved questions.

## Source-of-truth boundaries

The supplied mosquito blog brief, Careful Shopper style sheet and rough HTML example are the assignment references. The rough HTML is an example to inspect, not a finished implementation to copy wholesale. Where the source documents omit information, record the gap rather than inventing copy, products or URLs.

Do not commit private correspondence, credentials, payment details, or unrelated career records. Only add assets that may legally be redistributed in this public repository. Do not upload watermarked stock images or product/manufacturer photos unless the relevant source explicitly authorizes their use.

## License and attribution

No open-source license has been selected. Until one is added, assume the original project content and assets are **all rights reserved**. Confirm rights and attribution for every image and other third-party asset before publishing.
