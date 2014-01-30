Exemple de calcul de contraintes axisymmetriques 
avec singularites de contraintes dans un culot de vérin.
Deux geometries sont fournie:
     - culot.geo: dont le fond du verin et le corps sont soudés 
      bout a bout
     - culot_decale.geo : dont la soudure est légèrement décalé.

Les fichiers .geo permettent à travers gmsh de creer des maillages .med 
que l'on peut directement importer dans le module mesh de salomé-méca.
En comparant les deux géométries, on peut se rentre compte que le deuxieme
cas à une contrainte inférieure et est donc plus judicieuse. Elle necessite 
un usinage supplementaire. 

