# main.py

from menu import afficher_menu
from gestion import (
    ajouter_dataset,
    afficher_datasets,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    supprimer_dataset,
    sauvegarder,
    recharger,
)
from statistiques import statistiques


def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_dataset()
        elif choix == "2":
            afficher_datasets()
        elif choix == "3":
            rechercher_dataset()
        elif choix == "4":
            print("Vous avez quitté le programme !")
            break
        elif choix == "5":
            trier_dataset()
        elif choix == "6":
            modifier_dataset()
        elif choix == "7":
            supprimer_dataset()
        elif choix == "8":
            statistiques()
        elif choix == "9":
            sauvegarder()
        elif choix == "10":
            recharger()
        else:
            print("Choix invalide. Veuillez choisir entre 1 et 10.")


if __name__ == "__main__":
    main()
