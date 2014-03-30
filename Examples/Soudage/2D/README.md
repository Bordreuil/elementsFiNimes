Ce dossier contient une modelisation 2D d une ligne de fusion.
Les differents fichiers presents dans le repertoire sont:

    - plaque.py : qui modelise la moitie de la plaque. Le maillage defini
      est relativement fin
    
    - plaque_moyen.py : qui modelise la meme plaque avec un maillage un peu
      plus grossier

    - thermique.comm : un fichier de commande pour faire le calcul thermique
      de la modelisation du soudage, avec une seule partie du cordon

    - thermique_fin.comm : un fichier de commande pour faire toute la ligne 
      de fusion

    - meca.comm : un fichier de commande pour faire un calcul mecanique et 
      analyser les contraintes residuelles.
      
    - une image astk_poursuite permettant de voir les reglages pour realiser
      un calcul en mode poursuite. 
      Les fichiers dans ther_total.base doivent etre unzippe avant le lancement
      du calcul:effectuer la commande 'gunzip glob.1.gz' et 'gunzip pick1.gz' 