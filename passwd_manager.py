#Cette partie du programme permet à l'utilisateur d'avoir à disposition un gestionnaire de mots de passes

# On installe et on importe le module "cryptography"pour encrypter et décrypter les mots de passes
# On l'installe avec la commande suivante en ligne de commande : "pip install cryptography"

from cryptography.fernet import Fernet

# On définit une fonction pour le programme à suivre
def pwd ():

# Cette fonction est faite pour créer la clé de cryptage (On l'utilise juste une fois  pour créer la clé
# puis on commente l'expression (ligne 13 à 18)). "wb" signifie écrire en binaire

    '''
    def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    write_key() '''

# Cette fonction permet de charger la clé depuis le fichier key.key.

    def load_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key


    key = load_key()
    fer = Fernet(key)

# Cette fonction permet de consulter les mots de passes enregistrés dans notre gestionnaire
# De base, les mots de passes sont encryptés mais en les consultant
# On peut utiliser les méthodes decrypt et decode pour décrypter la clé et transmettre le mot de passe

    def consulter():
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("Utilisateur : ", user, "| Mot de passe : ",fer.decrypt(passw.encode()).decode())

# Cette fonction permet d'ajouter un mot de passe au gestionnaire.
# Cette fois, au lieu d'utiliser la méthode read, on utilise la méthode write puisqu'on veut ajouter des entrées au fichier "passwords.txt" qui sert de stockage.
# L'argument 'a' signifie append, il sert à ajouter les nouvelles lignes à la fin du fichier.

    def ajouter():
        name = input("Nom du compte : ")
        pwd = input("Mot de passe : ")

        with open('passwords.txt', 'a') as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Un menu simple et accessible pour l'utilisateur.
# On ajoute des boucles "if" pour les différents choix des utilisateurs.
# Ainsi, l'utilisateur peut choisir entre consulter la liste, ajouter un nouveau mot de passe ou quitter le programme.

    while True:
        print ("\n", "***** Bienvenue dans le gestionnaire de mots de passes *****")
        mode = input("""
                      1: Consulter
                      2: Ajouter
                      3: Quitter

                      Merci de choisir une option : """).lower()

        if mode == "3" or mode == "quitter":
            break
        if mode == "1" or mode == "consulter":
            consulter()
        elif mode == "2" or mode == "ajouter":
            ajouter()
        else:
            print("Invalide. Choisissez entre les options 1 à 3")
            continue