# Quickstart

This repository is an independent GitHub Pages launcher for a browser-based WordPress Playground preview.

## Read the references

- [Project brief](docs/PROJECT-BRIEF.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Build checklist](docs/BUILD-CHECKLIST.md)
- [Decisions](docs/DECISIONS.md)
- [Playground proof of concept](docs/PLAYGROUND-POC.md)

## Deploy

The workflow at `.github/workflows/pages.yml` deploys the repository root to GitHub Pages when a commit is pushed to `main`. Configure **Settings → Pages → Build and deployment → GitHub Actions** if needed.

## Test

1. Open the Pages URL.
2. Select **Open WordPress preview**.
3. Wait for Playground startup.
4. Confirm the bicycle-security guide is the front page and the Careful Shopper child theme is active.
5. Test the header and mobile Menu button at desktop and phone widths.
6. Repeat in a clean/private browser session.

The preview is isolated per visitor. It is not a shared WordPress database.
