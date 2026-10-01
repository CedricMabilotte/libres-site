# V-R8 — Cas réels qui vendent un peu : pratiques, montants, contrôles

Piste R8 de la re-exploration du périmètre de « Terre cultivée », l'association agricole du [modèle cible](../docs/dossiers/modele-ideal.md). Elle est non employeuse, sans chef d'exploitation, tenue par des bénévoles, et donne jusqu'ici sa récolte. La question posée : que font, en pratique, des associations proches qui vendent, échangent ou troquent un peu ? Pour quels montants, sous quelle forme, avec quels contrôles connus ?

**Bouclier 1.** Ce qui suit est une information juridique générale au 1er octobre 2026, pas un conseil. **Bouclier 2.** Tout changement réel passe par trois actes qui engagent : une modification des statuts, un nouveau rescrit et un avenant au commodat. Ils se préparent avec un notaire et un avocat spécialisés (foncier solidaire, ESS).

**Ce fichier ne refait pas le droit applicable.** Il y renvoie :
- fiscalité de la vente, 4 P, 206-5, 46 000 € et six manifestations : [fiscalite-et-prix-libre](../docs/dossiers/fiscalite-et-prix-libre.md), [V-R2](V-R2.md) ;
- capacité statutaire de vendre (L. 442-10 C. com.), habitude, déballage : [V-R1](V-R1.md) ;
- semences, plants et greffons : [V-R3](V-R3.md) ;
- consommation : [V-R4](V-R4.md) ;
- effets sur le montage : [V-R6](V-R6.md) ;
- sanitaire : [aliments-hors-marche](../docs/dossiers/aliments-hors-marche.md) ;
- seuils MSA : [sous-les-seuils](../docs/dossiers/sous-les-seuils.md), [chef-d-exploitation](../docs/dossiers/chef-d-exploitation.md) ;
- contrepartie au travail : [benevolat-et-recolte](../docs/dossiers/benevolat-et-recolte.md) ;
- association IG bénévole : [association-ig-benevole](../docs/dossiers/association-ig-benevole.md) ;
- rédaction des demandes : [rescrits-et-prises-de-position](../docs/dossiers/rescrits-et-prises-de-position.md).

Les fiches de cas déjà instruites sont dans [A3-cas](A3-cas.md) et [M2-R6](M2-R6.md). Ce fichier les complète sans les reprendre.

**Niveaux de preuve.**
- **texte** : code lu en vigueur, ou compte publié au JOAFE ;
- **décision** : lue en entier sur Juricaf ;
- **doctrine administrative** : BOFiP, publication d'un service de l'État ;
- **pratique documentée** : site de la structure, presse, répertoire SIRENE ;
- **non jugé** : rien trouvé, ou raisonnement.

**Méthode.**
- **Comptes publiés.** Je les ai interrogés par l'API ouverte du Journal officiel (jeu `jo_associations`, `source = "dca"`). Les PDF ont été téléchargés directement depuis le dépôt de la DILA, selon le schéma `https://fr.ftp.opendatasoft.com/datadila/JO/ASSOCIATIONS/DCA/PDF/{année}/{jjmm}/{siren}_{jjmmaaaa}.pdf`.
  - **Correction.** [M2-R6](M2-R6.md) jugeait ces comptes illisibles par voie automatique. Ils le sont par cette adresse.
  - Les comptes scannés ont été passés à l'OCR (tesseract). Leurs montants ont été vérifiés ligne à ligne sur l'image.
- **Répertoire SIRENE.** Lu par l'API Recherche d'entreprises (`recherche-entreprises.api.gouv.fr`).
- **Codes.** Code de commerce (à jour au 1er sept. 2026) et CGI, lus dans `/home/ced/codes/`.
- **Juricaf.** Recherches menées le 1er oct. 2026 :
  - « "jardins partagés" vente » : 5 résultats, tous en urbanisme ou expropriation ;
  - « "croqueurs de pommes" » : 1 résultat, lu ;
  - « "jardin partagé" association bénévoles » : 1 résultat, sans rapport (droit des étrangers) ;
  - trois recherches croisant association, bénévoles, vente de légumes, MSA et travail dissimulé : 0 résultat exploitable.
- **Légifrance** refuse les robots. Les liens sont donnés par identifiant LEGIARTI pour contrôle manuel.

---

## Synthèse

| Cas | Ce qui est cédé | Comment | Montant connu | Statut social et fiscal observé | Contrôle publié | Niveau |
|---|---|---|---|---|---|---|
| Croqueurs des Deux-Sèvres (verger de Secondigny) | Jus de pomme, pommes, greffons ; plants greffés « pour nos adhérents » | Depuis 2023, pépinière « en partenariat avec un pépiniériste » ; vente réservée aux adhérents ; jus fait par les bénévoles | Non publié. Presse 2011 : « quelque 20 tonnes de fruits » par an, vendus « pour financer l'entretien du site » | Effectif non vérifié (association non retrouvée dans SIRENE sous son nom) ; pas de comptes au JOAFE ; aucun rescrit connu | Aucun | pratique documentée |
| Croqueurs de Provence (verger de Puyricard) | Arbres de la pépinière, boutures, pommes, fruits à coque, objets | Deux journées portes ouvertes par an (3-4 oct. 2026), « vente au profit de l'association », au milieu de stands de producteurs tiers et d'une buvette | Non publié | Non employeuse (SIRENE : tranche « NN ») ; statuts sans mention de la vente de fruits ou d'arbres (art. 8) ; terrain « prêté par la ville d'Aix » | Aucun | texte (statuts publiés) + pratique documentée |
| Aux Prés en Bulles (La Marinie, Aveyron) | Pain au levain, savons | Dépôt au magasin de producteurs Les Giroflées (Figeac) | Non publié | **A eu 1 ou 2 salariés en 2023** (SIRENE), convention collective IDCC 7024, code NAF 01.11Z, certifiée bio ; pas d'immatriculation au RNE | Aucun | pratique documentée (SIRENE) |
| Jardins partagés « Ça pousse à Montfrin » (Gard) | Produits du jardin, marchandises | Non précisé | **1 878,57 € en 2025**, soit 31,5 % des produits ; 0 € en 2024 | Non employeuse ; comptes au JOAFE sans sectorisation ni mention fiscale | Aucun | texte (comptes publiés) |
| Jardins d'insertion (Potager extraordinaire, Potagers du Télégraphe, Jardin Soli-Bio) | Paniers, légumes, plants | Adhésion-panier, boutique, marchés, vente à des professionnels | 87 925 € à 124 840 € par an, soit 12 à 24 % des produits | Employeurs (250 000 à 530 000 € de salaires) ; financés surtout par des subventions | Aucun | texte (comptes publiés) |
| Kokopelli | Semences en sachets | Vente en ligne et en boutique | Non publié par l'association | Employeuse (20 à 49 salariés en 2023), NAF 01.64Z | Poursuites pénales jugées (Cass. crim. 2008, lue dans [V-R3](V-R3.md)) | décision + pratique documentée |

**Lecture d'ensemble.**
1. **Aucune association comparable à Terre cultivée n'a publié de contrôle** fiscal, URSSAF, MSA ou DDPP sur une petite vente. Je n'en ai trouvé ni sur Juricaf ni dans la presse.
2. **Deux sortes de cas se distinguent nettement.**
   - **Ceux qui vendent peu restent bénévoles.** Ils tiennent la vente dans des formes étroites : vente aux seuls adhérents, deux journées par an, ou petit montant (moins de 2 000 € par an à Montfrin).
   - **Ceux qui vendent régulièrement en circuit marchand ont tous des salariés.** C'est le cas de la Marinie (dépôt en magasin de producteurs), de Kokopelli et des jardins d'insertion.

   Le corpus ne contient **aucun contre-exemple** : pas d'association bénévole qui vende régulièrement en magasin ou sur un marché. C'est un constat sur un petit échantillon, pas une règle.
3. **Les montants observés pour des associations bénévoles sont très bas.** Le seul chiffre publié est celui de Montfrin : 1 878,57 € en 2025. Il est 43 fois inférieur à la franchise des impôts commerciaux de 2026 (81 051 €) et 24 fois inférieur au seuil agricole de TVA (46 000 €). Les seuils ne sont donc pas, en pratique, ce qui contraint ces associations. Ce qui les contraint, c'est **la forme** de la vente : son public, sa fréquence, son circuit. Cela rejoint [V-R1](V-R1.md) et [V-R2](V-R2.md).
4. **Le précédent de la Marinie diverge du modèle cible sur deux points.** Les comptes publiés d'Antidote ne montrent **aucune redevance** de la Marinie entre 2023 et 2025. L'association agricole a eu des salariés et vend en magasin. La Marinie confirme le schéma fonds, association des lieux, association agricole. Elle ne montre pas qu'une association agricole bénévole puisse vendre en circuit marchand.

---

## Q1. Croqueurs de Secondigny et de Puyricard : montants, statuts, rescrit, déclaration DDPP

### Q1-a. Croqueurs de pommes des Deux-Sèvres (verger de Secondigny)

1. **Ce qui est vendu.**
   - Le site de l'association présente « la préparation de scions greffés pour les adhérents afin de diffuser ces vieilles variétés » et « la fabrication de jus de pommes par les bénévoles ».
   - La page « Vente pour nos adhérents » précise : « Depuis 2023, une pépinière en partenariat avec un pépiniériste permet à notre association de fournir aux adhérents des plants greffés de pommiers, poiriers, pruniers, etc. Les variétés sont greffées en février-mars et en septembre ».
   - La page « Adhésion » liste parmi les avantages de l'adhérent : « Bénéficier d'un choix important de greffons et plants greffés » et participer à la « mise en bouteilles ».
   - **Aucun prix n'est publié.** Les listes de variétés de 2025 ne sont pas liées en ligne.

   **pratique documentée** (https://croqueurs79.fr/ ; https://croqueurs79.fr/vente-pour-nos-adherents/ ; https://croqueurs79.fr/adhesion/, consultés le 01/10/2026).

2. **Volume.**
   - Un article de presse locale du 3 novembre 2011 indique : « Chaque année, le verger conservatoire offre quelque 20 tonnes de fruits. Des pommes à croquer ou pour le jus de pomme vendues pour financer l'entretien du site ». Il mentionne aussi la vente de greffons « auprès du public intéressé ».
   - Le verger compte 1 ha et environ 110 à 120 variétés.
   - Aucune donnée récente.

   **pratique documentée** (*Caractères*, https://www.caracterres.fr/les-croqueurs-de-pommes-cultivent-les-essences-locales).

3. **Statut.**
   - L'association compte 180 adhérents en 2020 (site). Ce n'est pas la même que l'association nationale.
   - Elle **n'a déposé aucun compte au JOAFE** : aucune occurrence « croqueurs » dans la source `dca`.
   - La fiche « Office de tourisme » indique qu'elle accepte chèques et espèces.
   - **Rescrit** : aucun n'est publié (les rescrits individuels ne le sont jamais) et aucun n'est mentionné sur le site. **Non trouvé.**
   - **Déclaration à la DDPP** : non trouvée.
   - **pratique documentée.**

4. **Ce que le cas montre pour Terre cultivée.** Trois formes se superposent :
   - (a) **vente réservée aux adhérents** ;
   - (b) **production confiée en partie à un professionnel** : la pépinière « en partenariat avec un pépiniériste ». Qui vend juridiquement, de l'association ou du pépiniériste, n'est pas dit ;
   - (c) **transformation simple faite par les bénévoles** : le jus.

   La forme (b) est la plus intéressante pour le modèle. La part marchande peut être portée par un professionnel extérieur. Mais la convention entre l'association et le pépiniériste n'est pas publiée, et rien ne dit si l'association achète les plants pour les revendre (achat-revente, donc secteur lucratif, cf. [V-R2](V-R2.md)) ou si le pépiniériste vend directement aux adhérents. **Non jugé.**
   - Le titre foncier du verger reste celui relevé dans [M2-R6](M2-R6.md) Q1-a : la parcelle appartient à une MFR, sans titre publié.

### Q1-b. Croqueurs de pommes de Provence, Alpes, Côte d'Azur « Li Vieii Pero » (verger de Puyricard)

1. **Identité.** Association déclarée en juillet 1992, SIREN 501 391 502, RNA W131003024, NAF 94.99Z, sans tranche d'effectif salarié. **pratique documentée** (SIRENE).
2. **Statuts publiés en ligne** (https://croqueursdeprovence.fr/nos-statuts/). Ce sont des statuts associatifs, et leur version déposée en préfecture n'a pas été vue. **pratique documentée**.
   - Objet (art. 2) : « la recherche, la sauvegarde du patrimoine génétique fruitier régional, la promotion et la valorisation des variétés fruitières régionales, l'information et l'éducation du public […] ».
   - Ressources (art. 8) : les cotisations ; « les recettes provenant de la vente des brochures techniques et autres publications, des manifestations, fêtes et expositions diverses relatives à l'activité de l'Association » ; les subventions et dons manuels ; la publicité.
   - **Les statuts ne prévoient pas la vente de fruits ni d'arbres.** Elle se rattache seulement, au mieux, aux recettes « des manifestations ». C'est le point que [V-R1](V-R1.md) traite sous L. 442-10 C. com. : la vente habituelle de produits par une association dont les statuts ne la prévoient pas.
3. **Ce qui est vendu, et quand.** La charte de l'association mentionne « vente de fruits et de jeunes arbres, visites guidées du verger » et « 2 Journées Portes Ouvertes le premier week-end d'octobre ». Le tract des journées 2026 (3 et 4 octobre, « entrée et parking gratuits ») annonce une « Vente au profit de l'association » :
   - « Arbres fruitiers régionaux de notre pépinière » ;
   - « Boutures diverses (arbustes fruitiers et vivaces) » ;
   - « Pommes bio et raisonnées » ;
   - « Fruits à coques » ;
   - « Confections de sacs, pochettes, décorations en tissus », « Sacs et gobelets avec logo de l'association ».

   Il annonce aussi des stands tiers : « légumes bio, de bières bio, de miel, de biscuits, de glaces bio, de confitures, de nappes provençales, de savons […] ainsi qu'une buvette et des Foodtrucks ».

   **pratique documentée** (https://croqueursdeprovence.fr/charte-croqueurs-puyricard/ ; https://croqueursdeprovence.fr/wp-content/uploads/2026/05/@Flyer-JPO-Croqueurs-de_finitif.pdf).
4. **Foncier** : « verger de sauvegarde (situé sur un terrain prêté par la ville d'Aix-en-Provence) ». La convention n'est pas publiée. **pratique documentée.**
5. **Montants** : non publiés. Pas de comptes au JOAFE. **Rescrit et déclaration DDPP** : non trouvés.
6. **Ce que le cas montre pour Terre cultivée.** C'est le modèle de la **vente concentrée sur deux journées annuelles**, qui ressemble aux « six manifestations » du 261-7-1° c CGI (fiscalité : [V-R2](V-R2.md)). Deux traits empêchent d'en faire un modèle tel quel :
   - la présence d'exposants non producteurs (savons, faïences, nappes). Selon la lecture de L. 310-2 III 3° dans [V-R1](V-R1.md), la fête ne relève donc pas de l'exemption des « manifestations agricoles lorsque seuls des producteurs ou des éleveurs y sont exposants » ;
   - l'absence de base statutaire pour la vente de fruits et d'arbres.

   Le verger compte aussi « des ceps de vignes ». Les boutures vendues sont annoncées comme « arbustes fruitiers et vivaces », pas comme de la vigne. Sur l'exclusion de la vigne, voir [V-R3](V-R3.md).

### Q1-c. Une décision lue sur les Croqueurs : la marque et la « vie des affaires »

**TJ Lyon, 2 avril 2024, n° 21/04605.** **décision** (https://juricaf.org/arret/FRANCE-TRIBUNALJUDICIAIREDELYON-20240402-2104605).

- **Les faits.** L'Association nationale des Croqueurs de pommes est titulaire d'une marque semi-figurative (n° 99 784 010, déposée le 31 mars 1999, renouvelée en 2019). La marque vise notamment « produits agricoles ; fruits ; boissons de fruits et jus de fruits », « gelées confitures compotes », et l'éducation et les expositions. Une association locale, plus ancienne (1986), utilisait le nom pour ses ateliers, ses stands et son site.
- **La décision.** Le tribunal retient la contrefaçon. L'association locale « fait bien usage du signe dans la vie des affaires », car « une association poursuit un avantage économique indirect, adapté à sa qualité particulière, en diffusant une publication qui est susceptible de lui attirer de nouveaux adhérents ou des dons ». Il lui interdit l'usage du signe et la condamne à 4 000 € au titre de l'article 700 CPC.
- **La portée.** C'est une décision de première instance, et l'appel n'a pas été recherché. Elle ne dit rien de la fiscalité ni du droit social. Elle rappelle en revanche un risque oublié : **dès qu'une association vend des fruits, du jus ou des plants, le nom et le logo qu'elle met sur l'étiquette ou le stand relèvent du droit des marques**, quelle que soit sa non-lucrativité.
- **Pour Terre cultivée** : vérifier à l'INPI, avant toute vente étiquetée, que le nom choisi n'est pas une marque déposée pour les classes 29, 31 et 32. **Non jugé** pour l'application au cas.

---

## Q2. La Marinie : comment l'association agricole se situe-t-elle face au fonds Antidote ?

### Ce qui est établi

1. **Trois structures** (rappel [M2-R6](M2-R6.md), complété).
   - Le fonds de dotation **Antidote** (SIREN 882 625 288).
   - L'association **Les Communs de la Marinie** (SIREN 107 690 703, déclarée le 15 juillet 2021). Son objet : « donner une forme d'existence autonome aux Lieux […] réunir les usager·ères des Lieux qui lui sont confiés […] donner à ses membres d'une part le pouvoir de décider ensemble des usages des Lieux et d'autre part la responsabilité d'en prendre soin ».
   - L'association agricole **Aux Prés en Bulles** (SIREN 877 643 379, déclarée le 31 mai 2019). Son objet : « maintenir une vie Paysanne à La Marinie ; développer et promouvoir des activités agricoles, artisanales, sociales, pédagogiques et culturelles générant des dynamiques humaines et du lien social en milieu rural ».

   **texte** (JOAFE, annonces de création du 29/06/2019 et du 27/07/2021, via l'API `jo_associations`).
2. **Ce que vend l'association agricole.** Pain au levain cuit au feu de bois, variétés anciennes de blé ; savons saponifiés à froid (huile de colza, calendula cultivé sur place). Ils sont distribués par **Les Giroflées**, magasin de producteurs à Figeac. **pratique documentée** (https://www.les-giroflees.fr/producteurs/aux-pres-en-bulles/). Le site d'Antidote ajoute qu'« un petit appentis servira de lieu d'accueil et de vente une fois restauré ».
3. **Statut social et fiscal de l'association agricole** (SIRENE, mise à jour du 01/10/2026) :
   - code NAF **01.11Z** (culture de céréales) ;
   - **tranche d'effectif « 01 » (1 ou 2 salariés) pour 2023** ;
   - convention collective **IDCC 7024** (production agricole et CUMA) ;
   - « caractère employeur : N » à la date de mise à jour ;
   - certifiée **bio** ;
   - **non immatriculée au RNE** (Pappers).

   **pratique documentée** (https://annuaire-entreprises.data.gouv.fr/entreprise/877643379).

   **L'association agricole de la Marinie n'est donc pas non employeuse** : elle a eu au moins un salarié en 2023. C'est un troisième écart avec le modèle cible, en plus de la vente et de la redevance relevées dans [M2-R6](M2-R6.md).
4. **Le lieu est entré dans la dotation d'Antidote par donation.** Les comptes 2025 du fonds (exercice clos le 31/12/2025, publiés au JOAFE) détaillent la « dotation non consomptible ». **texte** (https://fr.ftp.opendatasoft.com/datadila/JO/ASSOCIATIONS/DCA/PDF/2025/3112/882625288_31122025.pdf, annexe p. 17-19).
   - Les actifs y sont intitulés « DONATION AUX PRES EN BULLES 12700 LA MARINIE ».
   - Il s'agit d'un terrain de 4 116 m², d'un bâtiment agricole de 580 m², d'une ruine de 170 m² et d'un appentis de 45 m², tous acquis le **22/11/2024**.
   - Leur valeur brute immobilisée est de **46 359,82 €** (terrain et quotes-parts de terrain : 7 480,78 € ; bâtiments : 38 879,04 €).
   - La dotation complémentaire de 2024 s'élève à **84 000 €** et couvre les donations de la Marinie et de Keriskis.
   - **Ambiguïté.** L'intitulé peut désigner l'association agricole comme **donatrice**, ou seulement comme **usagère** du bien donné. Le site d'Antidote raconte qu'un habitant du hameau avait mis « une partie du lieu à la disposition du collectif », puis la « décision d'acquérir le lieu ». Je n'ai pas lu l'acte de donation. **Non tranché.**
5. **Aucune redevance de la Marinie n'apparaît dans les comptes du fonds.**
   - Les produits du fonds de 2023 à 2025 comptent des dons manuels et du mécénat fléchés « Les Communs de la Marinie » : 776,40 € de dons en 2024, 97 € de dons et 3 000 € de mécénat en 2025.
   - En sens inverse, ils comptent des « quotes-parts de générosité reversée – LA MARINIE » : 13 000 € en 2023, 13 000 € en 2024, 3 000 € en 2025.
   - La seule ligne de « Loyers » est de 3 214 € en 2025, pour l'ensemble des lieux et sans affectation. Le fonds n'avait encaissé aucun loyer en 2024.
   - Les comptes ne mentionnent ni bail emphytéotique ni redevance par lieu.
   - **texte** (comptes 2023, 2024 et 2025, même dépôt, fichiers `882625288_31122023`, `882625288_31122024` et `882625288_31122025`).
   - **Conséquence.** La « redevance modique » annoncée sur le site d'Antidote ([M2-R6](M2-R6.md)) est soit nulle, soit pas encore exigée, soit noyée dans les 3 214 € de 2025. **Non tranché.**
6. **Régime fiscal du fonds.** L'annexe 2025 indique : « L'entité est un organisme sans but lucratif non soumis aux impôts commerciaux au régime de droit commun ». Les comptes sont certifiés par un commissaire aux comptes (2 660,36 € TTC d'honoraires). **texte**. Le régime fiscal d'Aux Prés en Bulles n'est pas publié : l'association ne dépose pas de comptes.

### Ce que le cas montre pour Terre cultivée

- La Marinie illustre la **circulation de fonds** entre un fonds et le lieu : le fonds collecte des dons fléchés puis les reverse en « quotes-parts ». Une association agricole qui vend un peu peut donc rester financée surtout par le don.
- Mais l'association agricole de la Marinie est **employeuse** et **vend en circuit marchand** : c'est l'hybride que le modèle cible écarte.
- Rien dans les pièces lues n'indique un rescrit ni une sectorisation fiscale.

---

## Q3. Grainothèques, maisons de semences, vergers conservatoires : prix, volumes, mentions, contrôles

1. **Bourses aux greffons réservées aux adhérents (Croqueurs d'Île-de-France).**
   - « Seuls les adhérents ont accès à la bourse ».
   - En 2025 : 80 participants, 286 variétés, environ 1 307 greffons distribués.
   - Depuis 2023, chaque adhérent est limité à deux greffons par variété.
   - Les prix et la contrepartie ne sont pas indiqués.

   **pratique documentée** (https://www.croqueur-idf.fr/se-procurer-greffons-et-porte-greffes/bilans-des-bourses-r%C3%A9centes.html).
2. **Bourse aux greffons ouverte au public (Bretoncelles Patrimoine & Nature, Orne).** Première édition le 11 février 2023, « plus de 120 visiteurs », « plus de 70 variétés » de pommes disponibles « à l'achat ». Prix non indiqués. **pratique documentée** (https://www.bretoncelles-patrimoine-nature.fr/accueil/patrimoine-naturel/bourse-aux-greffons.html). Pour la vente de greffons à des amateurs, voir [V-R3](V-R3.md).
3. **Maison des semences sur le mode du don (Pétanielle, Tarn, association, SIREN 795 050 053).**
   - Les semences de blé pré-multipliées par des jardiniers forment « un 1er stock de quelques kilos qui sera donné au paysan demandeur ».
   - Les « grains » sont distribués dans des AMAP, des fournils et des foires.
   - Aucune vente de semences n'apparaît sur le site.

   **pratique documentée** (https://www.petanielle.org/actions/redeploiement-des-semences/).
4. **Prix de marché d'un sachet, comme repère.**
   - Les Jardins du Largue (04) vendent leurs semences à « 2,50 € » le sachet, ou « 2 € le sachet à partir de 10 sachets ». Ils précisent que le contenu « correspond à l'utilisation d'un jardin familial », avec la mention « Semences standard destinées aux jardiniers amateurs ». Ce vendeur est **un entrepreneur individuel** (code juridique 1000, NAF 01.13Z), pas une association.
   - **pratique documentée** (https://www.les-jardins-du-largue.org/boutique/).
   - La mention « destinées aux jardiniers amateurs » est la pratique des petits vendeurs pour se placer sous l'exception de L. 661-8 C. rur. ([V-R3](V-R3.md)).
5. **Lecture du Réseau Semences Paysannes**, non officielle.
   - Vente de semences non inscrites possible « si elles sont destinées à un usage non commercial (ex : pour jardiniers amateurs […]) » ou pour les « espèces non réglementées ».
   - « Pour les plants, la vente de variétés non inscrites au Catalogue officiel est interdite pour les plants potagers, même à usage non commercial. Elle reste possible pour les plants fruitiers sans exploitation commerciale. »

   **pratique documentée** (https://www.semencespaysannes.org/semons-nos-droits/questions-frequentes.html). C'est conforme à [V-R3](V-R3.md), qui en donne les textes.
6. **Association qui vend à grande échelle : Kokopelli** (SIREN 433 481 124). NAF 01.64Z (traitement des semences), **20 à 49 salariés en 2023**, aucun compte au JOAFE sous ce nom. Les poursuites dont elle a fait l'objet (Cass. crim., 8 janv. 2008, n° 07-80.534) et l'arrêt CJUE C-59/11 sont lus dans [V-R3](V-R3.md). **pratique documentée** (SIRENE). Ce n'est pas un comparable : c'est une entreprise de semences sous forme associative.
7. **Contrôles connus.**
   - **DGCCRF, enquête « végétaux d'ornement », avril 2021 à avril 2022.** 62 établissements contrôlés ; « 33 % des établissements contrôlés présentaient des anomalies » ; 40 % de non-conformités sur 30 produits analysés, dont des semences de cosmos à germination nulle ; « 14 avertissements ». L'enquête vise des commerces : elle ne mentionne ni association, ni bourse aux plantes, ni grainothèque. **doctrine administrative** (https://www.economie.gouv.fr/dgccrf/laction-de-la-dgccrf/les-enquetes/vigilance-sur-la-qualite-et-la-loyaute-dans-le-secteur-des).
   - **Aucun contrôle publié** sur une grainothèque, une bourse aux greffons ou un verger conservatoire associatif. **Non trouvé.**

---

## Q4. Jardins partagés et forêts-jardins tenant un étal à prix libre : contrôles publiés ?

1. **Contrôles fiscaux, URSSAF, MSA ou DDPP publiés visant une association de jardin : aucun trouvé.**
   - Juricaf : voir la Méthode. Les cinq décisions trouvées avec « jardins partagés » et « vente » portent sur l'urbanisme ou l'expropriation (par ex. CAA Paris, 18 mars 2026, 24PA00836 ; CAA Marseille, 22 déc. 2020, 19MA03331). J'ai vérifié par mots-clés qu'aucune ne mentionne la TVA, l'IS, l'URSSAF, la MSA ou le travail dissimulé.
   - Aucune réponse ministérielle trouvée sur ce point.
   - **Non trouvé.**
2. **Contrôles du secteur, sans association visée.** Contrôle conjoint DDPP-URSSAF sur un marché de Vannes le 13 juin 2026 : étiquetage et origine d'une part, travail dissimulé d'autre part. **55 opérations** de ce type sont prévues en 2026 dans le Morbihan. Selon l'article, « aucun résultat chiffré n'a été communiqué ». **pratique documentée** (presse : https://info.fr/vannes-controle-conjoint-ddpp-urssaf-marche-fruits-legumes-travail-dissimule/, citant la préfecture du Morbihan ; source primaire non lue). Ce qui en ressort : **un étal sur un marché public est un lieu de contrôle ordinaire**. Un étal à la ferme ou dans une fête associative l'est beaucoup moins.
3. **Position du réseau de l'agriculture urbaine** (AFAUP, FAQ juridique, 22 juin 2023) : « Oui une association peut vendre ses légumes pour s'autofinancer. Mais pour bénéficier de l'exonération d'impôts commerciaux, elle doit respecter certaines conditions […] La vente n'est pas forcément réservée uniquement aux adhérents mais cela peut être une des alternatives pour respecter la condition d'absence de concurrence ». **pratique documentée** (https://www.afaup.org/helpie_faq/est-ce-quune-association-peut-vendre-ses-legumes-pour-sautofinancer-la-vente-est-elle-reservee-uniquement-a-ses-adherents/). Ce n'est pas une source officielle. Le raisonnement des 4 P est dans [V-R2](V-R2.md).
4. **Prix libre** : aucun compte publié ne distingue des recettes « à prix libre ». Montfrin enregistre ses ventes en comptes 701 (produits finis) et 707 (marchandises), ce qui est l'écriture d'une vente ordinaire. Le passage du prix libre au don est traité dans [fiscalite-et-prix-libre](../docs/dossiers/fiscalite-et-prix-libre.md). **Non jugé.**

---

## Q5. Comptes publiés : part des ventes dans les ressources

Comptes lus au JOAFE (source `dca`). L'URL du PDF suit le schéma `https://fr.ftp.opendatasoft.com/datadila/JO/ASSOCIATIONS/DCA/PDF/{aaaa}/3112/{siren}_3112{aaaa}.pdf`. **Niveau : texte** pour tous les montants.

| Association (SIREN) | Exercice | Ventes | Total des produits | Part des ventes | Autres ressources notables | Salaires | Sectorisation, mention fiscale |
|---|---|---|---|---|---|---|---|
| Jardins partagés « Ça pousse à Montfrin », Gard (924 978 653) | 2025 | **1 878,57 €** (produits finis 1 520,77 € ; marchandises 357,80 €) | 5 966,11 € | **31,5 %** | Cotisations 2 224 € ; cotisations avec contrepartie 130 € ; manifestations 510,99 € ; subvention 300 € ; abandons de frais 466,79 € | 0 | Aucune |
| Idem | 2024 | **0 €** | 4 241,92 € | 0 % | Cotisations 2 607 € ; générosité du public 371,70 € ; manifestations 783,22 € | 0 | Aucune |
| Terres nourricières et solidaires en Sud Morvan, Nièvre (923 696 702) | 2025 | 1 036,38 € (ligne « achats/ventes ») | 54 780,29 € | 1,9 % | Prestations 13 737,89 € ; subventions 4 780 € ; fondations 6 000 € ; commande groupée 27 858,32 € (opération de transit) | 8 839,32 € | Aucune (tableau simplifié) |
| Conservatoire du Potager extraordinaire, Vendée (828 189 837), chantier d'insertion | 2021 | **124 840 €** de biens (et 6 530 € de prestations) | 523 213 € (exploitation) | **23,9 %** | Subventions 113 421 € ; reprises et transferts de charges 265 767 € | 252 013 € | Non lue dans l'annexe (OCR) |
| Les Potagers du Télégraphe (498 644 368), chantier d'insertion | 2021 | **91 042 €** (104 727 € en 2020) | 769 793 € | **11,8 %** | Subventions 500 330 € | 527 983 € | Non lue |
| Jardin Soli-Bio, Eure-et-Loir (517 432 415), chantier d'insertion | 2024 | **87 925 €** : paniers adhérents 62 080 € ; légumes aux professionnels 11 850 € ; boutique du jardin 5 887 € ; plants 2 815 € ; vrac adhérents 1 054 € | 737 945 € | **11,9 %** | Subventions d'exploitation 553 899 € | 500 004 € | Ligne « Impôts sur les sociétés » vide |
| Fonds Antidote (882 625 288), pour mémoire | 2025 | Loyers 3 214 € | 160 642 € (exploitation) | 2,0 % | Dons 48 078 € ; mécénat 90 000 € | 0 | « non soumis aux impôts commerciaux » |

**Remarques.**
- **Pourquoi ces associations publient.** L. 612-4 C. com. oblige à publier les comptes au-delà de 153 000 € de subventions publiques par an (D. 612-5). Les jardins d'insertion y sont tenus. Montfrin et Sud Morvan sont loin du seuil : leur dépôt est volontaire, ou relève d'un autre motif non indiqué. **texte** pour le seuil ; **non trouvé** pour le motif.
- **Aucune des associations bénévoles du corpus de cas** (Croqueurs 79, Croqueurs PACA, Aux Prés en Bulles, Pétanielle, Maison de la Semence du Pilat) **ne publie ses comptes.** Le constat de [M2-R6](M2-R6.md) est confirmé.
- **Aucun compte lu ne fait apparaître de sectorisation** (secteur lucratif distinct) ni d'impôt sur les sociétés acquitté. Pour les jardins d'insertion, l'annexe n'a pas été lue en entier.
- **Repère pour Terre cultivée.** Le seul cas bénévole chiffré, Montfrin, vend pour environ 1 900 € par an. Cela représente près d'un tiers de ses ressources, mais reste à 2,3 % de la franchise de 2026. Les jardins d'insertion vendent 50 fois plus, mais ce sont des employeurs subventionnés : ils ne sont pas comparables au montage.

---

## Seuils et plafonds rencontrés dans les cas

Cette piste ne les instruit pas : ils le sont dans les dossiers voisins. Je les ai revérifiés dans les codes locaux là où un cas les met en jeu.

| Seuil | Valeur | Années | Texte | URL | Niveau |
|---|---|---|---|---|---|
| Franchise des impôts commerciaux (activités lucratives accessoires) | **80 011 €** | Exercices clos à compter du 31/12/2024 (IS) ; CET 2025 ; recettes TVA 2025 | CGI 206-1 bis ; 261-7-1° b ; actualité BOFiP du 16/04/2025 | https://www.weblex.fr/weblex-actualite/associations-nouveau-seuil-de-franchise-des-impots-commerciaux-pour-2025 (relais de l'actualité BOFiP, non lue directement) | doctrine administrative (de seconde main) |
| Idem | **81 051 €** | Exercices clos à compter du 31/12/2025 (IS) ; CET 2026 ; TVA 2026 | CGI 261-7-1° b (texte local : « dans la limite de 81 051 € ») ; BOI-IS-CHAMP-10-50-20-20-20260805 § 1 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054374042 ; https://bofip.impots.gouv.fr/bofip/2659-PGP.html/identifiant=BOI-IS-CHAMP-10-50-20-20-20260805 | texte + doctrine administrative |
| Assujettissement à la TVA agricole (remboursement forfaitaire au-delà) | **46 000 €** de recettes, en moyenne sur deux années civiles consécutives ; sortie sur trois périodes | Non indexé ; 2025 et 2026 | CGI 298 bis, II, 5° | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044873402 | texte |
| Manifestations de soutien exonérées | **6** par an | Non indexé | CGI 261-7-1° c | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054374042 | texte |
| Publication des comptes (subventions) | **153 000 €** de subventions par an | Non indexé ; 2025 et 2026 | C. com. L. 612-4 ; D. 612-5 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048539499 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006268871 | texte |
| Comptes annuels et commissaire aux comptes (personne morale non commerçante ayant une activité économique) | 2 critères sur 3 : **50** salariés ; **3 100 000 €** de chiffre d'affaires ou de ressources ; **1 550 000 €** de total de bilan | Non indexé ; 2025 et 2026 | C. com. L. 612-1 ; R. 612-1 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025883370 | texte |
| Vente au déballage | **2 mois** par année civile, même local ou emplacement | Version issue de la loi n° 2026-403 | C. com. L. 310-2 | voir [V-R1](V-R1.md) | texte (dans V-R1) |
| Revenus agricoles d'un organisme non lucratif | Taux de **24 %** sur le revenu net | — | CGI 206-5 ; 219 bis | voir [V-R2](V-R2.md) | texte (dans V-R2) |

**Correction à porter dans [V-R1](V-R1.md) § seuils.** Le tableau y donne **78 596 €** pour 2025. D'après l'actualité BOFiP du 16 avril 2025 relayée par la presse spécialisée, la valeur 2025 est **80 011 €**, comme dans [V-R6](V-R6.md). 78 596 € paraît être la valeur 2024. À confirmer sur la version archivée du BOFiP (BOI-IS-CHAMP-10-50-20-20, version d'avril 2025).

---

## Ce que les cas enseignent sur ce qui peut se vendre, s'échanger ou se troquer

Ces constats de pratique ne valent pas validation juridique. Le droit applicable est dans les fichiers cités.

1. **Vente réservée aux adhérents** (Croqueurs 79, Croqueurs IDF). C'est la forme la plus répandue chez les bénévoles. Elle réduit le « public » au sens des 4 P, sans écarter la vente ([V-R2](V-R2.md)), et pose la question de la cotisation comme contrepartie ([benevolat-et-recolte](../docs/dossiers/benevolat-et-recolte.md)). Aucun contrôle publié.
2. **Vente concentrée sur une ou deux journées par an** (Puyricard). Elle s'adosse aux six manifestations (261-7-1° c), à condition que les statuts le permettent et que la fête soit organisée « à leur profit exclusif ».
3. **Production partagée avec un professionnel** (pépinière de Secondigny). Elle permet de rendre service sans porter la vente, à condition que ce soit **le professionnel qui vende**. La convention n'a pas été vue.
4. **Petites ventes au fil de l'eau** (Montfrin, environ 1 900 € par an). Il n'y a pas de seuil atteint et pas de contrôle connu. La comptabilité les traite comme des ventes ordinaires, ce qui ferme la lecture « don » du prix libre.
5. **Vente en magasin de producteurs ou sur un marché** (Marinie). Dans le corpus, cette forme va toujours avec des salariés. Elle place l'association sur le terrain des contrôles ordinaires du secteur (DDPP-URSSAF sur les marchés). C'est la forme la plus éloignée du modèle cible.
6. **Échange et troc.** Aucun cas documenté de troc organisé par une association agricole bénévole. La pratique observée est le **don de semences** (Pétanielle) et la **bourse aux greffons** entre adhérents. **Non trouvé** pour le troc. La qualification de l'échange est dans [V-R2](V-R2.md) et [V-R3](V-R3.md).

---

## Incertitudes et pistes

1. **Donation de la Marinie** : qui a donné, l'association agricole ou un tiers ? Lire l'acte au service de la publicité foncière (Aveyron, acte du 22/11/2024), ou le demander à Antidote.
2. **Redevance de la Marinie** : nulle, différée ou comprise dans les 3 214 € de loyers de 2025 ? Les comptes ne permettent pas de trancher.
3. **Salariés d'Aux Prés en Bulles en 2023** : nature du contrat (aidé, saisonnier, CDD) et articulation avec le bénévolat. Non publié.
4. **Secondigny** : convention avec le pépiniériste (qui vend ?), montant des ventes de jus, déclaration DDPP. À demander à l'association.
5. **Puyricard** : montant des ventes aux journées portes ouvertes et convention d'occupation avec la ville d'Aix. La convention est communicable par la commune (CRPA L. 311-1, cf. [M2-R6](M2-R6.md) Q1-c).
6. **Montfrin** : nature exacte des « ventes de produits finis » (légumes ? plants ? confitures ?) et motif du dépôt des comptes. Petite association joignable.
7. **Valeur 2025 de la franchise** : 80 011 € d'après l'actualité BOFiP relayée. Contradiction avec V-R1 (78 596 €) à corriger après lecture de la version BOFiP archivée.
8. **Appel du jugement TJ Lyon du 2 avril 2024** : non recherché.
9. **Aucun contrôle publié** sur une association agricole bénévole qui vend un peu. Cette absence n'est pas une preuve de tolérance : les contrôles fiscaux et URSSAF qui n'aboutissent pas à un contentieux ne sont pas publiés.

---

## Sources

**Textes (codes locaux ; liens Légifrance pour contrôle manuel)**
- C. com., L. 612-1 (LEGIARTI000048539508), L. 612-4 (LEGIARTI000048539499), D. 612-5 (LEGIARTI000006268871), R. 612-1 (LEGIARTI000025883370) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048539499
- CGI, art. 261 (LEGIARTI000054374042), art. 298 bis (LEGIARTI000044873402)

**Comptes publiés (JOAFE, dépôt DILA)**
- Montfrin 2025 : https://fr.ftp.opendatasoft.com/datadila/JO/ASSOCIATIONS/DCA/PDF/2025/3112/924978653_31122025.pdf ; 2024 : …/PDF/2024/3112/924978653_31122024.pdf
- Terres nourricières Sud Morvan 2025 : …/PDF/2025/3112/923696702_31122025.pdf
- Potager extraordinaire 2021 : …/PDF/2021/3112/828189837_31122021.pdf
- Potagers du Télégraphe 2021 : …/PDF/2021/3112/498644368_31122021.pdf
- Jardin Soli-Bio 2024 : …/PDF/2024/3112/517432415_31122024.pdf
- Antidote 2023, 2024, 2025 : …/PDF/2025/3112/882625288_31122025.pdf (et 2024, 2023)
- API : https://journal-officiel-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/jo_associations/records

**Décision**
- TJ Lyon, 2 avr. 2024, n° 21/04605 : https://juricaf.org/arret/FRANCE-TRIBUNALJUDICIAIREDELYON-20240402-2104605

**Doctrine administrative**
- BOI-IS-CHAMP-10-50-20-20-20260805 § 1 : https://bofip.impots.gouv.fr/bofip/2659-PGP.html/identifiant=BOI-IS-CHAMP-10-50-20-20-20260805
- DGCCRF, végétaux d'ornement : https://www.economie.gouv.fr/dgccrf/laction-de-la-dgccrf/les-enquetes/vigilance-sur-la-qualite-et-la-loyaute-dans-le-secteur-des

**Pratique documentée**
- Croqueurs 79 : https://croqueurs79.fr/ ; https://croqueurs79.fr/vente-pour-nos-adherents/ ; https://croqueurs79.fr/adhesion/ ; *Caractères* : https://www.caracterres.fr/les-croqueurs-de-pommes-cultivent-les-essences-locales
- Croqueurs PACA : https://croqueursdeprovence.fr/nos-statuts/ ; https://croqueursdeprovence.fr/charte-croqueurs-puyricard/ ; tract 2026 : https://croqueursdeprovence.fr/wp-content/uploads/2026/05/@Flyer-JPO-Croqueurs-de_finitif.pdf
- Croqueurs IDF : https://www.croqueur-idf.fr/se-procurer-greffons-et-porte-greffes/bilans-des-bourses-r%C3%A9centes.html
- Bretoncelles : https://www.bretoncelles-patrimoine-nature.fr/accueil/patrimoine-naturel/bourse-aux-greffons.html
- Antidote, « Nos lieux » : https://aventure-antidote.org/qui-sommes-nous/nos-lieux/
- Les Giroflées : https://www.les-giroflees.fr/producteurs/aux-pres-en-bulles/
- SIRENE (Annuaire des entreprises) : https://annuaire-entreprises.data.gouv.fr/entreprise/877643379 ; 107690703 ; 501391502 ; 433481124 ; 795050053
- Pétanielle : https://www.petanielle.org/actions/redeploiement-des-semences/
- Jardins du Largue : https://www.les-jardins-du-largue.org/boutique/
- Réseau Semences Paysannes : https://www.semencespaysannes.org/semons-nos-droits/questions-frequentes.html
- AFAUP : https://www.afaup.org/helpie_faq/est-ce-quune-association-peut-vendre-ses-legumes-pour-sautofinancer-la-vente-est-elle-reservee-uniquement-a-ses-adherents/
- Contrôle DDPP-URSSAF Morbihan (presse) : https://info.fr/vannes-controle-conjoint-ddpp-urssaf-marche-fruits-legumes-travail-dissimule/
- Franchise 2025 (presse relayant le BOFiP) : https://www.weblex.fr/weblex-actualite/associations-nouveau-seuil-de-franchise-des-impots-commerciaux-pour-2025
