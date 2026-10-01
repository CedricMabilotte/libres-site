# Leçons — libres

- 2026-09-30 : un critère strict produit un corpus presque vide ; publier les épreuves avec la porte bloquante transforme ce vide en résultat. Toujours accompagner d'une analyse de sensibilité (demande du contradicteur).
- 2026-09-30 : le Maitron se lit avec curl, pas avec WebFetch.
- 2026-09-30 : garde-fou provenance : « Claude » matche « Saint-Claude » → motif `(?<!Saint-)\bClaude\b`.
- 2026-09-30 : le transfert de fichiers device→cloud (stage) a échoué toute la session ; tout le travail s'est fait sur la machine de Ced (python, playwright, gh présents).
- 2026-09-30 : un commit a poussé une fiche YAML invalide (« : » dans un scalaire non quoté) → CI en échec. Hook pre-commit local ajouté (générateur obligatoire) ; éditer les fiches par yaml.safe_load/dump plutôt que par remplacement de texte.
- 2026-10-01 : les numéros d'arrêts du blog kohenavocats.fr sont faux ou sans rapport : ne jamais citer une décision sans l'avoir vue sur Judilibre/Juricaf.
- 2026-10-01 : collèges successifs (recherche parallèle → lecture critique par les voix → comblement ciblé → vérification) : la lecture critique a trouvé les erreurs que la recherche ne voyait pas (jardins familiaux = parcelles individuelles ; partage de la récolte = avantage en nature ; société créée de fait).
- 2026-10-01 : liens .md entre dossiers convertis en ../slug/ par le générateur ; tableaux et URL longues : overflow-wrap:anywhere sur mobile.
- 2026-10-01 : Paged.js 0.4 n'applique pas une taille de page nommée différente (@page matrice { size: A4 landscape }) : toutes les pages restent au format du premier @page. Matrice gardée en portrait.
- 2026-10-01 : la version imprimable vit un niveau plus bas que le dossier : ses liens relatifs sont réécrits en URL absolues (utile aussi dans le PDF).
- 2026-10-01 : un texte juridique écrit comme « montage qui évite les qualifications » fournit à l'adversaire l'élément intentionnel ; écrire la qualification revendiquée et les pièces remises sur demande.
- 2026-10-01 : Paged.js (target-counter, querySelector) plante sur les id qui commencent par un chiffre (ids « 1-… » de l'extension toc) : préfixer les id et les href internes dans la version imprimée.
- 2026-10-01 : un <details> fermé reste fermé à l'impression ; le convertir en <div> et retirer <summary> dans la version imprimée.
- 2026-10-01 : overflow-wrap:anywhere sur les cellules casse les nombres (« 20/30 ») ; le réserver aux liens.
- 2026-10-01 : un workflow en arrière-plan survit à une reprise de session ; vérifier son état avant de le croire mort (journal.jsonl), puis TaskStop avant resume.
