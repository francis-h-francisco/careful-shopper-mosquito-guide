# Project Brief — Careful Shopper Bicycle Security Guide

## Current assignment

Eve's latest reply M003 (2026-11-06) changes the subject and product scope from the earlier mosquito brief. Build one coherent security-themed blog page using a regular WordPress theme, starting with Twenty Twenty-Five or GeneratePress. Select 3–6 complementary products from third-party Amazon Marketplace sellers. Use **SEE EXAMPLE** on buttons. Teach readers how to evaluate important product features rather than pushing a brand or model.

This implementation chooses **bicycle security**:
1. Hardened-steel chain lock.
2. Hardened-steel U-lock.
3. Motion-alarm lock.

The product categories form a layered setup: physically secure the frame, reinforce a second point, and add an audible warning. An alarm is not a substitute for a physical lock.

## Design direction

- Parent theme: WordPress.org Twenty Twenty-Five.
- Child theme: Careful Shopper.
- Rounded corners: approximately 24–25px.
- Narrow type range: Verdana, Geneva, Arial, sans-serif; 1rem reading text, 1.2rem zone headings, 1.4rem maximum page title.
- Retain the source Style Sheet's nine-zone editorial structure and presentation rules where they remain relevant, but do not retain mosquito-specific text, categories, or assets.
- Product cards: three per row on desktop, one per row on phone; card max width 14rem. Layer cards: three columns, stacking below 40rem.
- Product windows: 16:10, white, dashed green border, rounded 1.5rem, centered “Product window” text. No manufacturer product photos.
- CTA: “SEE EXAMPLE”, brown background, white bold text, at least 3rem high.
- No unnecessary explanatory notes, bracketed production notes, or stale mosquito-specific copy.

## Image

Use a free-to-use stock photo relevant to bicycle security, not the old mosquito photo and not an AI-generated image. Current source: Simon Reza's Pexels photo “A Chained Bicycle with Padlock” (Pexels photo 9068057). Credit: “Photo by Simon Reza / Pexels”. External image loading still requires browser verification.

## Product links

The current cards link to Amazon Marketplace category searches for the three chosen features. They are not verified individual product pages. On a product page, inspect **Sold by** and **Ships from**; Amazon explains that a third-party seller appears under “Sold by” with the seller's name. Do not claim that the exact seller, offer, price, stock, or affiliate tracking has been verified.

## Source hierarchy and content boundaries

- M003 is the latest employer instruction and supersedes the mosquito-specific topic and product count in M002's original attached documents.
- The original Mosquito Blog and Style Sheet remain available as layout/design references only where compatible with M003.
- The MHTML is a visual reference for editorial polish, not a content source for bicycle-security claims.
- No unsupported claims about product performance, certification, theft prevention, or guarantees.
- No product brand or model names in visible copy.

## Runtime boundary

GitHub Pages serves static launcher files. WordPress Playground runs in each visitor's browser and is isolated; it is not a shared PHP/MySQL host. Clean-browser startup/import and image loading are not yet verified.
