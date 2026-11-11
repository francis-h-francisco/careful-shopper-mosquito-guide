# Decision Log

## Confirmed
| Date | Decision | Basis |
|---|---|---|
| 2026-11-06 | Repository: careful-shopper-mosquito-guide. | User created the public repository. |
| 2026-11-06 | Independent test/demo, not official Careful Shopper production property. | Project boundary. |
| 2026-11-06 | Amazon CTA is **SEE EXAMPLE**. | Latest employer direction supersedes older “View on Amazon” wording. |
| 2026-11-06 | One near-final read-only review URL is enough; no simultaneous collaboration needed. | User's stated workflow. |
| 2026-11-06 | User authorizes selecting six suitable Zone 7 example product links. | Explicit user direction; exact categories remain fixed by source. |
| 2026-11-06 | Use dedicated Zone 5 section copy from MosquitoBlog. | It is the direct page-specific Zone 5 instruction; the Style Sheet defines layout only. |
| 2026-11-06 | Use approximately 50 words of lorem ipsum for Mrs. Shopper bio. | Explicit Blog instruction. |
| 2026-11-06 | Use the mosquito-bite photo from supplied HTML or the permitted free Dreamstime demo; exclude flea photo. | Style Sheet permission and user confirmation. |
| 2026-11-06 | Try Pages + Playground first; InfinityFree is authorized fallback if unsuitable. | Explicit user direction. |
| 2026-11-06 | Do not promise forced immediate refresh for all visitors. | Browser/CDN cache behavior must be tested. |

## Open
| Topic | State | Needed |
|---|---|---|
| Zone 7 URLs | Six destinations absent in source; selection authorized. | Research and select suitable examples, one per specified card category. |
| Footer targets | Five labels and “Read Mrs. Shopper’s full background” label are specified; target URLs are not. | Find authorized destinations or document unresolved link behavior; do not invent URLs. |
| Runtime | Pages + Playground import/startup untested. | Minimal technical spike; InfinityFree fallback authorized if needed. |

## Not done
- No WordPress page built.
- No Playground runtime deployed.
- No Pages workflow/public preview URL validated.
- No review link sent to Eve.


| 2026-11-06 | Use WordPress.org Twenty Twenty-Five as the parent theme and a Careful Shopper child theme for the Playground preview. | User asked to retain Twenty Twenty-Five if possible; MHTML is the visual reference. |
| 2026-11-06 | Disable automatic WordPress admin login in the Playground Blueprint. | Intended reviewer path is a front-end preview, not an admin session. |


## 2026-11-06 — Explicit topic/design correction

The user explicitly corrected the assistant: the requested project is the mosquito-protection blog, not bicycle security. Keep the original mosquito topic and source-driven design. Do not change the topic or redesign the page based on an ambiguous interpretation of employer wording. The user requested targeted fixes to images, navigation, mobile menu, content accuracy, unnecessary explanatory text and card breakpoints while preserving what already looks right.

## 2026-11-06 — Responsive/media repair choices

- Use the supplied mosquito-bite WebP already embedded in the static guide. For Playground, write the same bytes into the local uploads directory and use the generated media URL so WordPress does not have to preserve a `data:` URL in post content.
- Use a no-wrap desktop nav and switch to the Menu control at 55rem to prevent the last item from dropping to a second row.
- Enqueue a dedicated child-theme menu script; do not rely on a button with no event handler.
- Match the source card rules: three per desktop row, one per phone row, with an optional two-column intermediate tablet layout. Stack the three layer cards below 40rem.
- Remove the hero's extra preview CTA and the public footer note explaining internal link gaps; keep the standalone Playground launcher separate.
- Runtime and browser checks remain open until actually tested.

## 2026-11-11 — Two versions: strict and creative

| Decision | Basis |
|---|---|
| Version 1 (strict) follows the Style Sheet value by value; Version 2 (creative) follows only the content rules and must not resemble the rough-draft HTML. | User direction, 2026-11-11. |
| Both versions render the same copy from tools/guide_content.py. | Keeps words, products and disclosure identical. |
| Buttons: "See Example" in Version 1, "See example on Amazon" in Version 2. | Eve: "buttons can say: See example on Amazon or See Example". |
| The exact disclosure sits under the hero and directly above each product group in both versions. | Eve: wording is needed wherever readers might click a product link. |
| The CDC link is removed; it is not in the Blog copy. | Blog is the content source. |
| Links to pages outside the one-page test go to a styled "not part of the test" 404 page. | No destinations were supplied; no invented pages. |
| Version 1 phones: below 30rem the Zone 4 photo stops floating so the text beside it never shrinks to a few words per line. | Readability at 22.5rem; the only layout deviation from the sheet. |
| Version 2 loads Fraunces and Atkinson Hyperlegible from Google Fonts with local fallbacks; motion only under prefers-reduced-motion: no-preference. | Creative brief; accessibility. |
