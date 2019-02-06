######################################################
### Bonjour Mélissa                                ###
### Mes commentaires sont précédés de trois dièses ###
######################################################

### Tout d'abord, il faut commencer tout script python par cette ligne qui définit l'encodage des caractères:

# coding: utf-8

# print(articles)

n=0

### Tu as très bien fait de créer des compteurs du nombre d'articles par média!
### Je les ai simplement remontés plus haut, ici:
nbmlapresse = 0
nbmledevoir = 0
nbmlesoleil = 0
nbmlenouvelliste = 0
nbmlatribune = 0
nbmvoixdelest = 0

### Je remonte également ici ta variable «media» (que je rebaptise «medias»)
### C'est une idée originale pour aider au décompte du nombre d'articles par média
medias = ["La Presse+","Le Devoir","Le Soleil","Le Nouvelliste","La Tribune","La Voix de l'Est"]

### Ici, la variable «articles» n'existe pas...
### J'ai mis le début de ta boucle en commentaires
# for article in articles :

### Pour aller chercher le contenu de la variable commentaires, il était possible de faire quelque chose que j'avais prévu
### vous montrer, mais que je n'ai pas eu le temps de faire.
### Il suffisait de télécharger le fichier «eureka.py» et de le placer au même endroit que votre script,
### puis d'insérer la ligne de code suivante qui dit «dans le fichier «eureka», importe la variable «articles»:
from eureka import articles

### Ensuite, la variable «articles» existait. On pouvait donc écrire cette boucle:

for article in articles:
	print(article)
	n+=1
	print(n,article)
	article=article.split(',')
	
### Jusqu'ici tout va bien
### Après le «split», tu as une liste avec 3, 4, 5, 6 ou 7 éléments selon le cas.
### Le premier [0] est toujours le nom du média, donc

	media = article[0].strip()

### On peut intégrer ici les conditions que tu as utilisées pour compter le nombre d'articles par média
### En indentant le tout et en renommant quelques variables
	# if l2 == media[0] :
	if media == medias[0]:
		nbmlapresse +=1
	# elif l2 == media[1] :
	elif media == medias[1]:
		nbmledevoir +=1
	# elif l2 == media[2] :
	elif media == medias[2]:
		nbmlesoleil +=1
	# elif l2 == media[3] :
	elif media == medias[3]:
		nbmlenouvelliste +=1
	# elif l2 == media[4] :
	elif media == medias[4]:
		nbmlatribune +=1
	else : ### Excellent! Il n'est pas nécessaire de vérifier le nombre d'occurrences de La Voix de l'Est puisque c'est la seule autre option possible
		nbmvoixdelest +=1

### Il n'est pas clair ce que doit faire le code ci-dessous...

l2=[article[0:609][0]]

section=[article[0:609][1]]

mots=[article[0:609][2]]

pages=[article[0:609][3]]

### Pour extraire les autres variables, consulte le corrigé détaillé dans la page «devoir1» du syllabus
### Il s'agit essentiellement de faire la même chose que pour la variable «media», mais en utilisant «article[1]» et ainsi de suite.

### Même si le script ne fonctionne pas entièrement, je constate et récompense ton effort! N'hésite pas à poser des questions pour le prochain! :)

# print(articles)
# print("Il y a ", nbmlapresse, "dans", media[0], "\n", "Il y a ", nbmledevoir, "dans", media[1], "\n", "Il y a ", nbmlesoleil, "dans", media[2], "\n", "Il y a ", nbmlenouvelliste, "dans", media[3], "\n", "Il y a ", nbmlatribune, "dans", media[4], "\n", "Il y a ", nbmvoixdelest, "dans", media[5], "\n")
print("Il y a ", nbmlapresse, "dans", medias[0], "\n", "Il y a ", nbmledevoir, "dans", medias[1], "\n", "Il y a ", nbmlesoleil, "dans", medias[2], "\n", "Il y a ", nbmlenouvelliste, "dans", medias[3], "\n", "Il y a ", nbmlatribune, "dans", medias[4], "\n", "Il y a ", nbmvoixdelest, "dans", medias[5], "\n")