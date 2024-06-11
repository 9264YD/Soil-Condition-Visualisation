import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QTimer
import imageio

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 753)
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
        self.verticalWidget.setGeometry(QtCore.QRect(10, 0, 961, 721))
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
        self.layoutWidget.setGeometry(QtCore.QRect(19, 15, 730, 187))
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
        self.Inversion = QtWidgets.QWidget()
        self.Inversion.setObjectName("Inversion")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Inversion)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 436, 89))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_8 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_8.setObjectName("textEdit_8")
        self.horizontalLayout_4.addWidget(self.textEdit_8)
        self.spinBox_8 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_4.addWidget(self.spinBox_8)
        self.textEdit_9 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_9.setObjectName("textEdit_9")
        self.horizontalLayout_4.addWidget(self.textEdit_9)
        self.spinBox_11 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_11.setObjectName("spinBox_11")
        self.horizontalLayout_4.addWidget(self.spinBox_11)
        self.textEdit_10 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_10.setObjectName("textEdit_10")
        self.horizontalLayout_4.addWidget(self.textEdit_10)
        self.spinBox_10 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_10.setObjectName("spinBox_10")
        self.horizontalLayout_4.addWidget(self.spinBox_10)
        self.pushButton_5 = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 10, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 60, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.listView_3 = QtWidgets.QListView(self.Inversion)
        self.listView_3.setGeometry(QtCore.QRect(30, 110, 711, 431))
        self.listView_3.setObjectName("listView_3")
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

        self.Visualization = QtWidgets.QWidget()
        self.Visualization.setObjectName("Visualization")
        self.horizontalLayout_Vis_5 = QtWidgets.QHBoxLayout(self.Visualization)
        self.horizontalLayout_Vis_5.setObjectName("horizontalLayout_Vis_5")
        self.tabWidget_Vis = QtWidgets.QTabWidget(self.Visualization)
        self.tabWidget_Vis.setObjectName("tabWidget_Vis")

        self.Resistivity_Vis_Res = QtWidgets.QWidget()
        self.Resistivity_Vis_Res.setObjectName("Resistivity_Vis_Res")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Resistivity_Vis_Res)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout_Vis_Res = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget
        )
        self.horizontalLayout_Vis_Res.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Res.setObjectName("horizontalLayout_Vis_Res")

        self.radioButton_Vis_Res_cSche = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget
        )
        self.radioButton_Vis_Res_cSche.setObjectName("radioButton_Vis_Res_cSche")
        self.horizontalLayout_Vis_Res.addWidget(self.radioButton_Vis_Res_cSche)

        self.radioButton_Vis_Res_cSca = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget
        )
        self.radioButton_Vis_Res_cSca.setObjectName("radioButton_Vis_Res_cSca")
        self.horizontalLayout_Vis_Res.addWidget(self.radioButton_Vis_Res_cSca)

        self.radioButton_Vis_Res_Ani = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget
        )
        self.radioButton_Vis_Res_Ani.setObjectName("radioButton_Vis_Res_Ani")
        self.horizontalLayout_Vis_Res.addWidget(self.radioButton_Vis_Res_Ani)

        self.stackedWidget_Vis_Res_stackedWidget = QtWidgets.QStackedWidget(
            self.Resistivity_Vis_Res
        )
        self.stackedWidget_Vis_Res_stackedWidget.setGeometry(
            QtCore.QRect(0, 40, 891, 551)
        )

        self.stackedWidget_Vis_Res_stackedWidget.setObjectName(
            "stackedWidget_Vis_Res_stackedWidget"
        )
        self.page_Vis_Res_cSche = QtWidgets.QWidget()
        self.page_Vis_Res_cSche.setObjectName("page_Vis_Res_cSche")

        self.verticalLayoutWidget_22 = QtWidgets.QWidget(self.page_Vis_Res_cSche)
        self.verticalLayoutWidget_22.setGeometry(QtCore.QRect(0, 0, 231, 551))
        self.verticalLayoutWidget_22.setObjectName("verticalLayoutWidget_22")
        self.verticalLayout_Vis_Res_cSche = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_22
        )
        self.verticalLayout_Vis_Res_cSche.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Vis_Res_cSche.setObjectName("verticalLayout_Vis_Res_cSche")

        self.label_Vis_Res_fSele = QtWidgets.QLabel(self.verticalLayoutWidget_22)
        self.label_Vis_Res_fSele.setObjectName("label_Vis_Res_fSele")

        self.verticalLayout_Vis_Res_cSche.addWidget(self.label_Vis_Res_fSele)
        self.listWidget_Vis_Res_cSche_fSele = QtWidgets.QListWidget(
            self.verticalLayoutWidget_22
        )
        self.listWidget_Vis_Res_cSche_fSele.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget_Vis_Res_cSche_fSele.setObjectName(
            "listWidget_Vis_Res_cSche_fSele"
        )
        self.verticalLayout_Vis_Res_cSche.addWidget(self.listWidget_Vis_Res_cSche_fSele)
        
        self.label_Vis_Res_cSche_cSche = QtWidgets.QLabel(self.verticalLayoutWidget_22)
        self.label_Vis_Res_cSche_cSche.setObjectName("label_Vis_Res_cSche_cSche")

        self.verticalLayout_Vis_Res_cSche.addWidget(self.label_Vis_Res_cSche_cSche)
        self.listWidget_Vis_Res_cSche_cSche = QtWidgets.QListWidget(
            self.verticalLayoutWidget_22
        )
        self.listWidget_Vis_Res_cSche_cSche.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.listWidget_Vis_Res_cSche_cSche.setObjectName(
            "listWidget_Vis_Res_cSche_cSche"
        )
        self.verticalLayout_Vis_Res_cSche.addWidget(self.listWidget_Vis_Res_cSche_cSche)

        self.pushButton_Vis_Res_cSche_Apply = QtWidgets.QPushButton(
            self.verticalLayoutWidget_22
        )
        self.pushButton_Vis_Res_cSche_Apply.setObjectName(
            "pushButton_Vis_Res_cSche_Apply"
        )
        self.verticalLayout_Vis_Res_cSche.addWidget(self.pushButton_Vis_Res_cSche_Apply)

        self.graphicsView_Vis_Res_cSche_Disp = QtWidgets.QGraphicsView(
            self.page_Vis_Res_cSche
        )
        self.graphicsView_Vis_Res_cSche_Disp.setGeometry(
            QtCore.QRect(250, 20, 641, 501)
        )
        self.graphicsView_Vis_Res_cSche_Disp.setObjectName(
            "graphicsView_Vis_Res_cSche_Disp"
        )

        self.horizontalLayoutWidget_25 = QtWidgets.QWidget(self.page_Vis_Res_cSche)
        self.horizontalLayoutWidget_25.setGeometry(QtCore.QRect(630, 520, 261, 31))
        self.horizontalLayoutWidget_25.setObjectName("horizontalLayoutWidget_25")
        self.horizontalLayout_Vis_Res_cSche = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_25
        )
        self.horizontalLayout_Vis_Res_cSche.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Res_cSche.setObjectName(
            "horizontalLayout_Vis_Res_cSche"
        )

        self.pushButton_Vis_Res_cSche_Replay = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_25
        )
        self.pushButton_Vis_Res_cSche_Replay.setObjectName(
            "pushButton_Vis_Res_cSche_Replay"
        )
        self.horizontalLayout_Vis_Res_cSche.addWidget(
            self.pushButton_Vis_Res_cSche_Replay
        )

        self.pushButton_Vis_Res_cSche_Save = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_25
        )
        self.pushButton_Vis_Res_cSche_Save.setObjectName(
            "pushButton_Vis_Res_cSche_Save"
        )
        self.horizontalLayout_Vis_Res_cSche.addWidget(
            self.pushButton_Vis_Res_cSche_Save
        )

        self.stackedWidget_Vis_Res_stackedWidget.addWidget(self.page_Vis_Res_cSche)
        self.page_Vis_Res_cSca = QtWidgets.QWidget()
        self.page_Vis_Res_cSca.setObjectName("page_Vis_Res_cSca")

        self.graphicsView_Vis_Res_cSca_Disp = QtWidgets.QGraphicsView(
            self.page_Vis_Res_cSca
        )
        self.graphicsView_Vis_Res_cSca_Disp.setGeometry(QtCore.QRect(250, 20, 641, 501))
        self.graphicsView_Vis_Res_cSca_Disp.setObjectName(
            "graphicsView_Vis_Res_cSca_Disp"
        )

        self.verticalLayoutWidget_23 = QtWidgets.QWidget(self.page_Vis_Res_cSca)
        self.verticalLayoutWidget_23.setGeometry(QtCore.QRect(0, 0, 231, 541))
        self.verticalLayoutWidget_23.setObjectName("verticalLayoutWidget_23")
        self.verticalLayout_Vis_Res_cSca = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_23
        )
        self.verticalLayout_Vis_Res_cSca.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Vis_Res_cSca.setObjectName("verticalLayout_Vis_Res_cSca")
        
        self.label_Vis_Res_cSca_fSele = QtWidgets.QLabel(self.verticalLayoutWidget_23)
        self.label_Vis_Res_cSca_fSele.setObjectName("label_Vis_Res_cSca_fSele")
      
        self.verticalLayout_Vis_Res_cSca.addWidget(self.label_Vis_Res_cSca_fSele)
        self.listWidget_Vis_Res_cSca_fSele = QtWidgets.QListWidget(
            self.verticalLayoutWidget_23
        )
        self.listWidget_Vis_Res_cSca_fSele.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget_Vis_Res_cSca_fSele.setObjectName(
            "listWidget_Vis_Res_cSca_fSele"
        )
        self.verticalLayout_Vis_Res_cSca.addWidget(self.listWidget_Vis_Res_cSca_fSele)

        self.label_Vis_Res_cSca_cSca = QtWidgets.QLabel(self.verticalLayoutWidget_23)
        self.label_Vis_Res_cSca_cSca.setObjectName("label_Vis_Res_cSca_cSca")

        self.verticalLayout_Vis_Res_cSca.addWidget(self.label_Vis_Res_cSca_cSca)
        self.listWidget_Vis_Res_cSca_cSca = QtWidgets.QListWidget(
            self.verticalLayoutWidget_23
        )
        self.listWidget_Vis_Res_cSca_cSca.setObjectName("listWidget_Vis_Res_cSca_cSca")

        self.verticalLayout_Vis_Res_cSca.addWidget(self.listWidget_Vis_Res_cSca_cSca)
        self.pushButton_Vis_Res_cSca_Apply = QtWidgets.QPushButton(
            self.verticalLayoutWidget_23
        )
        self.pushButton_Vis_Res_cSca_Apply.setObjectName(
            "pushButton_Vis_Res_cSca_Apply"
        )
        self.verticalLayout_Vis_Res_cSca.addWidget(self.pushButton_Vis_Res_cSca_Apply)

        self.horizontalLayoutWidget_29 = QtWidgets.QWidget(self.page_Vis_Res_cSca)
        self.horizontalLayoutWidget_29.setGeometry(QtCore.QRect(630, 520, 261, 31))
        self.horizontalLayoutWidget_29.setObjectName("horizontalLayoutWidget_29")
        self.horizontalLayout_Vis_Res_cSca = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_29
        )
        self.horizontalLayout_Vis_Res_cSca.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Res_cSca.setObjectName(
            "horizontalLayout_Vis_Res_cSca"
        )
        
        self.pushButton_Vis_Res_cSca_Replay = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_29
        )
        self.pushButton_Vis_Res_cSca_Replay.setObjectName(
            "pushButton_Vis_Res_cSca_Replay"
        )
        self.horizontalLayout_Vis_Res_cSca.addWidget(
            self.pushButton_Vis_Res_cSca_Replay
        )
        
        self.pushButton_Vis_Res_cSca_Save = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_29
        )
        self.pushButton_Vis_Res_cSca_Save.setObjectName("pushButton_Vis_Res_cSca_Save")
        self.horizontalLayout_Vis_Res_cSca.addWidget(self.pushButton_Vis_Res_cSca_Save)
        self.stackedWidget_Vis_Res_stackedWidget.addWidget(self.page_Vis_Res_cSca)

        self.page_Vis_Res_Ani = QtWidgets.QWidget()
        self.page_Vis_Res_Ani.setObjectName("page_Vis_Res_Ani")
        
        self.verticalLayoutWidget_26 = QtWidgets.QWidget(self.page_Vis_Res_Ani)
        self.verticalLayoutWidget_26.setGeometry(QtCore.QRect(0, 0, 231, 551))
        self.verticalLayoutWidget_26.setObjectName("verticalLayoutWidget_26")
        
        self.verticalLayout_Vis_Res_Ani = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_26
        )
        self.verticalLayout_Vis_Res_Ani.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Vis_Res_Ani.setObjectName("verticalLayout_Vis_Res_Ani")
        
        self.label_Vis_Res_Ani_fSele = QtWidgets.QLabel(self.verticalLayoutWidget_26)
        self.label_Vis_Res_Ani_fSele.setObjectName("label_Vis_Res_Ani_fSele")
        self.verticalLayout_Vis_Res_Ani.addWidget(self.label_Vis_Res_Ani_fSele)
        
        self.listWidget_Vis_Res_Ani_fSele = QtWidgets.QListWidget(
            self.verticalLayoutWidget_26
        )
        self.listWidget_Vis_Res_Ani_fSele.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget_Vis_Res_Ani_fSele.setObjectName("listWidget_Vis_Res_Ani_fSele")
        self.verticalLayout_Vis_Res_Ani.addWidget(self.listWidget_Vis_Res_Ani_fSele)

        self.pushButton_Vis_Res_Ani_Apply = QtWidgets.QPushButton(
            self.verticalLayoutWidget_26
        )
        self.pushButton_Vis_Res_Ani_Apply.setObjectName("pushButton_Vis_Res_Ani_Apply")
        self.verticalLayout_Vis_Res_Ani.addWidget(self.pushButton_Vis_Res_Ani_Apply)

        self.graphicsView_Vis_Res_Ani_Disp = QtWidgets.QGraphicsView(
            self.page_Vis_Res_Ani
        )
        self.graphicsView_Vis_Res_Ani_Disp.setGeometry(QtCore.QRect(250, 20, 641, 501))
        self.graphicsView_Vis_Res_Ani_Disp.setObjectName(
            "graphicsView_Vis_Res_Ani_Disp"
        )
        self.horizontalLayoutWidget_30 = QtWidgets.QWidget(self.page_Vis_Res_Ani)

        self.horizontalLayoutWidget_30.setGeometry(QtCore.QRect(620, 520, 271, 31))
        self.horizontalLayoutWidget_30.setObjectName("horizontalLayoutWidget_30")
        self.horizontalLayout_Vis_Res_Ani = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_30
        )
        self.horizontalLayout_Vis_Res_Ani.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Res_Ani.setObjectName("horizontalLayout_Vis_Res_Ani")
        
        self.pushButton_Vis_Res_Ani_Replay = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_30
        )
        self.pushButton_Vis_Res_Ani_Replay.setObjectName(
            "pushButton_Vis_Res_Ani_Replay"
        )
        self.horizontalLayout_Vis_Res_Ani.addWidget(self.pushButton_Vis_Res_Ani_Replay)

        self.pushButton_Vis_Res_Ani_Save = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_30
        )
        self.pushButton_Vis_Res_Ani_Save.setObjectName("pushButton_Vis_Res_Ani_Save")
        self.horizontalLayout_Vis_Res_Ani.addWidget(self.pushButton_Vis_Res_Ani_Save)
        
        self.stackedWidget_Vis_Res_stackedWidget.addWidget(self.page_Vis_Res_Ani)
        
        self.tabWidget_Vis.addTab(self.Resistivity_Vis_Res, "")

        self.Water_Content_Vis_Wat = QtWidgets.QWidget()
        self.Water_Content_Vis_Wat.setObjectName("Water_Content_Vis_Wat")

        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.Water_Content_Vis_Wat)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 901, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        
        self.horizontalLayout_Vis_Wat = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_9
        )
        self.horizontalLayout_Vis_Wat.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Wat.setObjectName("horizontalLayout_Vis_Wat")

        self.radioButton_Vis_Wat_cSche = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget_9
        )
        self.radioButton_Vis_Wat_cSche.setObjectName("radioButton_Vis_Wat_cSche")
        self.horizontalLayout_Vis_Wat.addWidget(self.radioButton_Vis_Wat_cSche)
        
        self.radioButton_Vis_Wat_cSca = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget_9
        )
        self.radioButton_Vis_Wat_cSca.setObjectName("radioButton_Vis_Wat_cSca")
        self.horizontalLayout_Vis_Wat.addWidget(self.radioButton_Vis_Wat_cSca)
        
        self.radioButton_Vis_Wat_Ani = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget_9
        )
        self.radioButton_Vis_Wat_Ani.setObjectName("radioButton_Vis_Wat_Ani")
        self.horizontalLayout_Vis_Wat.addWidget(self.radioButton_Vis_Wat_Ani)

        self.stackedWidget_Vis_Wat_stackedWidget = QtWidgets.QStackedWidget(
            self.Water_Content_Vis_Wat
        )
        self.stackedWidget_Vis_Wat_stackedWidget.setGeometry(
            QtCore.QRect(0, 40, 891, 551)
        )
        self.stackedWidget_Vis_Wat_stackedWidget.setObjectName(
            "stackedWidget_Vis_Wat_stackedWidget"
        )

        self.page_Vis_Wat_cSche = QtWidgets.QWidget()
        self.page_Vis_Wat_cSche.setObjectName("page_Vis_Wat_cSche")
        self.verticalLayoutWidget_24 = QtWidgets.QWidget(self.page_Vis_Wat_cSche)
        
        self.verticalLayoutWidget_24.setGeometry(QtCore.QRect(0, 0, 231, 551))
        self.verticalLayoutWidget_24.setObjectName("verticalLayoutWidget_24")

        self.verticalLayout_Vis_Wat_cSche = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_24
        )
        self.verticalLayout_Vis_Wat_cSche.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Vis_Wat_cSche.setObjectName("verticalLayout_Vis_Wat_cSche")

        self.label_Vis_Wat_fSele = QtWidgets.QLabel(self.verticalLayoutWidget_24)
        self.label_Vis_Wat_fSele.setObjectName("label_Vis_Wat_fSele")
        self.verticalLayout_Vis_Wat_cSche.addWidget(self.label_Vis_Wat_fSele)

        self.listWidget_Vis_Wat_cSche_fSele = QtWidgets.QListWidget(
            self.verticalLayoutWidget_24
        )
        self.listWidget_Vis_Wat_cSche_fSele.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget_Vis_Wat_cSche_fSele.setObjectName(
            "listWidget_Vis_Wat_cSche_fSele"
        )
        self.verticalLayout_Vis_Wat_cSche.addWidget(self.listWidget_Vis_Wat_cSche_fSele)

        self.label_Vis_Wat_cSche_cSche = QtWidgets.QLabel(self.verticalLayoutWidget_24)
        self.label_Vis_Wat_cSche_cSche.setObjectName("label_Vis_Wat_cSche_cSche")
        self.verticalLayout_Vis_Wat_cSche.addWidget(self.label_Vis_Wat_cSche_cSche)
        
        self.listWidget_Vis_Wat_cSche_cSche = QtWidgets.QListWidget(
            self.verticalLayoutWidget_24
        )
        self.listWidget_Vis_Wat_cSche_cSche.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.listWidget_Vis_Wat_cSche_cSche.setObjectName(
            "listWidget_Vis_Wat_cSche_cSche"
        )
        self.verticalLayout_Vis_Wat_cSche.addWidget(self.listWidget_Vis_Wat_cSche_cSche)

        self.pushButton_Vis_Wat_cSche_Apply = QtWidgets.QPushButton(
            self.verticalLayoutWidget_24
        )
        self.pushButton_Vis_Wat_cSche_Apply.setObjectName(
            "pushButton_Vis_Wat_cSche_Apply"
        )
        self.verticalLayout_Vis_Wat_cSche.addWidget(self.pushButton_Vis_Wat_cSche_Apply)

        self.graphicsView_Vis_Wat_cSche_Disp = QtWidgets.QGraphicsView(
            self.page_Vis_Wat_cSche
        )
        self.graphicsView_Vis_Wat_cSche_Disp.setGeometry(
            QtCore.QRect(250, 20, 641, 501)
        )
        self.graphicsView_Vis_Wat_cSche_Disp.setObjectName(
            "graphicsView_Vis_Wat_cSche_Disp"
        )

        self.horizontalLayoutWidget_26 = QtWidgets.QWidget(self.page_Vis_Wat_cSche)
        self.horizontalLayoutWidget_26.setGeometry(QtCore.QRect(630, 520, 261, 31))
        self.horizontalLayoutWidget_26.setObjectName("horizontalLayoutWidget_26")
        self.horizontalLayout_Vis_Wat_cSche = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_26
        )
        self.horizontalLayout_Vis_Wat_cSche.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Wat_cSche.setObjectName(
            "horizontalLayout_Vis_Wat_cSche"
        )
        
        self.pushButton_Vis_Wat_cSche_Replay = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_26
        )
        self.pushButton_Vis_Wat_cSche_Replay.setObjectName(
            "pushButton_Vis_Wat_cSche_Replay"
        )
        self.horizontalLayout_Vis_Wat_cSche.addWidget(
            self.pushButton_Vis_Wat_cSche_Replay
        )
        
        self.pushButton_Vis_Wat_cSche_Save = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_26
        )
        self.pushButton_Vis_Wat_cSche_Save.setObjectName(
            "pushButton_Vis_Wat_cSche_Save"
        )
        self.horizontalLayout_Vis_Wat_cSche.addWidget(
            self.pushButton_Vis_Wat_cSche_Save
        )
        
        self.stackedWidget_Vis_Wat_stackedWidget.addWidget(self.page_Vis_Wat_cSche)

        self.page_Vis_Wat_cSca = QtWidgets.QWidget()
        self.page_Vis_Wat_cSca.setObjectName("page_Vis_Wat_cSca")

        self.graphicsView_Vis_Wat_cSca_Disp = QtWidgets.QGraphicsView(
            self.page_Vis_Wat_cSca
        )
        self.graphicsView_Vis_Wat_cSca_Disp.setGeometry(QtCore.QRect(250, 20, 641, 501))
        self.graphicsView_Vis_Wat_cSca_Disp.setObjectName(
            "graphicsView_Vis_Wat_cSca_Disp"
        )

        self.verticalLayoutWidget_25 = QtWidgets.QWidget(self.page_Vis_Wat_cSca)
        self.verticalLayoutWidget_25.setGeometry(QtCore.QRect(0, 0, 231, 541))
        self.verticalLayoutWidget_25.setObjectName("verticalLayoutWidget_25")
        self.verticalLayout_Vis_Wat_cSca = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_25
        )
        self.verticalLayout_Vis_Wat_cSca.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Vis_Wat_cSca.setObjectName("verticalLayout_Vis_Wat_cSca")
        self.label_Vis_Wat_cSca_fSele = QtWidgets.QLabel(self.verticalLayoutWidget_25)
        self.label_Vis_Wat_cSca_fSele.setObjectName("label_Vis_Wat_cSca_fSele")
        self.verticalLayout_Vis_Wat_cSca.addWidget(self.label_Vis_Wat_cSca_fSele)

        self.listWidget_Vis_Wat_cSca_fSele = QtWidgets.QListWidget(
            self.verticalLayoutWidget_25
        )
        self.listWidget_Vis_Wat_cSca_fSele.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget_Vis_Wat_cSca_fSele.setObjectName(
            "listWidget_Vis_Wat_cSca_fSele"
        )
        self.verticalLayout_Vis_Wat_cSca.addWidget(self.listWidget_Vis_Wat_cSca_fSele)

        self.label_Vis_Wat_cSca_cSca = QtWidgets.QLabel(self.verticalLayoutWidget_25)
        self.label_Vis_Wat_cSca_cSca.setObjectName("label_Vis_Wat_cSca_cSca")
        self.verticalLayout_Vis_Wat_cSca.addWidget(self.label_Vis_Wat_cSca_cSca)

        self.listWidget_Vis_Wat_cSca_cSca = QtWidgets.QListWidget(
            self.verticalLayoutWidget_25
        )
        self.listWidget_Vis_Wat_cSca_cSca.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.listWidget_Vis_Wat_cSca_cSca.setObjectName("listWidget_Vis_Wat_cSca_cSca")
        self.verticalLayout_Vis_Wat_cSca.addWidget(self.listWidget_Vis_Wat_cSca_cSca)

        self.pushButton_Vis_Wat_cSca_Apply = QtWidgets.QPushButton(
            self.verticalLayoutWidget_25
        )
        self.pushButton_Vis_Wat_cSca_Apply.setObjectName(
            "pushButton_Vis_Wat_cSca_Apply"
        )
        self.verticalLayout_Vis_Wat_cSca.addWidget(self.pushButton_Vis_Wat_cSca_Apply)

        self.horizontalLayoutWidget_31 = QtWidgets.QWidget(self.page_Vis_Wat_cSca)
        self.horizontalLayoutWidget_31.setGeometry(QtCore.QRect(630, 520, 261, 31))
        self.horizontalLayoutWidget_31.setObjectName("horizontalLayoutWidget_31")
        self.horizontalLayout_Vis_Wat_cSca = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_31
        )
        self.horizontalLayout_Vis_Wat_cSca.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Wat_cSca.setObjectName(
            "horizontalLayout_Vis_Wat_cSca"
        )

        self.pushButton_Vis_Wat_cSca_Replay = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_31
        )
        self.pushButton_Vis_Wat_cSca_Replay.setObjectName(
            "pushButton_Vis_Wat_cSca_Replay"
        )
        self.horizontalLayout_Vis_Wat_cSca.addWidget(
            self.pushButton_Vis_Wat_cSca_Replay
        )
       
        self.pushButton_Vis_Wat_cSca_Save = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_31
        )
        self.pushButton_Vis_Wat_cSca_Save.setObjectName("pushButton_Vis_Wat_cSca_Save")
        self.horizontalLayout_Vis_Wat_cSca.addWidget(self.pushButton_Vis_Wat_cSca_Save)
      
        self.stackedWidget_Vis_Wat_stackedWidget.addWidget(self.page_Vis_Wat_cSca)

        self.page_Vis_Wat_Ani = QtWidgets.QWidget()
        self.page_Vis_Wat_Ani.setObjectName("page_Vis_Wat_Ani")

        self.verticalLayoutWidget_27 = QtWidgets.QWidget(self.page_Vis_Wat_Ani)
        self.verticalLayoutWidget_27.setGeometry(QtCore.QRect(0, 0, 231, 551))
        self.verticalLayoutWidget_27.setObjectName("verticalLayoutWidget_27")
        self.verticalLayout_Vis_Wat_Ani = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_27
        )
        self.verticalLayout_Vis_Wat_Ani.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Vis_Wat_Ani.setObjectName("verticalLayout_Vis_Wat_Ani")
        
        self.label_Vis_Wat_Ani_fSele = QtWidgets.QLabel(self.verticalLayoutWidget_27)
        self.label_Vis_Wat_Ani_fSele.setObjectName("label_Vis_Wat_Ani_fSele")
        self.verticalLayout_Vis_Wat_Ani.addWidget(self.label_Vis_Wat_Ani_fSele)
        
        self.listWidget_Vis_Wat_Ani_fSele = QtWidgets.QListWidget(
            self.verticalLayoutWidget_27
        )
        self.listWidget_Vis_Wat_Ani_fSele.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget_Vis_Wat_Ani_fSele.setObjectName("listWidget_Vis_Wat_Ani_fSele")
        self.verticalLayout_Vis_Wat_Ani.addWidget(self.listWidget_Vis_Wat_Ani_fSele)
        
        self.pushButton_Vis_Wat_Ani_Apply = QtWidgets.QPushButton(
            self.verticalLayoutWidget_27
        )
        self.pushButton_Vis_Wat_Ani_Apply.setObjectName("pushButton_Vis_Wat_Ani_Apply")
        self.verticalLayout_Vis_Wat_Ani.addWidget(self.pushButton_Vis_Wat_Ani_Apply)

        self.graphicsView_Vis_Wat_Ani_Disp = QtWidgets.QGraphicsView(
            self.page_Vis_Wat_Ani
        )
        self.graphicsView_Vis_Wat_Ani_Disp.setGeometry(QtCore.QRect(250, 20, 641, 501))
        self.graphicsView_Vis_Wat_Ani_Disp.setObjectName(
            "graphicsView_Vis_Wat_Ani_Disp"
        )


        self.horizontalLayoutWidget_32 = QtWidgets.QWidget(self.page_Vis_Wat_Ani)
        self.horizontalLayoutWidget_32.setGeometry(QtCore.QRect(620, 520, 271, 31))
        self.horizontalLayoutWidget_32.setObjectName("horizontalLayoutWidget_32")
        self.horizontalLayout_Vis_Wat_Ani = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_32
        )
        self.horizontalLayout_Vis_Wat_Ani.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Vis_Wat_Ani.setObjectName("horizontalLayout_Vis_Wat_Ani")
        
        self.pushButton_Vis_Wat_Ani_Replay = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_32
        )
        self.pushButton_Vis_Wat_Ani_Replay.setObjectName(
            "pushButton_Vis_Wat_Ani_Replay"
        )
        self.horizontalLayout_Vis_Wat_Ani.addWidget(self.pushButton_Vis_Wat_Ani_Replay)
        
        self.pushButton_Vis_Wat_Ani_Save = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_32
        )
        self.pushButton_Vis_Wat_Ani_Save.setObjectName("pushButton_Vis_Wat_Ani_Save")
        self.horizontalLayout_Vis_Wat_Ani.addWidget(self.pushButton_Vis_Wat_Ani_Save)
       
        self.stackedWidget_Vis_Wat_stackedWidget.addWidget(self.page_Vis_Wat_Ani)

        self.tabWidget_Vis.addTab(self.Water_Content_Vis_Wat, "")
        self.horizontalLayout_Vis_5.addWidget(self.tabWidget_Vis)
        self.tabWidget.addTab(self.Visualization, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
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
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_Vis.setCurrentIndex(1)

        self.listWidget_Vis_Res_cSche_cSche.setCurrentRow(-1)

        self.radioButton_Vis_Wat_cSche.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_Vis_Wat_cSca.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_Vis_Wat_Ani.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_Vis_Res_cSche.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_Vis_Res_cSca.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_Vis_Res_Ani.toggled.connect(self.on_radio_button_toggled)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.vis_res_load_local_images()
        self.vis_wat_load_local_images()
        self.vis_set_color_items()
        self.vis_set_legend_scale()
        self.pushButton_Vis_Res_cSche_Apply.clicked.connect(self.apply_Vis_Res_cSche)
        self.pushButton_Vis_Res_cSche_Replay.clicked.connect(self.preview_Vis_Res_cSche)
        self.pushButton_Vis_Res_cSche_Save.clicked.connect(
            self.grey_from_txt_Vis_Res_cSche
        )

        self.pushButton_Vis_Res_Ani_Apply.clicked.connect(self.apply_Vis_Res_Ani)

        self.pushButton_Vis_Res_Ani_Replay.clicked.connect(self.replay_Vis_Res_Ani)
        self.pushButton_Vis_Res_Ani_Save.clicked.connect(self.save_Vis_Res_Ani)

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
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Geometry:</p></body></html>',
            )
        )
        self.textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">start</p></body></html>',
            )
        )
        self.textEdit_2.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">end</p></body></html>',
            )
        )
        self.textEdit_4.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Mesh:</p></body></html>',
            )
        )
        self.textEdit_5.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Quality</p></body></html>',
            )
        )
        self.textEdit_6.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Area</p></body></html>',
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
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">maxIter:</p></body></html>',
            )
        )
        self.textEdit_9.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Lam:</p></body></html>',
            )
        )
        self.textEdit_10.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">dPhi:</p></body></html>',
            )
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
                "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'.AppleSystemUIFont\'; font-size:13pt;">Temperture</span></p></body></html>',
            )
        )
        self.pushButton_12.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            _translate("MainWindow", "Water Content"),
        )
        self.radioButton_Vis_Res_cSche.setText(_translate("MainWindow", "Color Scheme"))
        self.radioButton_Vis_Res_cSca.setText(
            _translate("MainWindow", "Custom Color Scale")
        )
        self.radioButton_Vis_Res_Ani.setText(
            _translate("MainWindow", "Time-Serial Animation")
        )
        self.label_Vis_Res_fSele.setText(_translate("MainWindow", "File Selection"))
        self.label_Vis_Res_cSche_cSche.setText(_translate("MainWindow", "Color Scheme"))
        self.pushButton_Vis_Res_cSche_Apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Vis_Res_cSche_Replay.setText(
            _translate("MainWindow", "Preview")
        )
        self.pushButton_Vis_Res_cSche_Save.setText(_translate("MainWindow", "Refresh"))
        self.label_Vis_Res_cSca_fSele.setText(
            _translate("MainWindow", "File Selection")
        )
        self.label_Vis_Res_cSca_cSca.setText(_translate("MainWindow", "Color Scale"))
        self.pushButton_Vis_Res_cSca_Apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Vis_Res_cSca_Replay.setText(_translate("MainWindow", "Preview"))
        self.pushButton_Vis_Res_cSca_Save.setText(_translate("MainWindow", "Refresh"))
        self.label_Vis_Res_Ani_fSele.setText(_translate("MainWindow", "File Selection"))
        self.pushButton_Vis_Res_Ani_Apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Vis_Res_Ani_Replay.setText(_translate("MainWindow", "Replay"))
        self.pushButton_Vis_Res_Ani_Save.setText(_translate("MainWindow", "Save"))
        self.tabWidget_Vis.setTabText(
            self.tabWidget_Vis.indexOf(self.Resistivity_Vis_Res),
            _translate("MainWindow", "Resistivity"),
        )
        self.radioButton_Vis_Wat_cSche.setText(_translate("MainWindow", "Color Scheme"))
        self.radioButton_Vis_Wat_cSca.setText(
            _translate("MainWindow", "Custom Color Scale")
        )
        self.radioButton_Vis_Wat_Ani.setText(
            _translate("MainWindow", "Time-Serial Animation")
        )
        self.label_Vis_Wat_fSele.setText(_translate("MainWindow", "File Selection"))
        self.label_Vis_Wat_cSche_cSche.setText(_translate("MainWindow", "Color Scheme"))
        self.pushButton_Vis_Wat_cSche_Apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Vis_Wat_cSche_Replay.setText(
            _translate("MainWindow", "Preview")
        )
        self.pushButton_Vis_Wat_cSche_Save.setText(_translate("MainWindow", "Refresh"))
        self.label_Vis_Wat_cSca_fSele.setText(
            _translate("MainWindow", "File Selection")
        )
        self.label_Vis_Wat_cSca_cSca.setText(_translate("MainWindow", "Color Scale"))
        self.pushButton_Vis_Wat_cSca_Apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Vis_Wat_cSca_Replay.setText(_translate("MainWindow", "Preview"))
        self.pushButton_Vis_Wat_cSca_Save.setText(_translate("MainWindow", "Refresh"))
        self.label_Vis_Wat_Ani_fSele.setText(_translate("MainWindow", "File Selection"))
        self.pushButton_Vis_Wat_Ani_Apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Vis_Wat_Ani_Replay.setText(_translate("MainWindow", "Replay"))
        self.pushButton_Vis_Wat_Ani_Save.setText(_translate("MainWindow", "Save"))
        self.tabWidget_Vis.setTabText(
            self.tabWidget_Vis.indexOf(self.Water_Content_Vis_Wat),
            _translate("MainWindow", "Water Content"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Visualization),
            _translate("MainWindow", "Visualization"),
        )
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionGuidline.setText(_translate("MainWindow", "Guidline"))
        self.actionContract.setText(_translate("MainWindow", "Contract"))


class MyMainWindow_Vis(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow_Vis, self).__init__(parent)
        self.setupUi(self)

        self.timer = QTimer(self)

        self.scene_Vis_Res_cSche = QtWidgets.QGraphicsScene(self)
        self.scene_Vis_Res_cSca = QtWidgets.QGraphicsScene(self)
        self.scene_Vis_Res_Ani = QtWidgets.QGraphicsScene(self)
        self.scene_Vis_Wat_cSche = QtWidgets.QGraphicsScene(self)
        self.scene_Vis_Wat_cSca = QtWidgets.QGraphicsScene(self)
        self.scene_Vis_Wat_Ani = QtWidgets.QGraphicsScene(self)

    def on_radio_button_toggled(self, checked):
        if not checked:
            return
        if self.sender() == self.radioButton_Vis_Res_cSche:
            self.stackedWidget_Vis_Res_stackedWidget.setCurrentWidget(
                self.page_Vis_Res_cSche
            )
        elif self.sender() == self.radioButton_Vis_Res_cSca:
            self.stackedWidget_Vis_Res_stackedWidget.setCurrentWidget(
                self.page_Vis_Res_cSca
            )
        elif self.sender() == self.radioButton_Vis_Res_Ani:
            self.stackedWidget_Vis_Res_stackedWidget.setCurrentWidget(
                self.page_Vis_Res_Ani
            )
        elif self.sender() == self.radioButton_Vis_Wat_cSche:
            self.stackedWidget_Vis_Wat_stackedWidget.setCurrentWidget(
                self.page_Vis_Wat_cSche
            )
        elif self.sender() == self.radioButton_Vis_Wat_cSca:
            self.stackedWidget_Vis_Wat_stackedWidget.setCurrentWidget(
                self.page_Vis_Wat_cSca
            )
        elif self.sender() == self.radioButton_Vis_Wat_Ani:
            self.stackedWidget_Vis_Wat_stackedWidget.setCurrentWidget(
                self.page_Vis_Wat_Ani
            )

    def vis_res_load_local_images(self):
        files = os.listdir()
        filtered_files = [
            file_name
            for file_name in files
            if file_name.endswith(".txt") or file_name.endswith("_res.png")
        ]
        sorted_files = sorted(filtered_files, key=lambda x: x.split(".")[0])
        for file_name in sorted_files:
            self.listWidget_Vis_Res_cSche_fSele.addItem(file_name)
            self.listWidget_Vis_Res_cSca_fSele.addItem(file_name)
            self.listWidget_Vis_Res_Ani_fSele.addItem(file_name)

    def vis_wat_load_local_images(self):
        for file_name in os.listdir():
            if file_name.endswith("_wat.png") or file_name.endswith(".txt"):
                self.listWidget_Vis_Wat_cSche_fSele.addItem(file_name)
                self.listWidget_Vis_Wat_cSca_fSele.addItem(file_name)
                self.listWidget_Vis_Wat_Ani_fSele.addItem(file_name)

    def vis_set_color_items(self):
        colors = ["black", "red", "yellow", "blue", "green", "purple"]
        for color in colors:
            self.listWidget_Vis_Res_cSche_cSche.addItem(color)
            self.listWidget_Vis_Wat_cSche_cSche.addItem(color)

    def vis_set_legend_scale(self):
        method_cSca = ["cluster", "90%"]
        for method_cSca_i in method_cSca:
            self.listWidget_Vis_Res_cSca_cSca.addItem(method_cSca_i)
            self.listWidget_Vis_Wat_cSca_cSca.addItem(method_cSca_i)

    def grey_from_txt_Vis_Res_cSche(self):
        base_folder = "." 

        txt_files = [file for file in os.listdir(base_folder) if file.endswith(".txt")]

        for txt_file in txt_files:
            file_name = os.path.splitext(txt_file)[0]

            folder_path = os.path.join(base_folder, file_name)

            if os.path.exists(folder_path):
                ert_folder_path = os.path.join(folder_path, "ERTManager", "ERTManager")

                vtk_txt_file_path = os.path.join(
                    ert_folder_path, "ERTManager.resistivity.vtk.txt"
                )

                if os.path.exists(vtk_txt_file_path):
                    with open(vtk_txt_file_path, "r") as file:
                        lines = file.readlines()
                        data = [line.strip().split("\t") for line in lines]
                        data = np.array(data, dtype=float)

                x = data[:, 0]
                y = data[:, 1]
                resistance = data[:, 2]

                plt.scatter(x, y, c=resistance, cmap="gray", marker=".", s=3)
                plt.xlabel("X axis")
                plt.ylabel("Y axis")
                plt.title("ERTGrayscale image_" + file_name)
                plt.tight_layout()

                output_file_name = f"grey_{file_name}_res.png"

                output_file_path = os.path.join(base_folder, output_file_name)
                plt.savefig(output_file_path)
        self.refreshFileList()

    def apply_Vis_Res_cSche(self):
        if (
            not self.listWidget_Vis_Res_cSche_fSele.selectedItems()
            or not self.listWidget_Vis_Res_cSche_cSche.currentItem()
        ):
            return  

        selected_images = self.listWidget_Vis_Res_cSche_fSele.selectedItems()
        selected_color = self.listWidget_Vis_Res_cSche_cSche.currentItem().text()

        color_map = {
            "black": (0, 0, 0),
            "red": (0.5, 0, 0),  
            "yellow": (0.5, 0.5, 0),  
            "blue": (0, 0, 0.5),  
            "green": (0, 0.5, 0),  
            "purple": (0.25, 0, 0.25),  
        }

        color_white = (1, 1, 1)
        selected_color_rgb = color_map[selected_color]

        for item in selected_images:
            img_path = item.text()
            img = plt.imread(img_path)
            grayscale = img.mean(axis=2)  

            cmap = LinearSegmentedColormap.from_list(
                "custom_cmap", [np.array(color_white), np.array(selected_color_rgb)]
            )

            colorized = cmap(grayscale)[:, :, :3]  
            plt.imsave(f"{selected_color}_{img_path}", colorized)

            if item == selected_images[0]:
                pixmap = QtGui.QPixmap(f"{selected_color}_{img_path}")
                self.scene_Vis_Res_cSche.addPixmap(pixmap)
                self.graphicsView_Vis_Res_cSche_Disp.setScene(self.scene_Vis_Res_cSche)
                self.graphicsView_Vis_Res_cSche_Disp.fitInView(
                    self.scene_Vis_Res_cSche.itemsBoundingRect(),
                    QtCore.Qt.KeepAspectRatio,
                )
        self.refreshFileList()

    def apply_Vis_Wat_cSche(self):
        if (
            not self.listWidget_Vis_Wat_cSche_fSele.selectedItems()
            or not self.listWidget_Vis_Wat_cSche_cSche.currentItem()
        ):
            print("No file selected or no color selected.")

        selected_images = self.listWidget_Vis_Wat_cSche_fSele.selectedItems()
        selected_color = self.listWidget_Vis_Wat_cSche_cSche.currentItem().text()

        color_map = {
            "black": (0, 0, 0),
            "red": (1, 0, 0),
            "yellow": (1, 1, 0),
            "blue": (0, 0, 1),
            "green": (0, 1, 0),
            "purple": (0.5, 0, 0.5),
        }

        selected_color_rgb = color_map[selected_color]  

        for item in selected_images:
            img_path = item.text()
            img = plt.imread(img_path)
            grayscale = img.mean(axis=2)  

            cmap = LinearSegmentedColormap.from_list(
                "custom_cmap", [np.zeros(3), np.array(selected_color_rgb)]
            )

            colorized = cmap(grayscale)[:, :, :3]  
            plt.imsave(f"{selected_color}_{img_path}", colorized)

            if item == selected_images[0]:
                pixmap = QtGui.QPixmap(f"{selected_color}_{img_path}")
                self.scene_Vis_Res_cSche.addPixmap(pixmap)
                self.graphicsView_Vis_Res_cSche_Disp.setScene(self.scene_Vis_Res_cSche)
                self.graphicsView_Vis_Res_cSche_Disp.fitInView(
                    self.scene_Vis_Res_cSche.itemsBoundingRect(),
                    QtCore.Qt.KeepAspectRatio,
                )
        self.refreshFileList()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow_Vis()
    MainWindow.show()
    sys.exit(app.exec_())
