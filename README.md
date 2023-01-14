# Le projet

Ce projet à pour but de pratiquer la lecture des katakana par le biais des noms de pokemon.

# Installation
Deux versions sont disponibles, une version en terminal et un bot discord.  

Pour lancer les deux versions, il faut installer python3 et l'ensemble des dépendances du projet.  

## Version terminal
Contentez vous de lancer le fichier game_console.py.  
Utilisez ctrl+c pour quitter le jeu.

## Version discord
Avant le premier lancement du bot, la fonction create_database du fichier sqlite_utility.py doit être exécutée une fois pour créer la base de données.  
L'utilisation du code necessite au préalable la création d'un bot discord et l'obtention d'un token (le bot devra disposer de droits suffisant dans le serveur).  

Il vous faudra ensuite créer un fichier .env contenant la variable API_TOKEN.  
Finalement, lancez le fichier game_discord.py pour relier le script à votre bot.  
Les commandes seront visibles dans la liste des commandes du serveur discord (préfixées par un /).  

Il est à noter que ce bot n'a été prévu que pour un usage personnel et n'est pas prévu pour être hébergé sur un serveur public.  
Aussi, l'aspect sécurité n'a pas encore été implémenté et les commandes sont sûrement succeptibles d'échouer si mal utilisées.  