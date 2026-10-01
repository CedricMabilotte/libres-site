# Documenter un collectif agricole sans chef : grille d'entretien et pièces à réunir

*Les sources publiées disent comment vivent les fermes collectives, rarement comment elles sont déclarées, assurées et tenues. Ce guide donne la méthode pour combler ce manque avec les collectifs eux-mêmes, sans exposer les personnes ni fournir aux contrôleurs un dossier à charge.*

> **En bref**
> - Dix questions d'entretien, centrées sur le travail réel, la décision, la caisse, la relève et le rapport à la MSA [1].
> - Six familles de pièces : statuts, procès-verbaux d'assemblée, titre foncier, attestation MSA, comptes, conventions ; chacune répond à une porte précise du cadre [2].
> - Consentement écrit du collectif, aucune personne nommée, aucune pièce brute publiée : les papiers d'un lieu peuvent servir de preuve contre lui [3].
> - Le résultat se verse en fiche YAML conforme au référentiel, relue par le collectif avant publication (droit de réponse).
> - Huit cas sont prioritaires ; la question commune à tous est la qualité sous laquelle la MSA a enregistré le collectif, jamais publiée à ce jour [4][5].

## 1. Pourquoi enquêter sur le terrain

Les notes du projet le constatent : sur les fermes associatives, les reportages décrivent la planification tournante, la caisse commune, les chantiers ouverts, mais presque jamais la forme exacte de l'affiliation sociale ni le titre foncier [1][4]. Une seule source publiée affirme qu'une association sans salarié est inscrite à la MSA (Treynas, *Silence* n° 449) [6] ; un collectif rapporte qu'une caisse a d'abord refusé de l'enregistrer, puis l'a admis au vu d'un précédent dans une autre caisse (La Caillasse, *Silence* n° 535) [7]. Ce que les juges n'ont jamais tranché, les collectifs le savent par expérience : il faut aller le leur demander.

## 2. Règles avant tout entretien

| Règle | Application |
|---|---|
| Consentement du collectif | Accord écrit, donné par l'instance collective (assemblée, réunion), sur l'objet de l'entretien, son usage et sa publication. Un membre seul ne consent pas pour le lieu. |
| Non-identification | Aucun nom, âge, situation familiale, statut social individuel (RSA, titre de séjour, emploi extérieur) ; seuls des effectifs et des ordres de grandeur. Les personnes publiques citées par des sources publiées font exception [2]. |
| Pièces non publiées | Les pièces sont lues, pas reproduites. La fiche résume ce qu'elles établissent (« bail rural de 25 ans ») sans citer de montants nominatifs, d'adresses de personnes ni de signatures. |
| Prudence sur les preuves | La rubrique « à faire » des procès-verbaux d'un lieu a servi de preuve dans une requalification du bénévolat (CA Montpellier, 2025) ; un « tableau de service » nominatif est un indice de subordination [3]. On ne demande donc pas les plannings nominatifs. |
| Données sensibles | Rien sur la santé, les opinions, les situations administratives des personnes, les procédures pénales visant un membre. |
| Retrait | Le collectif peut retirer son accord avant publication ; après, il peut demander la correction ou le retrait de la fiche. |
| Information générale | Le projet documente ; il ne donne pas de conseil juridique au collectif. |

La lecture critique du collège 2 rappelle que la documentation elle-même peut devenir la grille du contrôleur [1]. D'où une règle simple : on publie ce qui protège un modèle (structure, montage, rapport aux institutions), pas ce qui expose des personnes.

## 3. La grille d'entretien

Les dix questions viennent de la lecture d'usage (@igor) du collège 2 [1]. Elles sont ouvertes et portent sur des faits récents.

| # | Question | Ce qu'on cherche | Champ de la fiche |
|---|---|---|---|
| 1 | Qui fait quoi chaque semaine ? | Planification tournante ou fixe, place du « responsable » | `gouvernance`, P4 |
| 2 | Quelle a été votre dernière décision difficile, et comment l'avez-vous prise ? | Consensus, vote, délégation, rôle des fondateurs | `gouvernance`, P4 |
| 3 | Quelles tâches ne voit-on pas ? | Comptabilité, papiers, soin, entretien : qui les porte | `gouvernance`, `economie` |
| 4 | Que paie la caisse, que ne paie-t-elle pas ? | Caisse commune, revenus extérieurs, ventes | `economie`, P3 |
| 5 | Sous quelle qualité la MSA vous a-t-elle enregistrés ? Quel précédent avez-vous cité ? | Association, chef d'exploitation désigné, cotisant de solidarité, rien ; caisse concernée | `rapport_etat`, `dossier_juridique` |
| 6 | Comment arrive un nouveau ou une nouvelle ? | Cooptation, période d'essai, apport demandé | `ouverture`, `transmission` |
| 7 | Qu'emporte celui ou celle qui part ? | Parts, apports remboursés, rien | `verrou`, P2 |
| 8 | Racontez un désaccord et comment il s'est réglé. | Instances, médiation, scission | P4, `transmission` |
| 9 | Qu'ont appris de vous les paysans voisins, et vous d'eux ? | Prêts de terres, entraide, conflits | `rapport_etat` |
| 10 | Qu'est-ce qui vous ferait passer au salariat ou à la société ? | Seuil de bascule (cf. La Caillasse, devenue SCOP en 2025) | `etat`, P1 |

Deux relances transversales : « avez-vous un écrit qui le montre ? » (pour relier la réponse à une pièce) et « peut-on le publier sans nommer personne ? ».

## 4. Les pièces à réunir

| Pièce | Où la trouver | Ce qu'elle établit | Porte | Précaution |
|---|---|---|---|---|
| Statuts de l'association (et de toute société liée) | Collectif ; Journal officiel des associations ; greffe pour une société | Objet, non-lucrativité, dévolution, instances | P1, P4 | Vérifier qu'aucun maillon n'est commercial ou à parts cessibles [2] |
| Procès-verbaux des dernières assemblées générales | Collectif | Vie associative réelle, mode de décision, rotation | P4 | Lire, ne pas copier ; pas de plannings nominatifs [3] |
| Titre foncier : acte de propriété, bail, commodat, convention | Collectif ; service de la publicité foncière | Porteur, durée, clauses d'inaliénabilité ou de dévolution | P2 | Un bail rural à une association suppose qu'elle exerce elle-même l'activité (Cass. 3e civ., 14 janv. 2015) et obtienne l'autorisation d'exploiter [8] |
| Attestation ou courrier de la MSA | Collectif | Qualité d'affiliation : association, chef désigné, cotisant de solidarité | — | Pièce la plus rare ; noter la caisse et l'année, pas l'assuré |
| Comptes annuels (deux ou trois exercices) | Collectif | Part des ventes, dons, absence de rémunération | P3 | Agrégats seulement ; pas de dépenses individuelles |
| Conventions (commune, fondation, réseau, voisins) | Collectif ; commune | Rapport à l'État, verrou de réseau, prêts de terres | P2, `rapport_etat` | Convention révocable = verrou faible |
| Extrait Sirene | Annuaire des entreprises | Forme, code d'activité, caractère employeur, date | P1 | Comparer au récit (Treynas : code 71.12B, non agricole) [6][9] |

Le registre public suffit souvent pour la forme et l'ancienneté ; le reste dépend de la confiance du collectif.

## 5. Verser au projet libres

1. **Fiche YAML** dans `data/fiches/<uid>.yml`, sur le modèle `docs/exemple-fiche.yml` : identité, `localisation`, `collectif`, `foncier`, quinze `dimensions`, cinq `portes` (`oui`, `partiel`, `non`, `inconnu`), `chronologie`, `fiabilite`, `dossier_juridique`, `sources` [2].
2. **Chaque valeur porte une source** (index dans la liste `sources`). Un entretien se cite comme « Entretien avec le collectif, date », sans nom. `inconnu` veut dire « aucune source trouvée » [2].
3. **Une porte ne change que sur preuve** : une pièce lue (statuts, titre) ou une source publiée. Une affirmation orale va dans `fiabilite.non_confirme` tant qu'elle n'est pas étayée.
4. **Validation** : la fiche doit se charger par `yaml.safe_load`, les clés et valeurs doivent appartenir à `scripts/referentiel.py`, les index de sources rester dans les bornes, aucun mot proscrit.
5. **Droit de réponse** (procédure proposée) : la fiche est envoyée au collectif avant publication avec un délai de réponse ; ses corrections factuelles sont intégrées, ses désaccords d'interprétation publiés en note ; après publication, toute demande de correction ou de retrait est traitée. La face `igor` peut accueillir le point de vue du collectif.

## 6. Cas prioritaires et questions ouvertes

| Cas (fiche) | Commune | Questions ouvertes |
|---|---|---|
| Longo Maï, Treynas (`longo-mai-treynas`) | Chanéac (07) | Qualité d'affiliation MSA depuis 2002 ; nature du contrat avec la fondation propriétaire ; lien entre Fonds de Terre et la « Fondation Longo Mai » inscrite au répertoire en 2025 ; régime fiscal des ventes de bois [6][9][10] |
| Ferme de l'Oseraie (`ferme-de-l-oseraie`) | Berville-sur-Seine (76) | Est-ce la ferme « déjà déclarée » à la caisse de Rouen citée par La Caillasse ? Propriétaire et bail des terres ; mode de décision [7] |
| La Caillasse (`la-caillasse-cucuron`) | Cucuron (84) | Qualité d'enregistrement obtenue en 2019-2024 ; existence d'une association pour les cultures non marchandes après la SCOP [7] |
| Ferme Légère (`ferme-legere-meracq`) | Méracq (64) | Régime MSA de l'association preneuse ; statut des ventes depuis 2017 ; clauses de la SCI [11] |
| Les Semeuses (`les-semeuses-bure`) | Mandres-en-Barrois (55) | Pourquoi le salariat ; affiliation de l'association exploitante [4] |
| Mas de Granier et La Cabrery | Saint-Martin-de-Crau (13), Vitrolles-en-Luberon (84) | Rôle des sociétés civiles au répertoire ; suite donnée à la réflexion sur l'OACAS [4][12] |
| Longo Maï, Limans (`longo-mai-limans`) | Limans (04) | Pourquoi deux exploitants déclarés ; ce que cela protège [13] |
| Ferme des Vaîtes, Commun Jardin | Besançon (25) | Convention avec la Ville ; preneur du bail rural ; statut social des maraîchers [4] |

L'ordre suit le gain attendu : Treynas et l'Oseraie peuvent établir l'existence d'une association agricole sans salarié reconnue par la MSA ; La Caillasse documente le moment de la bascule.

## 7. Données personnelles (RGPD)

Une fiche décrit un collectif, pas des personnes. Mais dans un lieu de moins de dix résidents, la commune, l'effectif, une date d'arrivée ou un propos rapporté suffisent à identifier quelqu'un. Les notes, enregistrements et transcriptions d'entretien sont, eux, des données personnelles. Le RGPD et la loi Informatique et libertés s'appliquent donc à l'enquête, sinon toujours à la fiche publiée.

**La base légale.** Tout traitement doit reposer sur l'une des bases de l'article 6 du RGPD, choisie avant la collecte et indiquée aux personnes [14][16]. Deux conviennent ici :
- l'**intérêt légitime** (art. 6, 1, f) du projet à documenter des formes collectives, à condition de mettre en balance cet intérêt et les droits des personnes, en tenant compte de leurs attentes raisonnables ; la CNIL demande de documenter cette pondération [16] ;
- le **consentement** (art. 6, 1, a), libre, spécifique, éclairé et univoque [16]. La CNIL distingue l'accord pour participer à une enquête du consentement au traitement des données : deux cases distinctes [16]. L'accord du collectif prévu au § 2 ne vaut pas consentement de chaque personne interrogée.

**Les exceptions de l'article 85.** Le RGPD laisse aux États le soin de concilier protection des données et liberté d'expression, y compris à des fins journalistiques et d'« expression universitaire, artistique ou littéraire » [14]. En France, l'article 80 de la loi Informatique et libertés écarte alors, « lorsqu'une telle dérogation est nécessaire », la limitation de durée de conservation, l'interdiction de traiter des données sensibles (art. 6 de la loi) et plusieurs droits des personnes ; il vise l'expression universitaire, artistique ou littéraire, et l'exercice « à titre professionnel » du journalisme [15]. Le projet ne remplit pas la seconde condition ; la première se discute pour un travail documentaire publié. Mieux vaut ne pas s'y adosser et respecter le droit commun.

**La recherche.** Pour les traitements à des fins de recherche scientifique ou historique, l'article 89 du RGPD et l'article 4 de la loi admettent une conservation plus longue et une réutilisation compatible, moyennant des garanties [14][15]. Le régime suppose une démarche de recherche réelle (protocole, finalité définie) ; il ne dispense pas de base légale [16].

**Les données sensibles (art. 9).** Les opinions politiques et les convictions religieuses ou philosophiques sont des données sensibles dont le traitement est interdit, sauf exceptions : consentement exprès, données « manifestement rendues publiques » par la personne, notamment [17]. Les champs `filiation` et `rapport_etat` décrivent le collectif ; ils ne doivent pas devenir l'opinion d'une personne identifiable. Règle pratique : ne renseigner ces champs qu'à partir de textes publiés par le collectif lui-même, et ne jamais attribuer d'opinion à un membre.

**Minimisation.** Ne collecter que ce qui sert la fiche (art. 5, 1, c) [14]. Prendre des notes plutôt qu'enregistrer ; si l'on enregistre, avec l'accord de chaque personne, et pour transcrire seulement. Pas de noms dans les notes : un code par personne, la table de correspondance conservée à part.

**Durée de conservation.** Elle se fixe avant l'entretien et figure dans l'information donnée aux personnes [18]. La CNIL cite en exemple trois ans à compter de la fin de la collecte ; à l'issue, les données sont supprimées ou anonymisées [18]. Procédure proposée : enregistrement détruit après validation de la transcription par le collectif ; notes pseudonymisées conservées trois ans après la publication de la fiche, puis détruites ; pièces lues non copiées (§ 2).

**Le droit d'opposition (art. 21).** Quand le traitement repose sur l'intérêt légitime, chacun peut s'y opposer pour des raisons tenant à sa situation particulière ; le responsable doit cesser, sauf motifs légitimes et impérieux, et répondre dans un délai d'un mois [20]. Ce droit s'ajoute au droit de réponse du collectif (§ 5) : une personne peut demander le retrait d'un passage même si le collectif l'approuve.

**Anonymiser les entretiens.** Remplacer un nom par un code est une pseudonymisation : les données restent personnelles [19]. Une donnée n'est anonyme que s'il est impossible d'isoler une personne, de relier des jeux de données la concernant et d'en déduire une information nouvelle (individualisation, corrélation, inférence) [19]. Pour un petit collectif, cela suppose d'agréger (« trois résidents sur cinq »), d'arrondir les dates, de ne pas citer mot pour mot un propos reconnaissable, et de croiser la fiche avec les sources publiques du lieu avant publication.

## Ce qui reste incertain

- Le consentement d'un collectif sans représentant désigné : qui signe ? La procédure proposée (décision de l'instance collective) n'a pas été éprouvée.
- La protection des pièces confiées : aucune règle de conservation n'est encore fixée par le projet.
- L'identité de la ferme associative déclarée à la caisse de Rouen : l'Oseraie est la candidate la plus probable (même article, seule ferme associative de l'agglomération documentée), sans confirmation [7].
- La qualité d'affiliation MSA de Treynas : ni *Silence* (2016), ni l'AFP (2025), ni le répertoire ne la donnent [6][10].
- Aucun autre collectif n'a été trouvé qui publie son rapport à la MSA, hors Limans (deux exploitants déclarés) [13].

## Sources

1. Projet libres, « Collège 2 — lectures critiques » (@igor, @antimeta), 1er octobre 2026 : recherche/college2-lectures.md.
2. Projet libres, « Cadre » (portes, dimensions, données personnelles) et `scripts/referentiel.py` : docs/cadre.md (consulté le 1er octobre 2026).
3. Projet libres, note R2 « Jurisprudence », § 2.4 (CA Montpellier 2025, Croix-Rouge 2002) : recherche/R2-jurisprudence.md (1er octobre 2026).
4. Projet libres, note R3 « Études de cas », 1er octobre 2026 : recherche/R3-cas.md.
5. Projet libres, dossier « Une association peut-elle exercer une activité agricole sans chef d'exploitation ? » : docs/dossiers/association-agricole.md (1er octobre 2026).
6. *Silence* n° 449, « Paysans forestiers de Treynas », 2016 : https://www.revuesilence.net/numeros/449-Vivre-avec-la-foret/paysans-forestiers-de-treynas (consulté le 1er octobre 2026).
7. *Silence* n° 535, « Des fermes associatives et militantes », 2024 : https://www.revuesilence.net/numeros/535-Creer-une-ferme-collective/des-fermes-associatives-et-militantes (consulté le 1er octobre 2026).
8. Code rural, art. L. 411-1 (bail rural), cité par la note R2 : recherche/R2-jurisprudence.md (1er octobre 2026).
9. Annuaire des entreprises, « ASS EUROPEENNE LONGO MAI » (SIREN 419 752 316) et « FONDATION LONGO MAI » (SIREN 988 546 610) : https://annuaire-entreprises.data.gouv.fr/entreprise/419752316 et https://annuaire-entreprises.data.gouv.fr/entreprise/988546610 (API Recherche d'entreprises consultée le 1er octobre 2026).
10. AFP, « En Ardèche, la communauté autogérée Longo Maï a pris racine », 31 mars 2025, reprise par La Gazette France : https://www.lagazettefrance.fr/article/en-ardeche-la-communaute-autogeree-longo-mai-a-pris-racine (consulté le 1er octobre 2026).
11. Ferme Légère, « Présentation détaillée » : https://fermelegere.greli.net/projet/details-du-projet.html (consulté le 1er octobre 2026).
12. *Silence* n° 527, « La Cabrery, des vins nature anticapitalistes et féministes », 2023 : https://www.revuesilence.net/numeros/527-Vivre-et-resister-a-Longo-Mai/la-cabrery-des-vins-natures-anticapitalistes-et-feministes (consulté le 1er octobre 2026).
13. *Silence* n° 458, « Les coopératives de Longo Maï », 2017 : https://www.revuesilence.net/numeros/458-Alternatives-en-Hautes-alpes-et-Alpes-de-haute-provence/les-cooperatives-de-longo-mai (cité par la note R5, 1er octobre 2026).
14. Règlement (UE) 2016/679 (RGPD), art. 5, 6, 9, 21, 85 et 89, texte publié par la CNIL : https://www.cnil.fr/fr/reglement-europeen-protection-donnees et https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre9 (consulté le 1er octobre 2026).
15. Loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, art. 4 et 80, texte publié par la CNIL : https://www.cnil.fr/fr/le-cadre-national/la-loi-informatique-et-libertes (consulté le 1er octobre 2026).
16. CNIL, « Recherche scientifique (hors santé) : quelle base légale pour un traitement de recherche ? », 6 janvier 2022 : https://www.cnil.fr/fr/recherche-scientifique-hors-sante-quelle-base-legale-pour-un-traitement-de-recherche (consulté le 1er octobre 2026).
17. CNIL, « Donnée sensible » : https://www.cnil.fr/fr/definition/donnee-sensible (consulté le 1er octobre 2026).
18. CNIL, « Recherche scientifique (hors santé) : les durées de conservation des données » : https://www.cnil.fr/fr/recherche-scientifique-hors-sante/durees-conservations-donnees (consulté le 1er octobre 2026).
19. CNIL, « Recherche scientifique (hors santé) : enjeux et avantages de l'anonymisation et de la pseudonymisation », 13 janvier 2022 : https://www.cnil.fr/fr/recherche-scientifique-hors-sante-enjeux-et-avantages-de-lanonymisation-et-de-la-pseudonymisation (consulté le 1er octobre 2026).
20. CNIL, « Le droit d'opposition : refuser l'utilisation de vos données » : https://www.cnil.fr/fr/comprendre-mes-droits/le-droit-dopposition-refuser-lutilisation-de-vos-donnees (consulté le 1er octobre 2026).
