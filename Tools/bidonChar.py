#
#    Projet Etudiants Polytech' MSI 2014
#      Parant - Happiette
#    Module de creation de bidons parametres
#    pour Salome meca
#




from math import *
PRECISION= 0.0005

def creerViroleEtDeuxGRC(L,D,around):
    """
    Creation d une virole avec deux fonds GRC suivant l axe around
    """
    Sommet_1 = geompy.MakeVertex((L/2)-(sqrt((9*D/10)**2-(2*D/5)**2)), 0, 0)
    Sommet_2 = geompy.MakeVertex((L/2)-(sqrt((9*D/10)**2-(2*D/5)**2))+D, 0, 0)
    Sommet_3 = geompy.MakeVertex((sqrt(65)*D+45*L)/90, 4*D/9, 0)
    Sommet_4 = geompy.MakeVertex(L/2, D/2, 0)
    Sommet_5 = geompy.MakeVertex(L/2, 2*D/5, 0)
    Sommet_6 = geompy.MakeVertex(-L/2, 2*D/5, 0)
    Sommet_7 = geompy.MakeVertex(-L/2, D/2, 0)
    Sommet_8 = geompy.MakeVertex(-((sqrt(65)*D+45*L)/90), 4*D/9, 0)
    Sommet_9 = geompy.MakeVertex(-((L/2)-(sqrt((9*D/10)**2-(2*D/5)**2))+D), 0, 0)
    Sommet_10 = geompy.MakeVertex(-((L/2)-(sqrt((9*D/10)**2-(2*D/5)**2))), 0, 0)
    Arc_1 = geompy.MakeArcCenter(Sommet_1, Sommet_2, Sommet_3,False)
    Arc_2 = geompy.MakeArcCenter(Sommet_5, Sommet_3, Sommet_4,False)
    Ligne_1 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_7)
    Arc_3 = geompy.MakeArcCenter(Sommet_6, Sommet_7, Sommet_8,False)
    Arc_4 = geompy.MakeArcCenter(Sommet_10, Sommet_8, Sommet_9,False)
    Contour_1 = geompy.MakeWire([Arc_1, Arc_2, Ligne_1, Arc_3, Arc_4],PRECISION )
    Revolution_1 = geompy.MakeRevolution(Contour_1,around, 360*pi/180.0)
    [Face_13,Face_16,Face_17,Face_18,Face_19] = geompy.ExtractShapes(Revolution_1, geompy.ShapeType["FACE"], True)
    FondG = geompy.MakeCompound([Face_13, Face_16])
    FondD = geompy.MakeCompound([Face_18, Face_19])
    Virole = geompy.MakeCompound([Face_17])
    return Virole,FondG,FondD

def creerPiedsEnU(Position_pieds,largeur_pieds, Largeur_pieds,Hauteur_pieds,D):
    Sommet_11 = geompy.MakeVertex(Position_pieds, 0, Largeur_pieds/2)
    Sommet_12 = geompy.MakeVertex(Position_pieds, 0, -Largeur_pieds/2)
    Ligne_2   = geompy.MakeLineTwoPnt(Sommet_11, Sommet_12)
    Sommet_13 = geompy.MakeVertex(Position_pieds-largeur_pieds, 0, Largeur_pieds/2)
    Sommet_14 = geompy.MakeVertex(Position_pieds-largeur_pieds, 0, -Largeur_pieds/2)
    Ligne_3   = geompy.MakeLineTwoPnt(Sommet_11, Sommet_13)
    Ligne_4   = geompy.MakeLineTwoPnt(Sommet_12, Sommet_14)
    Sommet_15 = geompy.MakeVertex(Position_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, Largeur_pieds/2)
    Sommet_16 = geompy.MakeVertex(Position_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, -Largeur_pieds/2)
    Sommet_17 = geompy.MakeVertex(Position_pieds-largeur_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, Largeur_pieds/2)
    Sommet_18 = geompy.MakeVertex(Position_pieds-largeur_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, -Largeur_pieds/2)
    Ligne_5   = geompy.MakeLineTwoPnt(Sommet_11, Sommet_15)
    Ligne_6   = geompy.MakeLineTwoPnt(Sommet_12, Sommet_16)
    Ligne_7   = geompy.MakeLineTwoPnt(Sommet_13, Sommet_17)
    Ligne_8   = geompy.MakeLineTwoPnt(Sommet_14, Sommet_18)
    Ligne_9   = geompy.MakeLineTwoPnt(Sommet_15, Sommet_17)
    Ligne_10  = geompy.MakeLineTwoPnt(Sommet_15, Sommet_16)
    Ligne_11  = geompy.MakeLineTwoPnt(Sommet_16, Sommet_18)
    Sommet_19 = geompy.MakeVertex(-Position_pieds, 0, Largeur_pieds/2)
    Sommet_20 = geompy.MakeVertex(-Position_pieds, 0, -Largeur_pieds/2)
    Ligne_12  = geompy.MakeLineTwoPnt(Sommet_19, Sommet_20)
    Sommet_21 = geompy.MakeVertex(-Position_pieds+largeur_pieds, 0, Largeur_pieds/2)
    Sommet_22 = geompy.MakeVertex(-Position_pieds+largeur_pieds, 0, -Largeur_pieds/2)
    Ligne_13  = geompy.MakeLineTwoPnt(Sommet_19, Sommet_21)
    Ligne_14  = geompy.MakeLineTwoPnt(Sommet_20, Sommet_22)
    Sommet_23 = geompy.MakeVertex(-Position_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, Largeur_pieds/2)
    Sommet_24 = geompy.MakeVertex(-Position_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, -Largeur_pieds/2)
    Sommet_25 = geompy.MakeVertex(-Position_pieds+largeur_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, Largeur_pieds/2)
    Sommet_26 = geompy.MakeVertex(-Position_pieds+largeur_pieds, -sqrt((D/2)**2-((Largeur_pieds)/2)**2)-Hauteur_pieds, -Largeur_pieds/2)
    Ligne_15  = geompy.MakeLineTwoPnt(Sommet_21, Sommet_25)
    Ligne_16  = geompy.MakeLineTwoPnt(Sommet_19, Sommet_23)
    Ligne_17  = geompy.MakeLineTwoPnt(Sommet_20, Sommet_24)
    Ligne_18  = geompy.MakeLineTwoPnt(Sommet_22, Sommet_26)
    Ligne_19  = geompy.MakeLineTwoPnt(Sommet_23, Sommet_25)
    Ligne_20  = geompy.MakeLineTwoPnt(Sommet_23, Sommet_24)
    Ligne_21  = geompy.MakeLineTwoPnt(Sommet_24, Sommet_26)
    Face_1    = geompy.MakeFaceWires([Ligne_3, Ligne_5, Ligne_7, Ligne_9], 1)
    Face_2    = geompy.MakeFaceWires([Ligne_2, Ligne_5, Ligne_6, Ligne_10], 1)
    Face_3    = geompy.MakeFaceWires([Ligne_4, Ligne_6, Ligne_8, Ligne_11], 1)
    Face_4    = geompy.MakeFaceWires([Ligne_13, Ligne_15, Ligne_16, Ligne_19], 1)
    Face_5    = geompy.MakeFaceWires([Ligne_12, Ligne_16, Ligne_17, Ligne_20], 1)
    Face_6    = geompy.MakeFaceWires([Ligne_14, Ligne_17, Ligne_18, Ligne_21], 1)
    Pied1     = geompy.MakeCompound([Face_1,Face_2,Face_3])
    Pied2     = geompy.MakeCompound([Face_4,Face_5,Face_6])
    return Pied1,Pied2


def couperPiedEtBidon(Pied1,Pied2,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Pied1, Pied2], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_1,Face_2,Virole,Face_3,Face_4] = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Partition_2 = geompy.MakePartition([Pied1, Pied2], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Pied1M,Bidon,Pied1G,Pied1D,geomObj_59,geomObj_60,Pied2G,Pied2D,geomObj_61,geomObj_62,Pied2M,geomObj_63] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Pieds = geompy.MakeCompound([ Pied1M, Pied1G, Pied1D, Pied2G, Pied2D, Pied2M])
    Virole = geompy.MakeCompound([ Virole])
    return Virole,Pieds

def creerPiquageVirole(Position,H,Alpha,Dp,Dbride):
    Sommet_27   = geompy.MakeVertex(Position, 0, 0)
    Sommet_28   = geompy.MakeVertex(Position, H*cos((Alpha*2*pi)/(360)), H*sin((Alpha*2*pi)/(360)))
    Ligne_22    = geompy.MakeLineTwoPnt(Sommet_27, Sommet_28)
    Cercle_1    = geompy.MakeCircle(Sommet_28, Ligne_22, Dp/2)
    Extrusion_1 = geompy.MakePrismVecH(Cercle_1, Ligne_22, -H)
    Cercle_2    = geompy.MakeCircle(Sommet_28, Ligne_22, Dbride/2)
    Face_13     = geompy.MakeFaceWires([Cercle_1, Cercle_2], 1)
    Piquage     =  geompy.MakeCompound([Extrusion_1])
    return Piquage,Face_13

def creerPiquageFondAxialPos(Hauteur,Rayon,Alpha,Dp,Dbride):
    Sommet_27   = geompy.MakeVertex(0., Rayon*cos((Alpha*2*pi)/(360)), Rayon*sin((Alpha*2*pi)/(360)))
    Sommet_28   = geompy.MakeVertex(Hauteur, Rayon*cos((Alpha*2*pi)/(360)), Rayon*sin((Alpha*2*pi)/(360)))
    Ligne_22    = geompy.MakeLineTwoPnt(Sommet_27, Sommet_28)
    Cercle_1    = geompy.MakeCircle(Sommet_28, Ligne_22, Dp/2)
    Extrusion_1 = geompy.MakePrismVecH(Cercle_1, Ligne_22, -Hauteur)
    Cercle_2    = geompy.MakeCircle(Sommet_28, Ligne_22, Dbride/2)
    Face_13     = geompy.MakeFaceWires([Cercle_1, Cercle_2], 1)
    Piquage     =  geompy.MakeCompound([Extrusion_1])
    return Piquage,Face_13
def creerPiquageFondAxialNeg(Hauteur,Rayon,Alpha,Dp,Dbride):
    Sommet_27   = geompy.MakeVertex(0., Rayon*cos((Alpha*2*pi)/(360)), Rayon*sin((Alpha*2*pi)/(360)))
    Sommet_28   = geompy.MakeVertex(Hauteur, Rayon*cos((Alpha*2*pi)/(360)), Rayon*sin((Alpha*2*pi)/(360)))
    Ligne_22    = geompy.MakeLineTwoPnt(Sommet_27, Sommet_28)
    Cercle_1    = geompy.MakeCircle(Sommet_28, Ligne_22, Dp/2)
    Extrusion_1 = geompy.MakePrismVecH(Cercle_1, Ligne_22, Hauteur)
    Cercle_2    = geompy.MakeCircle(Sommet_28, Ligne_22, Dbride/2)
    Face_13     = geompy.MakeFaceWires([Cercle_1, Cercle_2], 1)
    Piquage     =  geompy.MakeCompound([Extrusion_1])
    return Piquage,Face_13
def couperVirolePiquagePosCas1(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Virole = result[2]
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Virole,Piquage
def couperVirolePiquagePosCas2(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Virole = result[2]
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Virole,Piquage
def couperVirolePiquageNegCas1(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Virole = result[4]
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Virole,Piquage
def couperVirolePiquageNegCas2(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Virole = result[3]
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Virole,Piquage
def couperFondPiquagePosCas1(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Fond = geompy.MakeCompound([result[3],result[6]])
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Fond,Piquage

def couperFondPiquagePosCas2(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Fond = geompy.MakeCompound([result[3],result[5]])
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Fond,Piquage

def couperFondPiquagePosCas3Ou4(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Fond = geompy.MakeCompound([result[3],result[4]])
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_8] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_8])
    return Fond,Piquage

def couperFondPiquageNegCas1Ou2(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Fond = geompy.MakeCompound([result[0],result[3]])
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_9] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_7])
    return Fond,Piquage

def couperFondPiquageNegCas3(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    Fond = geompy.MakeCompound([result[0],result[3]])
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_9] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_7])
    return Fond,Piquage

def couperFondPiquageNegCas4(Piquage,Corps):
    Partition_1 = geompy.MakePartition([Corps], [Piquage], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    result = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
    ls=[]
    for i,res in enumerate(result[:3]):
         props = geompy.BasicProperties(res)
         ls.append((props[1],i))

    ls =  sorted(ls)
    #print ls

    Fond = geompy.MakeCompound([result[ls[1][1]],result[ls[2][1]]])
    Partition_2 = geompy.MakePartition([Piquage], [Corps], [], [], geompy.ShapeType["FACE"], 0, [], 0)
    [Face_7,Face_9] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
    Piquage   = geompy.MakeCompound([Face_7])
    return Fond,Piquage





def creerBidon(args):
    Bidon=geompy.MakeCompound(args)
    groups=[]
    for arg in args:
        group = geompy.CreateGroup(Bidon, geompy.ShapeType["FACE"])
        SubFaceList = geompy.SubShapeAllSorted(arg, geompy.ShapeType["FACE"])
        ids=[]
        for iid in SubFaceList:
            ids.append(geompy.LocalOp.GetSubShapeIndex(Bidon,iid))
        geompy.UnionIDs(group,ids)
        groups.append(group)
    return Bidon,groups
    
