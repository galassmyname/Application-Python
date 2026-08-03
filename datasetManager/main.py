from interface.menu import afficher_menu
from datasets.gestion import (
    ajouter_dataset,
    afficher_datasets,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    supprimer_dataset,
    datasets,
)
from datasets.statistiques import statistiques
from stockage.csv_manager import sauvegarder_csv, charger_csv
from stockage.json_manager import sauvegarder_json, charger_json


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
            sauvegarder_csv(datasets)
        elif choix == "10":
            resultat = charger_csv()
            if resultat is not None:
                datasets.clear()
                datasets.extend(resultat)
        elif choix == "11":
            sauvegarder_json(datasets)
        elif choix == "12":
            resultat = charger_json()
            if resultat is not None:
                datasets.clear()
                datasets.extend(resultat)
        else:
            print("Choix invalide. Veuillez choisir entre 1 et 12.")


if __name__ == "__main__":
    main()
