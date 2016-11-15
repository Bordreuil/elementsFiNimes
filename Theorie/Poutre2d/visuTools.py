from pylab import *

def plotElements(coords,els):
    for el in els:
        conn = el.connectivite()
        plot(coords[conn,0],coords[conn,1],'r',linewidth=2)

def plotNodes(coords):
    plot(coords[:,0],coords[:,1],'o')

def plotContraintes(els,Coords,sigmas,jet):
    masig = max(sigmas)
    misig = min(sigmas)
    DeltaS = masig-misig
    for i,el in enumerate(els):
        conn = el.connectivite()
        col  = (sigmas[i]-misig)/DeltaS
        plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)
    import matplotlib.pyplot as plt
    sm = plt.cm.ScalarMappable(cmap=jet, norm=plt.Normalize(vmin=misig, vmax=masig))
    sm._A = []
    plt.colorbar(sm)
