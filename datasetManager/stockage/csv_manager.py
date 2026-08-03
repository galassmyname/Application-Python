# stockage/csv_manager.py


def sauvegarder_csv(datasets, chemin="data/datasets.csv"):
    if len(datasets) == 0:
        print("\nAucun dataset à sauvegarder.\n")
        return

    fichier = open(chemin, "w", encoding="utf-8")
    fichier.write("nom,domaine,lignes,colonnes,taille,format,public\n")
    for d in datasets:
        ligne = f"{d['nom']},{d['domaine']},{d['lignes']},{d['colonnes']},{d['taille']},{d['format']},{d['public']}\n"
        fichier.write(ligne)
    fichier.close()
    print(f"\n{len(datasets)} dataset(s) sauvegardé(s) dans {chemin}\n")


def charger_csv(chemin="data/datasets.csv"):
    try:
        fichier = open(chemin, "r", encoding="utf-8")
        lignes_fichier = fichier.readlines()
        fichier.close()

        if len(lignes_fichier) <= 1:
            print("\nErreur : le fichier CSV est vide.\n")
            return None

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

        print(f"\n{len(nouveaux_datasets)} dataset(s) rechargé(s) depuis {chemin}\n")
        return nouveaux_datasets

    except FileNotFoundError:
        print(f"\nErreur : le fichier {chemin} n'existe pas. Sauvegardez d'abord.\n")
        return None
