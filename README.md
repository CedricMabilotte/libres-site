# libres — libres.actitude.org

Collectifs autogérés de droit civil installés sur des lieux tenus en communs en France depuis 1789 :
fiches sourcées, cinq portes d'entrée, prismes croisés, carte, frise, trois regards.

- Cadre (source de vérité) : `docs/cadre.md` · gabarit de fiche : `docs/exemple-fiche.yml`
- Fiches : `data/fiches/<uid>.yml` · regards des voix : `data/regards/` · lectures : `data/prismes.yml`
- Analyses (local, numpy/scipy) : `python3 scripts/analyser.py` → `analyses/analyses.json` (committé)
- Site (pyyaml seul, garde-fous) : `python3 scripts/generate_site.py` → `site/`
- Publication : push sur `main` → GitHub Actions → GitHub Pages (CNAME Gandi `libres` → cedricmabilotte.github.io.)

Texte : igor, avec eozen et antimeta · © Cedric Mabilotte · CC BY-NC-SA 4.0.
