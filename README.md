# Gestionnaire-de-mots-de-passes
Cette application permet d'encrypter, de stocker et de consulter les mots de passes ajoutés

L'exécution de ce code nécessite le module "cryptography". Pour vérifier que pip est bien installé, on tape **pip -V** en ligne de commande. Si la commande n'est pas reconnu, c'est que l'utilitaire pip n'est pas installé. Pour installer le module "cryptography", on tape la commande **pip install cryptography** sur une fenêtre de ligne de commande (terminal,cmd) ou directement sur le terminal de notre logiciel interpreteur par exemple VS Code.

Il est possible que la commande **pip install cryptography** ne fonctionne pas. Dans ce cas, il est possible que notre dossier python ou python/scripts ne se soit pas automatiquement ajoutés au **PATH** lors de l'installation de python. Alors on peut manuellement ajouter le dossier Python et Python\Scripts au **PATH**.
Dossier python présent par défaut sur : 
Dossier python\Scripts présent par défaut sur : C:\Utilisateurs\"Utilisateur"\AppData\Local\Programs\Python\Python310\Scripts

Pour ajouter ces dossiers au **PATH**, on tape sur la barre de recherche **Paramètres Systèmes Avancées**, puis on accéde au variable d'environnement présent sur la fenêtre affiché. A ce niveau, on ajoute une **Nouvelle** entrée au PATH et on choisit le chemin du dossier Python **C:\Utilisateurs\"Utilisateur"\AppData\Local\Programs\Python\Python310** et on confirme puis on refait la même manipulation mais cette fois ci pour le dossier Scritps de Python.

Méthode Alternative : On réinstalle Python et on coche la case **Add Python to PATH** pour que **pip** soit automatiquement disponible.

Une autre méthode pour installer **pip** : https://waytolearnx.com/2020/06/comment-installer-pip-pour-python-sur-windows.html
