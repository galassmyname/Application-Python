# gestion.py

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
datasets.append(
    {
        "nom": "Stock-Prices",
        "domaine": "Finance",
        "lignes": 2000000,
        "colonnes": 15,
        "taille": 300.0,
        "format": "CSV",
        "public": False,
    }
)
datasets.append(
    {
        "nom": "Crop-Yields",
        "domaine": "Agriculture",
        "lignes": 15000,
        "colonnes": 20,
        "taille": 25.0,
        "format": "CSV",
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

    print("\n=== Résumé du dataset ===")
    print(f"Nom       : {dataset['nom']}")
    print(f"Domaine   : {dataset['domaine']}")
    print(f"Lignes    : {dataset['lignes']}")
    print(f"Colonnes  : {dataset['colonnes']}")
    print(f"Taille    : {dataset['taille']} Mo")
    print(f"Format    : {dataset['format']}")
    print(f"Public    : {'Oui' if dataset['public'] else 'Non'}")
    print("==========================\n")


def afficher_datasets():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    print(f"\n=== Liste des datasets ({len(datasets)}) ===")
    for i, d in enumerate(datasets, start=1):
        print(f"\n--- Dataset {i} ---")
        print(f"Nom       : {d['nom']}")
        print(f"Domaine   : {d['domaine']}")
        print(f"Lignes    : {d['lignes']}")
        print(f"Colonnes  : {d['colonnes']}")
        print(f"Taille    : {d['taille']} Mo")
        print(f"Format    : {d['format']}")
        print(f"Public    : {'Oui' if d['public'] else 'Non'}")
    print("==========================\n")


def rechercher_dataset():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    nom_recherche = input("Nom du dataset à rechercher : ")
    for d in datasets:
        if d["nom"].lower() == nom_recherche.lower():
            print(f"\n=== Dataset trouvé ===")
            print(f"Nom       : {d['nom']}")
            print(f"Domaine   : {d['domaine']}")
            print(f"Lignes    : {d['lignes']}")
            print(f"Colonnes  : {d['colonnes']}")
            print(f"Taille    : {d['taille']} Mo")
            print(f"Format    : {d['format']}")
            print(f"Public    : {'Oui' if d['public'] else 'Non'}")
            print("==========================\n")
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


def sauvegarder():
    if len(datasets) == 0:
        print("\nAucun dataset à sauvegarder.\n")
        return

    fichier = open("datasets.csv", "w", encoding="utf-8")
    fichier.write("nom,domaine,lignes,colonnes,taille,format,public\n")
    for d in datasets:
        ligne = f"{d['nom']},{d['domaine']},{d['lignes']},{d['colonnes']},{d['taille']},{d['format']},{d['public']}\n"
        fichier.write(ligne)
    fichier.close()
    print(f"\n{len(datasets)} dataset(s) sauvegardé(s) dans datasets.csv\n")


def recharger():
    global datasets
    try:
        fichier = open("datasets.csv", "r", encoding="utf-8")
        lignes_fichier = fichier.readlines()
        fichier.close()

        if len(lignes_fichier) <= 1:
            print("\nErreur : le fichier datasets.csv est vide.\n")
            return

        nouveaux_datasets = []
        for ligne in lignes_fichier[1:]:
            valeurs = ligne.strip().split(",")
            dataset = {
                "nom": valeurs[0],
                "domaine": valeurs[1],
                "lignes": int(valeurs[2]),
                "colonnes": int(valeurs[3]),
                "taille": float(valeurs[4]),
                "format": valeurs[5],
                "public": valeurs[6] == "True",
            }
            nouveaux_datasets.append(dataset)

        datasets = nouveaux_datasets
        print(f"\n{len(datasets)} dataset(s) rechargé(s) depuis datasets.csv\n")

    except FileNotFoundError:
        print(
            "\nErreur : le fichier datasets.csv n'existe pas. Sauvegardez d'abord (option 9).\n"
        )
