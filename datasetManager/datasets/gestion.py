# datasets/gestion.py

from interface.affichage import afficher_resume_dataset, afficher_liste_datasets

domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")
datasets = []

datasets.append(
    {
        "nom": "Titanic",
        "domaine": "Transport",
        "lignes": 891,
        "colonnes": 12,
        "taille": 48.0,
        "format": "CSV",
        "public": True,
    }
)
datasets.append(
    {
        "nom": "COVID-Cases",
        "domaine": "Santé",
        "lignes": 500000,
        "colonnes": 8,
        "taille": 120.5,
        "format": "JSON",
        "public": True,
    }
)


def ajouter_dataset():
    nom = input("Nom du dataset : ")
    domaine = input("Domaine : ")
    if domaine not in domaines_autorises:
        print(f"Domaine invalide. Domaines autorisés : {domaines_autorises}\n")
        return

    try:
        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        taille = float(input("Taille en Mo : "))
    except ValueError:
        print(
            "\nErreur : veuillez saisir un nombre valide pour lignes/colonnes/taille.\n"
        )
        return

    while True:
        format_fichier = input("Format (csv ou json) : ").lower()
        if format_fichier == "csv" or format_fichier == "json":
            break
        else:
            print("Erreur : le format doit être csv ou json.")

    while True:
        public_input = input("Public (true ou false) : ").lower()
        if public_input == "true":
            public = True
            break
        elif public_input == "false":
            public = False
            break
        else:
            print("Erreur : veuillez saisir true ou false.")

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "lignes": lignes,
        "colonnes": colonnes,
        "taille": taille,
        "format": format_fichier.upper(),
        "public": public,
    }
    datasets.append(dataset)
    afficher_resume_dataset(dataset)


def afficher_datasets():
    afficher_liste_datasets(datasets)


def rechercher_dataset():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    nom_recherche = input("Nom du dataset à rechercher : ")
    for d in datasets:
        if d["nom"].lower() == nom_recherche.lower():
            print("\n=== Dataset trouvé ===")
            afficher_resume_dataset(d)
            return

    print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")


def trier_dataset():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    datasets_tries = sorted(datasets, key=lambda d: d["lignes"])
    print(f"\n=== Datasets triés par nombre de lignes ({len(datasets_tries)}) ===")
    for i, d in enumerate(datasets_tries, start=1):
        print(f"{i}. {d['nom']} — {d['lignes']} lignes")
    print("==========================\n")


def modifier_dataset():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    nom_recherche = input("Nom du dataset à modifier : ")
    for d in datasets:
        if d["nom"].lower() == nom_recherche.lower():
            print(f"\nDataset '{d['nom']}' trouvé. Laissez vide pour ne pas changer.")

            nouveau_domaine = input(f"Domaine ({d['domaine']}) : ")
            if nouveau_domaine != "":
                if nouveau_domaine not in domaines_autorises:
                    print(f"Domaine invalide, conservé : {d['domaine']}")
                else:
                    d["domaine"] = nouveau_domaine

            nouvelles_lignes = input(f"Lignes ({d['lignes']}) : ")
            if nouvelles_lignes != "":
                d["lignes"] = int(nouvelles_lignes)

            nouvelles_colonnes = input(f"Colonnes ({d['colonnes']}) : ")
            if nouvelles_colonnes != "":
                d["colonnes"] = int(nouvelles_colonnes)

            nouvelle_taille = input(f"Taille ({d['taille']} Mo) : ")
            if nouvelle_taille != "":
                d["taille"] = float(nouvelle_taille)

            print(f"\nDataset '{d['nom']}' mis à jour avec succès.\n")
            return

    print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")


def supprimer_dataset():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    nom_recherche = input("Nom du dataset à supprimer : ")
    for d in datasets:
        if d["nom"].lower() == nom_recherche.lower():
            datasets.remove(d)
            print(f"\nDataset '{d['nom']}' supprimé avec succès.\n")
            return

    print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")
