# Leçons — libres

- 2026-09-30 : un critère strict produit un corpus presque vide ; publier les épreuves avec la porte bloquante transforme ce vide en résultat. Toujours accompagner d'une analyse de sensibilité (demande du contradicteur).
- 2026-09-30 : le Maitron se lit avec curl, pas avec WebFetch.
- 2026-09-30 : garde-fou provenance : « Claude » matche « Saint-Claude » → motif `(?<!Saint-)\bClaude\b`.
- 2026-09-30 : le transfert de fichiers device→cloud (stage) a échoué toute la session ; tout le travail s'est fait sur la machine de Ced (python, playwright, gh présents).
- 2026-09-30 : un commit a poussé une fiche YAML invalide (« : » dans un scalaire non quoté) → CI en échec. Hook pre-commit local ajouté (générateur obligatoire) ; éditer les fiches par yaml.safe_load/dump plutôt que par remplacement de texte.
