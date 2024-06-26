from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QColor,QPainter
import os
import shutil
import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5.QtWidgets import  QGraphicsPixmapItem
import os
import matplotlib.pyplot as plt
import numpy as np
import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
import sys

import glob
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QFileDialog, QGraphicsScene, QGraphicsView)
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import QTimer
import imageio

tem_field=[(0,25)]
tem=25
save_directory = None
class Ui_MainWindow(object, ):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 660)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QTabBar::tab:selected {\n"
                                         "    background: lightblue;\n"
                                         "    color: black;\n"
                                         "}\n"
                                         "QTabBar::tab:!selected {\n"
                                         "    background: lightgray;\n"
                                         "    color: black;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalWidget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_Importing = QtWidgets.QTabWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_Importing.sizePolicy().hasHeightForWidth())
        self.tabWidget_Importing.setSizePolicy(sizePolicy)
        self.tabWidget_Importing.setMinimumSize(QtCore.QSize(781, 571))
        self.tabWidget_Importing.setMouseTracking(True)
        self.tabWidget_Importing.setAutoFillBackground(False)
        self.tabWidget_Importing.setStyleSheet("")
        self.tabWidget_Importing.setObjectName("tabWidget_Importing")
        self.Importing = QtWidgets.QWidget()
        self.Importing.setObjectName("Importing")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Importing)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget_Data = QtWidgets.QTabWidget(self.Importing)
        self.tabWidget_Data.setAutoFillBackground(False)
        self.tabWidget_Data.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "border-top-color: rgb(0, 0, 0);")
        self.tabWidget_Data.setObjectName("tabWidget_Data")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.listWidget_file_list = QtWidgets.QListWidget(self.Data)
        self.listWidget_file_list.setGeometry(QtCore.QRect(130, 20, 461, 451))
        self.listWidget_file_list.setStyleSheet("background: rgb(255, 255, 255); color: black")
        self.listWidget_file_list.setObjectName("listWidget_file_list")
        self.pushButton_Import = QtWidgets.QPushButton(self.Data)
        self.pushButton_Import.setGeometry(QtCore.QRect(630, 440, 82, 32))
        self.pushButton_Import.setObjectName("pushButton_Import")
        self.pushButton_importfile = QtWidgets.QPushButton(self.Data)
        self.pushButton_importfile.setGeometry(QtCore.QRect(610, 111, 141, 41))
        self.pushButton_importfile.setObjectName("pushButton_importfile")
        self.tabWidget_Data.addTab(self.Data, "")
        self.Pre_processing = QtWidgets.QWidget()
        self.Pre_processing.setObjectName("Pre_processing")
        self.pushButton_Transfer_Data = QtWidgets.QPushButton(self.Pre_processing)
        self.pushButton_Transfer_Data.setGeometry(QtCore.QRect(610, 110, 126, 41))
        self.pushButton_Transfer_Data.setObjectName("pushButton_Transfer_Data")
        self.pushButton_next_to_visualisation = QtWidgets.QPushButton(self.Pre_processing)
        self.pushButton_next_to_visualisation.setGeometry(QtCore.QRect(605, 459, 146, 32))
        self.pushButton_next_to_visualisation.setObjectName("pushButton_next_to_visualisation")
        self.textBrowser_showdata = QtWidgets.QTextBrowser(self.Pre_processing)
        self.textBrowser_showdata.setGeometry(QtCore.QRect(130, 20, 461, 451))
        self.textBrowser_showdata.setStyleSheet("background: rgb(255, 255, 255)")
        self.textBrowser_showdata.setObjectName("textBrowser_showdata")
        self.pushButton_next_to_domain = QtWidgets.QPushButton(self.Pre_processing)
        self.pushButton_next_to_domain.setGeometry(QtCore.QRect(605, 425, 134, 32))
        self.pushButton_next_to_domain.setObjectName("pushButton_next_to_domain")
        self.tabWidget_Data.addTab(self.Pre_processing, "")
        self.verticalLayout_5.addWidget(self.tabWidget_Data)
        self.tabWidget_Importing.addTab(self.Importing, "")
        self.Domain_Mesh = QtWidgets.QWidget()
        self.Domain_Mesh.setObjectName("Domain_Mesh")
        self.tabWidget = QtWidgets.QTabWidget(self.Domain_Mesh)
        self.tabWidget.setGeometry(QtCore.QRect(40, 0, 731, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.Domain = QtWidgets.QWidget()
        self.Domain.setObjectName("Domain")
        self.spinBox_startX = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_startX.setGeometry(QtCore.QRect(210, 20, 40, 21))
        self.spinBox_startX.setObjectName("spinBox_startX")
        
        self.graphicsView_domain = QtWidgets.QGraphicsView(self.Domain)
        self.graphicsView_domain.setGeometry(QtCore.QRect(100, 100, 511, 311))
        self.graphicsView_domain.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_domain.setObjectName("graphicsView_domain")
        graphicsView_domain_layout = QtWidgets.QVBoxLayout(self.graphicsView_domain)
        self.canvas_domain = FigureCanvas(plt.figure())
        graphicsView_domain_layout.addWidget(self.canvas_domain)
        
        self.pushButton_domain_apply = QtWidgets.QPushButton(self.Domain)
        self.pushButton_domain_apply.setGeometry(QtCore.QRect(500, 20, 101, 51))
        self.pushButton_domain_apply.setObjectName("pushButton_domain_apply")
        self.pushButton_next_to_mesh = QtWidgets.QPushButton(self.Domain)
        self.pushButton_next_to_mesh.setGeometry(QtCore.QRect(530, 430, 71, 32))
        self.pushButton_next_to_mesh.setObjectName("pushButton_next_to_mesh")
        self.pushButton_domain_save = QtWidgets.QPushButton(self.Domain)
        self.pushButton_domain_save.setGeometry(QtCore.QRect(110, 430, 73, 32))
        self.pushButton_domain_save.setObjectName("pushButton_domain_save")
        self.label_start = QtWidgets.QLabel(self.Domain)
        self.label_start.setGeometry(QtCore.QRect(117, 20, 41, 21))
        self.label_start.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.label_start.setObjectName("label_start")
        self.label_end = QtWidgets.QLabel(self.Domain)
        self.label_end.setGeometry(QtCore.QRect(117, 50, 41, 21))
        self.label_end.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);")
        self.label_end.setObjectName("label_end")
        self.spinBox_endX = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_endX.setGeometry(QtCore.QRect(210, 50, 40, 20))
        self.spinBox_endX.setObjectName("spinBox_endX")
        self.spinBox_stratY = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_stratY.setGeometry(QtCore.QRect(290, 20, 40, 20))
        self.spinBox_stratY.setObjectName("spinBox_stratY")
        self.spinBox_endY = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_endY.setGeometry(QtCore.QRect(290, 50, 40, 21))
        self.spinBox_endY.setObjectName("spinBox_endY")
        self.spinBox_endX.setObjectName("spinBox_endX")
        self.spinBox_endX.setMinimum(-8)
        self.spinBox_endX.setMaximum(50)
        self.spinBox_startY = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_startY.setGeometry(QtCore.QRect(290, 20, 40, 20))
        self.spinBox_startY.setObjectName("spinBox_startY")
        self.spinBox_startY.setMinimum(0)
        self.spinBox_startY.setMaximum(99)
        self.spinBox_endY = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_endY.setGeometry(QtCore.QRect(290, 50, 40, 21))
        self.spinBox_endY.setObjectName("spinBox_endY")
        self.spinBox_endY.setMinimum(-8)
        self.spinBox_endY.setMaximum(50)
 
        self.tabWidget.addTab(self.Domain, "")
        self.Mesh = QtWidgets.QWidget()
        self.Mesh.setObjectName("Mesh")
        self.label_quality = QtWidgets.QLabel(self.Mesh)
        self.label_quality.setGeometry(QtCore.QRect(120, 20, 51, 21))
        self.label_quality.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(0, 0, 0);")
        self.label_quality.setObjectName("label_quality")
        self.label_area = QtWidgets.QLabel(self.Mesh)
        self.label_area.setGeometry(QtCore.QRect(120, 50, 51, 21))
        self.label_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.label_area.setObjectName("label_area")
        self.doubleSpinBox_quality = QtWidgets.QDoubleSpinBox(self.Mesh)
        self.doubleSpinBox_quality.setGeometry(QtCore.QRect(210, 20, 62, 21))
        self.doubleSpinBox_quality.setObjectName("doubleSpinBox_quality")
        self.doubleSpinBox_area = QtWidgets.QDoubleSpinBox(self.Mesh)
        self.doubleSpinBox_area.setGeometry(QtCore.QRect(210, 50, 62, 21))
        self.doubleSpinBox_area.setObjectName("doubleSpinBox_area")
        self.graphicsView_mesh = QtWidgets.QGraphicsView(self.Mesh)
        self.graphicsView_mesh.setGeometry(QtCore.QRect(100, 100, 511, 311))
        self.graphicsView_mesh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_mesh.setObjectName("graphicsView_mesh")
        graphicsView_mesh_layout = QtWidgets.QVBoxLayout(self.graphicsView_mesh)
        self.canvas_mesh = FigureCanvas(plt.figure())
        graphicsView_mesh_layout.addWidget(self.canvas_mesh)
        self.pushButton_mesh_save = QtWidgets.QPushButton(self.Mesh)
        self.pushButton_mesh_save.setGeometry(QtCore.QRect(110, 430, 73, 31))
        self.pushButton_mesh_save.setObjectName("pushButton_mesh_save")
        self.pushButton_next_to_inversion = QtWidgets.QPushButton(self.Mesh)
        self.pushButton_next_to_inversion.setGeometry(QtCore.QRect(530, 430, 71, 32))
        self.pushButton_next_to_inversion.setObjectName("pushButton_next_to_inversion")
        self.tabWidget.addTab(self.Mesh, "")
        self.tabWidget_Importing.addTab(self.Domain_Mesh, "")
        self.Inversion = QtWidgets.QWidget()
        self.Inversion.setObjectName("Inversion")
        self.pushButton_inversion_apply = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_inversion_apply.setGeometry(QtCore.QRect(470, 30, 111, 51))
        self.pushButton_inversion_apply.setObjectName("pushButton_inversion_apply")
        #Add tooltip/explanation for Apply button
        self.pushButton_inversion_apply.setToolTip("Start inverting the imported data to generate the soil resistivity distribution map <br> after choosing the value for each parameter of inversion algorithm.")
        self.pushButton_inversion_save = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_inversion_save.setGeometry(QtCore.QRect(150, 450, 71, 31))
        self.pushButton_inversion_save.setObjectName("pushButton_inversion_save")
         #Add tooltip/explanation for Save button
        self.pushButton_inversion_save.setToolTip("Save the inverted soil resistivity distribution map.<br>")
        self.label_Lambda = QtWidgets.QLabel(self.Inversion)
        self.label_Lambda.setGeometry(QtCore.QRect(250, 50, 61, 16))
        self.label_Lambda.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.label_Lambda.setObjectName("label_Lambda")
        self.label_dPhi = QtWidgets.QLabel(self.Inversion)
        self.label_dPhi.setGeometry(QtCore.QRect(250, 80, 61, 16))
        self.label_dPhi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "text-align: center;")
        self.label_dPhi.setObjectName("label_dPhi")
        self.label_dPhi.setToolTip("Delta Phi determines the allowable change in resistivity between neighboring cells in the model.<br>")
        self.inversion_result_widget = QtWidgets.QWidget(self.Inversion)
        self.inversion_result_widget.setGeometry(QtCore.QRect(140, 120, 511, 311))
        self.inversion_result_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inversion_result_widget.setObjectName("inversion_result_widget")
        self.inversion_result_layout = QtWidgets.QVBoxLayout(self.inversion_result_widget) 
        self.inversion_result_layout.setObjectName("inversion_result_layout")   
        
        self.pushButton_next_to_watercontent = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_next_to_watercontent.setGeometry(QtCore.QRect(560, 450, 71, 32))
        self.pushButton_next_to_watercontent.setObjectName("pushButton_next_to_watercontent")
        self.spinBox_Iterations = QtWidgets.QSpinBox(self.Inversion)
        self.spinBox_Iterations.setGeometry(QtCore.QRect(330, 20, 40, 20))
        self.spinBox_Iterations.setProperty("value", 5)
        self.spinBox_Iterations.setObjectName("spinBox_Iterations")

        self.spinBox_Iterations.setMinimum(5)
        self.spinBox_Iterations.setMaximum(30)
        
        self.spinBox_dPhi = QtWidgets.QSpinBox(self.Inversion)
        self.spinBox_dPhi.setGeometry(QtCore.QRect(330, 80, 40, 20))
        self.spinBox_dPhi.setProperty("value", 1)
        self.spinBox_dPhi.setObjectName("spinBox_dPhi")
        self.spinBox_dPhi.setMinimum(1)
        self.spinBox_dPhi.setMaximum(10)     
        
        self.spinBox_Lambda = QtWidgets.QSpinBox(self.Inversion)
        self.spinBox_Lambda.setGeometry(QtCore.QRect(330, 50, 40, 20))
        self.spinBox_Lambda.setProperty("value", 5)
        self.spinBox_Lambda.setObjectName("spinBox_Lambda")
        self.spinBox_Lambda.setMinimum(5)
        self.spinBox_Lambda.setMaximum(30)      
        
        self.label_iterations = QtWidgets.QLabel(self.Inversion)
        self.label_iterations.setGeometry(QtCore.QRect(250, 20, 61, 16))
        self.label_iterations.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
        self.label_iterations.setObjectName("label_iterations")
        self.tabWidget_Importing.addTab(self.Inversion, "")
        self.Water_content = QtWidgets.QWidget()
        self.Water_content.setObjectName("Water_content")
        self.doubleSpinBox_Temperature = QtWidgets.QDoubleSpinBox(self.Water_content)
        self.doubleSpinBox_Temperature.setGeometry(QtCore.QRect(360, 40, 61, 31))
        self.doubleSpinBox_Temperature.setDecimals(1)
        self.doubleSpinBox_Temperature.setSingleStep(0.1)
        self.doubleSpinBox_Temperature.setProperty("value", 25.0)
        self.doubleSpinBox_Temperature.setObjectName("doubleSpinBox_Temperature")
        self.pushButton_watercontent_calculate = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_watercontent_calculate.setGeometry(QtCore.QRect(150, 450, 81, 31))
        self.pushButton_watercontent_calculate.setObjectName("pushButton_watercontent_calculate")
        self.label_Temperature = QtWidgets.QLabel(self.Water_content)
        self.label_Temperature.setGeometry(QtCore.QRect(240, 50, 91, 16))
        self.label_Temperature.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "color: rgb(0, 0, 0);")
        self.label_Temperature.setObjectName("label_Temperature")
        
        
        self.graphicsView_watercontent = QtWidgets.QGraphicsView(self.Water_content)
        self.graphicsView_watercontent.setGeometry(QtCore.QRect(50, 120, 711, 311))
        self.graphicsView_watercontent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_watercontent.setObjectName("graphicsView_watercontent")
        self.scene = QGraphicsScene()
        self.graphicsView_watercontent.setScene(self.scene)
        
        self.pushButton_next_to_vis = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_next_to_vis.setGeometry(QtCore.QRect(560, 450, 71, 32))
        self.pushButton_next_to_vis.setObjectName("pushButton_next_to_vis")
        
        self.pushButton_multiplefiles_processing = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_multiplefiles_processing.setGeometry(QtCore.QRect(560, 500, 160, 32))
        self.pushButton_multiplefiles_processing.setObjectName("pushButton_multiplefiles_procssing")        
        
        self.pushButton_import_soil_field = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_import_soil_field.setGeometry(QtCore.QRect(460, 40, 201, 31))
        self.pushButton_import_soil_field.setObjectName("pushButton_import_soil_field")
        self.tabWidget_Importing.addTab(self.Water_content, "")
        self.visualisation = QtWidgets.QWidget()
        self.visualisation.setObjectName("visualisation")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.visualisation)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.visualisation)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.Vis_resistivity = QtWidgets.QWidget()
        self.Vis_resistivity.setObjectName("Vis_resistivity")
        self.radioButton_vis_res_ani = QtWidgets.QRadioButton(self.Vis_resistivity)
        self.radioButton_vis_res_ani.setGeometry(QtCore.QRect(120, 10, 161, 20))
        self.radioButton_vis_res_ani.setObjectName("radioButton_vis_res_ani")
        self.label_resistivity_file = QtWidgets.QLabel(self.Vis_resistivity)
        self.label_resistivity_file.setGeometry(QtCore.QRect(120, 40, 91, 21))
        self.label_resistivity_file.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_resistivity_file.setObjectName("label_resistivity_file")
        
        self.listWidget_vis_res_pic = QtWidgets.QListWidget(self.Vis_resistivity)
        self.listWidget_vis_res_pic.setGeometry(QtCore.QRect(120, 70, 171, 281))
        self.listWidget_vis_res_pic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_vis_res_pic.setObjectName("listWidget_vis_res_pic")
        self.listWidget_vis_res_pic.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        
        self.pushButton_vis_res_apply = QtWidgets.QPushButton(self.Vis_resistivity)
        self.pushButton_vis_res_apply.setGeometry(QtCore.QRect(120, 360, 171, 31))
        self.pushButton_vis_res_apply.setObjectName("pushButton_vis_res_apply")
        self.graphicsView_vis_resistivity = QtWidgets.QGraphicsView(self.Vis_resistivity)
        self.graphicsView_vis_resistivity.setGeometry(QtCore.QRect(300, 70, 331, 281))
        self.graphicsView_vis_resistivity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_vis_resistivity.setObjectName("graphicsView_vis_resistivity")
        self.tabWidget_3.addTab(self.Vis_resistivity, "")
        self.Vis_water_content = QtWidgets.QWidget()
        self.Vis_water_content.setObjectName("Vis_water_content")
        self.radioButton_vis_water_ani = QtWidgets.QRadioButton(self.Vis_water_content)
        self.radioButton_vis_water_ani.setGeometry(QtCore.QRect(120, 10, 161, 20))
        self.radioButton_vis_water_ani.setObjectName("radioButton_vis_water_ani")
        self.label_water_file = QtWidgets.QLabel(self.Vis_water_content)
        self.label_water_file.setGeometry(QtCore.QRect(120, 40, 91, 21))
        self.label_water_file.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_water_file.setObjectName("label_water_file")
       
        self.listWidget_vis_water_pic = QtWidgets.QListWidget(self.Vis_water_content)
        self.listWidget_vis_water_pic.setGeometry(QtCore.QRect(120, 70, 171, 281))
        self.listWidget_vis_water_pic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_vis_water_pic.setObjectName("listWidget_vis_water_pic")
        self.listWidget_vis_water_pic.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        
        self.pushButton_vis_water_apply = QtWidgets.QPushButton(self.Vis_water_content)
        self.pushButton_vis_water_apply.setGeometry(QtCore.QRect(120, 360, 171, 31))
        self.pushButton_vis_water_apply.setObjectName("pushButton_vis_water_apply")
        self.graphicsView_vis_watercontent = QtWidgets.QGraphicsView(self.Vis_water_content)
        self.graphicsView_vis_watercontent.setGeometry(QtCore.QRect(300, 70, 331, 281))
        self.graphicsView_vis_watercontent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_vis_watercontent.setObjectName("graphicsView_vis_watercontent")
        self.tabWidget_3.addTab(self.Vis_water_content, "")
        self.horizontalLayout_5.addWidget(self.tabWidget_3)
        self.tabWidget_Importing.addTab(self.visualisation, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_Importing)
        self.verticalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
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
        self.menuHelp.addAction(self.actionGuidline)
        self.menuHelp.addAction(self.actionContract)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_Importing.setCurrentIndex(0)
        self.tabWidget_Data.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)

        # singal and plot

        # import and data transform part
        self.pushButton_importfile.clicked.connect(self.open_file_dialog)
        self.pushButton_Import.clicked.connect(self.switch_to_preprocessing_tab)
        self.pushButton_next_to_domain.clicked.connect(self.jump_to_next_page)
        self.pushButton_Transfer_Data.clicked.connect(self.data_show)
        self.pushButton_next_to_visualisation.clicked.connect(self.jump_to_next_visualisation)

        # domian and mesh part
        self.pushButton_domain_apply.clicked.connect(self.create_domain)
        self.pushButton_mesh_save.clicked.connect(self.create_mesh)

        # inversion part
        self.pushButton_inversion_apply.clicked.connect(self.startInversion)
        self.pushButton_inversion_save.clicked.connect(self.saveFig)

        # water content part
        self.pushButton_watercontent_calculate.clicked.connect(self.showImage)
        self.doubleSpinBox_Temperature.valueChanged.connect(self.update_variable)
        self.pushButton_import_soil_field.clicked.connect(self.openTableDialog)
        self.pushButton_multiplefiles_processing.clicked.connect(self.data_processing_multiple_files)         
        
        # visualisation part
        self.pushButton_next_to_vis.clicked.connect(self.vis_res_load_local_images)
        self.pushButton_next_to_vis.clicked.connect(self.vis_wat_load_local_images)

        #Animation page of Vis-Res
        self.pushButton_vis_res_apply.clicked.connect(self.apply_Vis_Res_Ani)

        #Animation page of Vis-Wat
        self.pushButton_vis_water_apply.clicked.connect(self.apply_Vis_Wat_Ani)
        
        #next button
        self.pushButton_next_to_mesh.clicked.connect(self.next_to_mesh)
        self.pushButton_next_to_inversion.clicked.connect(self.next_to_inversion)
        self.pushButton_next_to_watercontent.clicked.connect(self.next_to_watercontent)
        self.pushButton_next_to_vis.clicked.connect(self.next_to_vis)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def next_to_mesh(self):
       index_of_page = 1

       self.tabWidget.setCurrentIndex(index_of_page)
       
    def next_to_inversion(self):
       index_of_page = 2

       self.tabWidget_Importing.setCurrentIndex(index_of_page)
    def next_to_watercontent(self):
       index_of_page = 3

       self.tabWidget_Importing.setCurrentIndex(index_of_page)
    def next_to_vis(self):
       index_of_page = 4

       self.tabWidget_Importing.setCurrentIndex(index_of_page)        
    

    def switch_to_preprocessing_tab(self):

        index_of_page = 1

        self.tabWidget_Data.setCurrentIndex(index_of_page)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Select .tx0 files", "",
                                                "TX0 Files (*.tx0);;All Files (*)", options=options)
        global save_directory
        save_directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        print(f"Selected directory: {save_directory}")
        if not save_directory:
            return
        if files:
            self.listWidget_file_list.clear()

            # Create the directory if it does not exist
            os.makedirs(save_directory, exist_ok=True)

            for file in files:
                item = QtWidgets.QListWidgetItem(file)
                item.setForeground(QColor('black'))
                self.listWidget_file_list.addItem(item)

                # Define the destination file path in the save directory
                destination_file = os.path.join(save_directory, os.path.basename(file))

                # Copy the file to the new directory and replace if it already exists
                shutil.copy(file, destination_file)

            with open(files[0], 'r') as f:
                content = f.read()

                # set the content of the file as its text
                self.textBrowser_showdata.setPlainText(content)

    def data_transfer(self):
        global save_directory
        input_folder = save_directory
        output_folder = save_directory
        os.chdir(save_directory)
        for filename in os.listdir(input_folder):
            if filename.endswith('.tx0'):

                input_file_path = os.path.join(input_folder, filename)
                output_file_name = filename.replace('.tx0', '.txt')
                output_file_path = os.path.join(output_folder, output_file_name)

                fixed_data = ["48# Number of electrodes", "# x z"] + [f"{i}     0" for i in range(48)] + [
                    "909# Number of data"]

                data = []
                with open(input_file_path, 'r') as input_file:
                    lines = input_file.readlines()
                    data = [line.strip().split() for line in lines[243:]]

                selected_data = []
                for row in data:
                    row_transformed = row.copy()
                    for i in [1, 2, 3, 4]:  
                        item = float(row[i])
                        if item >= 48:
                            row_transformed[i] = str(
                                int(item - 48))  
                        else:
                            row_transformed[i] = str(
                                int(item))  
                    selected_data.append([row_transformed[i] for i in
                                          [1, 2, 3, 4, 10]])  

                with open(output_file_path, 'w') as output_file:
                    for line in fixed_data:
                        output_file.write(line + "\n")

                    output_file.write("# a b m n rhoa\n")
                    for row in selected_data:
                        output_file.write("\t".join(row) + "\n")
                  
  

    def data_show(self):
        global save_directory
        self.data_transfer()
        os.chdir(save_directory)
        for file in os.listdir(save_directory):
            if file.endswith('.txt'):
                with open(file, 'r') as fils:
                    content = fils.read()
                    self.textBrowser_showdata.setPlainText(content)
                break

    def jump_to_next_page(self):
        index_of_page = 1

        self.tabWidget_Importing.setCurrentIndex(index_of_page)

    def jump_to_next_visualisation(self):
        index_of_page = 4

        self.tabWidget_Importing.setCurrentIndex(index_of_page)


    #domain and mesh part

    def create_domain(self):
        # Create a matrix using the values of start and end
        start_x = self.spinBox_startX.value()
        start_y = self.spinBox_startY.value()
        end_x = self.spinBox_endX.value()
        end_y = self.spinBox_endY.value()

        self.geom = pg.meshtools.createWorld(start=[start_x, end_y], end=[end_x, start_y], worldMarker=False)
        ax = self.canvas_domain.figure.add_subplot(111)
        ax.clear()

        ax.yaxis.set_major_locator(plt.MultipleLocator(2.0))

        pg.show(self.geom, ax=ax, boundary=True)
        self.canvas_domain.draw()
        
    def create_mesh(self):
        # Create a matrix using the values of quality and area
        pg.show(self.geom, boundary=True)
        quality = self.doubleSpinBox_quality.value()
        area = self.doubleSpinBox_area.value()

        self.mesh = mt.createMesh(self.geom, quality, area, smooth=True)
        ab = self.canvas_mesh.figure.add_subplot(111)
        ab.clear()
        ab.yaxis.set_major_locator(plt.MultipleLocator(2.0))

        pg.show(self.mesh, ax=ab, boundary=True)
        self.canvas_mesh.draw()


    # Function to save generated figures
    def save(self):
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.ReadOnly
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None, "Save Figure", "", "PNG Files (*.png);;All Files (*)", options=options
            )
            if file_name:
                    # Save the figure as a PNG file
                    self.geom.savefig(file_name, format="png")

    #inversion part
    #single file process
    def startInversion(self):
        global save_directory
        # Read the values from the spin boxes
        maxIter = self.spinBox_Iterations.value()
        lam = self.spinBox_Lambda.value()
        dPhi = self.spinBox_dPhi.value()

        print(f"Using directory: {save_directory}")
    
        file_to_convert = None  
        os.chdir(save_directory)
        for file in os.listdir(save_directory):
           if file.endswith('.txt'):
               file_to_convert = file
               break

        #Create Geometry and Mesh
        geom = self.geom
        mesh = self.mesh

        # Inversion preparing 
        date = os.path.basename(file_to_convert)  # Extract the file name from the path
        self.date = date
        mgr = ert.ERTManager(file_to_convert, verbose=True, debug=True)
        self.mgr = mgr
        rhoa = np.array(mgr.data['rhoa'])
        Argw = np.argwhere(rhoa <= 0)
        pg.info('Filtered rhoa (min/max)', min(mgr.data['rhoa']), max(mgr.data['rhoa']))
        Accur = (1 - np.shape(Argw)[0] / np.shape(rhoa)[0]) * 100

        # Data processing Filter negative value
        mgr.data.remove(mgr.data["rhoa"] < 0)

        # Add estimated Error and geometrical factor
        mgr.data['err'] = ert.estimateError(mgr.data, absoluteError=0.001, relativeError=0.03)
        pg.info('Filtered rhoa (min/max)', min(mgr.data['rhoa']), max(mgr.data['rhoa']))
        mgr.data['k'] = ert.createGeometricFactors(mgr.data, numerical=True)
        #ert.show(mgr.data)

        # Inversion here
        inv = mgr.invert(mesh=mesh, lam=lam, maxIter=maxIter, dPhi=dPhi, CHI1OPT=5, Verbose=True)

        # Storing and saving data for later manipulation
        Storage = np.zeros([np.shape(mesh.cellMarkers())[0], 1])
        Storage[:, 0] = inv
        self.Storage = Storage
        mgr.saveResult(date[:-4])

        # Plotting
        fig1, (ax1) = plt.subplots(1, sharex=True, figsize=(16.0, 5))
        mgr.showResult(ax=ax1, cMin=50, cMax=15000)
        labels = date
        ax1.set_xlim(0, mgr.paraDomain.xmax())
        ax1.set_ylim(-8, mgr.paraDomain.ymax())
        ax1.set_title(labels)
        plt.tight_layout()
        # automatic save
        plt.savefig("result_res.jpg")

        #plt.show()
        self.canvas = FigureCanvas(fig1) 
        self.inversion_result_layout.addWidget(self.canvas)  

        # update the plot showing and save the fig1 for function saveFig later
        self.inversion_result_widget.update()
        self.fig1 = fig1

    def saveFig(self):
        # Prompt the user to select a location for saving the figure
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
        None, "Save Figure", "", "PNG Files (*.png);;All Files (*)", options=options
        )

        if file_name:
            self.fig1.savefig(file_name, format="png")  # Use the fig1 object obtained from startInversion   

    #water content part
    
    def showImage(self):
            # Invoke the Water Content Calculation Function
            print(tem_field)
            try:
                    self.watercomputing()
            except Exception as e:
                    print("An error occurred:", e)
            #The above functions will draw the results and save them as a specified name in JPG format, displaying the result image on the canvas
            image_path = "result_wat.jpg"
            pixmap = QPixmap(image_path)
            # Retrieve the Canvas Dimensions
            canvas_width = 765
            canvas_height = 600

            scaled_pixmap = pixmap.scaled(canvas_width, canvas_height, QtCore.Qt.KeepAspectRatio)

            pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
            self.scene.clear()
            self.scene.addItem(pixmap_item)
            self.scene.setSceneRect(pixmap_item.boundingRect())

    def watercomputing(self):
            geom = self.geom
            mesh = self.mesh
            print("mesh", mesh)
            centers = mesh.cellCenters()
            x_coordinates = centers[:, 0]
            y_coordinates = centers[:, 1]
            np.shape(centers)
            print("x_coordinates", x_coordinates)
            print("y_coordinates", y_coordinates)
            
            Storage = self.Storage
            fSWC = lambda x: 246.47 * x ** (-0.627)
            fSWC_2 = lambda x: 211 * x ** (-0.59)
            
            
            global tem_field
            print("t111111111111111",tem_field)
            temperature_points = tem_field
            T = 25.5
            temperature_points.sort(key=lambda x: x[0])
            for j in range(len(y_coordinates) - 1):
                    y = y_coordinates[j]
                    for i in range(len(temperature_points) - 1):
                            y1, T1 = temperature_points[i]
                            y2, T2 = temperature_points[i + 1]
                            if y1 <= y <= y2:
                                    T = T1 + (T2 - T1) * ((y - y1) / (y2 - y1))
                                    break
                            else:
                                    T = T1 if y < y1 else T2
                    Storage[j, :] = (1 + 0.025 * (T - 25)) * Storage[j, :]


            SWC = fSWC(Storage)

            print("11111111111")
            print(Storage)

            fig1, (ax1) = plt.subplots(1, sharex=(True), figsize=(15.5, 7), gridspec_kw={'height_ratios': [2]})
            pg.viewer.show(mesh=mesh, data=SWC[:, 0], hold=True, label='Soil water content', ax=ax1, cMin=0,
                           cMax=30,
                           cMap='Spectral', showMesh=True)
            print("12321321131321")

            labels = self.date
            ax1.set_xlim(-0, self.mgr.paraDomain.xmax())
            ax1.set_ylim(-8, self.mgr.paraDomain.ymax())
            ax1.set_title(labels)
            plt.savefig('result_wat.jpg')
            plt.close()
            print("end")


            

    
    def update_variable(self, value):
        self.my_variable = value
        global tem
        tem = self.my_variable
        global tem_field
        tem_field=[(0,tem)]
        print(f"Updated variable: {self.my_variable}")

    def openTableDialog(self):
            print("11111111111")
            dialog = TableDialog(self.Water_content)
            print("122112")
            dialog.exec_()  
            print("2222222")   
            
    def data_processing_multiple_files(self):
        global save_directory
        os.chdir(save_directory)
        for file in os.listdir(save_directory):
            if file.endswith('.txt'):
                
                
                file_to_convert = file
                start_x = self.spinBox_startX.value()
                start_y = self.spinBox_startY.value()
                end_x = self.spinBox_endX.value()
                end_y = self.spinBox_endY.value()

                self.geom = pg.meshtools.createWorld(start=[start_x, end_y], end=[end_x, start_y], worldMarker=False)
                ax = self.canvas_domain.figure.add_subplot(111)
                ax.clear()

                ax.yaxis.set_major_locator(plt.MultipleLocator(2.0))

                pg.show(self.geom, ax=ax, boundary=True)
                self.canvas_domain.draw()
                pg.show(self.geom, boundary=True)
                quality = self.doubleSpinBox_quality.value()
                area = self.doubleSpinBox_area.value()

                self.mesh = mt.createMesh(self.geom, quality, area, smooth=True)
                ab = self.canvas_mesh.figure.add_subplot(111)
                ab.clear()

                ab.yaxis.set_major_locator(plt.MultipleLocator(2.0))

                pg.show(self.mesh, ax=ab, boundary=True)
                self.canvas_mesh.draw()

                maxIter = self.spinBox_Iterations.value()
                lam = self.spinBox_Lambda.value()
                dPhi = self.spinBox_dPhi.value()
                geom = self.geom
                mesh = self.mesh
                
                # Inversion preparing 
                date = os.path.basename(file_to_convert)  # Extract the file name from the path
                self.date = date
                mgr = ert.ERTManager(file_to_convert, verbose=True, debug=True)
                self.mgr = mgr
                rhoa = np.array(mgr.data['rhoa'])
                Argw = np.argwhere(rhoa <= 0)
                pg.info('Filtered rhoa (min/max)', min(mgr.data['rhoa']), max(mgr.data['rhoa']))
                Accur = (1 - np.shape(Argw)[0] / np.shape(rhoa)[0]) * 100

                # Data processing Filter negative value
                mgr.data.remove(mgr.data["rhoa"] < 0)

                # Add estimated Error and geometrical factor
                mgr.data['err'] = ert.estimateError(mgr.data, absoluteError=0.001, relativeError=0.03)
                pg.info('Filtered rhoa (min/max)', min(mgr.data['rhoa']), max(mgr.data['rhoa']))
                mgr.data['k'] = ert.createGeometricFactors(mgr.data, numerical=True)
                #ert.show(mgr.data)

                # Inversion here
                inv = mgr.invert(mesh=mesh, lam=lam, maxIter=maxIter, dPhi=dPhi, CHI1OPT=5, Verbose=True)

                # Storing and saving data for later manipulation
                Storage = np.zeros([np.shape(mesh.cellMarkers())[0], 1])
                Storage[:, 0] = inv
                self.Storage = Storage
                mgr.saveResult(date[:-4])

                # Plotting
                fig1, (ax1) = plt.subplots(1, sharex=True, figsize=(16.0, 5))
                mgr.showResult(ax=ax1, cMin=50, cMax=15000)
                labels = date
                ax1.set_xlim(0, mgr.paraDomain.xmax())
                ax1.set_ylim(-8, mgr.paraDomain.ymax())
                ax1.set_title(labels)
                plt.tight_layout()
                # automatic save
                base_name = os.path.splitext(file_to_convert)[0]
                new_name_res = base_name +'_res.jpg'
                plt.savefig(new_name_res)

                print("mesh", mesh)
                centers = mesh.cellCenters()
                x_coordinates = centers[:, 0]
                y_coordinates = centers[:, 1]
                np.shape(centers)
                print("x_coordinates", x_coordinates)
                print("y_coordinates", y_coordinates)

                Storage = self.Storage
                fSWC = lambda x: 246.47 * x ** (-0.627)
                fSWC_2 = lambda x: 211 * x ** (-0.59)


                global tem_field
                print("t111111111111111",tem_field)
                temperature_points = tem_field
                T = 25.5
                temperature_points.sort(key=lambda x: x[0])
                for j in range(len(y_coordinates) - 1):
                        y = y_coordinates[j]
                        # Find the temperature segment the current belongs to
                        for i in range(len(temperature_points) - 1):
                                y1, T1 = temperature_points[i]
                                y2, T2 = temperature_points[i + 1]
                                if y1 <= y <= y2:
                                        # Linearly interpolate the temperature value
                                        T = T1 + (T2 - T1) * ((y - y1) / (y2 - y1))
                                        break
                                else:
                                        # If y is out of bounds of the temperature points, use the nearest boundary value
                                        T = T1 if y < y1 else T2
                        Storage[j, :] = (1 + 0.025 * (T - 25)) * Storage[j, :]


                SWC = fSWC(Storage)

                print("11111111111")
                print(Storage)

                fig1, (ax1) = plt.subplots(1, sharex=(True), figsize=(15.5, 7), gridspec_kw={'height_ratios': [2]})
                pg.viewer.show(mesh=mesh, data=SWC[:, 0], hold=True, label='Soil water content', ax=ax1, cMin=0,
                               cMax=30,
                               cMap='Spectral', showMesh=True)
                print("12321321131321")

                labels = self.date
                ax1.set_xlim(-0, self.mgr.paraDomain.xmax())
                ax1.set_ylim(-8, self.mgr.paraDomain.ymax())
                ax1.set_title(labels)
                new_name_wat = base_name +'_wat.jpg'
                plt.savefig(new_name_wat)
                plt.close()
                print("end")
        print('s')
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Import.setText(_translate("MainWindow", "Import"))
        self.pushButton_Import.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>load your data file and jump to data pre_processing page</p></body></html>"))
        self.pushButton_importfile.setText(_translate("MainWindow", "Choose your file"))
        self.pushButton_importfile.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Choose your file or files to upload, only .tx0 files will be reveiced</p></body></html>"))
        self.tabWidget_Data.setTabText(self.tabWidget_Data.indexOf(self.Data), _translate("MainWindow", "Data"))
        self.pushButton_Transfer_Data.setText(_translate("MainWindow", "Transfer Data"))
        self.pushButton_Transfer_Data.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Transfer your .tx0 raw data files to .txt files</p></body></html>"))
        self.pushButton_next_to_visualisation.setText(_translate("MainWindow", "tips for multiple files"))
        self.pushButton_next_to_visualisation.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>If you plan to process multiple files, you need next button to each tab to set the parameter. And click next button until to water content page, and click button Multiplefiles_processing </p></body></html>"))
        self.pushButton_next_to_domain.setText(_translate("MainWindow", "Next-single file"))
        self.tabWidget_Data.setTabText(self.tabWidget_Data.indexOf(self.Pre_processing),
                                       _translate("MainWindow", "Pre_processing"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Importing),
                                            _translate("MainWindow", "Importing"))
        self.pushButton_domain_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_domain_apply.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p>Press the button to generate a domain</p></body></html>"))
        self.pushButton_next_to_mesh.setText(_translate("MainWindow", "Next"))
        self.pushButton_next_to_mesh.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p>Press the button to the next step</p></body></html>"))
        self.pushButton_domain_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_domain_save.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Save the figure to your local directory</p></body></html>"))
        self.label_start.setText(_translate("MainWindow", "Start"))
        self.label_start.setToolTip(_translate("MainWindow",
                                             "<html><head/><body><p>The starting point of the domain. The position of the x-axis and y-axis are typically set to 0.</p></body></html>"))
        self.label_end.setText(_translate("MainWindow", "End"))
        self.label_end.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>The ending point of the domain. The position of the x-axis is typically set to 47, y-axis is typically set to -8.</p></body></html>"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Domain), _translate("MainWindow", "Domain"))
        self.label_quality.setText(_translate("MainWindow", "Quality"))
        self.label_quality.setToolTip(_translate("MainWindow",

                                               "<html><head/><body><p>Determine the grid quality, including element shape, size, and smoothness</p></body></html>"))
        self.label_area.setText(_translate("MainWindow", "Area"))
        self.label_area.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p>Control the area of individual mesh elements</p></body></html>"))
        
        self.pushButton_mesh_save.setText(_translate("MainWindow", "Apply"))
        self.pushButton_next_to_inversion.setText(_translate("MainWindow", "Next"))
        self.pushButton_next_to_inversion.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p>Press the button to the next step</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Mesh), _translate("MainWindow", "Mesh"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Domain_Mesh),
                                            _translate("MainWindow", "Domain and Mesh"))
        self.pushButton_inversion_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_inversion_save.setText(_translate("MainWindow", "Save"))
        self.label_Lambda.setText(_translate("MainWindow", "Lambda"))
        self.label_Lambda.setToolTip("Lambda controls the smoothness of the inverted model.<br> It helps prevent overfitting by penalizing complex models.")
        self.label_dPhi.setText(_translate("MainWindow", "Delta Phi"))
        self.pushButton_next_to_watercontent.setText(_translate("MainWindow", "Next"))
        
        
        self.label_iterations.setText(_translate("MainWindow", "Iterations"))
        self.label_iterations.setToolTip("Maximum number of iterations for the inversion algorithm.<br>")
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Inversion),
                                            _translate("MainWindow", "Inversion"))
        self.pushButton_watercontent_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_watercontent_calculate.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>After configuring the temperature field, click to start water content calculation based on resistivity.</p></body></html>"))
        
        self.label_Temperature.setText(_translate("MainWindow", "Temperature"))
        self.label_Temperature.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p>Set constant soil temperature, default is 25°C</p></body></html>"))
        self.pushButton_next_to_vis.setText(_translate("MainWindow", "Next"))
        self.pushButton_multiplefiles_processing.setText(_translate("MainWindow", "Multiplefiles_processing"))
        self.pushButton_multiplefiles_processing.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p>When you finish parameter setting, click this botton to start multiple files processing</p></body></html>"))
        
        self.pushButton_import_soil_field.setText(_translate("MainWindow", "Import Soil Temperatue Field"))
        self.pushButton_import_soil_field.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p> Click to open an editable table, enter temperature data from real sensors. First column is sensor depth, second column is temperature at that depth. </p></body></html>"))
        
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Water_content),
                                            _translate("MainWindow", "Water Content"))

        
        self.radioButton_vis_res_ani.setText(_translate("MainWindow", "Time Lapse Animation"))
        self.radioButton_vis_res_ani.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>visualisation Processing for Resistivity Image Files</p></body></html>"))
        
        self.label_resistivity_file.setText(_translate("MainWindow", "File Selection"))
        self.label_resistivity_file.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>After selecting one or more files, click Apply</p></body></html>"))
        
        self.pushButton_vis_res_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_vis_res_apply.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Generating a GIF file and automatically saved to the current local folder</p></body></html>"))
        
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Vis_resistivity),
                                    _translate("MainWindow", "Resistivity"))

        
        self.radioButton_vis_water_ani.setText(_translate("MainWindow", "Time Lapse Animation"))
        self.radioButton_vis_water_ani.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>visualisation Processing for Resistivity Image Files</p></body></html>"))
        
        self.label_water_file.setText(_translate("MainWindow", "File Selection"))
        self.label_water_file.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>After selecting one or more files, click Apply</p></body></html>"))
        
        self.pushButton_vis_water_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_vis_water_apply.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Generating a GIF file and automatically saved to the current local folder</p></body></html>"))
        
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Vis_water_content),
                                    _translate("MainWindow", "Water content"))

        
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.visualisation),
                                            _translate("MainWindow", "visualisation"))

        
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionGuidline.setText(_translate("MainWindow", "Guidline"))
        self.actionContract.setText(_translate("MainWindow", "Contract"))

    #water content part2
class TableDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("000000000")

        self.setWindowTitle('Editable Table Dialog')

        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setEditTriggers(QtWidgets.QTableWidget.AllEditTriggers)

        self.button = QtWidgets.QPushButton('Get Values', self)
        self.button.setGeometry(50, 220, 100, 30)
        try:
            self.button.clicked.connect(self.getValues)
        except Exception as e:
            print("An error occurred:", e)
            
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.button)

        
        self.setLayout(layout)
    def getValues(self):
        values = []
        global tem_field
        tem_field = []
        
        for row in range(self.table_widget.rowCount()):
            row_values = []
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if item is not None:
                    row_values.append(item.text())
                else:
                    row_values.append('')
            values.append(row_values)

        # tem_field=[]
        for row in values:
            print(float(row[0]))
            tem_field.append((float(row[0]),float(row[1])))

        print(tem_field)
        
class MyMainWindow_Vis(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow_Vis, self).__init__(parent)
        self.setupUi(self)

        self.timer = QTimer(self)

        self.scene_Vis_Res_Ani = QtWidgets.QGraphicsScene(self)
        self.scene_Vis_Wat_Ani = QtWidgets.QGraphicsScene(self)


    def vis_res_load_local_images(self):
        global save_directory
        os.chdir(save_directory)
        for file_name in os.listdir(save_directory):
            if file_name.endswith('_res.jpg'):
                self.listWidget_vis_res_pic.addItem(file_name)


    def vis_wat_load_local_images(self):
        global save_directory
        for file_name in os.listdir(save_directory):
            if file_name.endswith('_wat.jpg'):
                self.listWidget_vis_water_pic.addItem(file_name)


    def apply_Vis_Res_Ani(self):
            self.refreshFileList
            selected_files = sorted([item.text() for item in self.listWidget_vis_res_pic.selectedItems()],
                                    key=lambda x: x.split('_')[0])

            now = datetime.now()
            timestamp_str = now.strftime('%Y%m%d_%H%M%S')
            filename = f'animation_{timestamp_str}.gif'
            with imageio.get_writer(filename, mode='I', duration=0.5) as writer:
                    for file in selected_files:
                            image = imageio.v2.imread(file)
                            writer.append_data(image)

            self.viewer = AnimatedGIFViewer(filename, self)
            self.viewer.show()
    def apply_Vis_Wat_Ani(self):
            self.refreshFileList
            selected_files = sorted([item.text() for item in self.listWidget_vis_water_pic.selectedItems()],
                                    key=lambda x: x.split('_')[0])

            now = datetime.now()
            timestamp_str = now.strftime('%Y%m%d_%H%M%S')
            filename = f'animation_{timestamp_str}.gif'
            with imageio.get_writer(filename, mode='I', duration=0.5) as writer:
                    for file in selected_files:
                            image = imageio.v2.imread(file)
                            writer.append_data(image)

            self.viewer = AnimatedGIFViewer(filename, self)
            self.viewer.show()

    def refreshFileList(self):
        global save_directory
        self.listWidget_vis_res_pic_.clear()
        self.listWidget_vis_water_pic.clear()

        for file_name in os.listdir(save_directory):
                if file_name.endswith('_res.jpg'):
                        self.listWidget_vis_res_pic.addItem(file_name)
                elif file_name.endswith('_wat.jpg'):
                        self.listWidget_vis_water_pic.addItem(file_name)


class AnimatedGIFViewer(QGraphicsView):
    def __init__(self, gif_path, scene, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
 
        self.gif_reader = QImageReader(gif_path)

        scale_factor = 0.50
        scaled_width = int(self.gif_reader.size().width() * scale_factor)
        scaled_height = int(self.gif_reader.size().height() * scale_factor)

        self.frames = [QPixmap.fromImage(self.gif_reader.read()).scaled(scaled_width, scaled_height) for _ in
                       range(self.gif_reader.imageCount())]
        self.current_frame = 0

        self.pixmap_item = self.scene.addPixmap(self.frames[self.current_frame])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_frame)
        self.timer.start(400)  

    def next_frame(self):
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.pixmap_item.setPixmap(self.frames[self.current_frame])


class MyMainWindow(MyMainWindow_Vis):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
