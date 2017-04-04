from element2d  import *
import string

def readGmsh(fname,indX=1,indY=2):
    lignes    = open(fname,'r').readlines()
    numPoints = int(lignes[4])
    nodes    = Nodes()
    for i in range(numPoints):
        res   = string.split(lignes[i+5])
        numpt = int(res[0])-1
        x     = float(res[indX])
        y     = float(res[indY])
        nodes.addNode(numpt,Node(numpt,x,y))
    numElts   = int(lignes[numPoints+7])
    triangles = list()
    for i in range(numElts):
        res = string.split(lignes[numPoints+8+i])
        if int(res[1]) == 2:
            p1 = int(res[-3])-1
            p2 = int(res[-2])-1
            p3 = int(res[-1])-1
            triangles.append(TriangleMeca2d(nodes[p1],
                                            nodes[p2],
                                            nodes[p3]))
    return nodes,triangles

if __name__=='__main__':
        from pylab import *
        nodes,els=readGmsh('datas/plaque.msh')
        for el in els:
            coord = el.coordNodes()
            plot(coord[:,0],coord[:,1],'b')
        axis('equal')
        show()
            
