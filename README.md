# libres — libres.actitude.org

Collectifs autogérés de droit civil installés sur des lieux tenus en communs en France depuis 1789 :
fiches sourcées, cinq portes d'entrée, prismes croisés, carte, frise, trois regards.

- Cadre (source de vérité) : `docs/cadre.md` · gabarit de fiche : `docs/exemple-fiche.yml`
- Fiches : `data/fiches/<uid>.yml` · regards des voix : `data/regards/` · lectures : `data/prismes.yml`
- Analyses (local, numpy/scipy) : `python3 scripts/analyser.py` → `analyses/analyses.json` (committé)
- Site (pyyaml seul, garde-fous) : `python3 scripts/generate_site.py` → `site/`
- Publication : push sur `main` → GitHub Actions → GitHub Pages (CNAME Gandi `libres` → cedricmabilotte.github.io.)

Texte : igor, avec eozen et antimeta · © Cedric Mabilotte · textes CC BY-NC-SA 4.0, données ODbL 1.0, code AGPL-3.0 (`LICENSE`).

## Réutiliser

- **Une fiche = un fichier** `data/fiches/<uid>.yml`, adresse stable sur le site : `https://libres.actitude.org/f/<uid>/`.
  Champs : `uid`, `nom`, `autres_noms`, `famille`, `resume`, `localisation`, `debut`, `fin`, `collectif`, `foncier`,
  `dimensions`, `portes` (cinq portes du cadre, chacune avec `valeur` et sa source), `chronologie`, `fiabilite`, `liens`,
  `sources`, `faces` (regards des voix). Le gabarit commenté : `docs/exemple-fiche.yml` ; le cadre : `docs/cadre.md`.
- **Tout en un téléchargement** : `https://libres.actitude.org/donnees/libres.json` (tous les cas publiés, portes,
  dimensions, sources), `libres.csv` (une ligne par cas), `analyses.json` (croisements) — régénérés à chaque publication.
- **Licences** (`LICENSE`) : textes CC BY-NC-SA 4.0 ; données ODbL 1.0 ; code AGPL-3.0-or-later ; polices et fond de
  carte à leur licence.
- **Citer** : `CITATION.cff` (GitHub : « Cite this repository »). Archive pérenne : Software Heritage,
  https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/CedricMabilotte/libres-site
- **Corriger** : `CONTRIBUTING.md` — une issue ou une PR par fiche, source citée, réponse sous un mois.
