# Partie 2 : Structures de contrôle
domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")
datasets = []
while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("5. Trier")
    print("6. Modifier")
    print("7. Supprimer")
    print("==================")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom du dataset : ")
        domaine = input("Domaine : ")

        if domaine not in domaines_autorises:
            print(f"Domaine invalide. Domaines autorisés : {domaines_autorises}\n")

        else:
            lignes = int(input("Nombre de lignes : "))
            colonnes = int(input("Nombre de colonnes : "))
            taille = float(input("Taille en Mo : "))
            while True:
                format_fichier = input("Format (csv ou json) : ").lower()
                if format_fichier == "csv" or format_fichier == "json":
                    break
                else:
                    print("Erreur : le format doit être csv ou json.")

            # Vérification de public
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

    elif choix == "2":
        if len(datasets) == 0:
            print("\nAucun dataset enregistré pour le moment.\n")
        else:
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

    elif choix == "3":
        if len(datasets) == 0:
            print("\nAucun dataset enregistré pour le moment.\n")
        else:
            nom_recherche = input("Nom du dataset à rechercher : ")
            trouve = False
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
                    trouve = True
                    break

            if not trouve:
                print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")

    elif choix == "4":
        print("Vous avez quitté le programme !")
        break
    elif choix == "5":
        if len(datasets) == 0:
            print("\nAucun dataset enregistré pour le moment.\n")
        else:
            datasets_tries = sorted(datasets, key=lambda d: d["lignes"])
            print(
                f"\n=== Datasets triés par nombre de lignes ({len(datasets_tries)}) ==="
            )
            for i, d in enumerate(datasets_tries, start=1):
                print(f"{i}. {d['nom']} — {d['lignes']} lignes")
            print("==========================\n")
    elif choix == "6":
        if len(datasets) == 0:
            print("\nAucun dataset enregistré pour le moment.\n")
        else:
            nom_recherche = input("Nom du dataset à modifier : ")
            trouve = False
            for d in datasets:
                if d["nom"].lower() == nom_recherche.lower():
                    trouve = True
                    print(
                        f"\nDataset '{d['nom']}' trouvé. Laissez vide pour ne pas changer."
                    )

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
                    break

            if not trouve:
                print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")
    elif choix == "7":
        if len(datasets) == 0:
            print("\nAucun dataset enregistré pour le moment.\n")
        else:
            nom_recherche = input("Nom du dataset à supprimer : ")
            trouve = False
            for d in datasets:
                if d["nom"].lower() == nom_recherche.lower():
                    datasets.remove(d)
                    print(f"\nDataset '{d['nom']}' supprimé avec succès.\n")
                    trouve = True
                    break

            if not trouve:
                print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")
    else:
        print("Choix invalide. Veuillez choisir entre 1 et 7.")
