"""Version 2 (creative): same words as Version 1, a different design.

Concept: a field guide. A pine-dark hero with a netting texture, a sticky "On this page" rail,
numbered sections, a connected three-layer route, specimen-style product cards, and a footer
that closes the guide. Content rules still hold: the exact disclosure above every group of
product links, "See example on Amazon" buttons, no prices, ratings, dates or brand names in text.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import guide_content as C
sys.path.insert(0, HERE)
import art

NEW_TAB = 'target="_blank" rel="sponsored noopener noreferrer"'
BUTTON = "See example on Amazon"

MARK = (
    '<svg class="fg-mark" viewBox="0 0 48 48" width="44" height="44" aria-hidden="true" focusable="false">'
    '<path fill="#F0B44C" d="M24 2 43 9v13c0 12-8 20-19 24C13 42 5 34 5 22V9Z"/>'
    '<path fill="none" stroke="#173D2D" stroke-width="1" opacity=".35" '
    'd="M11 14 37 40M11 22 31 42M11 30 23 42M17 10 39 32M25 8 39 22M11 40 37 14M11 32 31 12M11 24 25 10M17 42 39 20M25 42 39 28"/>'
    '<path fill="none" stroke="#173D2D" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" '
    'd="m15 24 6.5 6.5L33 18"/></svg>')

HERO_ART = (
    '<div class="fg-hero__art" aria-hidden="true">'
    '<div class="fg-rings"><span class="fg-ring fg-ring--3"><b>Relieve</b></span>'
    '<span class="fg-ring fg-ring--2"><b>Reduce</b></span>'
    '<span class="fg-ring fg-ring--1"><b>Block</b></span>'
    '<svg class="fg-hero__shield" viewBox="0 0 48 48" focusable="false">'
    '<path fill="#F0B44C" d="M24 2 43 9v13c0 12-8 20-19 24C13 42 5 34 5 22V9Z"/>'
    '<path fill="none" stroke="#173D2D" stroke-width=".7" opacity=".4" '
    'd="M11 14 37 40M11 22 31 42M11 30 23 42M17 10 39 32M25 8 39 22M11 40 37 14M11 32 31 12M11 24 25 10M17 42 39 20M25 42 39 28"/>'
    '<path fill="none" stroke="#173D2D" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" d="m15 24 6.5 6.5L33 18"/>'
    '</svg></div></div>')

SECTIONS = [  # (anchor, number, heading) used by the rail and the section heads
    ("why", "01", C.WHY_TITLE),
    ("layers", "02", C.LAYERS_TITLE),
    ("compare", "03", C.TABLE_TITLE),
    ("barriers", "04", C.BARRIERS_TITLE),
    ("other-layers", "05", C.PAIRS_TITLE),
]


def block(html):
    return "<!-- wp:html -->\n" + html.strip() + "\n<!-- /wp:html -->"


def nav_items():
    out = []
    for label, href in C.NAV:
        cur = ' aria-current="page"' if label == C.CURRENT_NAV else ""
        out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(out)


def header():
    return block(f"""
<div class="fg fg-header">
<a class="fg-skip" href="#main">Skip to the guide</a>
<div class="fg-header__bar">
<div class="fg-brand"><a class="fg-brand__logo" href="/" aria-label="{C.SITE_NAME} home">{MARK}</a><span class="fg-brand__text"><span class="fg-brand__name">{C.SITE_NAME}</span><span class="fg-brand__tag">{C.TAGLINE}</span></span></div>
<nav class="fg-nav" aria-label="Main"><ul>{nav_items()}</ul></nav>
<button class="fg-menu-button" type="button" aria-expanded="false" aria-controls="fg-menu"><span class="fg-menu-button__bars" aria-hidden="true"></span>Menu</button>
</div>
<nav class="fg-menu" id="fg-menu" aria-label="Main menu"><ul>{nav_items()}</ul></nav>
</div>""")


def footer():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in C.FOOTER_LINKS)
    return block(f"""
<div class="fg fg-footer">
<div class="fg-footer__inner">
<section class="fg-footer__curator" aria-labelledby="curated-title">
<span class="fg-monogram" aria-hidden="true">MS</span>
<div>
<h2 id="curated-title">{C.CURATED_TITLE}</h2>
<p>{C.BIO}</p>
<p><a class="fg-footer__more" href="{C.BIO_LINK[1]}">{C.BIO_LINK[0]}</a></p>
</div>
</section>
<p class="fg-footer__pledge">{C.NO_SPONSORS}</p>
<nav class="fg-footer__nav" aria-label="Footer"><ul>{links}</ul></nav>
<p class="fg-footer__copy">{C.COPYRIGHT}</p>
</div>
</div>""")


def disclosure(anchor=None, extra=""):
    i = f' id="{anchor}"' if anchor else ""
    return (f'<aside class="fg-disclosure{extra}" aria-label="Affiliate disclosure"{i}>'
            f'<p class="fg-disclosure__label">Affiliate disclosure</p>'
            f'<p class="fg-disclosure__text">{C.DISCLOSURE}</p></aside>')


def section_head(anchor):
    _, num, title = next(s for s in SECTIONS if s[0] == anchor)
    return (f'<header class="fg-head"><span class="fg-head__num" aria-hidden="true">{num}</span>'
            f'<h2 id="{anchor}-title">{title}</h2></header>')


def facts(lines):
    return '<dl class="fg-facts">' + "".join(
        f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in lines) + "</dl>"


def card(i, name, url, layer, lines, kind="specimen"):
    label = f"{BUTTON}: {name.lower()} (opens in a new tab)"
    tag = layer or "Layer 1: Block"
    return f"""<li class="fg-card fg-card--{kind}">
<a class="fg-window" href="{url}" {NEW_TAB} tabindex="-1" aria-hidden="true"><span class="fg-window__no">No. {i:02d}</span>{art.svg(art.PRODUCT_ART[name], "fg-window__art")}<span class="fg-window__label">Product window</span></a>
<div class="fg-card__body">
<p class="fg-tag">{tag}</p>
<h3>{name}</h3>
{facts(lines)}
<a class="fg-button" href="{url}" {NEW_TAB} aria-label="{label}">{BUTTON}<span class="fg-button__arrow" aria-hidden="true">↗</span></a>
</div>
</li>"""


def content():
    crumbs = '<li><a href="/">Home</a></li>' + "".join(
        f'<li{" aria-current=\"page\"" if n == len(C.BREADCRUMB) - 1 else ""}>{c}</li>'
        for n, c in enumerate(C.BREADCRUMB))
    toc = "".join(f'<li><a href="#{a}"><span class="fg-toc__num">{n}</span><span>{t}</span></a></li>'
                  for a, n, t in SECTIONS)
    steps = "".join(
        f'<li class="fg-step{" is-here" if here else ""}"><span class="fg-step__dot" aria-hidden="true">{k}</span>'
        f'{art.svg(art.LAYER_ART[k - 1], "fg-step__art")}'
        f'<h3>{t}</h3><p>{d}</p>'
        f'{("<p class=\"fg-step__here\">" + C.YOU_ARE_HERE + "</p>") if here else ""}</li>'
        for k, (t, d, here) in enumerate(C.LAYERS, 1))
    head = "".join(f'<th scope="col" role="columnheader">{h}</th>' for h in C.TABLE_HEAD)
    rows = "".join(
        '<tr role="row">' + "".join(
            (f'<th scope="row" role="rowheader" data-label="{C.TABLE_HEAD[j]}">{c}</th>' if j == 0 else
             f'<td role="cell" data-label="{C.TABLE_HEAD[j]}">{c}</td>') for j, c in enumerate(r)) + "</tr>"
        for r in C.TABLE)
    barrier_cards = "".join(card(i, n, u, l, c) for i, (n, u, l, c) in enumerate(C.BARRIERS, 1))
    groups = []
    start = len(C.BARRIERS) + 1
    for layer in sorted({p[2] for p in C.PAIRS}):
        items = [(i, p) for i, p in enumerate(C.PAIRS, start) if p[2] == layer]
        cards = "".join(card(i, n, u, l, c, "pair") for i, (n, u, l, c) in items)
        groups.append(f'<div class="fg-pairs__group"><p class="fg-pairs__layer">{layer}</p><ul class="fg-pairs" role="list">{cards}</ul></div>')

    zones = [
        f"""<section class="fg fg-hero" id="top" aria-labelledby="page-title">
<div class="fg-hero__inner">
<div class="fg-hero__text">
<nav class="fg-crumbs" aria-label="Breadcrumb"><ol>{crumbs}</ol></nav>
<h1 id="page-title">{C.TITLE}</h1>
<p class="fg-byline"><span class="fg-monogram fg-monogram--small" aria-hidden="true">MS</span>{C.BYLINE}</p>
<div class="fg-answer"><p>{C.SHORT_ANSWER}</p></div>
</div>
{HERO_ART}
</div>
</section>""",
        f"""<nav class="fg fg-toc" aria-label="On this page">
<details class="fg-toc__box">
<summary class="fg-toc__title">On this page</summary>
<ol>{toc}</ol>
</details>
</nav>""",
        f'<div class="fg fg-lead">{disclosure("affiliate-disclosure", " fg-disclosure--lead")}</div>',
        f"""<section class="fg fg-section fg-why" id="why" aria-labelledby="why-title">
{section_head("why")}
<div class="fg-why__grid">
<figure class="fg-plate"><img src="__PHOTO_URL__" alt="{C.PHOTO_ALT}" width="992" height="662" loading="lazy" decoding="async"><figcaption>{C.PHOTO_CREDIT}</figcaption></figure>
<div class="fg-prose">{"".join(f"<p>{p}</p>" for p in C.WHY)}</div>
</div>
<div class="fg-risk">
{art.svg("mosquito", "fg-risk__art")}
<h3 class="fg-risk__title">{C.RISK_TITLE}</h3>
{"".join(f"<p>{p}</p>" for p in C.RISK)}
</div>
</section>""",
        f"""<section class="fg fg-section fg-layers" id="layers" aria-labelledby="layers-title">
{section_head("layers")}
<ol class="fg-steps">{steps}</ol>
<p class="fg-layers__close">{C.LAYERS_CLOSE}</p>
</section>""",
        f"""<section class="fg fg-section fg-compare" id="compare" aria-labelledby="compare-title">
{section_head("compare")}
<div class="fg-table" role="region" aria-labelledby="compare-title" tabindex="0">
<table role="table"><thead><tr role="row">{head}</tr></thead><tbody>{rows}</tbody></table>
</div>
</section>""",
        f"""<section class="fg fg-section fg-shop" id="barriers" aria-labelledby="barriers-title">
{section_head("barriers")}
<p class="fg-shop__intro">{C.BARRIERS_INTRO}</p>
<div class="fg-shop__layout">
{disclosure(extra=" fg-disclosure--rail")}
<ul class="fg-cards" role="list">{barrier_cards}</ul>
</div>
</section>""",
        f"""<section class="fg fg-section fg-shop fg-shop--pairs" id="other-layers" aria-labelledby="other-layers-title">
{section_head("other-layers")}
<p class="fg-shop__intro">{C.PAIRS_INTRO}</p>
<div class="fg-shop__layout">
{disclosure(extra=" fg-disclosure--rail fg-disclosure--closing")}
<div class="fg-pairs__groups">{"".join(groups)}</div>
</div>
</section>""",
    ]
    return "\n\n".join(block(z) for z in zones)


def not_built():
    return block(f"""
<section class="fg fg-hero fg-hero--short" aria-labelledby="page-title">
<div class="fg-hero__inner">
<div class="fg-hero__text">
<h1 id="page-title">{C.NOT_BUILT_TITLE}</h1>
<div class="fg-answer"><p>{C.NOT_BUILT_TEXT}</p>
<p><a class="fg-button fg-button--light" href="{C.NOT_BUILT_LINK[1]}">{C.NOT_BUILT_LINK[0]}</a></p></div>
</div>
{HERO_ART}
</div>
</section>""")


MAIN_OPEN = ('<!-- wp:group {"tagName":"main","anchor":"main","className":"fg-main","layout":{"type":"default"}} -->\n'
             '<main class="wp-block-group fg-main" id="main">')
MAIN_CLOSE = "</main>\n<!-- /wp:group -->"
PARTS = ('<!-- wp:template-part {"slug":"cs-header","tagName":"header","className":"fg-site-header"} /-->',
         '<!-- wp:template-part {"slug":"cs-footer","tagName":"footer","className":"fg-site-footer"} /-->')


def template(inner):
    return "\n".join([PARTS[0], MAIN_OPEN, inner, MAIN_CLOSE, PARTS[1]]) + "\n"


def write(rel, text):
    path = os.path.join(HERE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def render():
    write("content/guide.html", content() + "\n")
    write("theme/parts/cs-header.html", header() + "\n")
    write("theme/parts/cs-footer.html", footer() + "\n")
    page = template('<!-- wp:post-content {"layout":{"type":"default"}} /-->')
    for t in ("front-page", "page", "index", "singular"):
        write(f"theme/templates/{t}.html", page)
    write("theme/templates/404.html", template(not_built()))


if __name__ == "__main__":
    render()
