# Gestionnaire de Mots de Passe 

Ce programme est un gestionnaire de mots de passe avec une interface graphique, créé en utilisant le module tkinter de Python. Il permet de stocker de manière sécurisée des informations sensibles, telles que des mots de passe, de manière chiffrée.

## Prérequis
- Python 3
- Un environnement virtuel que vous pouvez installer à l'aide de la commande `python3 -m venv`
- Et exécuter cette env à l'aide `source .bin/activate`
- Le module tkinter (généralement inclus dans l'installation standard de Python)
- Le module cryptography, que vous pouvez installer avec `pip install cryptography`

## Fonctionnalités

- Chiffrement des informations sensibles avec une clé générée ou stockée dans un fichier.
- Ajout de nouveaux mots de passe associés à un site web et un nom d'utilisateur.
- Affichage des mots de passe stockés avec des options pour afficher, modifier et supprimer.
- Interface utilisateur conviviale pour une utilisation facile.

## Utilisation

1. Exécutez le programme en exécutant le script Python `gmdp.py`.

2. La fenêtre principale s'ouvrira, où vous pouvez ajouter de nouveaux mots de passe et afficher ceux qui sont déjà stockés.

3. Pour ajouter un nouveau mot de passe, saisissez le site web, le nom d'utilisateur et le mot de passe, puis cliquez sur le bouton "Ajouter mot de passe".

4. Pour afficher, modifier ou supprimer des mots de passe, utilisez le bouton `Afficher mot de passe` dans la fenêtre de gestion des mots de passe.

## Stockage des Mots de Passe

Les mots de passe sont stockés de manière sécurisée dans un fichier nommé "mots_de_passe.txt". Ils sont chiffrés à l'aide de la bibliothèque Fernet de cryptography. La clé de chiffrement est stockée dans un fichier "key.txt" ou générée si le fichier n'existe pas.

## Avertissement

Assurez-vous de ne pas perdre la clé de chiffrement, car vous ne pourrez pas récupérer les mots de passe sans elle. Conservez la clé en toute sécurité.


