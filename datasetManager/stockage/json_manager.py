# stockage/json_manager.py

import json


def sauvegarder_json(datasets, chemin="data/datasets.json"):
    if len(datasets) == 0:
        print("\nAucun dataset à sauvegarder.\n")
        return

    fichier = open(chemin, "w", encoding="utf-8")
    json.dump(datasets, fichier, indent=4, ensure_ascii=False)
    fichier.close()
    print(f"\n{len(datasets)} dataset(s) sauvegardé(s) dans {chemin}\n")


def charger_json(chemin="data/datasets.json"):
    try:
        fichier = open(chemin, "r", encoding="utf-8")
        nouveaux_datasets = json.load(fichier)
        fichier.close()

        if len(nouveaux_datasets) == 0:
            print("\nErreur : le fichier JSON est vide.\n")
            return None

        print(f"\n{len(nouveaux_datasets)} dataset(s) rechargé(s) depuis {chemin}\n")
        return nouveaux_datasets

    except FileNotFoundError:
        print(f"\nErreur : le fichier {chemin} n'existe pas. Sauvegardez d'abord.\n")
        return None
