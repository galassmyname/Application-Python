# Partie 1 : Types de base, variables, Entrées et sorties
# Saisie des métadonnées
nom = input("Nom du dataset : ")
domaine = input("Domaine : ")

nb_lignes = int(input("Nombre de lignes : "))
nb_colonnes = int(input("Nombre de colonnes : "))
taille = float(input("Taille (en Mo) : "))

# Vérification du format
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

# Affichage du résumé
print("\n RÉSUMÉ DU DATASET ")
print(f"Nom                 : {nom}")
print(f"Domaine             : {domaine}")
print(f"Nombre de lignes    : {nb_lignes}")
print(f"Nombre de colonnes  : {nb_colonnes}")
print(f"Taille              : {taille} Mo")
print(f"Format              : {format_fichier}")
print(f"Public              : {public}")