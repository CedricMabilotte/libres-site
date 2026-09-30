"""Référentiel du cadre libres (docs/cadre.md) — source unique des clés et libellés."""
import datetime as dt
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
FICHES = ROOT / "data" / "fiches"
REGARDS = ROOT / "data" / "regards"
ANNEE = dt.date.today().year

PORTES = [
    ("forme_civile", "P1", "Forme civile", "Toute la chaîne est de droit civil non lucratif."),
    ("foncier_verrouille", "P2", "Foncier verrouillé", "Le foncier est sorti du marché de façon opposable."),
    ("usage_ig", "P3", "Usage d'intérêt général", "Usage non marchand, ouvert au-delà du cercle restreint."),
    ("autogestion", "P4", "Autogestion", "Les usagers décident eux-mêmes."),
    ("etabli", "P5", "Établi", "Au moins dix ans d'usage continu sur le lieu."),
]
PKEYS = [p[0] for p in PORTES]
PVAL = {"oui": "Franchie", "partiel": "Partielle", "non": "Non franchie", "inconnu": "Non établie"}

FAMILLES = {
    "communaute_intentionnelle": "Communauté intentionnelle",
    "commun_foncier": "Commun foncier",
    "occupation_regularisee": "Occupation régularisée",
    "lieu_non_marchand": "Lieu non marchand",
}
PERIODES = [(1789, 1870, "1789-1870"), (1871, 1914, "1871-1914"), (1915, 1945, "1915-1945"),
            (1946, 1967, "1946-1967"), (1968, 1989, "1968-1989"), (1990, 2007, "1990-2007"), (2008, 9999, "2008-")]

DIM = {  # clé : (libellé, multi, {valeur: libellé})
    "acces": ("Accès au lieu", False, {"don_legs": "Don ou legs", "souscription": "Souscription", "achat_collectif": "Achat collectif",
              "occupation": "Occupation", "bail_public": "Bail public", "achat_prive_fondateur": "Achat privé du fondateur", "heritage": "Héritage"}),
    "titre": ("Titre d'usage", False, {"propriete": "Propriété", "bail_emphyteotique": "Bail emphytéotique", "commodat": "Commodat",
              "convention": "Convention", "bail_rural": "Bail rural", "usufruit": "Usufruit", "domanialite": "Domanialité", "sans_titre": "Sans titre"}),
    "verrou": ("Verrou", True, {"inalienabilite_statutaire": "Inaliénabilité statutaire", "domanialite_publique": "Domanialité publique",
               "veto_reseau": "Veto de réseau", "devolution_desinteressee": "Dévolution désintéressée", "bail_long": "Bail long", "aucun": "Aucun"}),
    "gouvernance": ("Gouvernance", False, {"assemblee_consensus": "Assemblée au consensus", "assemblee_majoritaire": "Assemblée majoritaire",
                    "conseil_delegue": "Conseil délégué", "fondateur": "Fondateur", "mixte": "Mixte"}),
    "economie": ("Économie des personnes", False, {"caisse_commune": "Caisse commune", "autosubsistance": "Autosubsistance",
                 "activites_non_marchandes": "Activités non marchandes", "activites_marchandes_annexes": "Activités marchandes annexes",
                 "revenus_individuels_externes": "Revenus individuels externes", "salariat_structure": "Salariat de la structure"}),
    "ouverture": ("Ouverture", False, {"ouvert_public": "Ouvert au public", "accueil_regulier": "Accueil régulier", "cercle_restreint": "Cercle restreint"}),
    "finalite": ("Finalités", True, {"agriculture": "Agriculture", "habitat": "Habitat", "education_populaire": "Éducation populaire", "culture": "Culture",
                 "accueil_soin": "Accueil, soin", "spiritualite": "Spiritualité", "lutte_territoriale": "Lutte territoriale",
                 "milieu_vivant": "Milieu vivant", "artisanat_production": "Artisanat, production", "consommation": "Consommation"}),
    "filiation": ("Filiation", True, {"socialisme_utopique": "Socialisme utopique", "anarchisme": "Anarchisme", "mouvement_ouvrier": "Mouvement ouvrier",
                  "christianisme_communautaire": "Christianisme communautaire", "non_violence": "Non-violence", "neo_ruralisme": "Néo-ruralisme",
                  "ecologie_politique": "Écologie politique", "autonomie": "Autonomie", "education_populaire": "Éducation populaire", "personnalisme": "Personnalisme"}),
    "rapport_etat": ("Rapport à l'État", False, {"conflit": "Conflit", "regularisation": "Régularisation", "conventionnement": "Conventionnement", "indifference": "Indifférence"}),
    "echelle": ("Échelle", False, {"moins_10": "Moins de 10", "10_50": "10 à 50", "50_200": "50 à 200", "plus_200": "Plus de 200"}),
    "transmission": ("Transmission", False, {"generations_renouvelees": "Générations renouvelées", "fondateurs_seuls": "Fondateurs seuls", "en_cours": "En cours"}),
    "etat": ("État", False, {"actif": "Actif", "disparu": "Disparu", "transforme": "Transformé"}),
    "fin": ("Mode de fin", False, {"succession_ratee": "Succession ratée", "faillite": "Faillite", "scission": "Scission", "captation": "Captation",
            "dissolution_volontaire": "Dissolution volontaire", "expropriation": "Expropriation", "expulsion": "Expulsion", "vente": "Vente"}),
}
FORMES = {"association": "Association", "collectif_de_fait": "Collectif de fait", "fonds_dotation": "Fonds de dotation", "fondation": "Fondation",
          "personne_publique": "Personne publique", "societe_civile_parts_cessibles": "Société civile à parts cessibles", "societe_civile": "Société civile",
          "societe_commerciale": "Société commerciale", "cooperative": "Coopérative", "personne_privee": "Personne privée",
          "congregation": "Congrégation", "aucune": "Aucune", "inconnu": "Non établie", None: "Non établie"}
STATUTS = {
    "corpus": ("Corpus", "Franchit les cinq portes."),
    "corpus_sous_condition": ("Corpus sous condition", "Franchit les cinq portes grâce à un verrou par titre (bail consenti par le propriétaire), dont l'opposabilité ou la tenue reste à confirmer."),
    "seuil": ("Au seuil", "Une seule porte manque."),
    "epreuve": ("Épreuve", "Instruit et publié ; au moins deux portes manquent."),
}
DISTANCE_LIB = {0: "0 porte manquante", 1: "1 porte manquante", 2: "2 portes", 3: "3 portes", 4: "4 portes", 5: "5 portes"}


def periode(debut):
    if not isinstance(debut, int):
        return None
    for a, b, lib in PERIODES:
        if a <= debut <= b:
            return lib
    return None


def charger():
    fiches = []
    for f in sorted(FICHES.glob("*.yml")):
        d = yaml.safe_load(f.read_text(encoding="utf-8"))
        d["_fichier"] = f.name
        fiches.append(d)
    regards = {f.stem: yaml.safe_load(f.read_text(encoding="utf-8")) for f in sorted(REGARDS.glob("*.yml"))}
    return fiches, regards


def val(d, k):
    v = ((d.get("dimensions") or {}).get(k) or {}).get("valeur")
    if v in (None, "inconnu", [], ["inconnu"]):
        return None
    return v


def verrou_type(d):
    """par_propriete / par_titre / aucun — distinction demandée par l'épreuve contradicteur."""
    v = val(d, "verrou") or []
    if any(x in v for x in ("inalienabilite_statutaire", "domanialite_publique", "devolution_desinteressee", "veto_reseau")):
        return "par_propriete"
    if "bail_long" in v or val(d, "titre") == "bail_emphyteotique":
        return "par_titre"
    return "aucun"


def calcul(d, variante=None):
    """Statut calculé, jamais saisi. `variante` sert à l'analyse de sensibilité."""
    p = {k: ((d.get("portes") or {}).get(k) or {}).get("valeur", "inconnu") for k in PKEYS}
    if variante == "p1_souple" and p["forme_civile"] == "partiel":
        p["forme_civile"] = "oui"
    if variante == "p2_titre_annonce" and p["foncier_verrouille"] == "partiel":
        p["foncier_verrouille"] = "oui"
    if variante == "p5_cinq_ans":
        deb, fin = d.get("debut"), d.get("fin")
        if isinstance(deb, int):
            p["etabli"] = "oui" if ((fin or ANNEE) - deb) >= 5 else "non"
    if variante == "partiel_vaut_oui":
        p = {k: ("oui" if v == "partiel" else v) for k, v in p.items()}
    manque = [k for k in PKEYS if p[k] != "oui"]
    if not manque:
        st = "corpus_sous_condition" if verrou_type(d) == "par_titre" else "corpus"
    elif len(manque) == 1:
        st = "seuil"
    else:
        st = "epreuve"
    return st, manque, p
