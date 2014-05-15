bidonCommPart1="""#
#
#
#	Traitement d un appareil a pression
#	modelise en plaque
#
#	Differents groupes doivent etre defini:
#	   de Noeuds:
#		   - Encastre : sur une ligne du supportage au niveau
#		     	        du Genie Civil
#		   - Appuis   : sur une ligne de supportage au niveau
#		     	        du Genie Civil et laissant la dilation
#				suivant l axe du bidon se faire.
#	  de Faces:
#		  - Virole
#		  - Fonds
#		  - Piquage
#		  - Bride
#		  - Supports

# Initialisation du calcul
DEBUT();

#
# Lecture du maillage au format
#
MA=LIRE_MAILLAGE(FORMAT='MED',);

#
# Definition des proprietes materiau
#
MATER=DEFI_MATERIAU(ELAS=_F(E=196200.0,
                            NU=0.3,
                            RHO=10000.0,),);
#
# Affectation des proprietes materiau
#
CHMAT=AFFE_MATERIAU(MAILLAGE=MA,
                    AFFE=_F(TOUT='OUI',
                            MATER=MATER,),);
#
# Le maillage etant sur des elements triangulaire
# on definit tout le modele sur une modelisation
# Discrete Kirchoff Triangle
#
MODELE=AFFE_MODELE(MAILLAGE=MA,
                   AFFE=_F(TOUT='OUI',
                           PHENOMENE='MECANIQUE',
                           MODELISATION='DKT',),);
#
# Affecation des caracteristiques des plaques.
# 	     Attention : malgre le fait qu on travaille en 
#	     modele isotrope il faut definir une orienation pour 
#	     les plaques. Par defaut elle est defini a partir du vecteur X
#	     mais cela pose des probleme pour le piquage et le support
#	     dont il faut modifier cette valeur par defaut a Z
#
CAREL=AFFE_CARA_ELEM(MODELE=MODELE,
                     COQUE=("""
                     
#                    _F(GROUP_MA='Virole',
#                               EPAIS=5.,),
#_F(GROUP_MA='Piquage',
#                               EPAIS=5.,
#                               VECTEUR=(0,0,1,),),
#                            _F(GROUP_MA='Supports',
#                               EPAIS=5.,
#                               VECTEUR=(0,0,1,),),
#                            _F(GROUP_MA='Bride',
#                               EPAIS=5.,),
#                            _F(GROUP_MA='Fonds',
#                               EPAIS=5.,),),);

bidonCommPart2="""
#
# Affectation du chargement mecanique
#
CHARGE=AFFE_CHAR_MECA(VERI_NORM='OUI',
                      MODELE=MODELE,
                      DDL_IMPO=(_F(GROUP_NO='Encastre',
                                   DX=0.0,
                                   DY=0.0,
                                   DZ=0.0,
                                   DRX=0.0,
                                   DRY=0.0,
                                   DRZ=0.0,),
                                _F(GROUP_NO='Appui',
                                   DY=0.0,
                                   DZ=0.0,
                                   DRX=0.0,
                                   DRY=0.0,
                                   DRZ=0.0,),),
                      FORCE_COQUE="""
bidonCommPart3="""
#
#	Resolution du probleme de statique
#
RESU=MECA_STATIQUE(MODELE=MODELE,
                   CHAM_MATER=CHMAT,
                   CARA_ELEM=CAREL,
                   EXCIT=_F(CHARGE=CHARGE,),);

#
#	Extraction des resultats avant impression
#	Pour les plaques les contraintes de flexion et de
#	membrane ne sont pas directement donnees, il faut d abord
#	extraire les contraintes sur le NIVE_COUCHE moyenne (Ligne neutre)
#	puis sur la couche superieure
#	On remarque que les resultats sont stockees dans deux resultats
#	differents NEUTRE et SUP qu'on pourra combiner dans 
#	paraview pour extraire la contrainte de membrane
#
# -------------------------------------------------
#	Definition du resultat sur la surface moyenne
#
NEUTRE=CALC_ELEM(RESULTAT=RESU,
                 REPE_COQUE=_F(TOUT='OUI',
                               NUME_COUCHE=1,
                               NIVE_COUCHE='MOY',),
                 OPTION=('SIEF_ELNO',
			 'SIGM_ELNO',
			 'SIEQ_ELNO',),);

# Moyennation au niveau des noeuds pour la visualisation

NEUTRE=CALC_NO(reuse =NEUTRE,
               RESULTAT=NEUTRE,
               OPTION=('SIEF_NOEU','SIGM_NOEU','SIEQ_NOEU',),);
# -------------------------------------------------
#	Definition du resultat sur la surface superieure
#
SUP=CALC_ELEM(RESULTAT=RESU,
              REPE_COQUE=_F(TOUT='OUI',
                            NIVE_COUCHE='SUP',),
              OPTION=('SIEF_ELNO','SIGM_ELNO','SIEQ_ELNO',),);

# Moyennation au niveau des noeuds pour la visualisation

SUP=CALC_NO(reuse =SUP,
            RESULTAT=SUP,
            OPTION=('SIEF_NOEU','SIGM_NOEU','SIEQ_NOEU',),);
#
#	Impression des resultats au format MED. 
#
IMPR_RESU(FORMAT='MED',
          UNITE=80,
          RESU=(_F(MAILLAGE=MA,
                   RESULTAT=NEUTRE,
                   NOM_CHAM=(	'SIEF_NOEU',
				'SIGM_NOEU',
				'SIEQ_NOEU',
				'DEPL',),),
                _F(MAILLAGE=MA,
                   RESULTAT=SUP,
                   NOM_CHAM=(	'SIEF_NOEU',
				'SIEQ_NOEU',
				'DEPL',
				'SIGM_NOEU',),),),);

FIN();"""