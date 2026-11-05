# Quickstart

This repository is currently a documentation scaffold. It does not yet contain a working WordPress Playground deployment.

## Get the repository

```bash
git clone https://github.com/francis-h-francisco/careful-shopper-mosquito-guide.git
cd careful-shopper-mosquito-guide
```

## Before implementation

Read:
- [Project brief](docs/PROJECT-BRIEF.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Build checklist](docs/BUILD-CHECKLIST.md)
- [Decision log](docs/DECISIONS.md)

Resolve the six missing Zone 7 destinations and the conflicting Zone 5 layer wording before final content work. Verify image licensing before adding any image to this public repository.

## Technical spike

Create a disposable WordPress Playground instance and test whether the chosen browser-based runtime can be initialized from static hosting with the required theme, page and assets. GitHub Pages cannot run conventional PHP/MySQL hosting. Treat each browser's Playground instance as isolated; do not expect visitor edits to synchronize.

Inspect any export archive before assuming it includes the database, plugins, themes and media needed for a repeatable restore. Test startup in a clean browser before publishing a preview.

## Release checklist

- Responsive desktop and mobile layout.
- Keyboard navigation, visible focus and accessible contrast.
- All product buttons and product windows use the same approved destination.
- Disclosure appears immediately before each product group.
- No unapproved products, brands, prices, ratings or unsupported claims.
- No placeholder notes remain in the final page.
- Record the commit/build version and test the public URL in a private window and on mobile.

A stable URL may serve later releases, but browser/CDN caches cannot be universally forced to refresh immediately. Use versioned assets and deliberate cache handling.
