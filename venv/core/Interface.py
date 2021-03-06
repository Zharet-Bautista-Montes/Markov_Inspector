# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MarkovInspector(object):
    def setupUi(self, MarkovInspector):
        MarkovInspector.setObjectName("MarkovInspector")
        MarkovInspector.resize(461, 502)
        self.centralwidget = QtWidgets.QWidget(MarkovInspector)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 461, 481))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 442, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.NetDescription = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.NetDescription.setGeometry(QtCore.QRect(20, 120, 411, 371))
        self.NetDescription.setObjectName("NetDescription")
        self.Instructions = QtWidgets.QLabel(self.NetDescription)
        self.Instructions.setGeometry(QtCore.QRect(10, 10, 391, 41))
        self.Instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.Instructions.setWordWrap(True)
        self.Instructions.setObjectName("Instructions")
        self.label_Node1 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node1.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_Node1.setObjectName("label_Node1")
        self.comboBox_Node1 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node1.setGeometry(QtCore.QRect(110, 60, 111, 22))
        self.comboBox_Node1.setObjectName("comboBox_Node1")
        self.comboBox_Node1.addItem("")
        self.comboBox_Node1.addItem("")
        self.comboBox_Node1.addItem("")
        self.comboBox_Node1.addItem("")
        self.label_Neighbors1 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors1.setGeometry(QtCore.QRect(230, 60, 51, 21))
        self.label_Neighbors1.setObjectName("label_Neighbors1")
        self.lineEdit_Neighbors1 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors1.setGeometry(QtCore.QRect(280, 60, 113, 20))
        self.lineEdit_Neighbors1.setObjectName("lineEdit_Neighbors1")
        self.label_Node2 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node2.setGeometry(QtCore.QRect(20, 90, 81, 21))
        self.label_Node2.setObjectName("label_Node2")
        self.comboBox_Node2 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node2.setGeometry(QtCore.QRect(110, 90, 111, 22))
        self.comboBox_Node2.setObjectName("comboBox_Node2")
        self.comboBox_Node2.addItem("")
        self.comboBox_Node2.addItem("")
        self.comboBox_Node2.addItem("")
        self.comboBox_Node2.addItem("")
        self.lineEdit_Neighbors2 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors2.setGeometry(QtCore.QRect(280, 90, 113, 20))
        self.lineEdit_Neighbors2.setObjectName("lineEdit_Neighbors2")
        self.label_Neighbors2 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors2.setGeometry(QtCore.QRect(230, 90, 51, 21))
        self.label_Neighbors2.setObjectName("label_Neighbors2")
        self.label_Node3 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_Node3.setObjectName("label_Node3")
        self.comboBox_Node3 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node3.setGeometry(QtCore.QRect(110, 120, 111, 22))
        self.comboBox_Node3.setObjectName("comboBox_Node3")
        self.comboBox_Node3.addItem("")
        self.comboBox_Node3.addItem("")
        self.comboBox_Node3.addItem("")
        self.comboBox_Node3.addItem("")
        self.lineEdit_Neighbors3 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors3.setGeometry(QtCore.QRect(280, 120, 113, 20))
        self.lineEdit_Neighbors3.setObjectName("lineEdit_Neighbors3")
        self.label_Neighbors3 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors3.setGeometry(QtCore.QRect(230, 120, 51, 21))
        self.label_Neighbors3.setObjectName("label_Neighbors3")
        self.label_Node4 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node4.setGeometry(QtCore.QRect(20, 150, 81, 21))
        self.label_Node4.setObjectName("label_Node4")
        self.comboBox_Node4 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node4.setGeometry(QtCore.QRect(110, 150, 111, 22))
        self.comboBox_Node4.setObjectName("comboBox_Node4")
        self.comboBox_Node4.addItem("")
        self.comboBox_Node4.addItem("")
        self.comboBox_Node4.addItem("")
        self.comboBox_Node4.addItem("")
        self.lineEdit_Neighbors4 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors4.setGeometry(QtCore.QRect(280, 150, 113, 20))
        self.lineEdit_Neighbors4.setObjectName("lineEdit_Neighbors4")
        self.label_Neighbors4 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors4.setGeometry(QtCore.QRect(230, 150, 51, 21))
        self.label_Neighbors4.setObjectName("label_Neighbors4")
        self.label_Node5 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node5.setGeometry(QtCore.QRect(20, 180, 81, 21))
        self.label_Node5.setObjectName("label_Node5")
        self.comboBox_Node5 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node5.setGeometry(QtCore.QRect(110, 180, 111, 22))
        self.comboBox_Node5.setObjectName("comboBox_Node5")
        self.comboBox_Node5.addItem("")
        self.comboBox_Node5.addItem("")
        self.comboBox_Node5.addItem("")
        self.comboBox_Node5.addItem("")
        self.lineEdit_Neighbors5 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors5.setGeometry(QtCore.QRect(280, 180, 113, 20))
        self.lineEdit_Neighbors5.setObjectName("lineEdit_Neighbors5")
        self.label_Neighbors5 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors5.setGeometry(QtCore.QRect(230, 180, 51, 21))
        self.label_Neighbors5.setObjectName("label_Neighbors5")
        self.label_Node6 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node6.setGeometry(QtCore.QRect(20, 210, 81, 21))
        self.label_Node6.setObjectName("label_Node6")
        self.comboBox_Node6 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node6.setGeometry(QtCore.QRect(110, 210, 111, 22))
        self.comboBox_Node6.setObjectName("comboBox_Node6")
        self.comboBox_Node6.addItem("")
        self.comboBox_Node6.addItem("")
        self.comboBox_Node6.addItem("")
        self.comboBox_Node6.addItem("")
        self.lineEdit_Neighbors6 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors6.setGeometry(QtCore.QRect(280, 210, 113, 20))
        self.lineEdit_Neighbors6.setObjectName("lineEdit_Neighbors6")
        self.label_Neighbors6 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors6.setGeometry(QtCore.QRect(230, 210, 51, 21))
        self.label_Neighbors6.setObjectName("label_Neighbors6")
        self.label_Node7 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node7.setGeometry(QtCore.QRect(20, 240, 81, 21))
        self.label_Node7.setObjectName("label_Node7")
        self.comboBox_Node7 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node7.setGeometry(QtCore.QRect(110, 240, 111, 22))
        self.comboBox_Node7.setObjectName("comboBox_Node7")
        self.comboBox_Node7.addItem("")
        self.comboBox_Node7.addItem("")
        self.comboBox_Node7.addItem("")
        self.comboBox_Node7.addItem("")
        self.lineEdit_Neighbors7 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors7.setGeometry(QtCore.QRect(280, 240, 113, 20))
        self.lineEdit_Neighbors7.setObjectName("lineEdit_Neighbors7")
        self.label_Neighbors7 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors7.setGeometry(QtCore.QRect(230, 240, 51, 21))
        self.label_Neighbors7.setObjectName("label_Neighbors7")
        self.label_Node8 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node8.setGeometry(QtCore.QRect(20, 270, 81, 21))
        self.label_Node8.setObjectName("label_Node8")
        self.comboBox_Node8 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node8.setGeometry(QtCore.QRect(110, 270, 111, 22))
        self.comboBox_Node8.setObjectName("comboBox_Node8")
        self.comboBox_Node8.addItem("")
        self.comboBox_Node8.addItem("")
        self.comboBox_Node8.addItem("")
        self.comboBox_Node8.addItem("")
        self.lineEdit_Neighbors8 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors8.setGeometry(QtCore.QRect(280, 270, 113, 20))
        self.lineEdit_Neighbors8.setObjectName("lineEdit_Neighbors8")
        self.label_Neighbors8 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors8.setGeometry(QtCore.QRect(230, 270, 51, 21))
        self.label_Neighbors8.setObjectName("label_Neighbors8")
        self.label_Node9 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node9.setGeometry(QtCore.QRect(20, 300, 81, 21))
        self.label_Node9.setObjectName("label_Node9")
        self.comboBox_Node9 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node9.setGeometry(QtCore.QRect(110, 300, 111, 22))
        self.comboBox_Node9.setObjectName("comboBox_Node9")
        self.comboBox_Node9.addItem("")
        self.comboBox_Node9.addItem("")
        self.comboBox_Node9.addItem("")
        self.comboBox_Node9.addItem("")
        self.lineEdit_Neighbors9 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors9.setGeometry(QtCore.QRect(280, 300, 113, 20))
        self.lineEdit_Neighbors9.setObjectName("lineEdit_Neighbors9")
        self.label_Neighbors9 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors9.setGeometry(QtCore.QRect(230, 300, 51, 21))
        self.label_Neighbors9.setObjectName("label_Neighbors9")
        self.label_Node10 = QtWidgets.QLabel(self.NetDescription)
        self.label_Node10.setGeometry(QtCore.QRect(20, 330, 81, 21))
        self.label_Node10.setObjectName("label_Node10")
        self.comboBox_Node10 = QtWidgets.QComboBox(self.NetDescription)
        self.comboBox_Node10.setGeometry(QtCore.QRect(110, 330, 111, 22))
        self.comboBox_Node10.setObjectName("comboBox_Node10")
        self.comboBox_Node10.addItem("")
        self.comboBox_Node10.addItem("")
        self.comboBox_Node10.addItem("")
        self.comboBox_Node10.addItem("")
        self.lineEdit_Neighbors10 = QtWidgets.QLineEdit(self.NetDescription)
        self.lineEdit_Neighbors10.setGeometry(QtCore.QRect(280, 330, 113, 20))
        self.lineEdit_Neighbors10.setObjectName("lineEdit_Neighbors10")
        self.label_Neighbors10 = QtWidgets.QLabel(self.NetDescription)
        self.label_Neighbors10.setGeometry(QtCore.QRect(230, 330, 51, 21))
        self.label_Neighbors10.setObjectName("label_Neighbors10")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 21, 16))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 391, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.Psc = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Psc.setGeometry(QtCore.QRect(200, 40, 51, 22))
        self.Psc.setMaximum(1.0)
        self.Psc.setSingleStep(0.01)
        self.Psc.setObjectName("Psc")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(100, 40, 21, 16))
        self.label_15.setObjectName("label_15")
        self.Pps = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Pps.setGeometry(QtCore.QRect(40, 40, 51, 22))
        self.Pps.setMaximum(1.0)
        self.Pps.setSingleStep(0.01)
        self.Pps.setObjectName("Pps")
        self.Pcp = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Pcp.setGeometry(QtCore.QRect(280, 40, 51, 22))
        self.Pcp.setMaximum(1.0)
        self.Pcp.setSingleStep(0.01)
        self.Pcp.setObjectName("Pcp")
        self.Pci = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Pci.setGeometry(QtCore.QRect(360, 40, 51, 22))
        self.Pci.setMaximum(1.0)
        self.Pci.setSingleStep(0.01)
        self.Pci.setObjectName("Pci")
        self.Psp = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Psp.setGeometry(QtCore.QRect(120, 40, 51, 22))
        self.Psp.setMaximum(1.0)
        self.Psp.setSingleStep(0.01)
        self.Psp.setObjectName("Psp")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(180, 40, 21, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(260, 40, 21, 16))
        self.label_17.setObjectName("label_17")
        self.NetNodes = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.NetNodes.setGeometry(QtCore.QRect(160, 80, 41, 22))
        self.NetNodes.setMaximum(10)
        self.NetNodes.setObjectName("NetNodes")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 80, 141, 20))
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setGeometry(QtCore.QRect(340, 40, 21, 16))
        self.label_14.setObjectName("label_14")
        self.SaveConfig = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SaveConfig.setGeometry(QtCore.QRect(300, 80, 131, 31))
        self.SaveConfig.setObjectName("SaveConfig")
        self.CleanConfig = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CleanConfig.setGeometry(QtCore.QRect(220, 80, 61, 31))
        self.CleanConfig.setObjectName("CleanConfig")
        self.Inspect_T = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Inspect_T.setGeometry(QtCore.QRect(340, 500, 75, 23))
        self.Inspect_T.setObjectName("Inspect_T")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(330, 530, 72, 13))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Cshare = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.Cshare.setGeometry(QtCore.QRect(230, 550, 72, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Cshare.setFont(font)
        self.Cshare.setLineWidth(1)
        self.Cshare.setSmallDecimalPoint(False)
        self.Cshare.setDigitCount(6)
        self.Cshare.setMode(QtWidgets.QLCDNumber.Dec)
        self.Cshare.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Cshare.setProperty("value", 0.0)
        self.Cshare.setObjectName("Cshare")
        self.Sshare = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.Sshare.setGeometry(QtCore.QRect(130, 550, 72, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Sshare.setFont(font)
        self.Sshare.setLineWidth(1)
        self.Sshare.setSmallDecimalPoint(False)
        self.Sshare.setDigitCount(6)
        self.Sshare.setMode(QtWidgets.QLCDNumber.Dec)
        self.Sshare.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Sshare.setProperty("value", 0.0)
        self.Sshare.setObjectName("Sshare")
        self.Ishare = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.Ishare.setGeometry(QtCore.QRect(330, 550, 72, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Ishare.setFont(font)
        self.Ishare.setLineWidth(1)
        self.Ishare.setSmallDecimalPoint(False)
        self.Ishare.setDigitCount(6)
        self.Ishare.setMode(QtWidgets.QLCDNumber.Dec)
        self.Ishare.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Ishare.setProperty("value", 0.0)
        self.Ishare.setObjectName("Ishare")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(230, 530, 72, 13))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.Pshare = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.Pshare.setGeometry(QtCore.QRect(30, 550, 72, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Pshare.setFont(font)
        self.Pshare.setLineWidth(1)
        self.Pshare.setSmallDecimalPoint(False)
        self.Pshare.setDigitCount(6)
        self.Pshare.setMode(QtWidgets.QLCDNumber.Dec)
        self.Pshare.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Pshare.setProperty("value", 0.0)
        self.Pshare.setObjectName("Pshare")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(30, 500, 171, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(30, 530, 72, 13))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Specify_T = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.Specify_T.setGeometry(QtCore.QRect(220, 500, 101, 22))
        self.Specify_T.setMaximum(100)
        self.Specify_T.setObjectName("Specify_T")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(130, 530, 72, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.PaintStudyNet = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.PaintStudyNet.setGeometry(QtCore.QRect(20, 590, 131, 30))
        self.PaintStudyNet.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.PaintStudyNet.setFont(font)
        self.PaintStudyNet.setFocusPolicy(QtCore.Qt.TabFocus)
        self.PaintStudyNet.setAutoFillBackground(False)
        self.PaintStudyNet.setObjectName("PaintStudyNet")
        self.SpanBehavior = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SpanBehavior.setGeometry(QtCore.QRect(160, 590, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.SpanBehavior.setFont(font)
        self.SpanBehavior.setFocusPolicy(QtCore.Qt.TabFocus)
        self.SpanBehavior.setObjectName("SpanBehavior")
        self.SpotCriticalNodes = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SpotCriticalNodes.setGeometry(QtCore.QRect(300, 590, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        self.SpotCriticalNodes.setFont(font)
        self.SpotCriticalNodes.setFocusPolicy(QtCore.Qt.TabFocus)
        self.SpotCriticalNodes.setObjectName("SpotCriticalNodes")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MarkovInspector.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MarkovInspector)
        self.statusbar.setObjectName("statusbar")
        MarkovInspector.setStatusBar(self.statusbar)

        self.retranslateUi(MarkovInspector)
        QtCore.QMetaObject.connectSlotsByName(MarkovInspector)

    def retranslateUi(self, MarkovInspector):
        _translate = QtCore.QCoreApplication.translate
        MarkovInspector.setWindowTitle(_translate("MarkovInspector", "MarkovInspector v1.1"))
        self.NetDescription.setTitle(_translate("MarkovInspector", "Descripci??n de la red a estudiar"))
        self.Instructions.setText(_translate("MarkovInspector", "<html><head/><body><p>Por cada nodo, elija su estado f??ctico e ingrese los nodos con los que se comunica (valores separados por comas. Ej.: 0,1,2)</p></body></html>"))
        self.label_Node1.setText(_translate("MarkovInspector", "Nodo 1: Estado"))
        self.comboBox_Node1.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node1.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node1.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node1.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node1.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors1.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node2.setText(_translate("MarkovInspector", "Nodo 2: Estado"))
        self.comboBox_Node2.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node2.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node2.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node2.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node2.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors2.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node3.setText(_translate("MarkovInspector", "Nodo 3: Estado"))
        self.comboBox_Node3.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node3.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node3.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node3.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node3.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors3.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node4.setText(_translate("MarkovInspector", "Nodo 4: Estado"))
        self.comboBox_Node4.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node4.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node4.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node4.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node4.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors4.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node5.setText(_translate("MarkovInspector", "Nodo 5: Estado"))
        self.comboBox_Node5.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node5.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node5.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node5.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node5.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors5.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node6.setText(_translate("MarkovInspector", "Nodo 6: Estado"))
        self.comboBox_Node6.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node6.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node6.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node6.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node6.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors6.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node7.setText(_translate("MarkovInspector", "Nodo 7: Estado"))
        self.comboBox_Node7.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node7.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node7.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node7.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node7.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors7.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node8.setText(_translate("MarkovInspector", "Nodo 8: Estado"))
        self.comboBox_Node8.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node8.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node8.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node8.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node8.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors8.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node9.setText(_translate("MarkovInspector", "Nodo 9: Estado"))
        self.comboBox_Node9.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node9.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node9.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node9.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node9.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors9.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_Node10.setText(_translate("MarkovInspector", "Nodo 10: Estado"))
        self.comboBox_Node10.setCurrentText(_translate("MarkovInspector", "Protegido"))
        self.comboBox_Node10.setItemText(0, _translate("MarkovInspector", "Protegido"))
        self.comboBox_Node10.setItemText(1, _translate("MarkovInspector", "Susceptible"))
        self.comboBox_Node10.setItemText(2, _translate("MarkovInspector", "Comprometido"))
        self.comboBox_Node10.setItemText(3, _translate("MarkovInspector", "Irrecuperable"))
        self.label_Neighbors10.setText(_translate("MarkovInspector", "Vecinos:"))
        self.label_10.setText(_translate("MarkovInspector", "Pps"))
        self.label_9.setText(_translate("MarkovInspector", "Asigne las probabilidades de la cadena de Markov aqu??: "))
        self.label_15.setText(_translate("MarkovInspector", "Psp"))
        self.label_16.setText(_translate("MarkovInspector", "Psc"))
        self.label_17.setText(_translate("MarkovInspector", "Pcp"))
        self.label.setText(_translate("MarkovInspector", "N??mero de nodos de la red:"))
        self.label_14.setText(_translate("MarkovInspector", "Pci"))
        self.SaveConfig.setText(_translate("MarkovInspector", "Guardar Configuraci??n"))
        self.CleanConfig.setText(_translate("MarkovInspector", "Limpiar"))
        self.Inspect_T.setText(_translate("MarkovInspector", "Revisar"))
        self.label_7.setText(_translate("MarkovInspector", "Irrecuperable"))
        self.label_6.setText(_translate("MarkovInspector", "Comprometido"))
        self.label_8.setText(_translate("MarkovInspector", "Ver distribuci??n en el momento t ="))
        self.label_4.setText(_translate("MarkovInspector", "Protegido"))
        self.label_5.setText(_translate("MarkovInspector", "Susceptible"))
        self.PaintStudyNet.setText(_translate("MarkovInspector", "Visualizar \n"
"Red Configurada"))
        self.SpanBehavior.setText(_translate("MarkovInspector", "Analizar Comportamiento\n"
" de la Infecci??n"))
        self.SpotCriticalNodes.setText(_translate("MarkovInspector", "Identificar \n"
"Nodos Cr??ticos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarkovInspector = QtWidgets.QMainWindow()
    ui = Ui_MarkovInspector()
    ui.setupUi(MarkovInspector)
    MarkovInspector.show()
    sys.exit(app.exec_())
