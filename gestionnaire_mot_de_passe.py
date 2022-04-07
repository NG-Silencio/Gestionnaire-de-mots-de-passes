from generateur_mdpf import gen_mdpf
from passwd_manager import pwd


def main():
   menu()

def menu():
   print("*******  Bienvenue sur l'application PassWD  *******")
   print()

   choice = input("""
                      1: Créer un mot de passe fort
                      2: Gestionnaire de mot de passe
                      3: Quitter

                      Merci de choisir une option : """)
   if choice == "1" :
      gen_mdpf()
      menu()
   elif choice == "2":
      pwd()
      menu()
   elif choice == "3":
      print ("\n", "***** Merci d'avoir utilisé notre application! A Bientôt ^^ *****", "\n")
      quit()
         
   else :
      print (" Veuillez réssayer ! Choississez un numéro entre 1 et 3")
      menu()

main()
