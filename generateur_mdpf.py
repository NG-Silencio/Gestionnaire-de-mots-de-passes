# Cette partie du programme couvre la création du mot de passe fort dans l'application PassWD

# On importe le module "random" pour mélanger au hasard les différents caractéres

import random

# On crée une fonction de générateur de mot de passe fort

def gen_mdpf():

# On déclare nos différents variables pour les caractéres de la création du mot de passe

        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMBER = "0123456789"
        symbol = "*_[]{}#()"
        ensemble = lower + upper + NUMBER + symbol

# Minimun de caractéres = 8 alors on laisse l'utilisateur choisir mais sans dépasser 15
        length = int(input('\n' "Choisir la taille de votre mot de passe entre 8 et 15 : "))
        while length < 8 or length > 15 : 
                length = int(input("Choisir la taille de votre mot de passe entre 8 et 15 : "))

        print ("\n","Taille choisie :",length)
        password = "".join(random.sample(ensemble,length))        
        
# Sortie du code
        print ("\n","Le mot de passe généré est : " ,password , "\n")
