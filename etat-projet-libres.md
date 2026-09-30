# État du projet — libres

## 2026-09-30 — V0.1
- Cadre strict à cinq portes, 16 dimensions, 4 familles (`docs/cadre.md`). Décisions dans `decisions/`.
- 41 fiches instruites (5 lots de recherche parallèles, sources publiées, portes au maillon faible).
- Résultat : 1 corpus sous condition (La Chapelle, Toulouse — verrou par titre, bail municipal 40 ans contesté), 5 au seuil (tous bloqués sur P2 : Tanneries, Lentillères, La Déviation, Manifesten, Ferme du Berquet), 35 épreuves.
- Faces igor/eozen/antimeta sur les 6 cas corpus+seuil ; transversaux des trois voix ; typologie de 6 mécanismes de capture (antimeta) ; épreuve contradicteur (verdict initial « retravailler » → thèse durcie + 3 garde-fous appliqués).
- Analyses : V de Cramér corrigé sur 37 variables (599 paires), ACM (Benzécri), sensibilité (5 variantes), entonnoir.
- Site généré (54 pages) : accueil, cas (filtres), fiches, portes, prismes (matrice, explorateur, plan factoriel), carte SVG locale, frise, regards, méthode, données (JSON/CSV).

## Points ouverts
- Corrections à reporter dans Communs (revue mémoire) : La Ruche = domaine du Pâtis à Rambouillet, loué dès 1904 (pas Saint-Maur, pas acheté) ; Boimondau : Barbu quitte la communauté en 1946 (candidat en 1965).
- La Chapelle : preuve de publication du bail au fichier immobilier ; association signataire.
- Antidote / CLIP : statuts et baux non publiés → P2 partiel ; demander les actes (droit de réponse).
- Ariège (Villeneuve-du-Bosc) : fiche quasi vide, à instruire sur sources primaires.
- Transmission et économie non documentées pour > 40 % des cas.

## 2026-09-30 (suite) — mise en ligne et vérification
- En ligne : repo CedricMabilotte/libres-site, Pages (workflow), CNAME Gandi `libres` créé. HTTPS : certificat en attente (vérification programmée) ; http OK.
- Vérification factuelle de 12 fiches : 7 exactes, 5 corrigées (La Déviation : crédits bancaires et locataire 2015-2019, 0,27 ha ; Berquet : mode de transfert inconnu ; Pommiers : reprise début 2016 ; Longo Maï : Spartakus autrichien, Hydra suisse ; La Ruche : chronologie 1905) + précisions (Tanneries 1997/1998, SCTL 6 357 ha et 99 ans selon larzac.org, Manifesten salarié en 2022).
- Traces agora posées (non commitées dans agents/ : working tree déjà modifié par d'autres sessions → code-task ct-2026-09-30-libres-commit-traces).
- Doc de synthèse dans le Project claude.ai « collectifs libres » : claude/libres-v0.1.md.

## 2026-09-30 (fin de soirée) — clôture de la V0.1
- Traces agora commitées sans toucher aux autres modifications en cours (a585c48, aaf40f9) ; bulle igor corrigée pour le validateur v7.1.
- Charte revue par @graphiste (valider avec corrections, option B) : terre d'igor #E2622E / #A8451A, ocre texte #8A5F1E, gris #6E685C (AA), statuts portés par la forme sur carte et plan factoriel, impression. `identite-libres.yaml` créé (herite_de identite-igor).
- Vignettes sociales 1200×630 (accueil + 41 cas) + og:image.
- Ligne vox `resources/vox/lignes/libres/` proposée, inactive.
- HTTPS : en attente du certificat GitHub (cache du joker Gandi, TTL 3 h) ; vérification programmée le 2026-10-01 à 01:15 UTC.

## 2026-10-01 — arbitrages de Ced appliqués
- P1 : personne publique admise au cas par cas si le montage établit clairement un commun (59 Rivoli et Rayol passent `partiel`).
- P2 : lecture au meilleur effort documentaire (pas de preuve de publication) → La Déviation et Manifesten entrent au corpus ; Hautes-Planches (P5) et Longo Maï (P1) au seuil ; lieux Antidote restent `partiel` (faculté documentée de vendre).
- Résultat : 2 corpus + 1 corpus sous condition (La Chapelle), 5 seuil, 33 épreuves. Prismes réécrits (V P1×P4 = 0,74), thèse mise à jour, faces trio pour les 2 nouveaux cas au seuil, vignettes régénérées.
- Registre : site libres en commentaire du champ site d'@igor. Ligne vox : pas encore.
- Redirection Telegram vue par Ced : cache du joker Gandi (*.actitude.org → t.me) + 301 mis en cache par le navigateur ; DNS correct. HTTPS relancé au passage de 01:15 UTC.
