# A3 — Cas réels : associations agricoles en bénévolat pur
Collège A, chercheur A3. Instruit le 1er octobre 2026. Complète `R3-cas.md` et `R4-formes-voisines.md` sans reprendre leurs cas.

**Cible de Ced.** Association d'intérêt général à activité agricole (culture, élevage, verger, semences, forêt nourricière, jardin vivrier collectif), sans chef d'exploitation ni rétribution, sans salarié, en bénévolat pur et contribution libre décorrélée de toute compensation, idéalement validée par la MSA ou l'administration fiscale (rescrit).

**Méthode.** Recherche web large (presse locale, sites des lieux, réseaux), puis contrôle de chaque structure au répertoire Sirene et au RNA par l'API Recherche d'entreprises (tranche d'effectif salarié, forme, code d'activité), consultée le 1er octobre 2026. Le contrôle Sirene a écarté plusieurs lieux présentés comme « associatifs » : salariés, SCI ou société civile agricole adossées.

## 1. Constat principal
**Aucune validation publique par la MSA ni aucun rescrit fiscal n'a été trouvé pour une association agricole en bénévolat pur.** Les cas qui collent le mieux à la cible sont de petites associations de conservation (vergers conservatoires, maisons de semences, forêts-jardins) qui ne vendent pas ou presque, n'emploient personne et n'ont manifestement jamais eu à se poser la question : elles restent sous le seuil où l'activité devient « agricole » au sens fiscal ou social. Leur faiblesse commune est le foncier : terrain communal sans titre publié, prêt gracieux, ou propriété privée d'un fondateur. Aucun des huit cas fichés n'entre au corpus.

Le seul cas trouvé qui publie une **reconnaissance d'intérêt général avec reçus fiscaux** est un refuge animalier sans salarié (Ferme des Rescapés, Lot), hors objet faute de production agricole.

## 2. Cas retenus (fiches écrites dans `data/fiches/`)
| uid | Commune | Forme, salariés | Foncier, titre | Cession | MSA / fisc | P1 | P2 | P3 | P4 | P5 | Statut calculé |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `foret-jardin-de-la-cartade` | Glaine-Montaigut (63) | Association 2020, non employeuse | Co-fondatrice, bail emphytéotique (durée inconnue), 0,56 ha | Aucune vente documentée | Rien de publié | non | partiel | oui | partiel | non | épreuve |
| `jardin-foret-du-brin-de-paille` | Saint-Genès-Champanelle (63) | Association 2022, non employeuse | Commune, loyer modeste, conditions : espace public, gratuité | Cueillette libre | Rien de publié | partiel | inconnu | oui | partiel | non | épreuve |
| `foret-jardin-de-persignat` | Aubiat (63) | Association Matercoop 2012, non employeuse | Commune, « carte blanche » | Aucune | Rien de publié | partiel | inconnu | partiel | partiel | non | épreuve |
| `maison-semence-loire-pilat` | Maclas (42) | Association 2011, non employeuse | Terrain « gracieusement prêté », puis Goély | Graines adoptées, distribuées, troquées gratuitement | Rien de publié ; L. 661-8 | inconnu | non | oui | partiel | partiel | épreuve |
| `verger-croqueurs-secondigny` | Secondigny (79) | Association 1990, bénévoles | MFR selon une étude de 2000, ou l'association (sources divergentes), 1 ha | Entrée gratuite ; jus, plants « pour une somme modique » | Rien de publié | partiel | inconnu | oui | partiel | oui | épreuve |
| `verger-croqueurs-puyricard` | Aix-en-Provence (13) | Association 1992, non employeuse | Ville d'Aix, mise à disposition | Ventes d'arbres et de fruits aux portes ouvertes | Rien de publié ; dévolution statutaire désintéressée | partiel | inconnu | partiel | partiel | oui | épreuve |
| `verger-patrimonial-de-fraize` | Fraize (88) | Association de patrimoine 1993, non employeuse | Verger communal, 55 ares | Greffons mis à disposition ; jus | Rien de publié ; aide FGER | partiel | inconnu | oui | partiel | oui | épreuve |
| `trucland-sorges` | Sorges-et-Ligueux-en-Périgord (24) | Association | SCI Truc'land (2019) | « Troc et vente » des surplus | Rien de publié | non | non | partiel | inconnu | non | épreuve |

Validation locale : valeurs contrôlées contre `scripts/referentiel.py` (familles, formes, dimensions, ordre des portes), index de sources dans les bornes, mots proscrits absents, relecture `yaml.safe_load`, statut recalculé par `referentiel.calcul`. Générateur complet non relancé.

## 3. Grille de proximité avec la cible
Lecture : `oui` = établi par une source ; `partiel` = en partie ou avec réserve ; `?` = non sourcé.

| Cas | Bénévolat pur (sans salarié ni rétribution) | Sans chef (décision collective) | Objet d'intérêt général | Contribution libre, gratuité | Validation MSA / fisc | Proximité |
|---|---|---|---|---|---|---|
| Maison de la Semence de la Loire, Pilat | oui | partiel (décisions en réunion, prêteur tiers) | oui (conservation, diffusion gratuite) | oui (adoption, troc, gratuité) | ? | **forte** |
| Brin de paille | oui | partiel (commune impose les conditions) | oui | oui (cueillette au besoin, gratuité imposée) | ? | **forte** |
| Verger de Secondigny | oui | ? | oui (conservation, accueil gratuit) | partiel (plants « pour une somme modique ») | ? | **forte** |
| Verger de Fraize | oui | partiel (projet municipal) | oui | oui (greffons mis à disposition) | ? | forte |
| La Cartade | oui | partiel (propriétaire co-fondatrice) | oui | ? (sort des récoltes non publié) | ? | forte |
| Verger de Puyricard | oui | partiel (CA élu) | oui (statuts) | non (ventes aux portes ouvertes) | ? | moyenne |
| Persignat | oui | partiel (animateur) | partiel | ? | ? | moyenne |
| Truc'land | partiel (lieu de vie) | ? | partiel | non (troc et vente) | ? | faible |

## 4. Cas examinés et écartés
| Cas | Commune | Raison |
|---|---|---|
| Forêt Gourmande | Diconne (71) | Association employeuse (1 à 2 salariés) ; « Atelier » et « École de la forêt gourmande » immatriculés séparément (Sirene) |
| Ferme de la Mhotte | Saint-Menoux (03) | Association employeuse (3 à 5 salariés) ; société civile agricole et SCI de la Mhotte au répertoire |
| Conservatoire des légumes anciens du Béarn (CLAB) | Assat (64) | Directrice salariée (presse 2022), tranche 3 à 5 salariés au répertoire ; vente de jus et confitures aux adhérents ; dons à l'aide alimentaire : proche par l'usage, hors cible par le salariat |
| Dans l'Ensemble, verger partagé | Baud (56) | Association employeuse (3 à 5 salariés) ; terrain municipal prêté (2021) ; confitures à prix libre : utile comme exemple de prix libre |
| Les Jardins Bénéfiques | Montcenis (71) | Projet porté par une fondatrice (« j'ai créé l'association ») ; vente des surplus (paniers à 10 €, tomates au kilo) |
| Les Jardins Nourriciers | Marignac-en-Diois, Sainte-Croix (26) | Jardin « à vocation professionnelle », légumes vendus aux adhérents |
| Ferme solidaire de l'écolieu Lacoste | Tarnos (40) | Atelier-chantier d'insertion, 17 salariés |
| La Ferme des 3 Ailes | Ville-sous-Anjou (38) | Ferme pédagogique bénévole (2020), mais portée par une fondatrice sur un foncier familial |
| La Ferme des Rescapés | Cassagnes (46) | Refuge sans salarié, reconnu d'intérêt général avec reçus fiscaux (seul cas trouvé), mais sans production agricole, foncier privé, tenu par deux personnes |
| Ferme conservatoire de Leyssart | Saint-Pey-de-Castets (33) | Association non employeuse (2001) ; aucune source publique hors registres : piste |
| FERME (Fédération pour promouvoir l'élevage des races domestiques menacées) | Souternon (42) | Réseau bénévole d'éleveurs, pas de lieu propre |
| Conservatoire des races d'Aquitaine | Mérignac (33) | Association employeuse (10 à 19 salariés) |
| Pétanielle, maison des semences | Tarn | Collection cultivée chez des partenaires changeants (CPIE à Réalmont en 2024, association Domino à Roquesérière en 2025) : pas de lieu propre |
| Collectif des Semeurs du Lodévois-Larzac | Lodève (34) | Site officiel détourné (contenu sans rapport) ; non instruit |
| Coopérative Cravirola, SAS Terres Communes | La Brigue (06) | Foncier loué à une SAS ; coopérative et vente des produits |
| Arche de Saint-Antoine | Saint-Antoine-l'Abbaye (38) | Maison communautaire d'accueil ; maraîchage vivrier marginal, hors cible agricole (possible fiche « lieu non marchand ») |
| Terre en Partage | Coudoux (13) | Jardins partagés à parcelles, réservés aux adhérents (2017) |

## 5. Ce que ces cas apportent au dossier « association agricole »
1. **Le silence administratif comme régime de fait.** Sans vente régulière ni salarié, aucune de ces associations ne publie de rapport à la MSA ; aucune source ne mentionne un contrôle. C'est l'inverse du cas d'Aspiran (R3) : l'exposition naît de la vente et du travail d'autrui, pas de la culture elle-même.
2. **Les semences et les plants offrent la seule brèche de cession écrite** : l'article L. 661-8 couvre la Maison de la Semence de la Loire et les ventes de plants des Croqueurs de pommes.
3. **La vente ponctuelle reste la ligne de partage** entre bénévolat pur (Pilat, Brin de paille, Fraize) et activité annexe (Puyricard, Secondigny pour le jus, Truc'land).
4. **Le foncier communal domine** (quatre cas sur huit), sans titre publié : la porte P2 reste « inconnu » partout. Le Brin de paille montre toutefois une piste : une commune qui conditionne la mise à disposition à l'usage public et à la gratuité.
5. **Le motif SCI** (Truc'land) reproduit à petite échelle l'exclusion nommée du cadre.

## 6. Pistes non abouties
- Demander aux associations Croqueurs (Deux-Sèvres, Provence) leur convention foncière et leur éventuelle reconnaissance d'intérêt général ; trancher la propriété du verger de Secondigny (MFR ou association).
- Demander à la commune de Saint-Genès-Champanelle l'acte de mise à disposition (durée, loyer, conditions).
- Chercher au Journal officiel (annonces des associations) les objets statutaires de La Cartade, du Brin de paille et de Matercoop.
- Rescrit MSA : aucune réponse publique trouvée ; seule voie restante, une demande directe de rescrit social à une caisse de MSA (référence exacte du texte à vérifier) ou un témoignage d'association.
- Réseau Forêts nourricières, Troisièmes Voix, réseau CLIP, ZAD de Notre-Dame-des-Landes : aucun nouveau cas exploitable trouvé au-delà des fiches existantes.

## Sources principales
- Tikographie, « Forêts nourricières #1/2 : portrait de trois collectifs avec bêche », 21 mars 2023.
- Sites des associations (msloirepilat.wordpress.com, croqueurs79.fr, croqueursdeprovence.fr, lacostelle.org, trucland.org).
- Gomet', reportage sur le verger de Puyricard (2024) ; PresseLib, CLAB d'Assat (2022) ; Kaizen et 18h39, verger partagé de Baud (2021).
- Répertoire Sirene et RNA via l'API Recherche d'entreprises, consultée le 1er octobre 2026.
