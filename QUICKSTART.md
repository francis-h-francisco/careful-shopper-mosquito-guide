# Quickstart

This repository now contains an initial static GitHub Pages entry page and WordPress Playground proof-of-concept harness. The full mosquito guide is not yet implemented, and the Pages deployment/browser test is not yet verified.

## Get the repository

```bash
git clone https://github.com/francis-h-francisco/careful-shopper-mosquito-guide.git
cd careful-shopper-mosquito-guide
```

## Read the project references

- [Project brief](docs/PROJECT-BRIEF.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Build checklist](docs/BUILD-CHECKLIST.md)
- [Decisions](docs/DECISIONS.md)
- [Playground proof of concept](docs/PLAYGROUND-POC.md)

## Deploy

The workflow at `.github/workflows/pages.yml` deploys the repository root to GitHub Pages when a commit is pushed to `main`.

If Pages is not configured yet:
1. Open the repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Save the setting.
5. Open **Actions**, then inspect the latest **Deploy static preview to GitHub Pages** run.
6. When the deployment finishes, open the URL shown by the deployment job.

## Test Playground

1. Open the deployed Pages URL.
2. Select **Open WordPress Playground test**.
3. Wait for the status to report that Playground is ready. First startup may take several minutes.
4. Confirm the WordPress frame displays the page titled **Playground Import Check**.
5. Repeat in a private/incognito browser window and, if possible, a second browser/device.

The runtime is isolated in each visitor's browser. It is not a shared WordPress database. Do not enter confidential information.

## Before full implementation

Select six authorized Zone 7 example destinations, then build the nine-zone page only after the Playground startup/import gate passes. The footer target URLs are absent from the source files and must not be invented.