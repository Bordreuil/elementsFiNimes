from bidonChar import * 

class bidonFondGRC:
    def __init__(self,Dvirole      = 500.,
                      Lvirole      = 1200.,
                      PositionPieds= 1280.,
                      LargeurPieds = 900.,
                      largeurPieds = 300.,
                      HauteurPieds = 800.):
        self._Dvirole       = Dvirole
        self._Lvirole       = Lvirole
        self._PositionPieds = PositionPieds
        self._LargeurPieds  = LargeurPieds
        self._largeurPieds  = largeurPieds
        self._HauteurPieds  = HauteurPieds
 
        OX                  = geompy.MakeVectorDXDYDZ(1, 0, 0)
        self._Axe           = OX
        Virole,FondG,FondD  = creerViroleEtDeuxGRC(Lvirole,Dvirole,OX)
        Pied1,Pied2         = creerPiedsEnU(PositionPieds,
                                            largeurPieds,
                                            LargeurPieds,
                                            HauteurPieds,
                                            Dvirole)

       
        Corps = geompy.MakeCompound([Virole,
                                             FondG,
                                             FondD])
        Virole,Pieds  = couperPiedEtBidon(Pied1,Pied2,Corps)
        self._virole  = Virole
        self._fondG   = FondG
        self._fondD   = FondD 
        self._pieds   = Pieds
        self._piquages = []
        self._updateCorps()
    def _updateCorps(self):
         self._Corps  = geompy.MakeCompound([self._virole,
                                             self._fondG,
                                             self._fondD])
    def ajouterPiquageVirole(self,Hpiquage,Dpiquage,Alpha,Position,Dbride):
        Piq2          = creerPiquage(Position,Hpiquage,Alpha,Dpiquage,Dbride)
        Virole,Piq2   = couperVirolePiquage(Piq2,self._Corps)
        self._virole  = Virole
        self._updateCorps()
        self._piquages.append(Piq2)
    def virole(self):
        return self._virole
    def fondG(self):
        return self._fondG
    def fondD(self):
        return self._fondD
    def pieds(self):
        return self._pieds
    def piquages(self):
        return self._piquages
    def fabriquerBidon(self):
        comps= [self._virole,self._fondG,self._fondD,self._pieds]
        for piq in self._piquages:
            comps.append(piq)
        return creerBidon(comps)
