# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 701)
        MainWindow.setWindowTitle("OpenMoldyn")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_model = QtWidgets.QWidget()
        self.tab_model.setObjectName("tab_model")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_model)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.paramsTreeWidget = QtWidgets.QTreeWidget(self.groupBox)
        self.paramsTreeWidget.setObjectName("paramsTreeWidget")
        self.horizontalLayout.addWidget(self.paramsTreeWidget)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 7)
        self.newModelBtn = QtWidgets.QToolButton(self.tab_model)
        self.newModelBtn.setObjectName("newModelBtn")
        self.gridLayout_2.addWidget(self.newModelBtn, 1, 0, 1, 1)
        self.loadModelBtn = QtWidgets.QToolButton(self.tab_model)
        self.loadModelBtn.setObjectName("loadModelBtn")
        self.gridLayout_2.addWidget(self.loadModelBtn, 1, 1, 1, 1)
        self.gotoSimuBtn = QtWidgets.QCommandLinkButton(self.tab_model)
        self.gotoSimuBtn.setEnabled(False)
        self.gotoSimuBtn.setObjectName("gotoSimuBtn")
        self.gridLayout_2.addWidget(self.gotoSimuBtn, 4, 0, 1, 7)
        self.saveModelBtn = QtWidgets.QToolButton(self.tab_model)
        self.saveModelBtn.setEnabled(False)
        self.saveModelBtn.setObjectName("saveModelBtn")
        self.gridLayout_2.addWidget(self.saveModelBtn, 1, 2, 1, 1)
        self.loadSimuBtn = QtWidgets.QToolButton(self.tab_model)
        self.loadSimuBtn.setObjectName("loadSimuBtn")
        self.gridLayout_2.addWidget(self.loadSimuBtn, 1, 6, 1, 1)
        self.tabWidget.addTab(self.tab_model, "")
        self.tab_simu = QtWidgets.QWidget()
        self.tab_simu.setEnabled(False)
        self.tab_simu.setObjectName("tab_simu")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_simu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progress_groupBox = QtWidgets.QGroupBox(self.tab_simu)
        self.progress_groupBox.setObjectName("progress_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.progress_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ETA = QtWidgets.QLabel(self.progress_groupBox)
        self.ETA.setObjectName("ETA")
        self.gridLayout_4.addWidget(self.ETA, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.progress_groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        self.simuProgressBar = QtWidgets.QProgressBar(self.progress_groupBox)
        self.simuProgressBar.setMaximum(1)
        self.simuProgressBar.setProperty("value", 0)
        self.simuProgressBar.setObjectName("simuProgressBar")
        self.gridLayout_4.addWidget(self.simuProgressBar, 1, 0, 1, 3)
        self.gridLayout_3.addWidget(self.progress_groupBox, 4, 0, 1, 2)
        self.simuBtn = QtWidgets.QCommandLinkButton(self.tab_simu)
        self.simuBtn.setObjectName("simuBtn")
        self.gridLayout_3.addWidget(self.simuBtn, 1, 1, 1, 1)
        self.gotoProcessBtn = QtWidgets.QCommandLinkButton(self.tab_simu)
        self.gotoProcessBtn.setEnabled(False)
        self.gotoProcessBtn.setObjectName("gotoProcessBtn")
        self.gridLayout_3.addWidget(self.gotoProcessBtn, 5, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.iterationsLabel = QtWidgets.QLabel(self.tab_simu)
        self.iterationsLabel.setObjectName("iterationsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iterationsLabel)
        self.iterationsSpinBox = QtWidgets.QSpinBox(self.tab_simu)
        self.iterationsSpinBox.setMaximum(210000766)
        self.iterationsSpinBox.setSingleStep(100)
        self.iterationsSpinBox.setProperty("value", 1000)
        self.iterationsSpinBox.setObjectName("iterationsSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iterationsSpinBox)
        self.simulationTimeLabel = QtWidgets.QLabel(self.tab_simu)
        self.simulationTimeLabel.setObjectName("simulationTimeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.simulationTimeLabel)
        self.simulationTimeLineEdit = QtWidgets.QLineEdit(self.tab_simu)
        self.simulationTimeLineEdit.setObjectName("simulationTimeLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.simulationTimeLineEdit)
        self.saveAllAtomsPositionLabel = QtWidgets.QLabel(self.tab_simu)
        self.saveAllAtomsPositionLabel.setObjectName("saveAllAtomsPositionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.saveAllAtomsPositionLabel)
        self.saveAllAtomsPositionCheckBox = QtWidgets.QCheckBox(self.tab_simu)
        self.saveAllAtomsPositionCheckBox.setObjectName("saveAllAtomsPositionCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.saveAllAtomsPositionCheckBox)
        self.gridLayout_3.addLayout(self.formLayout, 1, 0, 1, 1)
        self.temperature_groupBox = QtWidgets.QGroupBox(self.tab_simu)
        self.temperature_groupBox.setObjectName("temperature_groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.temperature_groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.designTemperatureBtn = QtWidgets.QPushButton(self.temperature_groupBox)
        self.designTemperatureBtn.setObjectName("designTemperatureBtn")
        self.horizontalLayout_6.addWidget(self.designTemperatureBtn)
        spacerItem1 = QtWidgets.QSpacerItem(522, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.temperature_groupBox, 2, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_simu)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 1, 1, 1, 1)
        self.RTViewBtn = QtWidgets.QToolButton(self.groupBox_3)
        self.RTViewBtn.setObjectName("RTViewBtn")
        self.gridLayout_6.addWidget(self.RTViewBtn, 1, 2, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.currentIterationLabel = QtWidgets.QLabel(self.groupBox_3)
        self.currentIterationLabel.setObjectName("currentIterationLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.currentIterationLabel)
        self.currentIteration = QtWidgets.QLabel(self.groupBox_3)
        self.currentIteration.setObjectName("currentIteration")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.currentIteration)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.currentTime = QtWidgets.QLabel(self.groupBox_3)
        self.currentTime.setObjectName("currentTime")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.currentTime)
        self.gridLayout_6.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab_simu, "")
        self.tab_processing = QtWidgets.QWidget()
        self.tab_processing.setEnabled(False)
        self.tab_processing.setObjectName("tab_processing")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_processing)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox2d = QtWidgets.QGroupBox(self.tab_processing)
        self.groupBox2d.setObjectName("groupBox2d")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox2d)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.surfListW = QtWidgets.QListWidget(self.groupBox2d)
        self.surfListW.setObjectName("surfListW")
        self.horizontalLayout_3.addWidget(self.surfListW)
        self.drawSurfButton = QtWidgets.QToolButton(self.groupBox2d)
        self.drawSurfButton.setObjectName("drawSurfButton")
        self.horizontalLayout_3.addWidget(self.drawSurfButton)
        self.gridLayout_5.addWidget(self.groupBox2d, 3, 0, 1, 2)
        self.groupBox_data_mgt = QtWidgets.QGroupBox(self.tab_processing)
        self.groupBox_data_mgt.setObjectName("groupBox_data_mgt")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_data_mgt)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 3, 1, 1)
        self.saveSimuBtn = QtWidgets.QToolButton(self.groupBox_data_mgt)
        self.saveSimuBtn.setObjectName("saveSimuBtn")
        self.gridLayout_7.addWidget(self.saveSimuBtn, 0, 2, 1, 1)
        self.saveRModelBtn = QtWidgets.QToolButton(self.groupBox_data_mgt)
        self.saveRModelBtn.setObjectName("saveRModelBtn")
        self.gridLayout_7.addWidget(self.saveRModelBtn, 0, 0, 1, 1)
        self.reuseModelBtn = QtWidgets.QToolButton(self.groupBox_data_mgt)
        self.reuseModelBtn.setObjectName("reuseModelBtn")
        self.gridLayout_7.addWidget(self.reuseModelBtn, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_data_mgt, 0, 0, 1, 2)
        self.groupBox1d_stat = QtWidgets.QGroupBox(self.tab_processing)
        self.groupBox1d_stat.setObjectName("groupBox1d_stat")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox1d_stat)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PDFButton = QtWidgets.QToolButton(self.groupBox1d_stat)
        self.PDFButton.setObjectName("PDFButton")
        self.horizontalLayout_5.addWidget(self.PDFButton)
        self.label = QtWidgets.QLabel(self.groupBox1d_stat)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.PDFNSpinBox = QtWidgets.QSpinBox(self.groupBox1d_stat)
        self.PDFNSpinBox.setMinimum(1)
        self.PDFNSpinBox.setMaximum(100000)
        self.PDFNSpinBox.setSingleStep(100)
        self.PDFNSpinBox.setProperty("value", 1000)
        self.PDFNSpinBox.setObjectName("PDFNSpinBox")
        self.horizontalLayout_5.addWidget(self.PDFNSpinBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox1d_stat)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.PDFDistSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox1d_stat)
        self.PDFDistSpinBox.setSingleStep(0.1)
        self.PDFDistSpinBox.setProperty("value", 1.5)
        self.PDFDistSpinBox.setObjectName("PDFDistSpinBox")
        self.horizontalLayout_5.addWidget(self.PDFDistSpinBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout_5.addWidget(self.groupBox1d_stat, 1, 0, 1, 2)
        self.groupBox1d = QtWidgets.QGroupBox(self.tab_processing)
        self.groupBox1d.setObjectName("groupBox1d")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox1d)
        self.gridLayout.setObjectName("gridLayout")
        self.lineListW = QtWidgets.QListWidget(self.groupBox1d)
        self.lineListW.setObjectName("lineListW")
        self.gridLayout.addWidget(self.lineListW, 0, 0, 2, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.asAFunctionOfLabel = QtWidgets.QLabel(self.groupBox1d)
        self.asAFunctionOfLabel.setObjectName("asAFunctionOfLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.asAFunctionOfLabel)
        self.lineComboW = QtWidgets.QComboBox(self.groupBox1d)
        self.lineComboW.setObjectName("lineComboW")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineComboW)
        self.plotB = QtWidgets.QPushButton(self.groupBox1d)
        self.plotB.setObjectName("plotB")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plotB)
        self.gridLayout.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox1d, 2, 0, 1, 1)
        self.groupBox_1doptions = QtWidgets.QGroupBox(self.tab_processing)
        self.groupBox_1doptions.setObjectName("groupBox_1doptions")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_1doptions)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.list1DOptions = QtWidgets.QListWidget(self.groupBox_1doptions)
        self.list1DOptions.setObjectName("list1DOptions")
        self.horizontalLayout_4.addWidget(self.list1DOptions)
        self.gridLayout_5.addWidget(self.groupBox_1doptions, 2, 1, 1, 1)
        self.groupBoxMovie = QtWidgets.QGroupBox(self.tab_processing)
        self.groupBoxMovie.setObjectName("groupBoxMovie")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBoxMovie)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.fPSLabel = QtWidgets.QLabel(self.groupBoxMovie)
        self.fPSLabel.setObjectName("fPSLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fPSLabel)
        self.FPSSpinBox = QtWidgets.QSpinBox(self.groupBoxMovie)
        self.FPSSpinBox.setProperty("value", 24)
        self.FPSSpinBox.setObjectName("FPSSpinBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FPSSpinBox)
        self.stepsByFrameLabel = QtWidgets.QLabel(self.groupBoxMovie)
        self.stepsByFrameLabel.setObjectName("stepsByFrameLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stepsByFrameLabel)
        self.stepsByFrameSpinBox = QtWidgets.QSpinBox(self.groupBoxMovie)
        self.stepsByFrameSpinBox.setProperty("value", 10)
        self.stepsByFrameSpinBox.setObjectName("stepsByFrameSpinBox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stepsByFrameSpinBox)
        self.gridLayout_8.addLayout(self.formLayout_4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 1, 1, 1)
        self.makeMovieBtn = QtWidgets.QToolButton(self.groupBoxMovie)
        self.makeMovieBtn.setObjectName("makeMovieBtn")
        self.gridLayout_8.addWidget(self.makeMovieBtn, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBoxMovie, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab_processing, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen_model = QtWidgets.QAction(MainWindow)
        self.actionOpen_model.setObjectName("actionOpen_model")
        self.actionNew_simulation = QtWidgets.QAction(MainWindow)
        self.actionNew_simulation.setObjectName("actionNew_simulation")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Current model"))
        self.paramsTreeWidget.headerItem().setText(0, _translate("MainWindow", "Property"))
        self.paramsTreeWidget.headerItem().setText(1, _translate("MainWindow", "Value"))
        self.paramsTreeWidget.headerItem().setText(2, _translate("MainWindow", "Unit"))
        self.newModelBtn.setText(_translate("MainWindow", "New"))
        self.loadModelBtn.setText(_translate("MainWindow", "Load"))
        self.gotoSimuBtn.setText(_translate("MainWindow", "Simulation"))
        self.saveModelBtn.setText(_translate("MainWindow", "Save"))
        self.loadSimuBtn.setText(_translate("MainWindow", "Load simulation history"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_model), _translate("MainWindow", "Model"))
        self.progress_groupBox.setTitle(_translate("MainWindow", "Progress"))
        self.ETA.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "ETA : "))
        self.simuProgressBar.setFormat(_translate("MainWindow", "%v/%m"))
        self.simuBtn.setText(_translate("MainWindow", "Launch simulation"))
        self.gotoProcessBtn.setText(_translate("MainWindow", "Process data"))
        self.iterationsLabel.setText(_translate("MainWindow", "Iterations"))
        self.simulationTimeLabel.setText(_translate("MainWindow", "Simulation time (s)"))
        self.saveAllAtomsPositionLabel.setText(_translate("MainWindow", "Save all atoms position"))
        self.temperature_groupBox.setTitle(_translate("MainWindow", "Temperature control"))
        self.designTemperatureBtn.setText(_translate("MainWindow", "Design"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Current state"))
        self.RTViewBtn.setText(_translate("MainWindow", "View current state"))
        self.currentIterationLabel.setText(_translate("MainWindow", "Current iteration : "))
        self.currentIteration.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Current time (s) : "))
        self.currentTime.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_simu), _translate("MainWindow", "Simulation"))
        self.groupBox2d.setTitle(_translate("MainWindow", "2D graphics"))
        self.drawSurfButton.setText(_translate("MainWindow", "Draw"))
        self.groupBox_data_mgt.setTitle(_translate("MainWindow", "Data management"))
        self.saveSimuBtn.setText(_translate("MainWindow", "Save simulation history"))
        self.saveRModelBtn.setText(_translate("MainWindow", "Save resulting model"))
        self.reuseModelBtn.setText(_translate("MainWindow", "New simulation with resulting model"))
        self.groupBox1d_stat.setTitle(_translate("MainWindow", "Static 1D graphics"))
        self.PDFButton.setText(_translate("MainWindow", "Pair Distribution Function"))
        self.label.setText(_translate("MainWindow", "Number of atoms :"))
        self.label_2.setText(_translate("MainWindow", "Maximum distance (times r_cut) :"))
        self.groupBox1d.setTitle(_translate("MainWindow", "1D graphics"))
        self.asAFunctionOfLabel.setText(_translate("MainWindow", "as a function of"))
        self.plotB.setText(_translate("MainWindow", "Plot"))
        self.groupBox_1doptions.setTitle(_translate("MainWindow", "1D options"))
        self.groupBoxMovie.setTitle(_translate("MainWindow", "Movie"))
        self.fPSLabel.setText(_translate("MainWindow", "FPS"))
        self.stepsByFrameLabel.setText(_translate("MainWindow", "Steps by frame"))
        self.makeMovieBtn.setText(_translate("MainWindow", "Make movie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_processing), _translate("MainWindow", "Processing"))
        self.actionNew.setText(_translate("MainWindow", "New model"))
        self.actionOpen_model.setText(_translate("MainWindow", "Open model"))
        self.actionNew_simulation.setText(_translate("MainWindow", "New simulation"))

