# CLAUDE.md — libres (libres.actitude.org)

## Point de reprise
Lire `etat-projet-libres.md`, puis `lecons-libres.md` et `TAF.md`. Le cadre est dans `docs/cadre.md` (clés, portes, dimensions) ; le référentiel exécutable dans `scripts/referentiel.py` — les deux doivent rester alignés.

## Identité
- Voix porteuse : **@igor** (le collectif vécu). Faces invitées : **@eozen** (montage), **@antimeta** (capture). @contradicteur a éprouvé la thèse (data/regards/contradicteur.yml). Signature « Texte : igor, avec les regards d'eozen et d'antimeta ». Droits : Cedric Mabilotte.
- Licence CC BY-NC-SA 4.0. Aucune mention d'IA dans les contenus publiés ni dans les commits ; pas de `Co-Authored-By`.
- Charte : famille actitude (papier #F5F2E9, Source Serif 4 + IBM Plex), canal igor : accent brique #9A3E23. Tokens dans `assets/style.css`, règle dans `docs/charte.md`.
- Sites frères : communs.actitude.org (montages fonciers, renvoi `liens.communs`), biblio.actitude.org (sources).

## Garde-fous
- Critère **strict** (décision de Ced, 2026-09-30) : cinq portes toutes `oui`. Le statut se **calcule** (`referentiel.calcul`), jamais saisi. `corpus_sous_condition` = corpus par verrou de titre.
- Le générateur échoue si : uid ≠ fichier, valeur hors cadre, porte franchie sans note/source, index de source hors bornes, lien interne cassé, mot de provenance IA, mot proscrit (résilience, paradigme, impact, empowerment).
- Aucune donnée personnelle non publique ; lieux au centre de la commune ; aucune personne privée nommée dans les analyses.
- Toute modification visuelle : `python3 /tmp/shots.py`-like (Playwright local) → `apercu/` (non versionné) avant de pousser.

## Publication
Push sur `main` → Actions → Pages. Autorisation de Ced (2026-09-30) pour la V0.1 : dépôt, Pages, DNS, HTTPS, déclarations agora. Au-delà : push sur confirmation.
