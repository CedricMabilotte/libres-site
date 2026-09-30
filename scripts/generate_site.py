#!/usr/bin/env python3
"""Génère libres.actitude.org depuis data/ (fiches, regards) et analyses/analyses.json vers site/.
Seule dépendance : pyyaml. Les garde-fous font échouer la génération.
"""
import csv, html, io, json, re, shutil, subprocess, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import referentiel as R

ROOT = R.ROOT
OUT = ROOT / "site"
ASSETS = ROOT / "assets"
BASE = "https://libres.actitude.org"
REPO = "https://github.com/CedricMabilotte/libres-site"
COMMUNS = "https://communs.actitude.org"
BIBLIO = "https://biblio.actitude.org"
CONTACT = "contact@actitude.org"
LICENCE_URL = "https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr"
VERSION = "0.1"
MOTS_PROSCRITS = ["résilience", "résilient", "paradigme", "empowerment", "impact"]
PROVENANCE = [r"\bIA\b", r"intelligence artificielle", r"(?<!Saint-)\bClaude\b", r"généré automatiquement", r"\bLLM\b", r"subagent", r"Anthropic"]
E = html.escape
erreurs = []

def err(m):
    erreurs.append(m)

fiches, regards = R.charger()
AN = json.loads((ROOT / "analyses" / "analyses.json").read_text(encoding="utf-8"))
PAR_UID = {d["uid"]: d for d in fiches}

# ------------------------------------------------------------------ garde-fous données
FORMES_OK = set(k for k in R.FORMES if k)
for d in fiches:
    u = d.get("uid")
    if d["_fichier"] != f"{u}.yml":
        err(f"{d['_fichier']} : uid ≠ nom de fichier")
    if d.get("famille") not in R.FAMILLES:
        err(f"{u} : famille hors cadre")
    ns = len(d.get("sources") or [])
    if ns == 0:
        err(f"{u} : aucune source")
    for k in R.PKEYS:
        p = (d.get("portes") or {}).get(k) or {}
        if p.get("valeur") not in R.PVAL:
            err(f"{u} : porte {k} valeur hors cadre")
        if p.get("valeur") == "oui" and (not p.get("note") or not p.get("source")):
            err(f"{u} : porte {k} franchie sans note ni source")
        s = p.get("source")
        if isinstance(s, int) and not (1 <= s <= ns):
            err(f"{u} : porte {k} source {s} hors bornes")
    for k, (lib, multi, vals) in R.DIM.items():
        dv = (d.get("dimensions") or {}).get(k) or {}
        v = dv.get("valeur")
        for x in (v if isinstance(v, list) else [v]):
            if x not in (None, "inconnu") and x not in vals:
                err(f"{u} : {k}={x} hors cadre")
        s = dv.get("source")
        if isinstance(s, int) and not (1 <= s <= ns):
            err(f"{u} : dimension {k} source {s} hors bornes")
    for c in d.get("chronologie") or []:
        s = c.get("source")
        if isinstance(s, int) and not (1 <= s <= ns):
            err(f"{u} : chronologie source {s} hors bornes")
    for k in ("porteur_forme",):
        if (d.get("foncier") or {}).get(k) not in FORMES_OK | {None, "inconnu"}:
            err(f"{u} : foncier.{k} hors cadre")
    if (d.get("collectif") or {}).get("forme") not in FORMES_OK:
        err(f"{u} : collectif.forme hors cadre")
for voix in ("igor", "eozen", "antimeta"):
    for u in (regards.get(voix) or {}).get("faces", {}):
        if u not in PAR_UID:
            err(f"regards/{voix} : uid inconnu {u}")
for m in (regards.get("antimeta") or {}).get("mecanismes", []):
    for u in m["exemples"]:
        if u not in PAR_UID:
            err(f"mécanisme {m['cle']} : uid inconnu {u}")

# ------------------------------------------------------------------ calculs
for d in fiches:
    st, manque, p = R.calcul(d)
    d["_statut"], d["_manque"], d["_p"] = st, manque, p
    d["_periode"] = R.periode(d.get("debut"))
    d["_verrou"] = R.verrou_type(d)
    d["_faces"] = {v: ((regards.get(v) or {}).get("faces") or {}).get(d["uid"]) for v in ("igor", "eozen", "antimeta")}
    d["_avant1901"] = isinstance(d.get("debut"), int) and d["debut"] < 1901
ORDRE_ST = {"corpus": 0, "corpus_sous_condition": 1, "seuil": 2, "epreuve": 3}
fiches.sort(key=lambda d: (ORDRE_ST[d["_statut"]], len(d["_manque"]), d["nom"].lower()))
CNT = Counter(d["_statut"] for d in fiches)

# ------------------------------------------------------------------ gabarit
NAV = [("", "Accueil"), ("fiches/", "Les cas"), ("portes/", "Les portes"), ("prismes/", "Prismes"), ("dossiers/association-agricole/", "Dossier"),
       ("carte/", "Carte"), ("frise/", "Frise"), ("regards/", "Regards"), ("methode/", "Méthode")]

def rel(depth):
    return "../" * depth

def page(chemin, titre, corps, description="", depth=None, image="_accueil"):
    depth = chemin.count("/") if depth is None else depth
    r = rel(depth)
    nav = "".join(f'<a href="{r}{h}"{" aria-current=page" if (h and chemin.startswith(h)) or (not h and chemin == "") else ""}>{E(l)}</a>' for h, l in NAV)
    t = f"{titre} — libres" if titre != "libres" else "libres — collectifs autogérés et lieux en communs en France depuis 1789"
    desc = description or "Collectifs autogérés de droit civil installés sur des lieux tenus en communs en France depuis 1789 : fiches sourcées, portes, prismes."
    canon = f"{BASE}/{chemin}"
    doc = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{E(t)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:image" content="{BASE}/assets/cards/{image}.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{r}assets/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head><body>
<a class="saut" href="#contenu">Aller au contenu</a>
<header class="site"><div class="in"><a class="marque" href="{r}">libres<span>.</span></a>
<nav class="principale" aria-label="Principale">{nav}</nav>
<button class="theme" type="button" data-theme-toggle aria-label="Basculer le thème clair ou sombre">clair / sombre</button></div></header>
<main id="contenu">{corps}</main>
<footer class="site"><div class="in"><div>Texte : igor, avec les regards d'eozen et d'antimeta · © Cedric Mabilotte · <a href="{LICENCE_URL}" rel="license">CC BY-NC-SA 4.0</a><br>
Version {VERSION} · <a href="{r}donnees/">Données</a> · <a href="{r}droit-de-reponse/">Droit de réponse</a> · <a href="{r}a-propos/">À propos</a> · <a href="{r}mentions-legales/">Mentions légales</a></div>
<div>Sites frères : <a href="{COMMUNS}">communs.actitude.org</a> (montages fonciers) · <a href="{BIBLIO}">biblio.actitude.org</a> (sources)</div></div></footer>
<script src="{r}assets/theme.js" defer></script>
</body></html>"""
    dest = OUT / chemin / "index.html" if (chemin == "" or chemin.endswith("/")) else OUT / chemin
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc, encoding="utf-8")
    PAGES.append(chemin)

PAGES = []

def empreinte(d, grand=False):
    cases = "".join(f'<i class="{d["_p"][k]}" title="{code} {E(lib)} : {E(R.PVAL[d["_p"][k]])}"></i>' for k, code, lib, _ in R.PORTES)
    txt = " ; ".join(f'{code} {R.PVAL[d["_p"][k]].lower()}' for k, code, lib, _ in R.PORTES)
    return f'<span class="empreinte{" grand" if grand else ""}" role="img" aria-label="Portes : {E(txt)}">{cases}</span>'

def statut(d):
    lib = R.STATUTS[d["_statut"]][0]
    return f'<span class="statut {d["_statut"]}">{E(lib)}</span>'

def legende():
    items = "".join(f'<span><span class="empreinte" aria-hidden="true"><i class="{v}"></i></span>{E(l)}</span>' for v, l in R.PVAL.items())
    return f'<div class="legende" aria-label="Légende des portes">{items}<span>· ordre : P1 forme civile, P2 foncier, P3 intérêt général, P4 autogestion, P5 établi</span></div>'

def lieu(d):
    l = d.get("localisation") or {}
    c = l.get("commune") or "commune non publiée"
    dep = f" ({l['departement']})" if l.get("departement") else ""
    return f"{c}{dep}"

def dates(d):
    a, b = d.get("debut"), d.get("fin")
    a = a if a else "date non établie"
    if b:
        return f"{a}–{b}"
    etat = R.val(d, "etat")
    return f"depuis {a}" if etat != "disparu" else f"{a}–?"

def lib_dim(k, v):
    if v in (None, "inconnu"):
        return "non établi"
    vals = R.DIM[k][2]
    if isinstance(v, list):
        return ", ".join(vals.get(x, x) for x in v if x != "inconnu") or "non établi"
    return vals.get(v, v)

def carte_cas(d, r):
    manque = ", ".join(next(c for k, c, _, _ in R.PORTES if k == m) for m in d["_manque"]) or "aucune"
    return f"""<article class="carte-cas"><div>{statut(d)} {empreinte(d)}</div>
<h3><a href="{r}f/{d['uid']}/">{E(d['nom'])}</a></h3><p class="meta">{E(lieu(d))} · {E(dates(d))} · {E(R.FAMILLES[d['famille']])}<br>Porte(s) manquante(s) : {E(manque)}</p></article>"""

def para(t):
    return "".join(f"<p>{E(x.strip())}</p>" for x in (t or "").strip().split("\n\n") if x.strip())

# ------------------------------------------------------------------ préparation sortie
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
shutil.copytree(ASSETS, OUT / "assets", ignore=shutil.ignore_patterns("france-departements.json"))
for d in fiches:
    if not (ASSETS / "cards" / f"{d['uid']}.jpg").exists():
        err(f"{d['uid']} : vignette manquante (python3 scripts/social_cards.py)")
(OUT / "CNAME").write_text("libres.actitude.org\n")
PRISMES = {}
pp = ROOT / "data" / "prismes.yml"
if pp.exists():
    import yaml
    PRISMES = yaml.safe_load(pp.read_text(encoding="utf-8")) or {}
nb = len(fiches)
seuil = [d for d in fiches if d["_statut"] == "seuil"]
corpus = [d for d in fiches if d["_statut"] in ("corpus", "corpus_sous_condition")]
EC = AN["echecs_par_porte"]

def entonnoir_svg():
    w, h, bh = 640, 40 * 6 + 10, 26
    items = [(f"{nb} cas instruits", nb)] + [(f'{e["porte"]} {e["libelle"]}', e["restent"]) for e in AN["entonnoir"]]
    rows = []
    for i, (lib, n) in enumerate(items):
        y = 8 + i * 40
        bw = max(2, 400 * n / nb)
        rows.append(f'<text x="0" y="{y+17}">{E(lib)}</text><rect class="barre" x="200" y="{y}" width="{bw:.1f}" height="{bh}"/><text x="{200+bw+8:.1f}" y="{y+17}">{n}</text>')
    return f'<svg class="entonnoir" viewBox="0 0 {w} {h}" role="img" aria-labelledby="ent-t"><title id="ent-t">Nombre de cas qui franchissent chaque porte, cumulativement</title>{"".join(rows)}</svg>'

# ------------------------------------------------------------------ accueil
these = (regards.get("contradicteur") or {}).get("these", "")
corps = f"""<p class="sur">Version {VERSION} · {nb} cas instruits · 1789–2026</p>
<h1>Les collectifs qui ont voulu tenir un lieu en commun, et ce qui leur a manqué</h1>
<p class="chapeau">libres documente les collectifs autogérés qui se sont installés sur un lieu en France depuis la Révolution pour le tenir hors du marché, en droit civil et pour l'intérêt général. Chaque cas passe cinq portes. Celles qu'il ne franchit pas sont publiées avec lui.</p>
<div class="chiffres"><div><b>{nb}</b><span>cas instruits, de 1832 à 2022</span></div>
<div><b>{CNT.get('corpus',0)+CNT.get('corpus_sous_condition',0)}</b><span>franchissent les cinq portes, dont {CNT.get('corpus_sous_condition',0)} sous condition</span></div>
<div><b>{CNT.get('seuil',0)}</b><span>au seuil : une seule porte manque</span></div>
<div><b>{EC['foncier_verrouille']}</b><span>sur {nb} ne franchissent pas la porte du foncier</span></div></div>
<blockquote class="these">{E(these.strip())}</blockquote>
<figure>{entonnoir_svg()}<figcaption>Lecture cumulative : combien de cas restent après chaque porte, dans l'ordre P1 à P5. {AN['entonnoir'][0]['restent']} franchissent la forme civile ; {AN['entonnoir'][1]['restent']} franchissent ensuite le foncier. <a href="portes/">Détail des portes et analyse de sensibilité</a>.</figcaption></figure>
<h2>Le corpus et le seuil</h2>
{legende()}
<div class="cartes">{"".join(carte_cas(d, "") for d in corpus + seuil)}</div>
<p><a href="fiches/">Voir les {nb} cas, épreuves comprises</a> · <a href="prismes/">Lire les prismes croisés</a> · <a href="regards/">Les trois regards</a></p>
<h2>Ce que libres n'est pas</h2>
<div class="texte"><p>Ni un palmarès, ni un annuaire des lieux sympathiques. Les contre-modèles souvent présentés comme des communs (foncières et fermes Terre de Liens, écolieux adossés à la Coopérative Oasis, SCI ou SCIC « de transition ») sont instruits avec la même grille et publiés comme épreuves : la critique porte sur le montage, jamais sur les personnes. Le montage foncier détaillé de chaque lieu relève de <a href="{COMMUNS}">communs.actitude.org</a>.</p></div>"""
page("", "libres", corps)

# ------------------------------------------------------------------ liste des cas
opts = lambda dic: "".join(f'<option value="{k}">{E(v)}</option>' for k, v in dic.items())
lignes = []
for d in fiches:
    manque = " ".join(d["_manque"])
    lignes.append(f"""<tr data-famille="{d['famille']}" data-statut="{d['_statut']}" data-periode="{d['_periode'] or ''}" data-manque="{manque}" data-texte="{E((d['nom']+' '+lieu(d)+' '+' '.join(d.get('autres_noms') or [])).lower())}">
<td><a href="../f/{d['uid']}/">{E(d['nom'])}</a><br><span class="petit">{E(lieu(d))}</span></td><td>{E(dates(d))}</td><td>{E(R.FAMILLES[d['famille']])}</td><td>{empreinte(d)}</td><td>{statut(d)}</td></tr>""")
corps = f"""<h1>Les {nb} cas instruits</h1>
<p class="chapeau">Tous les cas sont publiés, qu'ils franchissent les portes ou non. Le statut se calcule à partir des portes ; il n'est jamais saisi.</p>
{legende()}
<form class="filtres" aria-label="Filtrer les cas" onsubmit="return false">
<label>Recherche<input type="search" id="q" placeholder="nom, commune…"></label>
<label>Famille<select id="f-famille"><option value="">toutes</option>{opts(R.FAMILLES)}</select></label>
<label>Statut<select id="f-statut"><option value="">tous</option>{opts({k: v[0] for k, v in R.STATUTS.items()})}</select></label>
<label>Période<select id="f-periode"><option value="">toutes</option>{opts({p[2]: p[2] for p in R.PERIODES})}</select></label>
<label>Porte manquante<select id="f-manque"><option value="">toutes</option>{opts({k: f'{c} {l}' for k, c, l, _ in R.PORTES})}</select></label>
</form>
<p class="petit" id="compte" aria-live="polite">{nb} cas affichés</p>
<div class="defile"><table id="table-cas"><thead><tr><th>Cas</th><th>Dates</th><th>Famille</th><th>Portes</th><th>Statut</th></tr></thead><tbody>{"".join(lignes)}</tbody></table></div>
<script src="../assets/fiches.js" defer></script>"""
page("fiches/", "Les cas", corps)

# ------------------------------------------------------------------ fiche
def srcref(d, n):
    return f'<sup class="src"><a href="#s{n}" aria-label="source {n}">[{n}]</a></sup>' if isinstance(n, int) else ""

for i, d in enumerate(fiches):
    u = d["uid"]
    ptxt = "".join(f"""<li><span class="code">{code}</span><div><span class="v {d['_p'][k]}">{E(R.PVAL[d['_p'][k]])}</span> · <b>{E(lib)}</b><br>{E(((d['portes'].get(k) or {}).get('note') or '').strip())}{srcref(d, (d['portes'].get(k) or {}).get('source'))}</div></li>""" for k, code, lib, _ in R.PORTES)
    faces = ""
    for v, lib in (("igor", "igor · le collectif vécu"), ("eozen", "eozen · le montage"), ("antimeta", "antimeta · la capture")):
        if d["_faces"].get(v):
            faces += f'<div class="face {v}"><p class="qui">{E(lib)}</p>{para(d["_faces"][v])}</div>'
    if faces:
        faces = f"<h2>Trois regards</h2>{faces}"
    dims = "".join(f"<tr><th scope=row>{E(R.DIM[k][0])}</th><td>{E(lib_dim(k, ((d['dimensions'].get(k) or {}).get('valeur'))))}{srcref(d, (d['dimensions'].get(k) or {}).get('source'))}<br><span class=petit>{E(((d['dimensions'].get(k) or {}).get('note') or '').strip())}</span></td></tr>" for k in R.DIM if k != "fin" or R.val(d, 'fin'))
    chrono = "".join(f"<li><b>{E(str(c.get('annee') or ''))}</b>{E(c.get('evenement') or '')}{srcref(d, c.get('source'))}</li>" for c in d.get("chronologie") or [])
    fia = d.get("fiabilite") or {}
    fiab = ""
    if fia.get("verifie"):
        fiab += "<h3>Établi par les sources</h3><ul>" + "".join(f"<li>{E(x)}</li>" for x in fia["verifie"]) + "</ul>"
    if fia.get("non_confirme"):
        fiab += "<h3>Non confirmé</h3><ul>" + "".join(f"<li>{E(x)}</li>" for x in fia["non_confirme"]) + "</ul>"
    srcs = "".join(f'<li id="s{j}">{E(s.get("auteur") or "")}{", " if s.get("auteur") else ""}<a href="{E(s.get("url") or "")}" rel="noopener">{E(s.get("titre") or s.get("url") or "")}</a>{", " + str(s["annee"]) if s.get("annee") else ""}.</li>' for j, s in enumerate(d.get("sources") or [], 1))
    col, fon = d.get("collectif") or {}, d.get("foncier") or {}
    lc = (d.get("liens") or {}).get("communs")
    communs = f'<dt>Montage détaillé</dt><dd><a href="{COMMUNS}/l/{lc}/">fiche sur communs.actitude.org</a></dd>' if lc else ""
    avant = '<p class="note-prudence">Avant 1901, la liberté d\'association n\'existe pas en France : la porte P1 était juridiquement indisponible. Ce cas est lu avec la grille, mais son échec en P1 est d\'abord un fait d\'époque.</p>' if d["_avant1901"] else ""
    cond = f'<p class="note-prudence">{E(R.STATUTS[d["_statut"]][1])}</p>' if d["_statut"] == "corpus_sous_condition" else ""
    dj = f'<h2>Dossier juridique</h2>{para(d.get("dossier_juridique"))}<p class="petit">Information générale, pas un conseil. Voir aussi le <a href="../../dossiers/association-agricole/">dossier « association et activité agricole »</a>.</p>' if d.get("dossier_juridique") else ""
    prev_, next_ = fiches[i - 1], fiches[(i + 1) % len(fiches)]
    corps = f"""<p class="sur">{E(R.FAMILLES[d['famille']])}</p><h1>{E(d['nom'])}</h1>
<p class="meta">{E(lieu(d))} · {E(dates(d))}{' · aussi : ' + E(', '.join(d['autres_noms'])) if d.get('autres_noms') else ''}</p>
<p>{statut(d)} {empreinte(d, True)}</p>{cond}{avant}
<div class="grille-fiche"><div class="texte">
<p class="chapeau">{E((d.get('resume') or '').strip())}</p>
<h2>Les cinq portes</h2><ul class="portes-liste">{ptxt}</ul>
{faces}
{dj}<h2>Chronologie</h2><ul class="chrono">{chrono}</ul>
<h2>Prismes</h2><div class="defile"><table>{dims}</table></div>
<h2>Fiabilité</h2>{fiab}
<h2>Sources</h2><ol class="sources">{srcs}</ol>
</div><aside class="cote"><dl>
<dt>Collectif</dt><dd>{E(col.get('nom') or 'non établi')}<br><span class=petit>{E(R.FORMES.get(col.get('forme'), 'non établie'))}{', ' + str(col['annee']) if col.get('annee') else ''}</span></dd>
<dt>Propriétaire du foncier</dt><dd>{E(fon.get('porteur') or 'non établi')}<br><span class=petit>{E(R.FORMES.get(fon.get('porteur_forme'), 'non établie'))}</span></dd>
<dt>Surface</dt><dd>{E(str(fon['surface_ha']) + ' ha') if fon.get('surface_ha') else 'non établie'}</dd>
<dt>Durée du titre</dt><dd>{E(str(fon['titre_duree_ans']) + ' ans') if fon.get('titre_duree_ans') else 'non établie'}</dd>
<dt>Type de verrou</dt><dd>{ {'par_propriete': 'par la propriété', 'par_titre': 'par un titre consenti', 'aucun': 'aucun établi'}[d['_verrou']] }</dd>
<dt>Période</dt><dd>{E(d['_periode'] or 'non établie')}</dd>{communs}
<dt>Citer</dt><dd class="petit">« {E(d['nom'])} », libres.actitude.org, v{VERSION}, {BASE}/f/{u}/</dd>
</dl><p class="petit"><a href="../{prev_['uid']}/">← {E(prev_['nom'])}</a><br><a href="../{next_['uid']}/">{E(next_['nom'])} →</a></p>
<p class="petit">Une erreur, un fait manquant ? <a href="../../droit-de-reponse/">Droit de réponse</a></p></aside></div>"""
    page(f"f/{u}/", d["nom"], corps, description=(d.get("resume") or "")[:200], image=u)

# ------------------------------------------------------------------ portes
PORTES_CNT = AN["portes"]
rows = "".join(f"<tr><th scope=row>{code} {E(lib)}</th>" + "".join(f"<td class=n>{PORTES_CNT[code].get(v, 0)}</td>" for v in R.PVAL) + f"<td class=n><b>{EC[k]}</b></td></tr>" for k, code, lib, _ in R.PORTES)
sens = "".join(f"<tr><th scope=row>{E(s['libelle'])}</th><td class=n>{s['corpus']+s['corpus_sous_condition']}</td><td class=n>{s['seuil']}</td><td class=n>{s['epreuve']}</td><td>{', '.join(f'<a href=../f/{u}/>{E(PAR_UID[u][chr(110)+chr(111)+chr(109)])}</a>' for u in s['admis']) or '—'}</td></tr>" for s in AN["sensibilite"].values())
vt = Counter(d["_verrou"] for d in fiches)
regle = (regards.get("eozen") or {}).get("regle_p2", "")
avant = [d for d in fiches if d["_avant1901"]]
corps = f"""<h1>Les cinq portes</h1>
<p class="chapeau">Un cas entre au corpus seulement s'il franchit les cinq. Une porte partielle, refusée ou non établie le range parmi les épreuves, publiées avec la porte où il s'arrête.</p>
<div class="defile"><table><thead><tr><th>Porte</th>{''.join(f'<th class=n>{E(v)}</th>' for v in R.PVAL.values())}<th class=n>Ne franchit pas</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="petit">« Ne franchit pas » additionne partielle, non franchie et non établie. Total : {nb} cas.</p>
<figure>{entonnoir_svg()}<figcaption>Franchissements cumulés dans l'ordre P1 → P5.</figcaption></figure>
<h2>Au seuil : une porte manque</h2>
<div class="texte"><p>{len(seuil)} cas franchissent quatre portes sur cinq. Porte manquante : {", ".join(f"{sum(1 for d in seuil if k in d['_manque'])} × {c} {l.lower()}" for k, c, l, _ in R.PORTES if any(k in d['_manque'] for d in seuil))}. Aucun n'a de maillon commercial dans son usage ; là où le foncier retient, le verrou repose sur une relation (une majorité municipale, un conseil de fonds libre de vendre), pas sur un acte.</p></div>
<div class="cartes">{''.join(carte_cas(d, '../') for d in seuil)}</div>
<h2>Deux sortes de verrou</h2>
<div class="texte"><p>Le <b>verrou par la propriété</b> tient le lieu dans une structure qui ne peut pas le vendre (inaliénabilité, domanialité, dévolution, veto de réseau). Le <b>verrou par un titre</b> protège l'usage par un bail long consenti par un propriétaire qui, lui, reste libre de vendre le fonds : il tient tant que le bail court. Un cas franchit les cinq portes par un titre (La Chapelle) : il est affiché « corpus sous condition ». Les deux autres (La Déviation, Manifesten) tiennent par le veto du réseau CLIP, établi par des sources concordantes mais inscrit dans aucun acte publié.</p>
<p class="petit">Répartition : verrou par la propriété {vt.get('par_propriete',0)} · par un titre {vt.get('par_titre',0)} · aucun établi {vt.get('aucun',0)}.</p>
<div class="face eozen"><p class="qui">eozen · la règle P2</p>{para(regle)}</div></div>
<h2>Sensibilité : ce que devient le résultat si l'on assouplit</h2>
<div class="texte"><p>Le cadre est strict par choix. Pour qu'on puisse juger ce choix, voici le même corpus lu avec des portes assouplies une à une.</p></div>
<div class="defile"><table><thead><tr><th>Variante</th><th class=n>Admis</th><th class=n>Au seuil</th><th class=n>Épreuves</th><th>Cas admis</th></tr></thead><tbody>{sens}</tbody></table></div>
<p class="note-prudence">Même en tenant toute porte partielle pour franchie, moins d'un cas sur quatre entre au corpus. Le résultat ne tient pas qu'à la sévérité du cadre, mais la sévérité compte : c'est pourquoi elle est affichée. Historique : sous la première lecture de P2 (preuve de publication exigée, 30 septembre), un seul cas entrait.</p>
<h2>Avant 1901</h2>
<div class="texte"><p>Jusqu'à la loi du 1<sup>er</sup> juillet 1901, s'associer sans autorisation est interdit (loi Le Chapelier de 1791, article 291 du Code pénal). Les {len(avant)} cas antérieurs empruntent la forme de la société, faute de mieux : leur échec en P1 est d'abord un fait d'époque. Ils sont gardés parce qu'ils montrent ce que devient un lieu sans verrou.</p>
<p class="petit">{', '.join(f'<a href="../f/{d["uid"]}/">{E(d["nom"])}</a>' for d in avant)}</p></div>"""
page("portes/", "Les portes", corps, "Les cinq portes de libres, les cas au seuil, les deux sortes de verrou et l'analyse de sensibilité.")

# ------------------------------------------------------------------ prismes
V = AN["variables"]
HEAT = ["famille", "periode", "forme_collectif", "porteur", "acces", "titre", "verrou_type", "gouvernance", "economie", "ouverture", "rapport_etat", "transmission", "etat", "P1", "P2", "P3", "P4", "P5"]
HEAT = [h for h in HEAT if h in V]
def pv(a, b):
    return AN["paires"].get(f"{a}|{b}") or AN["paires"].get(f"{b}|{a}")
def cell(a, b):
    if a == b:
        return '<td aria-label="même variable">·</td>'
    c = pv(a, b)
    if not c:
        return '<td class="petit" title="effectif insuffisant">–</td>'
    alpha = min(1, c["v"]) * (0.9 if c["p"] < 0.05 else 0.35)
    marque = ("*" if c["p"] < 0.05 else "") + ("†" if c.get("mecanique") else "")
    return f'<td style="background:color-mix(in srgb,var(--brique) {alpha*100:.0f}%,transparent)" title="{E(V[a])} × {E(V[b])} : V={c["v"]}, p={c["p"]}, n={c["n"]}">{c["v"]:.2f}{marque}</td>'
heat = "<table class='heat'><thead><tr><th></th>" + "".join(f"<th class=c scope=col>{E(V[h])}</th>" for h in HEAT) + "</tr></thead><tbody>" + "".join(f"<tr><th class=r scope=row>{E(V[a])}</th>" + "".join(cell(a, b) for b in HEAT) + "</tr>" for a in HEAT) + "</tbody></table>"
fortes = [f for f in AN["fortes"] if not f["fragile"]][:18]
tf = "".join(f"<tr><td>{E(V[f['a']])} × {E(V[f['b']])}</td><td class=n>{f['v']:.2f}</td><td class=n>{f['p']:.3f}</td><td class=n>{f['n']}</td></tr>" for f in fortes)
lectures = ""
for pr in PRISMES.get("lectures", []):
    lectures += f'<div class="prisme"><h3>{E(pr["titre"])}</h3><p class="chiffre">{E(pr.get("chiffre",""))}</p>{para(pr["texte"])}</div>'
mec = (regards.get("antimeta") or {}).get("mecanismes", [])
mecs = "".join(f'<div><h3>{E(m["nom"])}</h3><p>{E(m["description"])}</p><p class="petit">Exemples : {", ".join(f"<a href=../f/{u}/>{E(PAR_UID[u][chr(110)+chr(111)+chr(109)])}</a>" for u in m["exemples"])}</p></div>' for m in mec)
# ACM
acm = AN["acm"]
xs = [p["x"] for p in acm["individus"]] + [m["x"] for m in acm["modalites"]]
ys = [p["y"] for p in acm["individus"]] + [m["y"] for m in acm["modalites"]]
x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
W, H, M = 760, 520, 40
sx = lambda x: M + (x - x0) / (x1 - x0 or 1) * (W - 2 * M)
sy = lambda y: H - M - (y - y0) / (y1 - y0 or 1) * (H - 2 * M)
coul = {"corpus": "var(--foret)", "corpus_sous_condition": "var(--brique)", "seuil": "var(--ocre-texte)", "epreuve": "var(--inconnu)"}

def marque(st, x, y, k=1.0):
    """Forme + couleur par statut (jamais la couleur seule)."""
    if st in ("corpus", "corpus_sous_condition"):
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7*k:.1f}" fill="{coul[st]}"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{11*k:.1f}" fill="none" stroke="{coul[st]}" stroke-width="{2*k:.1f}"/>'
    if st == "seuil":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7*k:.1f}" fill="var(--papier)" stroke="var(--ocre-texte)" stroke-width="{3.5*k:.1f}"/>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5*k:.1f}" fill="var(--inconnu)" fill-opacity=".55" stroke="var(--inconnu)" stroke-width="{1.2*k:.1f}" stroke-dasharray="{2*k:.1f} {1.5*k:.1f}"/>'

pts = "".join(f'<a href="../f/{p["uid"]}/"><g>{marque(PAR_UID[p["uid"]]["_statut"], sx(p["x"]), sy(p["y"]), .8)}<title>{E(PAR_UID[p["uid"]]["nom"])} — {E(R.STATUTS[PAR_UID[p["uid"]]["_statut"]][0])}</title></g></a>' for p in acm["individus"])
MODS_AFF = {("P2", "oui"), ("P1", "oui"), ("P1", "non"), ("P4", "oui"), ("P4", "non"), ("porteur", "cooperative"), ("porteur", "personne_publique"), ("porteur", "fonds_dotation"),
            ("forme_collectif", "cooperative"), ("forme_collectif", "collectif_de_fait"), ("etat", "disparu"), ("famille", "occupation_regularisee"), ("famille", "communaute_intentionnelle"),
            ("famille", "commun_foncier"), ("famille", "lieu_non_marchand"), ("verrou_type", "par_propriete"), ("verrou_type", "aucun"), ("periode", "2008-"), ("periode", "1871-1914"), ("economie", "salariat_structure"), ("gouvernance", "assemblee_consensus")}
def modlib(v, m):
    if v.startswith("P"):
        return f"{v} {'franchie' if m == 'oui' else 'non franchie'}"
    if v == "famille":
        return R.FAMILLES.get(m, m)
    if v in ("porteur", "forme_collectif"):
        return ("porteur " if v == "porteur" else "collectif ") + R.FORMES.get(m, m).lower()
    if v == "verrou_type":
        return {"par_propriete": "verrou par la propriété", "par_titre": "verrou par un titre", "aucun": "sans verrou"}[m]
    if v == "periode":
        return m
    return lib_dim(v, m) if v in R.DIM else m
labs = "".join(f'<text x="{sx(m["x"])+4:.1f}" y="{sy(m["y"])-4:.1f}" font-size="11" fill="var(--encre-2)">▪ {E(modlib(m["var"], m["mod"]))}</text>' for m in acm["modalites"] if (m["var"], m["mod"]) in MODS_AFF)
acm_svg = f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto" role="img" aria-labelledby="acm-t"><title id="acm-t">Plan factoriel des {nb} cas (analyse des correspondances multiples)</title><line x1="{M}" x2="{W-M}" y1="{sy(0):.1f}" y2="{sy(0):.1f}" stroke="var(--filet)"/><line y1="{M}" y2="{H-M}" x1="{sx(0):.1f}" x2="{sx(0):.1f}" stroke="var(--filet)"/>{labs}{pts}</svg>'
corps = f"""<h1>Prismes croisés</h1>
<p class="chapeau">Les {nb} cas sont décrits sur une vingtaine de dimensions. On les croise ici deux à deux, puis toutes ensemble, pour voir ce qui va avec quoi.</p>
<p class="note-prudence">{E(AN['avertissement'])} Les valeurs « non établi » sont exclues de chaque croisement : l'effectif n varie d'une paire à l'autre.</p>
<h2>Six lectures</h2>{lectures or '<p>À venir.</p>'}
<h2>Associations les plus nettes</h2>
<div class="texte"><p>V de Cramér corrigé (0 : aucune association, 1 : association parfaite), test exact de Fisher pour les tableaux 2×2, χ² sinon. Sont écartées ici les paires liées par construction (par exemple la porte P2 et le type de verrou) et les tableaux trop creux.</p></div>
<div class="defile"><table><thead><tr><th>Paire</th><th class=n>V</th><th class=n>p</th><th class=n>n</th></tr></thead><tbody>{tf}</tbody></table></div>
<h2>Matrice des associations</h2>
<p class="petit">* p &lt; 0,05 · † association attendue par construction · – effectif insuffisant. Survolez une case pour le détail.</p>
<div class="defile">{heat}</div>
<h2>Explorer un croisement</h2>
<form class="filtres" onsubmit="return false" aria-label="Choisir deux dimensions">
<label>Lignes<select id="x-a"></select></label><label>Colonnes<select id="x-b"></select></label></form>
<div id="x-sortie" class="defile" aria-live="polite"></div>
<h2>Plan factoriel</h2>
<figure>{acm_svg}<figcaption>Analyse des correspondances multiples sur {len(acm['variables'])} dimensions (famille, période, formes, titre, accès, verrou, gouvernance, économie, ouverture, état, portes). Axe horizontal : {acm['inertie_benzecri'][0]*100:.0f} % de l'inertie corrigée ; vertical : {acm['inertie_benzecri'][1]*100:.0f} %. Points : cas (disque cerclé : corpus sous condition ; anneau épais : seuil ; petit disque pointillé : épreuve) ; carrés : modalités choisies. Deux points proches partagent beaucoup de modalités ; la distance n'a pas d'autre sens.</figcaption></figure>
<h2>Six mécanismes de capture</h2><p class="petit">Typologie proposée par antimeta à partir des épreuves.</p><div class="mecanismes">{mecs}</div>
<script src="../assets/croise.js" defer></script>"""
page("prismes/", "Prismes croisés", corps, "Corrélations multi-thématiques entre les dimensions des "+str(nb)+" cas : associations, matrice, croisements, plan factoriel, mécanismes de capture.")

# ------------------------------------------------------------------ carte
import math
FR = json.loads((ASSETS / "france-departements.json").read_text(encoding="utf-8"))
K = math.cos(math.radians(46.5))
def pr(lon, lat):
    return (lon + 5.5) * K * 100, (51.3 - lat) * 100
paths = "".join(f'<path d="{p["d"]}"><title>{E(p["nom"])}</title></path>' for p in FR["departements"] if not p["code"].startswith("97"))
pts, sans = [], []
for d in sorted(fiches, key=lambda d: -ORDRE_ST[d["_statut"]]):
    l = d.get("localisation") or {}
    if isinstance(l.get("lat"), (int, float)) and isinstance(l.get("lon"), (int, float)):
        x, y = pr(l["lon"], l["lat"])
        pts.append(f'<a href="../f/{d["uid"]}/"><g>{marque(d["_statut"], x, y, 1.0)}<title>{E(d["nom"])} — {E(lieu(d))} — {E(R.STATUTS[d["_statut"]][0])}</title></g></a>')
    else:
        sans.append(d)
MARQ_CSC, MARQ_SEUIL, MARQ_EPR = marque("corpus_sous_condition", 9, 9, .7), marque("seuil", 9, 9, .9), marque("epreuve", 9, 9, 1.2)
liste = "".join(f'<li><a href="../f/{d["uid"]}/">{E(d["nom"])}</a> — {E(lieu(d))} — {E(R.STATUTS[d["_statut"]][0])}</li>' for d in sorted(fiches, key=lambda d: (str((d.get("localisation") or {}).get("departement")), d["nom"])))
corps = f"""<h1>Carte</h1>
<p class="chapeau">Les {nb} cas, placés au centre de leur commune (jamais à une adresse). Aucune tuile ni requête extérieure : le fond est dessiné ici, d'après les contours de l'IGN.</p>
<div class="legende"><span><svg width="18" height="18" aria-hidden="true">{MARQ_CSC}</svg>corpus sous condition (disque cerclé)</span><span><svg width="18" height="18" aria-hidden="true">{MARQ_SEUIL}</svg>au seuil (anneau épais)</span><span><svg width="18" height="18" aria-hidden="true">{MARQ_EPR}</svg>épreuve (petit disque pointillé)</span></div>
<figure><svg class="carte-france" viewBox="0 0 1060 1000" style="width:100%;max-width:760px;height:auto" role="img" aria-labelledby="carte-t"><title id="carte-t">Carte de France métropolitaine des cas instruits</title>{paths}{"".join(pts)}</svg>
<figcaption>Fond : départements, d'après IGN ADMIN EXPRESS (Licence Ouverte 2.0), simplifiés. {len(sans)} cas sans commune publiée ne sont pas placés.</figcaption></figure>
<h2>Liste équivalente, par département</h2><ul class="petit">{liste}</ul>"""
page("carte/", "Carte", corps, "Carte des collectifs autogérés et lieux en communs instruits par libres.")

# ------------------------------------------------------------------ frise
A0, A1 = 1780, 2030
FW, LH, GX = 1000, 22, 250
tri = sorted(fiches, key=lambda d: (d.get("debut") or 3000))
barres = []
for j, d in enumerate(tri):
    y = 30 + j * LH
    a = d.get("debut")
    if not isinstance(a, int):
        barres.append(f'<a href="../f/{d["uid"]}/"><text x="0" y="{y+12}">{E(d["nom"][:36])}</text></a><text x="{GX}" y="{y+12}">date de début non établie</text>')
        continue
    b = d.get("fin") or (R.ANNEE if R.val(d, "etat") != "disparu" else a + 1)
    x = GX + (a - A0) / (A1 - A0) * (FW - GX)
    w = max(3, (b - a) / (A1 - A0) * (FW - GX))
    ouvert = "" if d.get("fin") else ' stroke-dasharray="2 2"'
    barres.append(f'<a href="../f/{d["uid"]}/"><text x="0" y="{y+12}">{E(d["nom"][:36])}</text><rect x="{x:.1f}" y="{y+3}" width="{w:.1f}" height="12" fill="{coul[d["_statut"]]}"{ouvert}><title>{E(d["nom"])} : {E(dates(d))}</title></rect></a>')
axes = "".join(f'<line class="ligne" x1="{GX+(t-A0)/(A1-A0)*(FW-GX):.1f}" x2="{GX+(t-A0)/(A1-A0)*(FW-GX):.1f}" y1="20" y2="{30+len(tri)*LH}"/><text x="{GX+(t-A0)/(A1-A0)*(FW-GX):.1f}" y="14" text-anchor="middle">{t}</text>' for t in (1789, 1830, 1870, 1901, 1945, 1968, 2008))
corps = f"""<h1>Frise</h1>
<p class="chapeau">Chaque barre va de l'installation sur le lieu à la fin du collectif, ou jusqu'à aujourd'hui s'il est actif. Repères : 1789, 1830, 1870, 1901 (liberté d'association), 1945, 1968, 2008 (fonds de dotation).</p>
<figure><svg class="frise-svg" viewBox="0 0 {FW} {40+len(tri)*LH}" role="img" aria-labelledby="frise-t"><title id="frise-t">Durée d'existence des {nb} cas, de 1789 à aujourd'hui</title>{axes}{"".join(barres)}</svg>
<figcaption>Couleur : statut (brique corpus sous condition, ocre seuil, gris épreuve) ; barre en pointillé : collectif encore actif. Le nom et l'infobulle donnent le statut en texte. Les dates sont celles établies par les sources de chaque fiche.</figcaption></figure>"""
page("frise/", "Frise", corps, "Frise chronologique des collectifs instruits par libres, de 1789 à aujourd'hui.")

# ------------------------------------------------------------------ regards
c = regards.get("contradicteur") or {}
corps = f"""<h1>Trois regards, et une épreuve</h1>
<p class="chapeau">Un même collectif se lit de trois façons sans qu'aucune remplace les autres : ce qu'il vit, ce qui le protège, ce qui peut le prendre. Puis la thèse du site passe l'épreuve d'un contradicteur.</p>
<div class="texte">
<div class="face igor"><p class="qui">igor · ce que la pratique dit des {nb} cas</p>{para((regards.get('igor') or {}).get('transversal'))}</div>
<div class="face eozen"><p class="qui">eozen · les outils juridiques, période par période</p>{para((regards.get('eozen') or {}).get('transversal'))}<p class="petit">Information juridique générale, pas un conseil. Tout acte se prépare avec un notaire et un avocat.</p></div>
<div class="face antimeta"><p class="qui">antimeta · deux âges de la capture</p>{para((regards.get('antimeta') or {}).get('transversal'))}</div>
<h2>L'épreuve du contradicteur</h2>
<h3>La meilleure objection</h3>{para(c.get('steelman'))}
<h3>La faille</h3>{para(c.get('faille'))}
<h3>La thèse, durcie</h3><blockquote class="these">{E((c.get('these') or '').strip())}</blockquote><p class="petit">{E((c.get('note_version') or '').strip())}</p>
<h3>Les garde-fous qui en découlent</h3><ul>{''.join(f'<li>{E(g)}</li>' for g in c.get('garde_fous') or [])}</ul>
<p class="petit">Les trois garde-fous sont appliqués : dénominateur et <a href="../portes/">sensibilité</a> publiés, cas antérieurs à 1901 signalés, verrou par titre distingué du verrou par propriété.</p>
</div>"""
page("regards/", "Regards", corps, "Lectures d'igor, d'eozen et d'antimeta sur les cas instruits, et l'épreuve du contradicteur.")

# ------------------------------------------------------------------ méthode
dimrows = "".join(f"<tr><th scope=row>{E(lib)}</th><td>{E(', '.join(vals.values()))}{' (plusieurs possibles)' if multi else ''}</td></tr>" for k, (lib, multi, vals) in R.DIM.items())
prow = "".join(f"<tr><th scope=row>{code} {E(lib)}</th><td>{E(q)}</td></tr>" for k, code, lib, q in R.PORTES)
corps = f"""<h1>Méthode</h1>
<div class="texte">
<p class="chapeau">libres décrit des collectifs, pas des propriétés. L'unité est le groupe qui s'autogère et sa trajectoire sur un lieu.</p>
<h2>Le critère d'entrée</h2><p>Un cas entre au corpus seulement s'il franchit les cinq portes. Chaque porte vaut franchie, partielle, non franchie ou non établie, avec une note et une source. Une porte franchie sans note ni source bloque la publication.</p>
<div class="defile"><table>{prow}</table></div>
<p><b>Lecture au maillon faible.</b> La chaîne entière est lue, du propriétaire du sol jusqu'au collectif qui l'utilise. Un collectif associatif logé par une société à parts cessibles échoue en P1 ; une ferme portée par une foncière commerciale aussi, même si le fermier est de bonne foi.</p>
<p><b>Ce qui est admis en P1.</b> Association (loi 1901, ou 1908 en Alsace-Moselle), fonds de dotation, fondation, collectif de fait. Une personne publique peut être propriétaire du sol, au cas par cas, si le montage établit clairement un commun (usage confié durablement à un collectif autogéré) ; elle ne l'est pas quand elle garde la main sur l'usage. Aucun maillon commercial ou coopératif, aucune société à parts cessibles.</p>
<p><b>Comment se lit P2.</b> Au meilleur effort documentaire : un verrou (inaliénabilité, veto de réseau, dévolution, bail d'au moins 30 ans) établi par des sources concordantes suffit, même si l'acte n'est pas publié. Une faculté documentée de vendre, un titre court ou l'absence de titre retiennent la porte.</p>
<h2>Les exclusions nommées</h2><p>Foncières et fermes Terre de Liens (société en commandite par actions, actions cessibles), écolieux adossés à la Coopérative Oasis (société coopérative d'intérêt collectif), SCI ou GFA à parts cessibles, SAS ou SCIC « de transition », propriété privée « vertueuse » : instruits et publiés comme épreuves, pour que la frontière soit visible et discutable.</p>
<h2>Les dimensions</h2><div class="defile"><table>{dimrows}</table></div>
<p>La période se calcule depuis la date d'installation ; le statut, la distance au corpus et le type de verrou se calculent depuis les portes et les dimensions. Rien de tout cela n'est saisi à la main.</p>
<h2>Comment les cas ont été choisis</h2><p>Échantillon raisonné de {nb} cas, non exhaustif : des communautés du XIX<sup>e</sup> siècle aux lieux acquis depuis 2015, en couvrant les quatre familles et les contre-modèles. Les cas déjà instruits par communs.actitude.org ont été repris et revérifiés. Chaque fait vient d'une source publiée, citée sur la fiche ; ce qui n'a pas pu être vérifié est listé comme « non confirmé ».</p>
<h2>Ce que le cadre ne conclut pas</h2><p>Il ne juge ni la valeur humaine d'un collectif ni la sincérité des personnes. Il ne mesure pas la domination interne non inscrite dans les actes. « Non établi » veut dire « aucune source trouvée », jamais « n'existe pas ». Les associations statistiques sont exploratoires : avec {nb} cas, elles décrivent ce corpus, elles ne prouvent aucune cause.</p>
<h2>Données personnelles</h2><p>Aucune donnée personnelle non publique. Les lieux sont placés au centre de leur commune. Seules des structures sont nommées dans les analyses.</p>
<h2>Les voix</h2><p>Le texte est porté par igor (le collectif vécu). eozen tient la lecture juridique, antimeta celle des captures ; le contradicteur a éprouvé la thèse avant publication. Le cadre complet est versionné dans le <a href="{REPO}">dépôt public</a> (docs/cadre.md).</p>
</div>"""
page("methode/", "Méthode", corps, "Critère d'entrée à cinq portes, dimensions, exclusions nommées, limites et sources de libres.")

# ------------------------------------------------------------------ dossiers
import markdown as _md
_dp = ROOT / "docs" / "dossier-association-agricole.md"
if _dp.exists():
    _html = _md.markdown(_dp.read_text(encoding="utf-8"), extensions=["tables"])
    _html = re.sub(r"<h1>.*?</h1>", "", _html, count=1, flags=re.S)
    _cas = [d for d in fiches if d.get("dossier_juridique")]
    corps = f"""<p class="sur">Dossier</p><h1>Une association peut-elle cultiver sans chef d'exploitation ?</h1>
<div class="texte">{_html}<h2>Cas documentés</h2><ul>{''.join(f'<li><a href="../../f/{d['uid']}/">{E(d['nom'])}</a> — {E(lieu(d))}</li>' for d in _cas)}</ul>
<p class="note-prudence">Information juridique générale, pas un conseil. Tout montage se vérifie avec un avocat ou un conseil spécialisé (MSA, fiscalité agricole).</p></div>"""
    page("dossiers/association-agricole/", "Association et activité agricole", corps, "Textes, positions de la MSA, décisions de justice et cas documentés : une association peut-elle exercer une activité agricole sans chef d'exploitation ?")
# ------------------------------------------------------------------ données
PUB = []
for d in fiches:
    PUB.append({
        "uid": d["uid"], "nom": d["nom"], "autres_noms": d.get("autres_noms") or [], "famille": d["famille"],
        "statut": d["_statut"], "portes_manquantes": d["_manque"], "periode": d["_periode"], "verrou_type": d["_verrou"],
        "localisation": {k: (d.get("localisation") or {}).get(k) for k in ("commune", "departement", "region", "lat", "lon")},
        "debut": d.get("debut"), "fin": d.get("fin"), "resume": d.get("resume"),
        "collectif": {k: (d.get("collectif") or {}).get(k) for k in ("nom", "forme", "annee")},
        "foncier": {k: (d.get("foncier") or {}).get(k) for k in ("porteur", "porteur_forme", "surface_ha", "titre_duree_ans")},
        "portes": {k: {"valeur": d["_p"][k], "note": ((d["portes"].get(k) or {}).get("note"))} for k in R.PKEYS},
        "dimensions": {k: ((d["dimensions"].get(k) or {}).get("valeur")) for k in R.DIM},
        "sources": [{k: s.get(k) for k in ("titre", "auteur", "annee", "url")} for s in d.get("sources") or []],
        "url": f"{BASE}/f/{d['uid']}/",
    })
(OUT / "donnees").mkdir(exist_ok=True)
(OUT / "donnees" / "libres.json").write_text(json.dumps({"version": VERSION, "licence": "CC BY-NC-SA 4.0", "cas": PUB}, ensure_ascii=False, indent=1), encoding="utf-8")
(OUT / "donnees" / "analyses.json").write_text(json.dumps(AN, ensure_ascii=False), encoding="utf-8")
buf = io.StringIO()
w = csv.writer(buf)
w.writerow(["uid", "nom", "famille", "statut", "commune", "departement", "debut", "fin", "forme_collectif", "porteur_forme", "verrou_type"] + [c for _, c, _, _ in R.PORTES] + list(R.DIM))
for d in PUB:
    w.writerow([d["uid"], d["nom"], d["famille"], d["statut"], d["localisation"]["commune"], d["localisation"]["departement"], d["debut"], d["fin"], d["collectif"]["forme"], d["foncier"]["porteur_forme"], d["verrou_type"]] + [d["portes"][k]["valeur"] for k in R.PKEYS] + ["|".join(v) if isinstance(v, list) else (v or "") for v in d["dimensions"].values()])
(OUT / "donnees" / "libres.csv").write_text(buf.getvalue(), encoding="utf-8")
corps = f"""<h1>Données</h1><div class="texte"><p>Toutes les données publiées sont libres de réutilisation non commerciale, sous licence <a href="{LICENCE_URL}">CC BY-NC-SA 4.0</a>, en citant « libres.actitude.org ».</p>
<ul><li><a href="libres.json">libres.json</a> — les {nb} cas, portes, dimensions et sources</li><li><a href="libres.csv">libres.csv</a> — une ligne par cas</li><li><a href="analyses.json">analyses.json</a> — croisements, V de Cramér, plan factoriel, sensibilité</li></ul>
<p>Les fiches sources (YAML), le cadre et les scripts sont dans le <a href="{REPO}">dépôt public</a>.</p></div>"""
page("donnees/", "Données", corps)

# ------------------------------------------------------------------ pages simples
corps = f"""<h1>Droit de réponse</h1><div class="texte"><p>Vous faites partie d'un collectif décrit ici, ou d'une structure citée comme contre-modèle ? Une erreur, une source manquante, un acte que nous n'avons pas vu : écrivez à <a href="mailto:{CONTACT}?subject=libres%20%E2%80%94%20droit%20de%20r%C3%A9ponse">{CONTACT}</a>.</p>
<p>Chaque demande reçoit une réponse. Une correction sourcée est intégrée ; une réponse de fond peut être publiée sur la fiche, signée par la structure. Un acte publié (statuts, bail, clause d'inaliénabilité) peut faire passer une porte de « partielle » à « franchie » : c'est précisément ce que le site demande à voir.</p>
<p>Terre de Liens, la Coopérative Oasis et toute structure dont un lieu figure parmi les épreuves y sont expressément invitées.</p></div>"""
page("droit-de-reponse/", "Droit de réponse", corps)
corps = f"""<h1>À propos</h1><div class="texte"><p>libres est un projet d'actitude.org, frère de <a href="{COMMUNS}">communs.actitude.org</a> (l'annuaire critique des montages de libération des terres) et de <a href="{BIBLIO}">biblio.actitude.org</a> (la veille documentaire). Là où communs décrit un montage foncier, libres suit un collectif dans le temps.</p>
<p>Texte : igor, avec les regards d'eozen et d'antimeta. Droits : Cedric Mabilotte. Licence <a href="{LICENCE_URL}">CC BY-NC-SA 4.0</a> ; polices sous SIL Open Font License ; fond de carte d'après IGN ADMIN EXPRESS (Licence Ouverte 2.0).</p>
<p>Version {VERSION} : {nb} cas. Les versions suivantes élargiront le corpus (maisons du peuple, communautés de travail, biens sectionaux, lieux du réseau CLIP et du fonds Antidote à mesure que leurs actes seront publiés).</p></div>"""
page("a-propos/", "À propos", corps)
corps = f"""<h1>Mentions légales</h1><div class="texte"><p>Éditeur : Cedric Mabilotte, actitude.org — {CONTACT}. Hébergement : GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p><p>Ce site ne dépose aucun cookie, n'utilise aucun outil de mesure d'audience et ne charge aucune ressource extérieure. Le choix du thème clair ou sombre est gardé dans votre navigateur, nulle part ailleurs.</p></div>"""
page("mentions-legales/", "Mentions légales", corps)
page("404.html", "Page introuvable", '<h1>Page introuvable</h1><p><a href="/">Retour à l\'accueil</a> · <a href="/fiches/">Les cas</a></p>', depth=0)

# ------------------------------------------------------------------ sitemap, robots
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE}/{p}</loc></url>" for p in PAGES if p != "404.html") + "</urlset>\n", encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")

# ------------------------------------------------------------------ garde-fous sortie
for f in OUT.rglob("*.html"):
    t = f.read_text(encoding="utf-8")
    corps_txt = re.sub(r"<[^>]+>", " ", t)
    for pat in PROVENANCE:
        if re.search(pat, corps_txt):
            err(f"{f.relative_to(OUT)} : mot de provenance « {pat} »")
    for mot in MOTS_PROSCRITS:
        for m in re.finditer(mot, corps_txt, re.I):
            ctx = corps_txt[max(0, m.start()-60):m.end()+20].replace("\n", " ")
            # toléré dans un titre de source cité
            if f.parts[-3:-2] == ("f",) and "<ol class=\"sources\">" in t and ctx.strip() and mot.lower() in "".join(re.findall(r'<ol class="sources">.*?</ol>', t, re.S)).lower():
                continue
            err(f"{f.relative_to(OUT)} : mot proscrit « {mot} » … {ctx.strip()[:90]}")
    for href in re.findall(r'href="([^"#:]+)(?:#[^"]*)?"', t):
        if href.startswith(("http", "mailto")) or href in ("/",):
            continue
        cible = (f.parent / href).resolve() if not href.startswith("/") else (OUT / href.lstrip("/")).resolve()
        if cible.is_dir():
            cible = cible / "index.html"
        if not cible.exists():
            err(f"{f.relative_to(OUT)} : lien interne cassé {href}")
if erreurs:
    print("ÉCHEC — garde-fous :", *sorted(set(erreurs)), sep="\n  ")
    sys.exit(1)
print(f"OK — {len(PAGES)} pages, {nb} cas ({dict(CNT)})")
