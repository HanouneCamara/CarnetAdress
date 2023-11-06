contacts = {}

def Ajouter_contact():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    adresse = input("Adresse : ")
    numero_tel = input("Numéro de téléphone : ")
    contacts[nom] = {
        'prenom': prenom,
        'adresse': adresse,
        'numero_tel': numero_tel
    }
    print('Contact ajouté!')
    
def Afficher_contact():
    for nom, infos in contacts.items():
        print(f"Nom :  {nom}")
        print(f"Prénom : {infos['prenom']}")
        print(f"Adresse : {infos['adresse']}")
        print(f"Numéro de téléphone : {infos['numero_tel']}")
        
Ajouter_contact()
print("Liste des contacts : ")
Afficher_contact()