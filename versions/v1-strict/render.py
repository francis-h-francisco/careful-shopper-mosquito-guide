"""Version 1 (strict): renders the page content, header and footer parts and templates.

Every class here is styled in theme/style.css with the exact Style Sheet values.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import guide_content as C

NEW_TAB = 'target="_blank" rel="sponsored noopener noreferrer"'

LOGO = (
    '<svg class="cs-logo" viewBox="0 0 48 48" width="48" height="48" aria-hidden="true" focusable="false">'
    '<path fill="#006633" d="M24 2 43 9v13c0 12-8 20-19 24C13 42 5 34 5 22V9Z"/>'
    '<path fill="none" stroke="#FFFFFF" stroke-width="1" opacity=".55" '
    'd="M11 14 37 40M11 22 31 42M11 30 23 42M17 10 39 32M25 8 39 22M11 40 37 14M11 32 31 12M11 24 25 10M17 42 39 20M25 42 39 28"/>'
    '<path fill="none" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" '
    'd="m15 24 6.5 6.5L33 18"/></svg>')


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
<div class="cs cs-header">
<a class="cs-skip" href="#main">Skip to the guide</a>
<div class="cs-header__inner">
<a class="cs-brand" href="/">{LOGO}<span class="cs-brand__name">{C.SITE_NAME}</span></a>
<nav class="cs-nav" aria-label="Main"><ul>{nav_items()}</ul></nav>
<button class="cs-menu-button" type="button" aria-expanded="false" aria-controls="cs-menu">Menu</button>
</div>
<nav class="cs-menu" id="cs-menu" aria-label="Main menu"><ul>{nav_items()}</ul></nav>
</div>""")


def footer():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in C.FOOTER_LINKS)
    return block(f"""
<div class="cs cs-footer">
<section class="cs-zone cs-zone--green" aria-labelledby="curated-title">
<div class="cs-zone__inner">
<h2 id="curated-title">{C.CURATED_TITLE}</h2>
<p>{C.BIO}</p>
<p><a href="{C.BIO_LINK[1]}">{C.BIO_LINK[0]}</a></p>
<p>{C.NO_SPONSORS}</p>
<nav class="cs-footer-nav" aria-label="Footer"><ul>{links}</ul></nav>
<p class="cs-copyright">{C.COPYRIGHT}</p>
</div>
</section>
</div>""")


def disclosure(anchor=None):
    i = f' id="{anchor}"' if anchor else ""
    return f'<p class="cs-disclosure"{i}>{C.DISCLOSURE}</p>'


def card(name, url, layer, lines):
    cap = "".join(f'<span class="cs-caption__line"><strong>{a}</strong> {b}</span>' for a, b in lines)
    return f"""<li class="cs-card">
<a class="cs-window" href="{url}" {NEW_TAB} aria-label="Product window: see an example of {name.lower()} on Amazon (opens in a new tab)">Product window</a>
<h3>{name}</h3>
<p class="cs-caption">{cap}</p>
<a class="cs-button" href="{url}" {NEW_TAB} aria-label="{C.BUTTON_LABEL}: {name.lower()} on Amazon (opens in a new tab)">{C.BUTTON_LABEL}</a>
</li>"""


def content():
    crumbs = " ".join([f'<a href="/">Home</a>'] + [f'<span aria-hidden="true">›</span> {c}' for c in C.BREADCRUMB])
    layers = "".join(
        f'<li class="cs-layer"><h3>{t}</h3><p>{d}{(" <strong>" + C.YOU_ARE_HERE + "</strong>") if here else ""}</p></li>'
        for t, d, here in C.LAYERS)
    head = "".join(f'<th scope="col">{h}</th>' for h in C.TABLE_HEAD)
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in C.TABLE)
    zones = [
        # Zone 2: hero
        f"""<section class="cs cs-zone cs-zone--green cs-hero" id="top" aria-labelledby="page-title">
<div class="cs-zone__inner">
<nav class="cs-breadcrumb" aria-label="Breadcrumb"><p>{crumbs}</p></nav>
<h1 id="page-title">{C.TITLE}</h1>
<p class="cs-byline">{C.BYLINE}</p>
<p>{C.SHORT_ANSWER}</p>
</div>
</section>""",
        # Zone 3: disclosure
        f'<div class="cs cs-disclosure-zone">{disclosure("affiliate-disclosure")}</div>',
        # Zone 4: education text with the floated photo
        f"""<section class="cs cs-zone cs-zone--white" aria-labelledby="why-title">
<div class="cs-zone__inner">
<figure class="cs-photo"><img src="__PHOTO_URL__" alt="{C.PHOTO_ALT}" width="992" height="662"><figcaption>{C.PHOTO_CREDIT}</figcaption></figure>
<h2 id="why-title">{C.WHY_TITLE}</h2>
{"".join(f"<p>{p}</p>" for p in C.WHY)}
<h2 class="cs-clear">{C.RISK_TITLE}</h2>
{"".join(f"<p>{p}</p>" for p in C.RISK)}
</div>
</section>""",
        # Zone 5: three-layer strip
        f"""<section class="cs cs-zone cs-zone--mint" aria-labelledby="layers-title">
<div class="cs-zone__inner">
<h2 id="layers-title">{C.LAYERS_TITLE}</h2>
<ul class="cs-layers">{layers}</ul>
<p class="cs-layers__close">{C.LAYERS_CLOSE}</p>
</div>
</section>""",
        # Zone 6: comparison table
        f"""<section class="cs cs-zone cs-zone--white" aria-labelledby="table-title">
<div class="cs-zone__inner">
<h2 id="table-title">{C.TABLE_TITLE}</h2>
<div class="cs-table" role="region" aria-labelledby="table-title" tabindex="0">
<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>
</div>
</div>
</section>""",
        # Zone 7: barrier product cards
        f"""<section class="cs cs-zone cs-zone--beige" id="barriers" aria-labelledby="barriers-title">
<div class="cs-zone__inner">
<h2 id="barriers-title">{C.BARRIERS_TITLE}</h2>
<p>{C.BARRIERS_INTRO}</p>
{disclosure()}
<ul class="cs-cards">{"".join(card(n, u, l, c) for n, u, l, c in C.BARRIERS)}</ul>
</div>
</section>""",
        # Zone 8: pairing cards
        f"""<section class="cs cs-zone cs-zone--mint" id="other-layers" aria-labelledby="pairs-title">
<div class="cs-zone__inner">
<h2 id="pairs-title">{C.PAIRS_TITLE}</h2>
<p>{C.PAIRS_INTRO}</p>
{disclosure()}
<ul class="cs-cards">{"".join(card(n, u, l, c) for n, u, l, c in C.PAIRS)}</ul>
</div>
</section>""",
    ]
    return "\n\n".join(block(z) for z in zones)


def not_built():
    return block(f"""
<section class="cs cs-zone cs-zone--green cs-hero" aria-labelledby="page-title">
<div class="cs-zone__inner">
<h1 id="page-title">{C.NOT_BUILT_TITLE}</h1>
<p>{C.NOT_BUILT_TEXT}</p>
<p><a href="{C.NOT_BUILT_LINK[1]}">{C.NOT_BUILT_LINK[0]}</a></p>
</div>
</section>""")


MAIN_OPEN = ('<!-- wp:group {"tagName":"main","anchor":"main","className":"cs-main","layout":{"type":"default"}} -->\n'
             '<main class="wp-block-group cs-main" id="main">')
MAIN_CLOSE = "</main>\n<!-- /wp:group -->"
PARTS = ('<!-- wp:template-part {"slug":"cs-header","tagName":"header","className":"cs-site-header"} /-->',
         '<!-- wp:template-part {"slug":"cs-footer","tagName":"footer","className":"cs-site-footer"} /-->')


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
