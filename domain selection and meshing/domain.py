import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 660)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalWidget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_Importing = QtWidgets.QTabWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget_Importing.sizePolicy().hasHeightForWidth()
        )
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
        self.tabWidget_Data.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "border-top-color: rgb(0, 0, 0);"
        )
        self.tabWidget_Data.setObjectName("tabWidget_Data")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.listWidget_file_list = QtWidgets.QListWidget(self.Data)
        self.listWidget_file_list.setGeometry(QtCore.QRect(130, 20, 461, 451))
        self.listWidget_file_list.setStyleSheet("background: rgb(255, 255, 255)")
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
        self.pushButton_next_to_visualization = QtWidgets.QPushButton(
            self.Pre_processing
        )
        self.pushButton_next_to_visualization.setGeometry(
            QtCore.QRect(605, 459, 146, 32)
        )
        self.pushButton_next_to_visualization.setObjectName(
            "pushButton_next_to_visualization"
        )
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
        self.spinBox_startX.setMinimum(0)
        self.spinBox_startX.setMaximum(99)
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
        self.pushButton_domain_apply.clicked.connect(self.create_domain)

        self.pushButton_next_to_mesh = QtWidgets.QPushButton(self.Domain)
        self.pushButton_next_to_mesh.setGeometry(QtCore.QRect(530, 430, 71, 32))
        self.pushButton_next_to_mesh.setObjectName("pushButton_next_to_mesh")
        self.pushButton_domain_save = QtWidgets.QPushButton(self.Domain)
        self.pushButton_domain_save.setGeometry(QtCore.QRect(110, 430, 73, 32))
        self.pushButton_domain_save.setObjectName("pushButton_domain_save")
        self.label_start = QtWidgets.QLabel(self.Domain)
        self.label_start.setGeometry(QtCore.QRect(117, 20, 41, 21))
        self.label_start.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_start.setObjectName("label_start")
        self.label_end = QtWidgets.QLabel(self.Domain)
        self.label_end.setGeometry(QtCore.QRect(117, 50, 41, 21))
        self.label_end.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_end.setObjectName("label_end")
        self.spinBox_endX = QtWidgets.QSpinBox(self.Domain)
        self.spinBox_endX.setGeometry(QtCore.QRect(210, 50, 40, 20))
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
        self.label_quality.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_quality.setObjectName("label_quality")
        self.label_area = QtWidgets.QLabel(self.Mesh)
        self.label_area.setGeometry(QtCore.QRect(120, 50, 51, 21))
        self.label_area.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_area.setObjectName("label_area")
        self.doubleSpinBox_quality = QtWidgets.QDoubleSpinBox(self.Mesh)
        self.doubleSpinBox_quality.setGeometry(QtCore.QRect(210, 20, 62, 21))
        self.doubleSpinBox_quality.setObjectName("doubleSpinBox_quality")
        self.doubleSpinBox_quality.setMinimum(15.0)
        self.doubleSpinBox_quality.setMaximum(50.0)
        self.doubleSpinBox_area = QtWidgets.QDoubleSpinBox(self.Mesh)
        self.doubleSpinBox_area.setGeometry(QtCore.QRect(210, 50, 62, 21))
        self.doubleSpinBox_area.setObjectName("doubleSpinBox_area")
        self.doubleSpinBox_area.setMaximum(1.0)
        self.doubleSpinBox_area.setSingleStep(0.01)
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
        self.pushButton_mesh_save.clicked.connect(self.create_mesh)

        self.pushButton_next_to_inversion = QtWidgets.QPushButton(self.Mesh)
        self.pushButton_next_to_inversion.setGeometry(QtCore.QRect(530, 430, 71, 32))
        self.pushButton_next_to_inversion.setObjectName("pushButton_next_to_inversion")
        self.pushButton_domain_apply_2 = QtWidgets.QPushButton(self.Mesh)
        self.pushButton_domain_apply_2.setGeometry(QtCore.QRect(500, 20, 101, 51))
        self.pushButton_domain_apply_2.setObjectName("pushButton_domain_apply_2")
        self.tabWidget.addTab(self.Mesh, "")

        self.tabWidget_Importing.addTab(self.Domain_Mesh, "")
        self.Inversion = QtWidgets.QWidget()
        self.Inversion.setObjectName("Inversion")
        self.pushButton_inversion_apply = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_inversion_apply.setGeometry(QtCore.QRect(470, 30, 111, 51))
        self.pushButton_inversion_apply.setObjectName("pushButton_inversion_apply")
        self.pushButton_inversion_save = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_inversion_save.setGeometry(QtCore.QRect(150, 450, 71, 31))
        self.pushButton_inversion_save.setObjectName("pushButton_inversion_save")
        self.label_Lambda = QtWidgets.QLabel(self.Inversion)
        self.label_Lambda.setGeometry(QtCore.QRect(250, 50, 61, 16))
        self.label_Lambda.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_Lambda.setObjectName("label_Lambda")
        self.label_dPhi = QtWidgets.QLabel(self.Inversion)
        self.label_dPhi.setGeometry(QtCore.QRect(250, 80, 61, 16))
        self.label_dPhi.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);\n"
            "text-align: center;"
        )
        self.label_dPhi.setObjectName("label_dPhi")
        self.graphicsView_inversion = QtWidgets.QGraphicsView(self.Inversion)
        self.graphicsView_inversion.setGeometry(QtCore.QRect(140, 120, 511, 311))
        self.graphicsView_inversion.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.graphicsView_inversion.setObjectName("graphicsView_inversion")
        self.pushButton_next_to_watercontent = QtWidgets.QPushButton(self.Inversion)
        self.pushButton_next_to_watercontent.setGeometry(QtCore.QRect(560, 450, 71, 32))
        self.pushButton_next_to_watercontent.setObjectName(
            "pushButton_next_to_watercontent"
        )
        self.spinBox_Iterations = QtWidgets.QSpinBox(self.Inversion)
        self.spinBox_Iterations.setGeometry(QtCore.QRect(330, 20, 40, 20))
        self.spinBox_Iterations.setProperty("value", 5)
        self.spinBox_Iterations.setObjectName("spinBox_Iterations")
        self.spinBox_dPhi = QtWidgets.QSpinBox(self.Inversion)
        self.spinBox_dPhi.setGeometry(QtCore.QRect(330, 80, 40, 20))
        self.spinBox_dPhi.setProperty("value", 1)
        self.spinBox_dPhi.setObjectName("spinBox_dPhi")
        self.spinBox_Lambda = QtWidgets.QSpinBox(self.Inversion)
        self.spinBox_Lambda.setGeometry(QtCore.QRect(330, 50, 40, 20))
        self.spinBox_Lambda.setProperty("value", 5)
        self.spinBox_Lambda.setObjectName("spinBox_Lambda")
        self.label_iterations = QtWidgets.QLabel(self.Inversion)
        self.label_iterations.setGeometry(QtCore.QRect(250, 20, 61, 16))
        self.label_iterations.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
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
        self.pushButton_watercontent_calculate = QtWidgets.QPushButton(
            self.Water_content
        )
        self.pushButton_watercontent_calculate.setGeometry(
            QtCore.QRect(150, 450, 81, 31)
        )
        self.pushButton_watercontent_calculate.setObjectName(
            "pushButton_watercontent_calculate"
        )
        self.label_Temperature = QtWidgets.QLabel(self.Water_content)
        self.label_Temperature.setGeometry(QtCore.QRect(240, 50, 91, 16))
        self.label_Temperature.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_Temperature.setObjectName("label_Temperature")
        self.graphicsView_watercontent = QtWidgets.QGraphicsView(self.Water_content)
        self.graphicsView_watercontent.setGeometry(QtCore.QRect(140, 120, 511, 311))
        self.graphicsView_watercontent.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.graphicsView_watercontent.setObjectName("graphicsView_watercontent")
        self.pushButton_next_to_vis = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_next_to_vis.setGeometry(QtCore.QRect(560, 450, 71, 32))
        self.pushButton_next_to_vis.setObjectName("pushButton_next_to_vis")
        self.pushButton_import_soil_field = QtWidgets.QPushButton(self.Water_content)
        self.pushButton_import_soil_field.setGeometry(QtCore.QRect(460, 40, 201, 31))
        self.pushButton_import_soil_field.setObjectName("pushButton_import_soil_field")
        self.tabWidget_Importing.addTab(self.Water_content, "")
        self.Visualization = QtWidgets.QWidget()
        self.Visualization.setObjectName("Visualization")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Visualization)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.Visualization)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.Vis_resistivity = QtWidgets.QWidget()
        self.Vis_resistivity.setObjectName("Vis_resistivity")
        self.radioButton_vis_res_ani = QtWidgets.QRadioButton(self.Vis_resistivity)
        self.radioButton_vis_res_ani.setGeometry(QtCore.QRect(120, 10, 161, 20))
        self.radioButton_vis_res_ani.setObjectName("radioButton_vis_res_ani")
        self.label_resistivity_file = QtWidgets.QLabel(self.Vis_resistivity)
        self.label_resistivity_file.setGeometry(QtCore.QRect(120, 40, 91, 21))
        self.label_resistivity_file.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);"
        )
        self.label_resistivity_file.setObjectName("label_resistivity_file")
        self.listView_vis_res_pic = QtWidgets.QListView(self.Vis_resistivity)
        self.listView_vis_res_pic.setGeometry(QtCore.QRect(120, 70, 171, 281))
        self.listView_vis_res_pic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView_vis_res_pic.setObjectName("listView_vis_res_pic")
        self.pushButton_vis_res_apply = QtWidgets.QPushButton(self.Vis_resistivity)
        self.pushButton_vis_res_apply.setGeometry(QtCore.QRect(120, 360, 171, 31))
        self.pushButton_vis_res_apply.setObjectName("pushButton_vis_res_apply")
        self.graphicsView_vis_resistivity = QtWidgets.QGraphicsView(
            self.Vis_resistivity
        )
        self.graphicsView_vis_resistivity.setGeometry(QtCore.QRect(300, 70, 331, 281))
        self.graphicsView_vis_resistivity.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
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
        self.listView_vis_water_pic = QtWidgets.QListView(self.Vis_water_content)
        self.listView_vis_water_pic.setGeometry(QtCore.QRect(120, 70, 171, 281))
        self.listView_vis_water_pic.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.listView_vis_water_pic.setObjectName("listView_vis_water_pic")
        self.pushButton_vis_water_apply = QtWidgets.QPushButton(self.Vis_water_content)
        self.pushButton_vis_water_apply.setGeometry(QtCore.QRect(120, 360, 171, 31))
        self.pushButton_vis_water_apply.setObjectName("pushButton_vis_water_apply")
        self.graphicsView_vis_watercontent = QtWidgets.QGraphicsView(
            self.Vis_water_content
        )
        self.graphicsView_vis_watercontent.setGeometry(QtCore.QRect(300, 70, 331, 281))
        self.graphicsView_vis_watercontent.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.graphicsView_vis_watercontent.setObjectName(
            "graphicsView_vis_watercontent"
        )
        self.tabWidget_3.addTab(self.Vis_water_content, "")
        self.horizontalLayout_5.addWidget(self.tabWidget_3)
        self.tabWidget_Importing.addTab(self.Visualization, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_Importing)
        self.verticalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 22))
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
        self.tabWidget_Importing.setCurrentIndex(1)
        self.tabWidget_Data.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.pushButton_importfile.clicked.connect(self.listWidget_file_list.clear)  # type: ignore
        self.pushButton_Import.clicked.connect(self.tabWidget_Data.close)  # type: ignore
        self.pushButton_next_to_domain.clicked.connect(self.tabWidget_Importing.close)  # type: ignore
        self.pushButton_Transfer_Data.clicked.connect(self.textBrowser_showdata.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_domain(self):
        # Create a matrix using the values of start and end
        start_x = self.spinBox_startX.value()
        start_y = self.spinBox_startY.value()
        end_x = self.spinBox_endX.value()
        end_y = self.spinBox_endY.value()

        self.geom = pg.meshtools.createWorld(
            start=[start_x, end_y], end=[end_x, start_y], worldMarker=False
        )
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Import.setText(_translate("MainWindow", "Import"))
        self.pushButton_importfile.setText(_translate("MainWindow", "Choose your file"))
        self.tabWidget_Data.setTabText(
            self.tabWidget_Data.indexOf(self.Data), _translate("MainWindow", "Data")
        )
        self.pushButton_Transfer_Data.setText(_translate("MainWindow", "Transfer Data"))
        self.pushButton_next_to_visualization.setText(
            _translate("MainWindow", "Next-multiple file")
        )
        self.pushButton_next_to_domain.setText(
            _translate("MainWindow", "Next-single file")
        )
        self.tabWidget_Data.setTabText(
            self.tabWidget_Data.indexOf(self.Pre_processing),
            _translate("MainWindow", "Pre_processing"),
        )
        self.tabWidget_Importing.setTabText(
            self.tabWidget_Importing.indexOf(self.Importing),
            _translate("MainWindow", "Importing"),
        )
        self.pushButton_domain_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_next_to_mesh.setText(_translate("MainWindow", "Next"))
        self.pushButton_domain_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_domain_save.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Save the figure to your local directory</p></body></html>",
            )
        )
        self.label_start.setText(_translate("MainWindow", "Start"))
        self.label_start.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>The starting point of the domain. The position of the x-axis and y-axis are typically set to 0.</p></body></html>",
            )
        )
        self.label_end.setText(_translate("MainWindow", "End"))
        self.label_end.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>The ending point of the domain. The position of the x-axis is typically set to 47, y-axis is typically set to -8.</p></body></html>",
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Domain), _translate("MainWindow", "Domain")
        )
        self.label_quality.setText(_translate("MainWindow", "Quality"))
        self.label_quality.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Determine the grid quality, including element shape, size, and smoothness</p></body></html>",
            )
        )
        self.label_area.setText(_translate("MainWindow", "Area"))
        self.label_area.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Control the area of individual mesh elements</p></body></html>",
            )
        )
        self.pushButton_mesh_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_next_to_inversion.setText(_translate("MainWindow", "Next"))
        self.pushButton_domain_apply_2.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Mesh), _translate("MainWindow", "Mesh")
        )
        self.tabWidget_Importing.setTabText(
            self.tabWidget_Importing.indexOf(self.Domain_Mesh),
            _translate("MainWindow", "Domain and Mesh"),
        )
        self.pushButton_inversion_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_inversion_save.setText(_translate("MainWindow", "Save"))
        self.label_Lambda.setText(_translate("MainWindow", "Lambda"))
        self.label_dPhi.setText(_translate("MainWindow", "dPhi"))
        self.pushButton_next_to_watercontent.setText(_translate("MainWindow", "Next"))
        self.label_iterations.setText(_translate("MainWindow", "Iterations"))
        self.tabWidget_Importing.setTabText(
            self.tabWidget_Importing.indexOf(self.Inversion),
            _translate("MainWindow", "Inversion"),
        )
        self.pushButton_watercontent_calculate.setText(
            _translate("MainWindow", "Calculate")
        )
        self.label_Temperature.setText(_translate("MainWindow", "Temperature"))
        self.pushButton_next_to_vis.setText(_translate("MainWindow", "Next"))
        self.pushButton_import_soil_field.setText(
            _translate("MainWindow", "Import Soil Temperatue Field")
        )
        self.tabWidget_Importing.setTabText(
            self.tabWidget_Importing.indexOf(self.Water_content),
            _translate("MainWindow", "Water Content"),
        )
        self.radioButton_vis_res_ani.setText(
            _translate("MainWindow", "Time Lapse Animation")
        )
        self.label_resistivity_file.setText(_translate("MainWindow", "File Selection"))
        self.pushButton_vis_res_apply.setText(_translate("MainWindow", "Apply"))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.Vis_resistivity),
            _translate("MainWindow", "Resistivity"),
        )
        self.radioButton_vis_water_ani.setText(
            _translate("MainWindow", "Time Lapse Animation")
        )
        self.label_water_file.setText(_translate("MainWindow", "File Selection"))
        self.pushButton_vis_water_apply.setText(_translate("MainWindow", "Apply"))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.Vis_water_content),
            _translate("MainWindow", "Water content"),
        )
        self.tabWidget_Importing.setTabText(
            self.tabWidget_Importing.indexOf(self.Visualization),
            _translate("MainWindow", "Visualization"),
        )
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
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
