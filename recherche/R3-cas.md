# R3 — Études de cas : fermes et collectifs agricoles associatifs
Collège de recherche n° 1, chercheur R3. Instruit le 1er octobre 2026.
Question : où une association loi 1901 ou un collectif de fait exerce-t-il (ou a-t-il tenté) une activité agricole sans chef d'exploitation ni salarié ?

## 1. Cas retenus (fiches écrites dans `data/fiches/`)

| uid | Commune | Forme | Foncier | Déclaration agricole | P1 | P2 | P3 | P4 | P5 | Statut calculé |
|---|---|---|---|---|---|---|---|---|---|---|
| `longo-mai-treynas` | Chanéac (07) | Association (Longo Maï Ardèche) | Fondation Fonds de Terre, location | **Inscrite à la MSA, membres tous bénévoles** (Silence, 2016) ; qualité d'affiliation non publiée | oui | oui | oui | oui | oui | corpus |
| `longo-mai-mas-de-granier` | Saint-Martin-de-Crau (13) | Association (réseau Longo Maï) | Fondation selon le réseau ; société civile « SCA Mas de Granier » active depuis 1990 | Non documentée ; ventes régulières sur les marchés | partiel | partiel | oui | oui | oui | épreuve |
| `longo-mai-la-cabrery` | Vitrolles-en-Luberon (84) | Association (réseau Longo Maï) | Fondation selon le réseau ; « SCA Cabrery » créée 1992, fermée le 24/09/2026 | Non documentée ; 12 000 bouteilles/an | partiel | partiel | oui | oui | oui | épreuve |
| `ferme-des-vaites-besancon` | Besançon (25) | Association, aucun salarié | Ville (espace vert municipal) | Aucune ; inspection vétérinaire 2019, identification des ruminants et porcs demandée | partiel | inconnu | oui | partiel | partiel | épreuve |
| `zone-a-patates-pertuis` | Pertuis (84) | Collectif de fait | Établissement public foncier (maisons) | Aucune ; cultures sans titre | partiel | non | oui | inconnu | non | épreuve (expulsion 2022) |
| `les-semeuses-bure` | Mandres-en-Barrois (55) | Association, code 01.13Z | Agriculteur privé, ~3 ha mis à disposition | Association se présentant comme exploitante ; **3 salariés à temps partiel** en 2023 | non | non | oui | inconnu | non | épreuve |
| `commun-jardin-besancon` | Besançon (25) | Association, code 01.13Z, membres pluriactifs | Ville, bail rural 9 ans (preneur non précisé) | Non documentée ; question AMA / cotisant de solidarité | partiel | non | partiel | inconnu | non | épreuve |

Chaque fiche porte un champ `dossier_juridique`. Validation locale : clés et valeurs conformes à `scripts/referentiel.py`, index de sources dans les bornes, aucun mot proscrit ; générateur complet non relancé.

## 2. Cas écartés

| Cas | Commune | Raison |
|---|---|---|
| La Caillasse, Ferme de l'Oseraie | Cucuron, Berville-sur-Seine | Déjà fichés (`la-caillasse-cucuron`, `ferme-de-l-oseraie`) ; seuls cas associatifs de *Silence* n° 535 |
| Gaec de la Blada | Arvière-en-Valromey (01) | GAEC (Silence n° 535) |
| La Clef des sables | Isère | Coopérative (Silence n° 535) |
| Fermes partagées | réseau | Coopérative de réseau, pas un lieu |
| Ferme collective de Peyregoux | Peyregoux (81) | Exploitants installés, terres Terre de Liens (Reporterre) |
| Goutailloux | Tarnac (19) | SCI Le Goutailloux + GAEC Terras Comunas (répertoire Sirene) |
| Ferme du Ter'Ter | Marcillé-Raoul (35) | SCIC propriétaire + GAEC preneur |
| Saute-Mouton | Tigy (45) | Ferme gérée par une SARL, association pédagogique annexe |
| Village Emmaüs Lescar-Pau | Lescar (64) | Association employeuse (tranche 100 à 199 salariés au répertoire), ferme intégrée au village ; sources sur la ferme inaccessibles |
| Ferme Emmaüs Baudonne | Tarnos (40) | Structure d'insertion salariée |
| La Ferme du Bonheur | Nanterre (92) | Lieu porté par un fondateur et une compagnie, salariés ; agriculture secondaire. Possible épreuve ultérieure (conflit avec la mairie depuis 1997) |
| La Flayssière (Arche) | Joncels (34) | Association employeuse (1-2 salariés), propriété non documentée |
| Filature de Chantemerle (Longo Maï) | Saint-Chaffrey (05) | Salariat imposé selon le réseau ; activité textile |
| Le Jardin des Passages | Quézac (15) | Lieu d'accueil ; maraîchage vivrier marginal ; collectif depuis 2021-2022 |
| Ferme Chamboule-tout | Salies-de-Béarn (64) | Activité agricole en projet, collectif de trois personnes (2023) |
| Les Vagues des Terres | Ploumilliau (22) | Projet d'achat (2024), pas d'activité documentée |
| Maraîcher d'Aspiran (wwoofing) | Aspiran (34) | Exploitant individuel poursuivi par la MSA : utile au dossier juridique, hors objet |
| Association foncière agricole libre de Douelle | Douelle (46) | Association de propriétaires, pas un collectif exploitant ; source non consultable |
| ZAD NDDL (AACB, Abrakadabois), Lentillères, Limans | — | Couverts par les fiches existantes ; Abrakadabois est forestier |

## 3. Constats utiles au dossier « association agricole »

1. **Treynas est le seul cas trouvé où une source publiée affirme qu'une association sans salarié est inscrite à la MSA** (Silence n° 449, 2016). La qualité d'affiliation (chef d'exploitation désigné ? cotisant de solidarité ?) reste à demander au collectif.
2. **Le réseau Longo Maï se dit associatif, mais le répertoire Sirene montre des sociétés** au nom de ses fermes : « SCA Mas de Granier » (société civile, 1990, active), « SCA Cabrery » (société civile, 1992, fermée le 24 septembre 2026), « SICA Longo Mai » à Limans (société d’intérêt collectif agricole, 1991, employeuse). Le maillon foncier réel est à établir.
3. **Communautés de l'Arche** : une « SCEA Communautés de l'Arche » (société civile d'exploitation agricole) existe à Roqueredonde depuis 2017. Information à verser à la fiche `arche-borie-noble` (non modifiée ici) : l'activité agricole y passe par une société civile.
4. Deux associations récentes (Les Semeuses, Commun Jardin) s'immatriculent avec un code agricole (01.13Z) : l'association se présente comme exploitante. L'une emploie, l'autre repose sur la pluriactivité ; aucune ne publie son régime MSA.
5. Le statut OACAS (organisme d'accueil communautaire et d'activités solidaires) est étudié en 2023 par la Cabrery et le Mas de Granier pour régulariser des personnes accueillies dans des fermes : piste juridique nouvelle (Silence n° 527 ; voir aussi Silence n° 525, « A4, des papiers… et des terres pour s'installer »).

## 4. Pistes non abouties

- **Treynas** : article AFP/France 24 du 31 mars 2025 (« En Ardèche, la communauté autogérée Longo Maï a pris racine ») non lisible (robots) ; à consulter pour l'état actuel.
- **Mas de Granier, Cabrery** : statuts des sociétés civiles (Infogreffe) et fichier immobilier (service de la publicité foncière) pour établir le propriétaire et un éventuel apport à la fondation en 2026.
- **Silence n° 525**, « A4, des papiers… et des terres pour s'installer » : statut OACAS en agriculture, non lu.
- **Transrural initiatives**, « Jeunesse déterminée recherche fermes collectives à son goût » (juin 2026) : non lu.
- **Sivens** (Métairie neuve, 2014-2015) : aucune source exploitable trouvée sur l'activité agricole de l'occupation.
- **Bure** : autres initiatives agricoles (élevage de chèvres envisagé en 2023) ; maison associative L'Augustine (association créée en 2024).
- **Ferme des Vaîtes** : convention avec la Ville et activité après 2022, à demander à l'association.
- **Commun Jardin** : identité du preneur du bail rural (association ou membres) ; statut social des maraîchers.
- Non explorés faute de résultat ciblé : RENETA, Accueil paysan, Solidarité paysans, Atelier paysan, CIAP (statut coopératif, P1 exclu d'emblée), Kaizen, Socialter, Basta, Radio Parleur, lundimatin, Campagnes solidaires. Aucun « réseau des fermes associatives » n'a été trouvé.
- *Silence* (revuesilence.net) bloque certains outils de lecture (erreur 403) mais reste lisible par simple téléchargement des pages.

## Sources principales

- Silence n° 449 (2016), n° 512 (2022), n° 527 (2023), n° 535 (2024) : revuesilence.net
- Reporterre : « Dans le Vaucluse, la Zap de Pertuis a été expulsée » (2022) ; « Près de Bure, des maraîchères cultivent les terres confisquées par le nucléaire » (2023) ; « Ces agronomes déserteurs ont monté une ferme collective »
- Marsactu (2022) ; webzine de Grand Besançon Métropole (2022, 2026) ; blog de la petite ferme des Vaîtes ; sites lacabrery.org, masdegranier.org, fermeduterter.fr, lafermedubonheur.fr
- Répertoire Sirene via l'API Recherche d'entreprises (consultée le 1er octobre 2026)
