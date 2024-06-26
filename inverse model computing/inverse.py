import os
import matplotlib.pyplot as plt
import numpy as np
import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert
import pybert as pb
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 597)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "QTabBar::tab:selected {\n"
            "    background: lightblue;\n"
            "    color: black;\n"
            "}\n"
            "QTabBar::tab:!selected {\n"
            "    background: lightgray;\n"
            "    color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.verticalWidget.setObjectName("verticalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalWidget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(781, 571))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.Importing = QtWidgets.QWidget()
        self.Importing.setObjectName("Importing")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Importing)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Importing)
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "border-top-color: rgb(0, 0, 0);"
        )
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.gridLayout = QtWidgets.QGridLayout(self.Data)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.Data)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.Data)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.Data)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.Data, "")
        self.Pre_processing = QtWidgets.QWidget()
        self.Pre_processing.setObjectName("Pre_processing")
        self.pushButton_2 = QtWidgets.QPushButton(self.Pre_processing)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView = QtWidgets.QListView(self.Pre_processing)
        self.listView.setGeometry(QtCore.QRect(20, 50, 711, 431))
        self.listView.setObjectName("listView")
        self.tabWidget_2.addTab(self.Pre_processing, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.Importing, "")
        self.Domain_Mesh = QtWidgets.QWidget()
        self.Domain_Mesh.setObjectName("Domain_Mesh")
        self.pushButton_4 = QtWidgets.QPushButton(self.Domain_Mesh)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 50, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.Domain_Mesh)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 110, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.listView_2 = QtWidgets.QListView(self.Domain_Mesh)
        self.listView_2.setGeometry(QtCore.QRect(30, 180, 701, 361))
        self.listView_2.setObjectName("listView_2")
        self.layoutWidget = QtWidgets.QWidget(self.Domain_Mesh)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 15, 730, 154))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout.addWidget(self.textEdit_3)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.spinBox_3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.spinBox_4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout.addWidget(self.spinBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_3.addWidget(self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.horizontalLayout_3.addWidget(self.textEdit_5)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox)
        self.textEdit_6 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_6.setObjectName("textEdit_6")
        self.horizontalLayout_3.addWidget(self.textEdit_6)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.Domain_Mesh, "")

        self.label_start = QtWidgets.QLabel(MainWindow)  

        self.Inversion = QtWidgets.QWidget()
        self.Inversion.setObjectName("Inversion")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Inversion)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 411, 73))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_8 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_8.setObjectName("textEdit_8")
        self.horizontalLayout_4.addWidget(self.textEdit_8)

        """Max iteration of Inversion """
        self.spinBox_8 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_4.addWidget(self.spinBox_8)
 
        self.spinBox_8.setMinimum(5)
        self.spinBox_8.setMaximum(30)

        self.textEdit_9 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_9.setObjectName("textEdit_9")
        self.horizontalLayout_4.addWidget(self.textEdit_9)

        """Lambda of inversion"""
        self.spinBox_11 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_11.setObjectName("spinBox_11")
        self.horizontalLayout_4.addWidget(self.spinBox_11)

        self.spinBox_11.setMinimum(5)
        self.spinBox_11.setMaximum(30)

        self.textEdit_10 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_10.setObjectName("textEdit_10")
        self.horizontalLayout_4.addWidget(self.textEdit_10)

        """DPhi of inversion"""
        self.spinBox_10 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_10.setObjectName("spinBox_10")
        self.horizontalLayout_4.addWidget(self.spinBox_10)

        self.spinBox_10.setMinimum(1)
        self.spinBox_10.setMaximum(10)

        text_boxes = [self.textEdit_8, self.textEdit_9, self.textEdit_10]
        for text_box in text_boxes:
            text_box.setReadOnly(True)
            text_box.setStyleSheet("QTextEdit { text-align: center; }")
            text_box.setFixedHeight(30)

        """ Pushbutton_5 is the Apply of Inversion"""
        self.pushButton_5 = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 10, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setToolTip(
            "Start inverting the imported data to generate the soil resistivity distribution map <br> after choosing the value for each parameter of inversion algorithm."
        )

        """ New added inversion function"""
        self.pushButton_5.clicked.connect(self.startInversion)

        """Pushbutton_9 is the Save of Inversion"""
        self.pushButton_9 = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 60, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setToolTip(
            "Save the inverted soil resistivity distribution map.<br>"
        )
        self.pushButton_9.clicked.connect(self.saveFig)
        self.listView_3 = QtWidgets.QListView(self.Inversion)
        self.listView_3.setGeometry(QtCore.QRect(30, 110, 711, 431))
        self.listView_3.setObjectName("listView_3")
        self.inversion_result_widget = QtWidgets.QWidget(self.Inversion)

        """Embed the generated pics in the main window"""
        self.inversion_result_widget.setGeometry(
            QtCore.QRect(0, 100, 711, 431)
        )  
        self.inversion_result_widget.setObjectName("inversion_result_widget")
        self.inversion_result_layout = QtWidgets.QVBoxLayout(
            self.inversion_result_widget
        )
        self.inversion_result_layout.setObjectName("inversion_result_layout")
        self.tabWidget.addTab(self.Inversion, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_11 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_11.setGeometry(QtCore.QRect(0, 10, 111, 31))
        self.textEdit_11.setObjectName("textEdit_11")
        self.listView_6 = QtWidgets.QListView(self.tab_5)
        self.listView_6.setGeometry(QtCore.QRect(0, 60, 711, 431))
        self.listView_6.setObjectName("listView_6")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(120, 10, 71, 31))
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setProperty("value", 25.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(200, 10, 81, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget.addTab(self.tab_5, "")
        self.visualisation = QtWidgets.QWidget()
        self.visualisation.setObjectName("visualisation")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.visualisation)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.visualisation)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.Resistivity = QtWidgets.QWidget()
        self.Resistivity.setObjectName("Resistivity")
        self.pushButton_7 = QtWidgets.QPushButton(self.Resistivity)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 10, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.Resistivity)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 10, 111, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.listView_4 = QtWidgets.QListView(self.Resistivity)
        self.listView_4.setGeometry(QtCore.QRect(30, 50, 711, 431))
        self.listView_4.setObjectName("listView_4")
        self.tabWidget_3.addTab(self.Resistivity, "")
        self.Water_content = QtWidgets.QWidget()
        self.Water_content.setObjectName("Water_content")
        self.pushButton_6 = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 10, 81, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 10, 71, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.listView_5 = QtWidgets.QListView(self.Water_content)
        self.listView_5.setGeometry(QtCore.QRect(20, 50, 711, 431))
        self.listView_5.setObjectName("listView_5")
        self.tabWidget_3.addTab(self.Water_content, "")
        self.horizontalLayout_5.addWidget(self.tabWidget_3)
        self.tabWidget.addTab(self.visualisation, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionGuidline = QtWidgets.QAction(MainWindow)
        self.actionGuidline.setObjectName("actionGuidline")
        self.actionContract = QtWidgets.QAction(MainWindow)
        self.actionContract.setObjectName("actionContract")
        self.menuProject.addAction(self.actionNew)
        self.menuProject.addAction(self.actionOpen)
        self.menuProject.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionGuidline)
        self.menuHelp.addAction(self.actionContract)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def startInversion(self):
        # Read the values from the spin boxes
        maxIter = self.spinBox_8.value()
        lam = self.spinBox_11.value()
        dPhi = self.spinBox_10.value()

        file_to_convert = "./2022-07-03_09-00-00.txt"

        # Create Geometry and Mesh
        geom = mt.createWorld(start=[0, 0], end=[47, -8], worldMarker=False)
        mesh = mt.createMesh(geom, quality=33.5, area=0.5, smooth=True)
        mesh.save("mesh.bms")

        # Inversion preparing
        date = os.path.basename(file_to_convert)  
        mgr = ert.ERTManager(file_to_convert, verbose=True, debug=True)
        rhoa = np.array(mgr.data["rhoa"])
        Argw = np.argwhere(rhoa <= 0)
        pg.info("Filtered rhoa (min/max)", min(mgr.data["rhoa"]), max(mgr.data["rhoa"]))
        Accur = (1 - np.shape(Argw)[0] / np.shape(rhoa)[0]) * 100

        # Data processing Filter negative value
        mgr.data.remove(mgr.data["rhoa"] < 0)

        # Add estimated Error and geometrical factor
        mgr.data["err"] = ert.estimateError(
            mgr.data, absoluteError=0.001, relativeError=0.03
        )
        pg.info("Filtered rhoa (min/max)", min(mgr.data["rhoa"]), max(mgr.data["rhoa"]))
        mgr.data["k"] = ert.createGeometricFactors(mgr.data, numerical=True)

        # Inversion here
        tolerance = (
            1  # Abort criterion for chi2 (chi-squared) for an inversion process.
        )
        for iteration in range(maxIter):
            inv = mgr.invert(
                mesh=mesh, lam=lam, maxIter=1, dPhi=dPhi, CHI1OPT=5, Verbose=True
            )
            chi2 = inv.chi2()  

            # Check if chi2 is below the tolerance level
            if chi2 < tolerance:
                pg.info(f"Inversion converged at iteration {iteration}. Chi2: {chi2}")
                break

        # Storing and saving data for later manipulation
        Storage = np.zeros([np.shape(mesh.cellMarkers())[0], 1])
        Storage[:, 0] = inv
        mgr.saveResult(date[:-4])

        # Plotting
        fig1, (ax1) = plt.subplots(1, sharex=True, figsize=(16.0, 5))
        mgr.showResult(ax=ax1, cMin=50, cMax=15000)
        labels = date
        ax1.set_xlim(0, mgr.paraDomain.xmax())
        ax1.set_ylim(-8, mgr.paraDomain.ymax())
        ax1.set_title(labels)
        plt.tight_layout()

        self.canvas = FigureCanvas(
            fig1
        )  
        self.inversion_result_layout.addWidget(self.canvas)

        self.inversion_result_widget.update()
        self.fig1 = fig1

    def saveFig(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save Figure", "", "PNG Files (*.png);;All Files (*)", options=options
        )

        if file_name:
            self.fig1.savefig(
                file_name, format="png"
            )  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Import"))
        self.pushButton.setText(_translate("MainWindow", "Choose your file"))
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.Data), _translate("MainWindow", "Data")
        )
        self.pushButton_2.setText(_translate("MainWindow", "Clean Data"))
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.Pre_processing),
            _translate("MainWindow", "Pre_processing"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Importing),
            _translate("MainWindow", "Importing"),
        )
        self.pushButton_4.setText(_translate("MainWindow", "Apply"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.textEdit_3.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:9pt;">Geometry:</span></p></body></html>',
            )
        )
        self.textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:9pt;">start</span></p></body></html>',
            )
        )
        self.textEdit_2.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:9pt;">end</span></p></body></html>',
            )
        )
        self.textEdit_4.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:9pt;">Mesh:</span></p></body></html>',
            )
        )
        self.textEdit_5.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:9pt;">Quality</span></p></body></html>',
            )
        )
        self.textEdit_6.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:9pt;">Area</span></p></body></html>',
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Domain_Mesh),
            _translate("MainWindow", "Domain and Mesh"),
        )
        self.textEdit_8.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:12pt;">Iterations</span></p></body></html>',
            )
        )
        self.textEdit_8.setToolTip(
            "Maximum number of iterations for the inversion algorithm.<br>"
        )
        self.textEdit_9.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:12pt;">Lambda</span></p></body></html>',
            )
        )
        self.textEdit_9.setToolTip(
            "Lambda controls the smoothness of the inverted model.<br> It helps prevent overfitting by penalizing complex models."
        )

        self.textEdit_10.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'SimSun\'; font-size:12pt;">dPhi</span></p></body></html>',
            )
        )
        self.textEdit_10.setToolTip(
            "Delta Phi determines the allowable change in resistivity between neighboring cells in the model.<br>"
        )

        self.pushButton_5.setText(_translate("MainWindow", "Apply"))
        self.pushButton_9.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Inversion),
            _translate("MainWindow", "Inversion"),
        )
        self.textEdit_11.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Temperature</p></body></html>',
            )
        )
        self.pushButton_12.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            _translate("MainWindow", "Water Content"),
        )
        self.pushButton_7.setText(_translate("MainWindow", "Result"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.Resistivity),
            _translate("MainWindow", "Resistivity"),
        )
        self.pushButton_6.setText(_translate("MainWindow", "Convert"))
        self.pushButton_11.setText(_translate("MainWindow", "Save"))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.Water_content),
            _translate("MainWindow", "Water content"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.visualisation),
            _translate("MainWindow", "visualisation"),
        )
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionGuidline.setText(_translate("MainWindow", "Guidline"))
        self.actionContract.setText(_translate("MainWindow", "Contract"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
