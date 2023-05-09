from element3dT4  import *
import string
import matplotlib.pyplot as plt


def readDat_modifT4Thermal(fname,indX=1,indY=2):
    lignes    = open(fname,'r').readlines()
    res       = lignes[0].split()
    #print(res[0])
    numPoints = int(res[0])
    numElts   = int(res[1])
    #print('nombre de noeuds:',numPoints)
    nodes    = Nodes()
    for i in range(numPoints):
        res   = lignes[i+1].split()
        #print(res)
        numpt = int(res[0])-1
        x     = float(res[1])
        y     = float(res[2])
        z     = float(res[3])
        nodes.addNode(numpt,Node(numpt,x,y,z))

    tetras = list()
    #print('Nombre d elements:',numElts)

    for i in range(numElts):
        res = lignes[numPoints+1+i].split()
        if int(res[1]) == 304:
                        p1 = int(res[5])-1
                        p2 = int(res[4])-1
                        p3 = int(res[3])-1
                        p4 = int(res[2])-1

                        tetras.append(T4Thermal3d(nodes[p1],
                                           nodes[p2],
                                           nodes[p3],
                                           nodes[p4]))

    return nodes,tetras
