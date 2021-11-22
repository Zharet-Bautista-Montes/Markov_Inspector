import sys, matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvas
from matplotlib.backend_bases import NavigationToolbar2
from Interface import *
from MultipleMC import *
from MarkovChain import *

class MainWindow(QtWidgets.QMainWindow, Ui_MarkovInspector):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.CleanConfig.clicked.connect(self.clean)
        self.SaveConfig.clicked.connect(self.setConfigurations)
        self.PaintStudyNet.clicked.connect(self.showNetworkChain)
        self.SpanBehavior.clicked.connect(self.showBehavior)
        self.SpotCriticalNodes.clicked.connect(self.showCritical)
        self.Inspect_T.clicked.connect(self.getCapture)
        self.establishedContext = False
        self.Progress = []
        self.HeatMap = []
        self.NetStructure = {}
        self.nodes = []
        self.edges = []
        self.MT = []
        self.Prob_sp = 0
        self.Prob_sc = 0

    def clean(self):
        self.Pps.setValue(0.0)
        self.Psp.setValue(0.0)
        self.Psc.setValue(0.0)
        self.Pcp.setValue(0.0)
        self.Pci.setValue(0.0)
        self.NetNodes.setValue(0)
        self.Specify_T.setValue(0)
        self.Pshare.display(0)
        self.Sshare.display(0)
        self.Cshare.display(0)
        self.Ishare.display(0)
        for u in range(1, 11):
            combobox = self.__getattribute__('comboBox_Node'+str(u))
            combobox.setCurrentIndex(combobox.findText('Protegido'))
            linedit = self.__getattribute__('lineEdit_Neighbors'+str(u))
            linedit.setText('')

    def setConfigurations(self):
        pps = self.Pps.value()
        psc = self.Psc.value()
        pci = self.Pci.value()
        psp = self.Psp.value()
        pcp = self.Pcp.value()
        self.Prob_sp, self.Prob_sc, self.MT = setNonDefaults((pps, psp, psc, pcp, pci))
        Nsize = self.NetNodes.value()
        self.Specify_T.setValue(0)
        self.establishedContext = True
        self.HeatMap, states, arcs = [], [], []
        for v in range(1, Nsize+1):
            combobox = self.__getattribute__('comboBox_Node'+str(v))
            states.append(combobox.currentText())
            linedit = self.__getattribute__('lineEdit_Neighbors'+str(v))
            arcs.append(linedit.text())
        self.nodes, self.edges, self.NetStructure = UIBuildNetwork(states, arcs, self.MT)
    
    def getCapture(self):
        momenT = self.Specify_T.value()
        Prate, Srate, Crate, Irate = self.Progress[momenT]
        self.Pshare.display(Prate)
        self.Sshare.display(Srate)
        self.Cshare.display(Crate)
        self.Ishare.display(Irate)

    def showNetworkChain(self):
        FigureCanvas(graphNetwork(self.nodes, self.edges))

    def showBehavior(self):
        if self.establishedContext:
            Nnodes, counter = len(self.nodes), 0
            refVector = scanDistribution(Nnodes, self.NetStructure)
            self.Progress = [refVector]
            while ((refVector != np.array([0.0, 0.0, 0.0, 1.0])).any()):
                refVector = scanDistribution(Nnodes, self.NetStructure)
                self.Progress.append(performStepAllNodes(Nnodes, self.NetStructure, self.Prob_sp, self.Prob_sc))
                self.HeatMap.append(spotNodeStates(Nnodes, self.NetStructure))
                counter += 1
            self.Specify_T.setMaximum(counter)
        self.establishedContext = False
        Behavior = np.transpose(np.array(self.Progress))
        FigureCanvas(paintProgressMC(Behavior))

    def showCritical(self):
        Critical = np.transpose(np.array(self.HeatMap))
        FigureCanvas(retrieveHeatMap(Critical, len(self.HeatMap), len(self.HeatMap[0])))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()