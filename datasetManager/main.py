# Partie 2 : Structures de contrôle
while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("==================")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Ajout d'un dataset.")

    elif choix == "2":
        print("Affichage des datasets.")

    elif choix == "3":
        print("Recherche d'un dataset.")

    elif choix == "4":
        print("Vous avez quitté le programme !")
        break

    else:
        print("Choix invalide. Veuillez choisir entre 1 et 4.")