# Careful Shopper — Mosquito Protection Guide

> **Independent test/demo workspace.** This repository is a technical experiment for a WordPress Playground-based preview of a mosquito-protection buyer guide. It is not the official Careful Shopper production website and is not affiliated with or endorsed by Careful Shopper.

## Purpose

Build a polished, accessible, mobile-first, nine-zone educational guide that helps readers understand mosquito-bite protection choices without pressuring them to buy a particular product. The intended business model may include affiliate commissions, disclosed clearly and consistently.

The current editorial direction supplied for this test is to use **SEE EXAMPLE** on Amazon product links—not “BUY NOW”. The link may lead to an example product page; the guide itself should explain needs, trade-offs and appropriate use rather than promote brands.

## Project status

**Scaffold only — implementation and deployment have not yet been validated.**

- [x] Public repository created.
- [x] Project brief and quickstart documentation added.
- [ ] Confirm the content ambiguities and missing product URLs listed in [the build checklist](docs/BUILD-CHECKLIST.md).
- [ ] Choose and validate the Playground packaging/startup approach.
- [ ] Build the nine-zone page to the supplied specifications.
- [ ] Test accessibility, responsive layouts, links and cache/update behavior.
- [ ] Publish and verify a review URL before sharing it.

## Important architecture note

GitHub Pages is a static host. It does not run a conventional WordPress PHP/MySQL server. A browser-based WordPress Playground experiment may load WordPress inside each visitor's browser using WebAssembly and browser storage. That means each visitor has a separate local instance; edits and database changes are **not shared** between visitors.

This is therefore an experimental review/demo architecture, not a replacement for a conventional shared WordPress website. A static Pages URL and a preconfigured Playground startup/import flow must be tested in real browsers before this repository can promise a working WordPress preview.

## Repository map

- `README.md` — project overview and current status.
- [`QUICKSTART.md`](QUICKSTART.md) — contributor setup and first-run checklist.
- [`docs/PROJECT-BRIEF.md`](docs/PROJECT-BRIEF.md) — scope, editorial direction and constraints.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — Playground + Pages experiment and limitations.
- [`docs/BUILD-CHECKLIST.md`](docs/BUILD-CHECKLIST.md) — blockers, acceptance checks and required inputs.
- [`docs/DECISIONS.md`](docs/DECISIONS.md) — decisions and unresolved questions.

## Source-of-truth boundaries

The supplied mosquito blog brief, Careful Shopper style sheet and rough HTML example are the assignment references. The rough HTML is an example to inspect, not a finished implementation to copy wholesale. Where the source documents conflict or omit information, record the issue and resolve it explicitly rather than inventing copy, products or URLs.

Do not commit private correspondence, credentials, payment details, or unrelated career records. Only add assets that may legally be redistributed in this public repository. Do not upload watermarked stock images or product/manufacturer photos unless the relevant source explicitly authorizes their use.

## License and attribution

No open-source license has been selected. Until one is added, assume the original project content and assets are **all rights reserved**. Confirm rights and attribution for every image and other third-party asset before publishing.
