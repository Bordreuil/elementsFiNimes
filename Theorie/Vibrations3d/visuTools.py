from pylab import *
import vtk

class resultsFile:
    def __init__(self,fname):
        self._fname        = fname
        self._resultsCell  = []
        self._resultsPoint = []
    def defineMesh(self,nodes,elements):
        self._points    = vtk.vtkPoints()
        self._hexs = vtk.vtkUnstructuredGrid() #vtk.vtkCellArray()
        for i in range(len(nodes)):
             self._points.InsertNextPoint(nodes[i].x(),nodes[i].y(),nodes[i].z())
        for el  in elements:
             hexa  = vtk.vtkHexahedron()
             conn = el.connectivite()
             for ii,n in enumerate(conn):
                 hexa.GetPointIds().SetId(ii,n)
             self._hexs.InsertNextCell(hexa.GetCellType(), hexa.GetPointIds())
        self._hexs.SetPoints(self._points)
    def addVectorToNode(self,fieldValues,name):
        datas = vtk.vtkDoubleArray()
        datas.SetNumberOfComponents(3)
        datas.SetName(name)
        for value in fieldValues:
            datas.InsertNextTuple3(value[0],value[1],value[2])
        self._hexs.GetPointData().AddArray(datas)
    def addVectorToCell(self,fieldValues,name):
        datas = vtk.vtkDoubleArray()
        datas.SetNumberOfComponents(6)
        datas.SetName(name)
        for value in fieldValues:
            datas.InsertNextTuple(value)
        self._hexs.GetCellData().AddArray(datas)

    def write(self):
        # polydata = vtk.vtkPolyData()
        # polydata.SetPoints(self._points)
        # polydata.SetPolys(self._hexs)
        # for ptData in self._resultsPoint:
        #     polydata.GetPointData().AddArray(ptData)
        # for cellData in self._resultsCell:
        #     polydata.GetCellData().AddArray(cellData)
            
        # polydata.Modified()
        writer = vtk.vtkXMLUnstructuredGridWriter()
        writer.SetFileName(self._fname)
        if vtk.VTK_MAJOR_VERSION <= 5:
            writer.SetInput(self._hexs)
        else:
            writer.SetInputData(self._hexs)
        writer.Write()
        
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
