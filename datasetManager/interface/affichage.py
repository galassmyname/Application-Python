# interface/affichage.py


def afficher_resume_dataset(d):
    print("\n=== Résumé du dataset ===")
    print(f"Nom       : {d['nom']}")
    print(f"Domaine   : {d['domaine']}")
    print(f"Lignes    : {d['lignes']}")
    print(f"Colonnes  : {d['colonnes']}")
    print(f"Taille    : {d['taille']} Mo")
    print(f"Format    : {d['format']}")
    print(f"Public    : {'Oui' if d['public'] else 'Non'}")
    print("==========================\n")


def afficher_liste_datasets(datasets):
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    print(f"\n=== Liste des datasets ({len(datasets)}) ===")
    for i, d in enumerate(datasets, start=1):
        print(f"\n--- Dataset {i} ---")
        afficher_resume_dataset(d)
