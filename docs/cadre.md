# Cadre de description — libres.actitude.org

Version 0.1.1 — 2026-10-01 (P1 et P2 précisées par Ced). Source de vérité des clés, des portes et des dimensions.
Toute valeur hors de ce cadre fait échouer le générateur.

## 0. Objet

**libres** documente les collectifs autogérés qui se sont installés sur un lieu en France
depuis 1789 et qui l'ont tenu comme un commun : hors du marché, pour l'intérêt général,
sous une forme de droit civil. L'unité décrite est le **collectif** et sa trajectoire
sur un lieu. Le montage foncier détaillé relève de communs.actitude.org (renvoi par `uid`),
les sources de biblio.actitude.org (renvoi par identifiant).

## 1. Le critère d'entrée : cinq portes, toutes obligatoires

Un cas entre au **corpus** seulement s'il franchit les cinq portes (valeur `oui`).
Un `partiel`, un `non` ou un `inconnu` le range dans les **épreuves** : il est publié,
avec la porte où il s'arrête. Le statut se **calcule**, il ne se saisit jamais.

| Porte | Clé | Question | `oui` si |
|---|---|---|---|
| P1 | `forme_civile` | Toute la chaîne est-elle de droit civil non lucratif ? | Le collectif et le porteur du foncier sont une association (1901, 1908 en Alsace-Moselle), un fonds de dotation, une fondation ou un collectif de fait ; une personne publique propriétaire est admise au cas par cas, si le montage établit clairement un commun (sinon `partiel`). Aucun maillon commercial ou coopératif (SCIC, SAS, SA, SCA, SCOP, coopérative d'habitants), aucune société à parts cessibles. |
| P2 | `foncier_verrouille` | Le foncier est-il sorti du marché de façon opposable ? | Inaliénabilité, veto de réseau, dévolution désintéressée verrouillée ou titre d'usage d'au moins 30 ans, **établis au meilleur effort documentaire** (sources concordantes, acte publié non exigé). Une faculté documentée de vendre, une promesse, une mise à disposition gracieuse non écrite ou une propriété privée « bienveillante » ne suffisent pas. |
| P3 | `usage_ig` | L'usage est-il non marchand et ouvert au-delà du cercle restreint ? | Pas de rente, pas de loyer spéculatif, activité tournée vers un public ou un territoire (accueil, éducation populaire, soin, culture, lutte, milieu). Un entre-soi, même non lucratif, ne suffit pas. |
| P4 | `autogestion` | Les usagers décident-ils eux-mêmes ? | Assemblée des usagers souveraine sur l'usage ; pas de fondateur, de propriétaire ou de financeur qui tranche seul. |
| P5 | `etabli` | Le collectif s'est-il établi ? | Au moins dix ans d'usage continu sur le lieu (ou jusqu'à sa fin, si elle survient après dix ans). |

Valeurs d'une porte : `oui`, `partiel`, `non`, `inconnu`. Chaque porte porte `note` et `source` ;
un `oui` sans note ni source fait échouer le générateur.

**Lecture au maillon faible.** La chaîne entière est lue : un collectif associatif logé
par une SCI à parts cessibles échoue en P1 ; une ferme portée par une foncière commerciale
échoue en P1 même si le fermier est de bonne foi.

## 2. Exclusions nommées (épreuves de référence)

Instruites et publiées comme épreuves, pour que la frontière soit visible :
foncières et fermes Terre de Liens (SCA commerciale, actions cessibles),
Coopérative Oasis et écolieux adossés (SCIC, financeur plutôt qu'usager),
SCI ou GFA à parts cessibles, SAS ou SCIC « de transition », propriété privée « vertueuse ».
La critique porte sur le **motif structurel**, jamais sur les personnes.

## 3. Familles

`communaute_intentionnelle` · `commun_foncier` · `occupation_regularisee` · `lieu_non_marchand`
(habitat collectif, tiers-lieu, maison du peuple, lieu d'éducation populaire).

## 4. Dimensions de classification (prismes)

Chaque dimension : `{valeur, note, source}` ; valeur `inconnu` admise (exclue des calculs,
jamais pénalisante). Les dimensions `multi` prennent une liste.

| Clé | Valeurs |
|---|---|
| `periode` (calculée depuis `debut`) | `1789-1870` · `1871-1914` · `1915-1945` · `1946-1967` · `1968-1989` · `1990-2007` · `2008-` |
| `acces` — comment le lieu a été obtenu | `don_legs` · `souscription` · `achat_collectif` · `occupation` · `bail_public` · `achat_prive_fondateur` · `heritage` |
| `titre` — titre d'usage du collectif | `propriete` · `bail_emphyteotique` · `commodat` · `convention` · `bail_rural` · `usufruit` · `domanialite` · `sans_titre` |
| `porteur_foncier` — nature du propriétaire | `association` · `fonds_dotation` · `fondation` · `personne_publique` · `societe_civile_parts_cessibles` · `societe_commerciale` · `cooperative` · `personne_privee` · `congregation` · `collectif_de_fait` |
| `forme_collectif` | `association` · `collectif_de_fait` · `fonds_dotation` · `fondation` · `cooperative` · `societe_civile` · `societe_commerciale` · `congregation` · `aucune` |
| `verrou` (multi) | `inalienabilite_statutaire` · `domanialite_publique` · `veto_reseau` · `devolution_desinteressee` · `bail_long` · `aucun` |
| `gouvernance` | `assemblee_consensus` · `assemblee_majoritaire` · `conseil_delegue` · `fondateur` · `mixte` |
| `economie` — ce qui fait vivre les personnes | `caisse_commune` · `autosubsistance` · `activites_non_marchandes` · `activites_marchandes_annexes` · `revenus_individuels_externes` · `salariat_structure` |
| `ouverture` | `ouvert_public` · `accueil_regulier` · `cercle_restreint` |
| `finalite` (multi) | `agriculture` · `habitat` · `education_populaire` · `culture` · `accueil_soin` · `spiritualite` · `lutte_territoriale` · `milieu_vivant` · `artisanat_production` · `consommation` |
| `filiation` (multi) | `socialisme_utopique` · `anarchisme` · `mouvement_ouvrier` · `christianisme_communautaire` · `non_violence` · `neo_ruralisme` · `ecologie_politique` · `autonomie` · `education_populaire` · `personnalisme` |
| `rapport_etat` | `conflit` · `regularisation` · `conventionnement` · `indifference` |
| `echelle` — personnes vivant ou œuvrant sur le lieu | `moins_10` · `10_50` · `50_200` · `plus_200` |
| `transmission` | `generations_renouvelees` · `fondateurs_seuls` · `en_cours` |
| `etat` | `actif` · `disparu` · `transforme` |
| `fin` (si disparu ou transformé) | `succession_ratee` · `faillite` · `scission` · `captation` · `dissolution_volontaire` · `expropriation` · `expulsion` · `vente` |

## 5. Ce que le cadre ne conclut pas

Il ne juge pas la valeur humaine d'un collectif, ni la sincérité des personnes.
Il ne mesure pas la domination interne non inscrite dans les actes (dérive de fondateur,
emprise) — limite assumée, signalée en prose quand une source l'établit.
Un `inconnu` veut dire « aucune source trouvée », jamais « n'existe pas ».
Aucune donnée personnelle non publique ; seules les personnes publiques
(fondateurs cités par des sources publiées) sont nommées.

## 6. Faces (regards)

Chaque fiche du corpus peut porter trois faces courtes, sans se substituer :
`igor` (le collectif vécu : ce qui tient, ce qui casse), `eozen` (le montage :
ce qui protège, ce qui est fragile), `antimeta` (la capture : par quel mécanisme
le lieu pourrait être récupéré, ou l'a été).
