"""Rend les versions A4 (Paged.js) des dossiers imprimables en PDF : assets/pdf/<slug>.pdf.
Usage : python3 scripts/imprimer.py  (après generate_site.py), puis relancer generate_site.py."""
import http.server, threading, functools, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent
SLUGS = sys.argv[1:] or ["modele-ideal"]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
H = functools.partial(Q, directory=str(ROOT / "site"))
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
(ROOT / "assets" / "pdf").mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for slug in SLUGS:
        pg = b.new_page()
        pg.goto(f"http://127.0.0.1:{port}/dossiers/{slug}/imprimer/")
        pg.wait_for_function("document.querySelectorAll('.pagedjs_page').length > 0 && !!document.querySelector('.pagedjs_pages')", timeout=60000)
        pg.wait_for_timeout(2500)
        n = pg.evaluate("document.querySelectorAll('.pagedjs_page').length")
        over = pg.evaluate("[...document.querySelectorAll('.pagedjs_page')].map((p,i)=>{const a=p.querySelector('.pagedjs_page_content');return a&&a.scrollWidth>a.clientWidth+2?i+1+':'+[...a.querySelectorAll('*')].filter(e=>e.scrollWidth>a.clientWidth+2).slice(-1).map(e=>e.tagName+' '+(e.textContent||'').slice(0,60)).join(''):null}).filter(Boolean)")
        if "--png" in sys.argv[0:0] or True:
            (ROOT / "apercu" / "impr").mkdir(parents=True, exist_ok=True)
            for i, el in enumerate(pg.query_selector_all(".pagedjs_page")):
                el.screenshot(path=str(ROOT / "apercu" / "impr" / f"{slug}-{i+1:02d}.png"))
        out = ROOT / "assets" / "pdf" / f"{slug}.pdf"
        pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
        print(slug, n, "pages ; pages en débordement horizontal :", over, "→", out.stat().st_size // 1024, "Ko")
    b.close()
srv.shutdown()
