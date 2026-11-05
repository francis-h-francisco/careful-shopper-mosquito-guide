# Build Checklist

## Confirmed from source / user
- [x] Six Zone 7 card categories are specified; user authorizes selecting suitable example Amazon destinations for those exact categories.
- [x] Zone 5 page copy: use the dedicated Zone 5 block in MosquitoBlog: Layer 2 “Repellents, traps, and standing-water control cut how many are around.” Layer 3 “Creams and balms calm the bites that still get through.” Style Sheet governs layout, not layer wording.
- [x] Zone 4 mosquito-bite photo may be taken from the supplied HTML or a free watermarked Dreamstime demo; no purchase/license needed for this test per Style Sheet and user confirmation. Exclude flea photo; credit Dreamstime_216036901.
- [x] Zone 9 bio is approximately 50 words of lorem ipsum, explicitly required by MosquitoBlog.
- [x] Five footer link labels and “Read Mrs. Shopper’s full background” are supplied. Their target URLs are not supplied; do not invent destinations or treat rough HTML # links as working links.
- [x] Try GitHub Pages + WordPress Playground first; user authorizes conventional shared WordPress hosting as fallback if the experiment is unsuitable.
- [x] Latest CTA is SEE EXAMPLE.
- [x] Initial Pages entry page, Playground iframe shell, Blueprint and Actions workflow committed.

## Current technical gate — not yet verified
- [ ] Configure GitHub Pages to use GitHub Actions if required.
- [ ] Confirm Actions deployment succeeds and identify the actual Pages URL.
- [ ] In a clean browser, confirm WordPress Playground starts from the Pages URL without a local server.
- [ ] Confirm the Blueprint imports the nine-zone guide as the WordPress front page.
- [ ] Reload in a clean/private session and repeat startup.
- [ ] Repeat in a second browser or device if available.
- [ ] Record startup time, browser/device and any errors. Do not claim success before observation.

## Still to resolve
- [ ] Research and select six suitable example Amazon destinations, one for each specified Zone 7 card category. Verify category fit; do not imply current stock, price, endorsement or affiliate tracking.
- [ ] Identify authorized target URLs for the five footer links and “Read Mrs. Shopper’s full background”. Do not invent them. If no targets can be established, present them without misleading navigation or seek an authorized destination.
- [ ] If the Playground route fails, investigate the failure and test the authorized conventional WordPress-hosting fallback.

## Available
- [x] Five Zone 8 example URLs copied from source document; not independently validated or confirmed affiliate links.
- [x] Layout, typography, disclosure, product-window, caption and accessibility requirements summarized in project brief.
- [x] Rough HTML source read fully; it is a flawed example, not a model to copy.
- [x] DOCX source pages rendered and visually inspected.

## Sequence
1. Enable/configure Pages and validate the minimal Playground startup/import proof.
2. If viable, research/select the six Zone 7 examples and build the nine-zone guide to the supplied specifications. If not, use the authorized fallback and record why.
3. Extract the permitted mosquito-bite image, preserve the Dreamstime_216036901 credit, and exclude the flea photo.
4. Implement exact copy, layout and disclosures from the two DOCX files; no invented footer targets.
5. Test desktop and 22.5rem mobile, keyboard access, 200% zoom, contrast, links, image ratios and cache updates.
6. Check every item against the Style Sheet self-check and Blog content instructions.
7. Publish only after the technical and content acceptance gates pass.
8. Capture the requested screenshot and share a review URL only after checking it.

Do not invent destinations, product claims, biography facts, affiliate status, photo rights or shared database behavior. Remove all internal placeholders before final review.
## 2026-11-06 — Public guide implementation

- [x] Nine-zone public guide implemented in index.html in source order.
- [x] Verdana typography, specified palette, rounded zones, 60rem content width and source heading/body sizes.
- [x] Header text mark, nav labels and responsive Menu control.
- [x] Hero copy and breadcrumb reproduced from MosquitoBlog.
- [x] Exact affiliate disclosure after hero and repeated immediately above both product groups.
- [x] Zone 4 education text reproduced; supplied mosquito-bite photo at 16:9 with Dreamstime_216036901 credit; flea photo excluded.
- [x] Zone 5 controlling layer copy; Zone 6 comparison table; six Zone 7 categories; five Zone 8 products; Zone 9 lorem ipsum bio and footer labels.
- [x] Product windows 16:10; same destination as each CTA; links open new tabs; card width constrained below desktop photo width.
- [x] Mobile one-column cards/layers, stacked navigation and table-only horizontal scrolling.

## Real-browser QA still required
- [ ] User visual check at desktop and 22.5rem phone width.
- [ ] Confirm photo displays/crop, disclosure wraps, menu works and no page-level horizontal overflow.
- [ ] Keyboard navigation, focus visibility and 200% zoom.
- [ ] Playground startup and Blueprint import at /playground.html.
- [ ] Capture final screenshot after QA.

## Open items
- [ ] Zone 7 currently uses Amazon category-search links, not verified individual product pages. Select/verify one suitable destination per category before employer review.
- [ ] Footer and Shopping Index/Contact nav destinations were not supplied; flagged rather than invented.
- [ ] Zone 7 destinations are not confirmed affiliate-tracked links; test-only status is disclosed.
- [ ] Playground is isolated per visitor and not a shared production WordPress backend.
- [ ] No screenshot or employer submission; nothing sent to Eve.


## 2026-11-06 — Requested repair pass

- [x] Confirmed topic remains mosquito protection; no bicycle/security substitution.
- [x] Static header navigation no longer wraps; Menu control replaces it at 55rem and below.
- [x] Static Menu supports tap/click, link-close, outside-click close and Escape.
- [x] Playground child theme enqueues a dedicated mobile-menu script with the same behavior.
- [x] Playground importer uploads the supplied mosquito-bite WebP into the local Playground uploads directory and stores the resulting image URL; post content no longer relies on a data URI.
- [x] Playground import is versioned and updates the existing page by slug instead of skipping an earlier import or creating a duplicate.
- [x] Child-theme CSS follows the source Style Sheet's Verdana font, restricted type scale, exact color roles, zone widths and card/window ratios.
- [x] Cards: three columns on desktop, one column below 40rem (including the required 22.5rem phone width); two columns are limited to intermediate widths. Layer cards stack below 40rem.
- [x] Removed the extra hero preview link and internal explanatory footer note from the nine-zone public page.
- [x] Simplified the separate Playground launcher.
- [ ] Verify latest GitHub Pages deployment and cache propagation.
- [ ] Verify photo rendering on the live static page and inside Playground.
- [ ] Verify Playground first-run import and re-import in a clean browser.
- [ ] Test Menu by touch and keyboard on a real phone-width browser.
- [ ] Test 200% zoom, focus visibility, page overflow and the comparison-table-only horizontal scroll.
- [ ] Capture screenshot only after visual QA.

The CSS and script changes are committed source, not proof of successful browser behavior.
