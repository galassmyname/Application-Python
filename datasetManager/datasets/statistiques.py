# statistiques.py

from datasets.gestion import datasets, domaines_autorises


def statistiques():
    if len(datasets) == 0:
        print("\nAucun dataset enregistré pour le moment.\n")
        return

    nb_datasets = len(datasets)
    total_lignes = sum(d["lignes"] for d in datasets)
    moyenne_colonnes = sum(d["colonnes"] for d in datasets) / nb_datasets
    nb_publics = len([d for d in datasets if d["public"]])
    nb_prives = len([d for d in datasets if not d["public"]])
    nb_csv = len([d for d in datasets if d["format"] == "CSV"])
    nb_json = len([d for d in datasets if d["format"] == "JSON"])

    repartition_domaines = {
        domaine: len([d for d in datasets if d["domaine"] == domaine])
        for domaine in domaines_autorises
        if any(d["domaine"] == domaine for d in datasets)
    }

    print("\n=== Statistiques ===")
    print(f"Nombre de datasets       : {nb_datasets}")
    print(f"Nombre total de lignes   : {total_lignes}")
    print(f"Nombre moyen de colonnes : {moyenne_colonnes:.0f}")
    print(f"Datasets publics         : {nb_publics}")
    print(f"Datasets privés          : {nb_prives}")
    print(f"Format CSV               : {nb_csv}")
    print(f"Format JSON              : {nb_json}")
    print("Répartition par domaine :")
    for domaine, nb in repartition_domaines.items():
        print(f"  {domaine} : {nb}")
    print("==========================\n")
