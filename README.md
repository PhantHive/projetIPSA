# projetIPSA
#### morpion > Ici on detail ce qui a ete fait et ce qui devrait pouvoir etre fait!

1.`initialisation de notre projet avec une premiere fenetre
interface graphique ou l'idee serai de recuperer les infos
quant au niveau et nombre de match`

2.`Nous avons ajoute un premier niveau facile (topLevel) ou le bot repond 
aleatoirement a la suite de l'utilisateur`

3.`customisation de la fenetre principale avec un fond grace a la librairie pillow`

4.`ajout du mode moyen et difficile`

5.`ajout d'une page de login lie a un fichier json: login.json ou 
l'on recup identifiant et mdp`

6.`Ajout d'un leaderboard offline ou l'on recupere les resultats
a chaque fin de game classe sous forme de dictionnaire de dictionnaire de dictionnaire
de la forme { pseudo:{difficulte: {victoire:valeur, defaite:valeur, egalite:valeur}}}`

7.`Ajout du niveau cauchemar et virtuose issue d'une pur creativite de notre groupe aha (mode blind vision/ mode blindvision+rotate)`

8.`Ajout de compteur (pour mettre des delais entre depart de jeu et fermeture)`

9.`Voice mode: avec mixer de pygame on ajoute grace a des textToSpeech en ligne des voix pour chaque resultat et plus...`

10.`Pour pouvoir continuer nos tests sans que les personnes aient a se reinscrire nous descidons de proceder 
avec une connection par base de donnee de type nosql, on utilise alors pymongo`

11.`On rajoute une 2 eme collection dans notre base de donnee cette fois pour un leaderboard en ligne
pour l'instant ce leaderboard prend en compte que le nombre de victoire (tout mode de jeu confondu) il ne classe que les 3 premiers`

12.`Ajout d'un mode multi (sur meme pc)`

13.`Customisation de nos interfaces en ajoutant des curseurs custom`

###### Objectifs a atteindre si possible:
*mettre en place un morpion 3x3x9
* mettre en place un leaderboard plus grand (top50 avec scrollbar sur un toplevel)
* Mettre en place un mode chrono
* Ajoute une collection (argent) afin de rajouter un mode SuperPouvoir permettant de jouer sur un morpion 3x3x9
avec ces super pouvoirs.



###### Repartition des taches:
> Responsable niveau facile/extreme => Talaat

> Responsable niveau moyen/cauchemar => Thomas

> Responsable niveau difficile/virtuose => Zakaria

> Responsable tri des donnees => Principalement Zakaria

> Responsable customisation => tout le monde

* On s'est tous entre-aider pour chaque choses dont on ete responsable.
* Nous utilisons Git pour communiquer nos codes en temps reels sans perdre de temps.

NOTE: Nous n'utilisons pas d'algorithmes comme celui du Mini-max ce qui ne nous permet pas de faire un bot
imbattable, ce bot est le pur fruit de notre raisonnement d'ou le nombre de ligne de code important.

#IPSA2024


