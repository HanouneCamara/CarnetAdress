import pandas as pd

csv_filename = "donnees_utilisateur.csv"

def saisir_donnees():
    # Demander à l'utilisateur de saisir les données
    name_input = input("Entrez le nom (séparé par des virgules si plusieurs noms) : ")
    lastName_input = input("Entrez le prenom (séparé par des virgules si plusieurs prénoms) : ")
    adress_input = input("Entrez l'adresse (séparé par des virgules si plusieurs adresses) : ")
    number_input = input("Entrez le numéro de téléphone (séparé par des virgules si plusieurs numéros) : ")

    # Convertir les entrées en listes
    names = [name.strip() for name in name_input.split(',')]
    lastNames = [lastNames.strip() for lastNames in lastName_input.split(',')]
    adress = [adress.strip() for adress in adress_input.split(',')]
    num = [num.strip() for num in number_input.split(',')]

    # Créer le DataFrame
    df = pd.DataFrame({"Names": names,"Last Name": lastNames, "Adresses": adress, "Number phone": num})

    # Ajouter les nouvelles données au fichier CSV existant
    try:
        existing_df = pd.read_csv(csv_filename)
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass  # Le fichier n'existe pas encore, il sera créé lors de la sauvegarde ci-dessous

    # Stocker les données dans le fichier CSV
    df.to_csv(csv_filename, index=False)

    print(f"Les données ont été enregistrées dans le fichier CSV : {csv_filename}")

def afficher_donnees():
    try:
        # Afficher les données depuis le fichier CSV
        df_from_csv = pd.read_csv(csv_filename)
        print("\nAffichage des données depuis le fichier CSV :")
        print(df_from_csv)
    except FileNotFoundError:
        print(f"Le fichier CSV '{csv_filename}' ne contient aucune donnée.")

# Exécuter la fonction pour saisir les données
saisir_donnees()

# Exécuter la fonction pour afficher les données
afficher_donnees()
