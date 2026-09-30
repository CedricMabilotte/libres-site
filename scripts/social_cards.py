#!/usr/bin/env python3
"""Vignettes 1200×630 (accueil + une par cas) → assets/cards/<uid>.jpg. Local (Playwright). Commit des JPEG."""
import asyncio, html, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import referentiel as R
from playwright.async_api import async_playwright
ROOT = R.ROOT; FONTS = (ROOT / "assets" / "fonts").as_uri()
E = html.escape
CSS = f"""@font-face{{font-family:S;src:url({FONTS}/source-serif-4-latin-opsz-normal.woff2)}}@font-face{{font-family:S;src:url({FONTS}/source-serif-4-latin-ext-opsz-normal.woff2);unicode-range:U+0100-02AF}}
@font-face{{font-family:P;src:url({FONTS}/ibm-plex-sans-latin-500-normal.woff2)}}
body{{margin:0;width:1200px;height:630px;background:#F5F2E9;color:#22201B;font-family:S;display:flex;flex-direction:column;justify-content:space-between;padding:64px 72px;box-sizing:border-box;border-bottom:14px solid #E2622E}}
.sur{{font:500 24px P;letter-spacing:.08em;text-transform:uppercase;color:#A8451A}}h1{{font-size:68px;line-height:1.05;margin:18px 0 0;font-weight:600;letter-spacing:-.01em}}
.meta{{font:500 26px P;color:#58534A}}.e{{display:flex;gap:10px}}.e i{{width:44px;height:44px;border:3px solid #58534A;box-sizing:border-box;position:relative}}
.e i.oui{{background:#1C4A32;border-color:#1C4A32}}.e i.partiel{{background:linear-gradient(135deg,#B9832E 50%,transparent 50%);border-color:#8A5F1E}}.e i.non{{border-color:#A8451A}}.e i.non::after{{content:"";position:absolute;inset:18px 2px;border-top:3px solid #A8451A;transform:rotate(45deg)}}.e i.inconnu{{border-style:dotted;border-color:#6E685C}}
.bas{{display:flex;justify-content:space-between;align-items:flex-end}}.m{{font:600 40px S}}.m span{{color:#E2622E}}"""
async def main():
    fiches, _ = R.charger()
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1200, "height": 630})
        items = [("_accueil", "Collectifs autogérés et lieux en communs · France depuis 1789", "Les collectifs qui ont voulu tenir un lieu en commun, et ce qui leur a manqué", f"{len(fiches)} cas instruits · cinq portes · prismes croisés", None)]
        for d in fiches:
            st, _, pv = R.calcul(d)
            l = d.get("localisation") or {}
            items.append((d["uid"], R.FAMILLES[d["famille"]] + " · " + R.STATUTS[st][0], d["nom"], f'{l.get("commune") or ""}{" · depuis " + str(d["debut"]) if d.get("debut") and not d.get("fin") else (" · " + str(d["debut"]) + "–" + str(d["fin"]) if d.get("debut") else "")}', pv))
        for uid, sur, titre, meta, pv in items:
            emp = "".join(f'<i class="{pv[k]}"></i>' for k in R.PKEYS) if pv else ""
            await pg.set_content(f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div><div class=sur>{E(sur)}</div><h1>{E(titre)}</h1></div><div class=meta>{E(meta)}</div><div class=bas><div class=e>{emp}</div><div class=m>libres<span>.</span>actitude.org</div></div></body></html>')
            await pg.wait_for_timeout(120)
            await pg.screenshot(path=str(ROOT / "assets" / "cards" / f"{uid}.jpg"), type="jpeg", quality=82)
        await b.close()
    print(len(items), "vignettes")
asyncio.run(main())
