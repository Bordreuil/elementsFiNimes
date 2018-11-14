from element3d  import *
import string

def readDat(fname,indX=1,indY=2):
    lignes    = open(fname,'r').readlines()
    res       = string.split(lignes[0])
    numPoints = int(res[0])
    numElts   = int(res[1])
    print 'nombre de noeuds:',numPoints
    nodes    = Nodes()
    for i in range(numPoints):
        res   = string.split(lignes[i+1])
        numpt = int(res[0])-1
        x     = float(res[1])
        y     = float(res[2])
        z     = float(res[3])
        nodes.addNode(numpt,Node(numpt,x,y,z))

    hexs = list()
    print 'Nombre d elements:',numElts
    for i in range(numElts):
         res = string.split(lignes[numPoints+1+i])
         if int(res[1]) == 308:
             p1 = int(res[2])-1
             p2 = int(res[3])-1
             p3 = int(res[4])-1
             p4 = int(res[5])-1
             p5 = int(res[6])-1
             p6 = int(res[7])-1
             p7 = int(res[8])-1
             p8 = int(res[9])-1
    
             hexs.append(H8Meca3d(nodes[p4],
                                   nodes[p8],
                                   nodes[p7],
                                   nodes[p3],
                                   nodes[p1],
                                   nodes[p5],
                                   nodes[p6],
                                   nodes[p2]))
    return nodes,hexs

if __name__=='__main__':
        from pylab import *
        nodes,els=readDat('datas/Maillage_2.dat')
        print len(nodes),len(els)
        # for el in els:
        #     coord = el.coordNodes()
        #     plot(coord[:,0],coord[:,1],'b')
        # axis('equal')
        # show()
            
