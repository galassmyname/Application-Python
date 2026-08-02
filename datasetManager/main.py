# Partie 2 : Structures de contrôle
domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")
while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
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
        print("Affichage des datasets.")

    elif choix == "3":
        print("Recherche d'un dataset.")

    elif choix == "4":
        print("Vous avez quitté le programme !")
        break
    else:
        print("Choix invalide. Veuillez choisir entre 1 et 4.")
