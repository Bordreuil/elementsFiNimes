Calcul d'une poutre encastree:
-----------------------------

Version Salomeca   : v2014.2 
Version Code Aster : 11.

Actions a realiser dans salome-meca (la version francaise est disponible
dans Fichier/Preferences):

MODULE GEOMETRY:
---------------
       - Nouvel Objet/Sommet : Ajouter deux sommets
       - Nouvel Objet/Ligne  : Ajouter une ligne base sur ces sommets
  	 	        Possibilite de renommer la ligne en poutre
			ou TOUT
	- Nouvel Objet/Groupe : Definir un groupe de point :
  	 	        Encastre
			Effort
	- Vous pouvez visualiser dans le module geometry les elements de 
	       structure. Il faut alors ouvrir un module eficas ouvrir le
	       fichier .comm que vous allez utiliser dans le calcul et ensuite
	       cliquer sur AFFE_CARA_ELEM est demandé view3d.

MODULE MESH:
------------
	- Creer Maillage (Selectionner la ligne) (Menu Maillage)
	- Choisir l'algorithme Wire discretisation
	- Dans les hypotheses cliquer sur l'engrenage.
	- Choisir Nb Segments et mettre le nombre desire.
	- Dans Maillage creer des groupes a partir de la geometrie:
	       Deux groupes de noeuds doivent apparaitre:
	       	    - Encastrement et Effort 
	       Un groupe d'aretes (Edge) doit etre defini:
	       	    - TOUT


MODULE ASTER:
-------------
	- Creer un cas d etude
	- Nommer le cas d etude : 'poutre'
	- Choisir le point fichier poutre.comm sur le disque
	- Choisir le maillage dans l'arbre d etude
	- Verifier la version du code aster (.comm = v10)
	- Cliquez interactive follow-up
	- Valider

	Dans l'arbre d etude, le module aster apparait
	avec un cas d etude 'poutre'. Vous pouvez modifier
	le maillage dans le cas d etude ou le temps de calcul
	en cliquant droit sur le cas d'etude et en faisant edit

	Il faut verifier que le fichier .comm soit compatible
	avec la version que vous utilisez du code aster.
	An allant dans datas du cas d etude, le fichier 
	poutre.comm apparait. En faisant un clique droit
	vous pouvez faire 'Run Eficas' qui verifiera la syntaxe.

	Si tout est validé vous pouvez lancer le calcul pour le cas
	d etude: Clique droit Run sur l'objet cas d etude.


MODULE POST_PRO:
---------------

	Faites les analyses que vous desirez.

