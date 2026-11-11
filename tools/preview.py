#!/usr/bin/env python3
"""Local check without Playground: assemble header part + page content + footer part with the
child stylesheet, open it in Chromium at several widths, and audit the result.

The parent theme's defaults that matter are imitated (a non-Verdana body font, 1.2rem flow
gaps, light heading weight), so any element the child theme forgets to style shows up as a
wrong font, size or weight in the audit.

Usage: python3 tools/preview.py v1-strict [v2-creative]   (screenshots go to build/preview/)
"""
import json, os, re, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "preview")
PARENT_IMITATION = """
body{margin:0;font-family:Georgia,serif;font-size:1.13rem;line-height:1.4;letter-spacing:-0.1px;color:#111111;background:#FFFFFF}
h1,h2,h3{font-weight:400;line-height:1.125;letter-spacing:-0.1px}
:where(.wp-site-blocks) > * {margin-block-start:1.2rem}
:where(.is-layout-flow) > * {margin-block-start:1.2rem;margin-block-end:0}
:where(.is-layout-flow) > :first-child {margin-block-start:0}
a{color:#111111}
"""

def strip_blocks(html):
    return re.sub(r"<!-- /?wp:[^>]*?-->", "", html)

def assemble(version, kind="page"):
    vdir = os.path.join(ROOT, "versions", version)
    theme = os.path.join(vdir, "theme")
    css = open(os.path.join(theme, "style.css"), encoding="utf-8").read()
    extra_head = ""
    fn = open(os.path.join(theme, "functions.php"), encoding="utf-8").read()
    for url in re.findall(r"'(https://fonts\.googleapis\.com/[^']+)'", fn):
        extra_head += f'<link rel="stylesheet" href="{url}">'
    header = strip_blocks(open(os.path.join(theme, "parts", "cs-header.html"), encoding="utf-8").read())
    footer = strip_blocks(open(os.path.join(theme, "parts", "cs-footer.html"), encoding="utf-8").read())
    pre = "fg" if version.startswith("v2") else "cs"
    if kind == "page":
        body = '<div class="entry-content wp-block-post-content is-layout-flow">' + strip_blocks(open(os.path.join(vdir, "content", "guide.html"), encoding="utf-8").read()) + "</div>"
    else:
        tpl = open(os.path.join(theme, "templates", "404.html"), encoding="utf-8").read()
        body = strip_blocks(re.search(r'<main[^>]*>(.*)</main>', tpl, re.S).group(1))
    body = body.replace("__PHOTO_URL__", "file://" + os.path.join(ROOT, "assets", "20261111-MosquitoBite.webp"))
    js = "".join(open(os.path.join(theme, f), encoding="utf-8").read() for f in sorted(os.listdir(theme)) if f.endswith(".js"))
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"{extra_head}<style>{PARENT_IMITATION}</style><style>{css}</style></head><body>"
            f"<div class='wp-site-blocks'><header class='wp-block-template-part {pre}-site-header'>{header}</header>"
            f"<main class='wp-block-group {pre}-main is-layout-flow' id='main'>{body}</main>"
            f"<footer class='wp-block-template-part {pre}-site-footer'>{footer}</footer></div><script>{js}</script></body></html>")

AUDIT = r"""() => {
 const R={overflowPx: document.documentElement.scrollWidth - innerWidth, fonts:{}, sizes:{}, colors:{}, bg:{}, italic:0, issues:[]};
 const vis=e=>{const r=e.getBoundingClientRect();const s=getComputedStyle(e);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'};
 const rgb2hex=c=>{const m=c.match(/\d+(\.\d+)?/g);if(!m)return c;if(m.length>3&&+m[3]===0)return 'transparent';return '#'+m.slice(0,3).map(x=>(+x).toString(16).padStart(2,'0')).join('').toUpperCase()};
 const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
 while(w.nextNode()){const n=w.currentNode;if(!n.textContent.trim())continue;const e=n.parentElement;if(!vis(e))continue;
  const s=getComputedStyle(e);const f=s.fontFamily.split(',')[0].replace(/["']/g,'').trim();R.fonts[f]=(R.fonts[f]||0)+1;
  const k=(parseFloat(s.fontSize)/16).toFixed(3)+'rem/'+s.fontWeight;R.sizes[k]=(R.sizes[k]||0)+1;
  const c=rgb2hex(s.color);R.colors[c]=(R.colors[c]||0)+1;if(s.fontStyle!=='normal')R.italic++;}
 for(const e of document.querySelectorAll('body *')){if(!vis(e))continue;const s=getComputedStyle(e);
  for(const p of ['backgroundColor','borderTopColor']){const c=rgb2hex(s[p]);if(c!=='transparent'&&!(p==='borderTopColor'&&parseFloat(s.borderTopWidth)===0))R.bg[c]=(R.bg[c]||0)+1;}
  const r=e.getBoundingClientRect();if(r.right>innerWidth+0.5&&!e.closest('[role=region]'))R.issues.push('wide '+e.tagName+'.'+e.className);}
 const q=s=>[...document.querySelectorAll(s)].filter(vis).map(e=>e.getBoundingClientRect());
 R.cards=[...new Set(q('.cs-card,.fg-card').map(r=>Math.round(r.width)))];
 R.cardRows=[...new Set(q('.cs-cards').map(()=>0))];
 R.perRow=[...document.querySelectorAll('.cs-cards,.fg-cards,.fg-pairs')].map(ul=>{const tops=[...ul.children].map(li=>Math.round(li.getBoundingClientRect().top));return tops.filter(t=>t===tops[0]).length});
 R.window=q('.cs-window,.fg-window').slice(0,1).map(r=>Math.round(r.width)+'x'+Math.round(r.height));
 R.photo=q('.cs-photo img,.fg-plate img').map(r=>Math.round(r.width)+'x'+Math.round(r.height));
 R.menu=q('.cs-menu-button,.fg-menu-button').map(r=>Math.round(r.width)+'x'+Math.round(r.height));
 R.navTops=[...new Set(q('.cs-nav li,.fg-nav li').map(r=>Math.round(r.top)))];
 R.layersPerRow=(()=>{const l=q('.cs-layer,.fg-step');return l.filter(r=>Math.round(r.top)===Math.round(l[0]&&l[0].top)).length})();
 const t=document.querySelector('.cs-table,.fg-table');if(t)R.table=t.clientWidth+'/'+t.scrollWidth;
 R.text=document.body.innerText; return R;}"""

def run(versions, widths=(1440, 1024, 768, 600, 360)):
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for v in versions:
            for kind in ("page", "404"):
                path = os.path.join(OUT, f"{v}-{kind}.html")
                open(path, "w", encoding="utf-8").write(assemble(v, kind))
                for w in (widths if kind == "page" else (1440, 360)):
                    pg = b.new_page(viewport={"width": w, "height": 900})
                    pg.goto("file://" + path, wait_until="networkidle")
                    r = pg.evaluate(AUDIT)
                    text = r.pop("text")
                    print(f"\n== {v} {kind} @ {w}px  overflow={r['overflowPx']}  menu={r['menu']} navRowTops={r['navTops']}")
                    for k in ("fonts", "sizes", "colors", "bg"):
                        print(f"   {k}: {r[k]}")
                    print(f"   italic={r['italic']} cards={r['cards']} perRow={r['perRow']} layersPerRow={r['layersPerRow']} window={r['window']} photo={r['photo']} table={r.get('table')}")
                    if r["issues"]:
                        print("   ISSUES", r["issues"][:6])
                    if "[" in text or ">>" in text:
                        print("   ISSUE: [ or >> in visible text")
                    shot = os.path.join(OUT, f"{v}-{kind}-{w}.png")
                    pg.screenshot(path=shot, full_page=True)
                    if kind == "page" and w == 360:
                        btn = pg.query_selector(".cs-menu-button,.fg-menu-button")
                        if btn and btn.is_visible():
                            btn.click()
                            pg.screenshot(path=os.path.join(OUT, f"{v}-menu-open-360.png"), clip={"x": 0, "y": 0, "width": 360, "height": 560})
                    pg.close()
        b.close()

if __name__ == "__main__":
    run(sys.argv[1:] or ["v1-strict"])
