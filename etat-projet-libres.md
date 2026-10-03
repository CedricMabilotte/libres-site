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

## 2026-10-01 — association agricole sans chef d'exploitation
- Demande de Ced : documenter « Ferme 14 » et l'association reconnue par la CA de Grenoble comme association non employeuse à activité agricole sans chef d'exploitation.
- Résultat : ni « Ferme 14 » ni l'arrêt n'ont été retrouvés (Judilibre, presse, réseaux). Décision grenobloise la plus proche, en sens inverse : CA Grenoble 16/11/2023 RG 22/00174 (pension d'équidés, président déclaré chef d'exploitation). Source de Ced demandée.
- Ajouts : 5 fiches (Ferme de l'Oseraie 76, La Caillasse 84, Ferme légère Méracq 64, Ferme associative du Pays du Mont-Blanc 74, Jardins ouvriers des Vertus 93), toutes épreuves, avec clé `dossier_juridique` ; page « Dossier : association et activité agricole » (docs/dossier-association-agricole.md). 46 cas.

## 2026-10-01 — collèges d'agents : « Une association peut-elle cultiver sans chef d'exploitation ? »
- Collège 1 (recherche, 5 chercheurs) : textes et doctrine (R1), jurisprudence (R2, ~20 décisions nouvelles), cas de fermes associatives (R3, 7 fiches), formes voisines (R4, 6 fiches), comparaisons et généalogie (R5). Notes dans `recherche/`.
- Collège 2 (lecture critique) : @eozen, @igor, @antimeta, @contradicteur, @valorisation → `recherche/college2-lectures.md`.
- Collège 3 (comblement + rédaction, 6 rédacteurs) : 13 dossiers dans `docs/dossiers/` (dossier maître, défendre le modèle, chef d'exploitation, autorisation d'exploiter, bénévolat et récolte, accident et assurance, fiscalité et prix libre, aliments hors marché, foncier, OACAS, habitat et urbanisme, formes voisines, documenter un cas).
- Vérification : 62 références contrôlées (5 corrections), cohérence juridique @eozen (23 reformulations appliquées), 18 fiches vérifiées (1 correction) ; itération 5 sur les oublis (loi 1901 et société créée de fait, cotisations au-delà du seuil, RGPD, habitat).
- Résultat : 59 cas ; corpus 3 + 1 sous condition (Treynas entre au corpus) ; 5 au seuil ; section /dossiers/ en ligne ; prismes réécrits (+ 7e lecture : « cultiver sans chef : possible, rarement établi »).
- Point dur identifié : autorisation d'exploiter (L331-2 I 3° b) pour toute structure sans membre exploitant. Arrêt « grenoblois » favorable : seulement deux jugements de première instance (TJ Grenoble 2021), infirmés en appel.

## 2026-10-01 — cible « association d'intérêt général agricole en bénévolat pur »
- Collège A (5 chercheurs) : rescrit social MSA (A1), rescrit fiscal et IG (A2), cas (A3, 8 fiches), seuils et démarches (A4), voies communautaires (A5).
- Collège B : @eozen (séquence : prise de position du préfet L331-4-1 → rescrit MSA → L80 B → L80 C), @contradicteur (condition décisive : les produits ne reviennent pas aux membres en tant que membres ; robustesse 2→3), @antimeta (ce que le rescrit fait au collectif), @igor (deux mondes : conservation sous les seuils / vie communautaire au-dessus).
- Collège C : 4 dossiers (association-ig-benevole, rescrits-et-prises-de-position, sous-les-seuils, voies-communautaires) + compléments (statuts, comptes, taxe foncière, responsabilité, coûts).
- Vérification : 64 références (7 corrections), 14 reformulations @eozen, 8 fiches (5 corrigées ; propriétaire du verger de Secondigny = MFR de Frécul).
- Constat central : **aucun rescrit MSA ni fiscal publié ou revendiqué** pour une association agricole en bénévolat pur. Les cas les plus proches (vergers conservatoires, maisons de semences, forêts-jardins) vivent sous les seuils sans validation écrite. 67 cas.
- Note : un agent a créé /home/ced/codes/ (copie locale du Code rural, Code civil, Code de l'urbanisme) et $HOME/w/ (sauvegardes) hors du dossier projet.

## 2026-10-01 — dossier « modèle cible » (workflow, 22 agents)
- Passe méta (pensée critique, @eozen, @antimeta, @igor) → `recherche/M-meta.md` : questions, 6 prismes (Π1 démarchandisation des flux, Π2 suffisance et convivialité, Π3 gouvernance sans chef, Π4 reproduction et externalités, Π5 licéité et preuve, Π6 capture et réversibilité) × 10 dimensions (foncier, gouvernance, travail, récolte, argent, subsistance, échelle et vivant, habitat, État et preuve, transmission).
- Instruction ligne par ligne, rédaction, 5 critiques (@eozen, @contradicteur, @antimeta, @igor, @lumen), révision (52 remplacements, 17 manques traités, liens vérifiés).
- `docs/dossiers/modele-ideal.md`, placé en tête des dossiers. Matrice 60 cellules : 11 possibles, 32 sous conditions, 10 non jugées, 2 impossibles en droit actuel (nourrir d'abord les cultivateurs ; protection sociale sans salariat), 5 hors droit. Aucun cas du corpus n'atteint la cible.
- Durcissement @contradicteur intégré : le lieu revendique sa qualification au lieu d'éviter les contrôles ; liste des adhérents remise sur demande ; le quart de SMA borne l'affiliation, pas la requalification en salariat.
- Version A4 Paged.js (`/dossiers/modele-ideal/imprimer/`, 17 pages, une fiche par dimension avec espace de notes d'assemblée) et PDF `assets/pdf/modele-ideal.pdf` produit par `scripts/imprimer.py` (Playwright). Polyfill Paged.js 0.4.3 (MIT) embarqué localement.
- Reste : corps ~4 500 mots (au-dessus de la cible 4 000) ; questions renvoyées au §9 (taille minimale du groupe, calendrier saisonnier, parcours d'arrivée/départ, reprise du commodat en veille, régime de la donation d'immeuble).

## 2026-10-01 — dossier « modèle cible » v2 : trois parties (workflow, 27 agents)
- Consignes de Ced : philosophie concrète « marcher libres sur une terre libre » ; nue-propriété en fonds de dotation ; communs et droits d'usage par groupe bénéficiaire ; dons acceptables par soin et pédagogie ; lexique et notes liées ; références associatives strictes ; cas idéal « possible » ; puis modèle à trois parties (fonds de dotation, association socioculturelle, association agricole).
- Verdict : raisonnable sous sept conditions (titres directs fonds → associations, gratuité stricte, deux associations d'intérêt général, séparation réelle et non-cumul, toute la culture dans l'agricole, argent public seulement à la socioculturelle, groupe d'au moins ~15 réguliers ; sinon variante à deux parties).
- Titres : commodat écrit de 30 ans puis droit réel de jouissance spéciale daté (Maison de Poésie, Cass. 3e civ. 2012, 2016) si un rescrit en écarte le coût ; usufruit écarté (taxé comme libéralité). ORE de 99 ans. Accord SAFER requis 10 ans en cas de rétrocession (R. 142-1).
- Cas fictif « Les Communaux du Bief » (Gâtine, 3 ha, ~150 000 € de collecte, 6 500 à 16 500 €/an, frise 2027-2058). Faisceau de droits × 10 groupes ; tableau des gestes permis, à risque, exclus.
- 116 sources, lexique de 38 entrées ; notes : appel lié directement à la source + note courte en bas de page à l'impression.
- Recherche : recherche/M2-R1 à R7 ; v1 dans recherche/modele-ideal-v1.md.
- Mise en page revue par @graphiste : colonne de 132 mm à 10 pt, sommaire paginé, couverture (En bref seul, avertissement au pied), appels collés et regroupés, notes courtes, en-têtes de tableau répétés, termes du lexique soulignés en pointillé, grille sur sa propre page, insécables. PDF 32 p.
- Reste : gabarit d'identité imprimé (niveaux 2 et 3, identite-libres.yaml sans bloc `imprime:`) à décider ; contacts à prendre (questions rédigées dans M2-R3).

## 2026-10-01 — dossier « Vendre, échanger, troquer » (workflow, 21 agents)
- Périmètre de l'association agricole du montage à trois parties : 24 seuils datés 2025/2026, matrice de 22 gestes × 8 régimes, échelle de paliers 0 (donner) à 4 (jamais), clauses de statuts par palier, fiches fête de soutien / graines et greffons / foin, Communaux du Bief recalculés (≈ 1 730 € de ventes et troc par an, IS de 0 à ≈ 350 €), effets sur le fonds et la socioculturelle. 85 sources, 26 entrées de lexique. Notes : recherche/V-R1 à V-R8.
- Seuils clés : franchise lucrative 80 011 € (TVA 2025) / 81 051 € (2026) ; 6 manifestations de soutien ; ventes aux membres ≤ 10 % ; revenus agricoles d'une association à l'IS 24 % sans franchise ; TVA agricole au-delà de 46 000 € ; heures de vente comptées par la MSA (instruction 2015-370) ; L. 442-7 C. com. (vente prévue aux statuts).
- Huit corrections à reporter dans les dossiers voisins : listées au dossier (§ « corrections à reporter »).

## 2026-10-03 — dossier « Échanger de l'argent sans être un professionnel » (workflow, 24 agents)
- Citoyen et association : six frontières (commerce, profession, impôt, TVA, social, pénal) + consommation ; tableaux de seuils 2025/2026 ; 25 fiches (Permis / Jusqu'où / Bascule / À tenir) ; échelle en cinq paliers du don à la profession ; trois montages pour un lieu collectif et leurs risques ; comparaison Royaume-Uni, Allemagne, Italie, Belgique. 146 sources, 33 entrées de lexique. Notes : recherche/E-R1 à E-R10.
- Constat central : aucun statut général de l'activité occasionnelle en droit français ; tout revenu est imposable au premier euro ; ce qui fait basculer, ce sont des indices (achat pour revendre, habitude, organisation, publicité, outillage), pas un montant.
- Points non vérifiés sur source primaire listés au dossier (Légifrance inaccessible aux robots pour 8 articles hors codes locaux).
