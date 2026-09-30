#!/usr/bin/env python3
"""Analyses croisées de libres → analyses/analyses.json (committé ; le site ne dépend que de pyyaml).
Dépendances locales : numpy, scipy. Relancer après toute modification de data/.
Prudence : n ≤ 41, échantillon raisonné — les associations sont exploratoires, jamais causales.
"""
import itertools, json, math, sys
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.stats import chi2_contingency, fisher_exact
sys.path.insert(0, str(Path(__file__).parent))
import referentiel as R

fiches, _ = R.charger()

def variables(d):
    st, manque, p = R.calcul(d)
    v = {
        "famille": d.get("famille"),
        "periode": R.periode(d.get("debut")),
        "porteur": (d.get("foncier") or {}).get("porteur_forme") if (d.get("foncier") or {}).get("porteur_forme") not in (None, "inconnu") else None,
        "forme_collectif": (d.get("collectif") or {}).get("forme"),
        "verrou_type": R.verrou_type(d),
        "statut": "corpus_ou_seuil" if st != "epreuve" else "epreuve",
        "distance": str(len(manque)),
    }
    for k, (lib, multi, _) in R.DIM.items():
        if not multi:
            v[k] = R.val(d, k)
    for k in ("finalite", "filiation", "verrou"):
        vals = R.val(d, k)
        if vals:
            for m in R.DIM[k][2]:
                v[f"{k}:{m}"] = "oui" if m in vals else "non"
    for k, code, lib, _ in R.PORTES:
        v[code] = "oui" if p[k] == "oui" else ("non" if p[k] in ("non", "partiel") else None)
    return v

rows = [variables(d) for d in fiches]
uids = [d["uid"] for d in fiches]
allvars = sorted({k for r in rows for k in r})
# garder les indicateurs multi assez fréquents (≥ 4 « oui »)
def keep(k):
    vals = [r.get(k) for r in rows if r.get(k)]
    if ":" in k:
        return sum(1 for x in vals if x == "oui") >= 4 and sum(1 for x in vals if x == "non") >= 4
    c = Counter(vals)
    return len(c) >= 2 and len(vals) >= 12
VARS = [k for k in allvars if keep(k)]

def libelle(k):
    if ":" in k:
        a, b = k.split(":")
        return f"{R.DIM[a][0]} : {R.DIM[a][2].get(b, b)}"
    return {"famille": "Famille", "periode": "Période", "porteur": "Porteur du foncier", "forme_collectif": "Forme du collectif",
            "verrou_type": "Type de verrou", "statut": "Statut (corpus/seuil vs épreuve)", "distance": "Portes manquantes",
            "P1": "P1 forme civile", "P2": "P2 foncier verrouillé", "P3": "P3 intérêt général", "P4": "P4 autogestion", "P5": "P5 établi"}.get(k) or R.DIM[k][0]

def cramer(a, b):
    pairs = [(r[a], r[b]) for r in rows if r.get(a) and r.get(b)]
    n = len(pairs)
    if n < 12:
        return None
    la = sorted({x for x, _ in pairs}); lb = sorted({y for _, y in pairs})
    if len(la) < 2 or len(lb) < 2:
        return None
    t = np.zeros((len(la), len(lb)))
    for x, y in pairs:
        t[la.index(x), lb.index(y)] += 1
    chi2, p, dof, exp = chi2_contingency(t, correction=False)
    phi2 = chi2 / n
    r_, k_ = t.shape
    phi2c = max(0, phi2 - (k_ - 1) * (r_ - 1) / (n - 1))
    rc = r_ - (r_ - 1) ** 2 / (n - 1); kc = k_ - (k_ - 1) ** 2 / (n - 1)
    v = math.sqrt(phi2c / max(1e-9, min(kc - 1, rc - 1))) if min(kc, rc) > 1 else 0.0
    if t.shape == (2, 2):
        p = fisher_exact(t)[1]
    faible = float((exp < 5).mean())
    return {"v": round(v, 3), "p": round(float(p), 4), "n": n, "cellules_faibles": round(faible, 2),
            "table": {"lignes": la, "colonnes": lb, "valeurs": t.astype(int).tolist()}}

paires = {}
for a, b in itertools.combinations(VARS, 2):
    if a.split(":")[0] == b.split(":")[0] and ":" in a and ":" in b:
        continue  # indicateurs d'une même dimension : dépendance mécanique
    if {a, b} & {"statut", "distance"} and {a, b} & {"P1", "P2", "P3", "P4", "P5"}:
        continue  # le statut est calculé depuis les portes
    c = cramer(a, b)
    if c:
        paires[f"{a}|{b}"] = c

# familles de variables liées par construction : leurs associations sont attendues, pas découvertes
BLOCS = [{"verrou", "verrou_type", "P2", "titre", "porteur"}, {"P4", "gouvernance"}, {"P1", "forme_collectif", "porteur"},
         {"statut", "distance"}, {"etat", "fin"}, {"P5", "periode"}]
def racine(k):
    return k.split(":")[0]
def mecanique(a, b):
    return any(racine(a) in bl and racine(b) in bl for bl in BLOCS)
for k, c in paires.items():
    a, b = k.split("|")
    c["mecanique"] = mecanique(a, b)
    c["fragile"] = c["cellules_faibles"] > 0.5 or c["n"] < 20
fortes = sorted(({"a": k.split("|")[0], "b": k.split("|")[1], **{x: y for x, y in c.items() if x != "table"}}
                 for k, c in paires.items() if c["v"] >= 0.3 and c["p"] < 0.05 and not c["mecanique"]), key=lambda x: (x["fragile"], -x["v"]))

# ACM (analyse des correspondances multiples) sur les dimensions nominales principales, valeurs manquantes passives
ACM_VARS = ["famille", "periode", "porteur", "forme_collectif", "gouvernance", "economie", "ouverture", "titre", "acces", "verrou_type", "etat", "P1", "P2", "P3", "P4", "P5"]
mods = [(v, m) for v in ACM_VARS for m in sorted({r[v] for r in rows if r.get(v)})]
Z = np.array([[1.0 if r.get(v) == m else 0.0 for v, m in mods] for r in rows])
keepc = Z.sum(0) >= 2
Z, mods = Z[:, keepc], [m for m, k in zip(mods, keepc) if k]
P = Z / Z.sum(); rm = P.sum(1); cm = P.sum(0)
S = (P - np.outer(rm, cm)) / np.sqrt(np.outer(rm, cm))
U, s, Vt = np.linalg.svd(S, full_matrices=False)
eig = s ** 2
# correction de Benzécri
Q = len(ACM_VARS)
benz = np.array([((Q / (Q - 1)) * (math.sqrt(e) - 1 / Q)) ** 2 if math.sqrt(e) > 1 / Q else 0 for e in eig])
taux = (benz / benz.sum()).tolist() if benz.sum() else (eig / eig.sum()).tolist()
F = (U * s) / np.sqrt(rm)[:, None]
G = (Vt.T * s) / np.sqrt(cm)[:, None]
acm = {
    "variables": ACM_VARS,
    "inertie_benzecri": [round(t, 3) for t in taux[:3]],
    "individus": [{"uid": u, "x": round(float(F[i, 0]), 3), "y": round(float(F[i, 1]), 3)} for i, u in enumerate(uids)],
    "modalites": [{"var": v, "mod": m, "x": round(float(G[j, 0]), 3), "y": round(float(G[j, 1]), 3), "effectif": int(Z[:, j].sum())}
                  for j, (v, m) in enumerate(mods)],
}

# portes, sensibilité, entonnoir
portes = {code: Counter(((d.get("portes") or {}).get(k) or {}).get("valeur", "inconnu") for d in fiches) for k, code, _, _ in R.PORTES}
sens = {}
for var, lib in [(None, "Cadre publié (P2 au meilleur effort documentaire)"), ("p1_souple", "P1 : une forme partiellement civile suffit"),
                 ("p2_titre_annonce", "P2 : tout verrou partiel vaut franchi"), ("p5_cinq_ans", "P5 : cinq ans d'usage suffisent"),
                 ("partiel_vaut_oui", "Toute porte partielle vaut franchie")]:
    c = Counter(R.calcul(d, var)[0] for d in fiches)
    sens[var or "strict"] = {"libelle": lib, **{k: c.get(k, 0) for k in R.STATUTS},
                             "admis": sorted(d["uid"] for d in fiches if R.calcul(d, var)[0] in ("corpus", "corpus_sous_condition"))}
entonnoir = []
restant = list(fiches)
for k, code, lib, _ in R.PORTES:
    restant = [d for d in restant if ((d.get("portes") or {}).get(k) or {}).get("valeur") == "oui"]
    entonnoir.append({"porte": code, "libelle": lib, "restent": len(restant)})
bloquante_seule = Counter()
for d in fiches:
    st, manque, _ = R.calcul(d)
    for m in manque:
        bloquante_seule[m] += 1
out = {
    "n": len(fiches),
    "avertissement": "Échantillon raisonné de 41 cas, non exhaustif. Associations exploratoires : un V de Cramér élevé signale une co-occurrence dans ce corpus, pas une cause.",
    "variables": {k: libelle(k) for k in VARS},
    "paires": paires, "fortes": fortes, "acm": acm,
    "portes": {k: dict(v) for k, v in portes.items()},
    "echecs_par_porte": {k: bloquante_seule[k] for k in R.PKEYS},
    "entonnoir": entonnoir, "sensibilite": sens,
}
Path(R.ROOT / "analyses").mkdir(exist_ok=True)
(R.ROOT / "analyses" / "analyses.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(VARS), "variables ;", len(paires), "paires ;", len(fortes), "associations fortes (V≥0,3, p<0,05)")
for f in fortes[:40]:
    print("F" if f["fragile"] else " ", f"{f['v']:.2f} p={f['p']:.3f} n={f['n']} faibles={f['cellules_faibles']}  {libelle(f['a'])} × {libelle(f['b'])}")
print("ACM inertie", acm["inertie_benzecri"]); print(json.dumps(sens, ensure_ascii=False)[:600]); print(entonnoir, dict(bloquante_seule))
