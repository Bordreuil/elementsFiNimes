# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.6.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.notebook


###
### GEOM component
###

import GEOM
import geompy
import math
import SALOMEDS


geompy.init_geom(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)


Rayon   = 50.;   # Largeur de la piece au niveau de l axe
Rtrou   = 15.;   # Rayon de l axe
Rgorge  = 5.;    # Rayon de la gorge
Lhaut   = 100. ; # Largeur au niveau de la gorge

Sommet_1 = geompy.MakeVertex(0.    ,0.            , 0.  );
Sommet_2 = geompy.MakeVertex(Rayon ,0.            , 0.  );
Sommet_3 = geompy.MakeVertex(Rtrou ,0.            , 0.  );
Sommet_4 = geompy.MakeVertex(0.    ,Rtrou         , 0.  );
Sommet_5 = geompy.MakeVertex(-Rtrou,0.            , 0.  );
Sommet_6 = geompy.MakeVertex(0.,   -Rtrou         , 0.  );  
Sommet_7 = geompy.MakeVertex(Lhaut ,200.          , 0.  );
Sommet_8 = geompy.MakeVertex(0.    ,200.          , 0.  );
Sommet_9 = geompy.MakeVertex(0.    ,200.+Rgorge   , 0.  );
Sommet_10 = geompy.MakeVertex(0.    ,200.+2.*Rgorge, 0.  );
Sommet_11 = geompy.MakeVertex(Lhaut ,200.+2*Rgorge , 0.  );
Sommet_12 = geompy.MakeVertex(-Lhaut,200.+2*Rgorge , 0. );
Sommet_13 = geompy.MakeVertex(-Rayon,0.            , 0. );
Sommet_14 = geompy.MakeVertex(0., -Rayon           , 0. );  
Sommet_15 = geompy.MakeVertex(-Rgorge,200.+Rgorge  , 0. );
Sommet_16 = geompy.MakeVertex(0.,200.+2.*Rgorge+Lhaut  , 0. );
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_7)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_8)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_10, Sommet_11)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_12, Sommet_13)

Arc_1 = geompy.MakeArcCenter(Sommet_9, Sommet_8, Sommet_15,False)
Arc_2 = geompy.MakeArcCenter(Sommet_9, Sommet_15, Sommet_10,False)
Arc_3 = geompy.MakeArcCenter(Sommet_10, Sommet_11, Sommet_16,False)
Arc_4 = geompy.MakeArcCenter(Sommet_10, Sommet_16, Sommet_12,False)
Arc_5 = geompy.MakeArcCenter(Sommet_1, Sommet_3, Sommet_4,False)
Arc_6 = geompy.MakeArcCenter(Sommet_1, Sommet_4, Sommet_5,False)
Arc_7 = geompy.MakeArcCenter(Sommet_1, Sommet_5, Sommet_6,False)
Arc_8 = geompy.MakeArcCenter(Sommet_1, Sommet_6, Sommet_3,False)
Arc_9 = geompy.MakeArcCenter(Sommet_1, Sommet_13, Sommet_14,False)
Arc_10 = geompy.MakeArcCenter(Sommet_1, Sommet_14, Sommet_2,False)

Crochet = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Arc_1, Arc_2, Arc_3, Arc_4, Arc_5, Arc_6, Arc_7, Arc_8, Arc_9, Arc_10], 1)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_7, 'Sommet_7' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Sommet_9, 'Sommet_9' )
geompy.addToStudy( Sommet_10, 'Sommet_10' )
geompy.addToStudy( Sommet_11, 'Sommet_11' )
geompy.addToStudy( Sommet_12, 'Sommet_12' )
geompy.addToStudy( Sommet_13, 'Sommet_13' )
geompy.addToStudy( Sommet_14, 'Sommet_14' )
geompy.addToStudy( Sommet_15, 'Sommet_15' )
geompy.addToStudy( Sommet_16, 'Sommet_16' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Arc_2, 'Arc_2' )
geompy.addToStudy( Arc_3, 'Arc_3' )
geompy.addToStudy( Arc_4, 'Arc_4' )
geompy.addToStudy( Arc_5, 'Arc_5' )
geompy.addToStudy( Arc_6, 'Arc_6' )
geompy.addToStudy( Arc_7, 'Arc_7' )
geompy.addToStudy( Arc_8, 'Arc_8' )
geompy.addToStudy( Arc_9, 'Arc_9' )
geompy.addToStudy( Arc_10, 'Arc_10' )
geompy.addToStudy( Crochet, 'Crochet' )



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
