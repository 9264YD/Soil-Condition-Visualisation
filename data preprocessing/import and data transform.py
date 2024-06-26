from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QColor
import os
import shutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 720)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # stylesheet to change background colour
        self.centralwidget.setStyleSheet("QTabBar::tab:selected {\n"
                                         "    background: lightblue;\n"
                                         "    color: black;\n"
                                         "}\n"
                                         "QTabBar::tab:!selected {\n"
                                         "    background: lightgray;\n"
                                         "    color: black;\n"
                                         "}")
        # arrange widgets by change their layout
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
        self.gridLayout = QtWidgets.QGridLayout(self.Data)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_file_list = QtWidgets.QListWidget(self.Data)
        self.listWidget_file_list.setStyleSheet("background: rgb(255, 255, 255)")
        self.listWidget_file_list.setObjectName("listWidget_file_list")
        self.gridLayout.addWidget(self.listWidget_file_list, 1, 0, 1, 1)
        self.pushButton_Import = QtWidgets.QPushButton(self.Data)
        self.pushButton_Import.setObjectName("pushButton_Import")
        self.gridLayout.addWidget(self.pushButton_Import, 0, 2, 1, 1)
        self.pushButton_importfile = QtWidgets.QPushButton(self.Data)
        self.pushButton_importfile.setObjectName("pushButton_importfile")
        self.gridLayout.addWidget(self.pushButton_importfile, 0, 0, 1, 1)
        self.tabWidget_Data.addTab(self.Data, "")
        self.Pre_processing = QtWidgets.QWidget()
        self.Pre_processing.setObjectName("Pre_processing")
        self.formLayoutWidget = QtWidgets.QWidget(self.Pre_processing)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 741, 491))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Transfer_Data = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_Transfer_Data.setObjectName("pushButton_Transfer_Data")
        self.gridLayout_2.addWidget(self.pushButton_Transfer_Data, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_next_to_visualisation = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_next_to_visualisation.setObjectName("pushButton_next_to_visualisation")
        self.gridLayout_2.addWidget(self.pushButton_next_to_visualisation, 2, 1, 1, 1)
        self.textBrowser_showdata = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_showdata.setStyleSheet("background: rgb(255, 255, 255)")
        self.textBrowser_showdata.setObjectName("textBrowser_showdata")
        self.gridLayout_2.addWidget(self.textBrowser_showdata, 0, 0, 1, 1)
        self.pushButton_next_to_domain = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_next_to_domain.setObjectName("pushButton_next_to_domain")
        self.gridLayout_2.addWidget(self.pushButton_next_to_domain, 1, 1, 1, 1)
        self.tabWidget_Data.addTab(self.Pre_processing, "")
        self.verticalLayout_5.addWidget(self.tabWidget_Data)
        self.tabWidget_Importing.addTab(self.Importing, "")
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
        self.layoutWidget.setGeometry(QtCore.QRect(19, 15, 730, 164))
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
        self.tabWidget_Importing.addTab(self.Domain_Mesh, "")
        self.Inversion = QtWidgets.QWidget()
        self.Inversion.setObjectName("Inversion")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Inversion)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 411, 76))
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
        self.tabWidget_Importing.addTab(self.Inversion, "")
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
        self.tabWidget_Importing.addTab(self.tab_5, "")
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
        self.tabWidget_Importing.addTab(self.visualisation, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_Importing, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 24))
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
        # index of tabwidget shows the page when users start the application
        self.retranslateUi(MainWindow)
        self.tabWidget_Importing.setCurrentIndex(0)
        self.tabWidget_Data.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        # signal and plot to connect different buttons and output area
        self.pushButton_importfile.clicked.connect(self.open_file_dialog)  # type: ignore
        self.pushButton_Import.clicked.connect(self.switch_to_preprocessing_tab)  # type: ignore
        self.pushButton_next_to_domain.clicked.connect(self.jump_to_next_page)  # type: ignore
        self.pushButton_Transfer_Data.clicked.connect(self.data_show)  # type: ignore
        self.pushButton_next_to_visualisation.clicked.connect(self.jump_to_next_visualisation)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # allows users to locate and move to specific page
    def switch_to_preprocessing_tab(self):

        index_of_page = 1
        self.tabWidget_Data.setCurrentIndex(index_of_page)

    # allows users to upload and save files from their computer
    def open_file_dialog(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)

        if files:
            self.listWidget_file_list.clear()

            # Define the directory to save data
            save_directory = "./data"

            # Create the directory if it does not exist
            os.makedirs(save_directory, exist_ok=True)

            for file in files:
                item = QtWidgets.QListWidgetItem(file)
                item.setForeground(QColor('lightblue'))
                self.listWidget_file_list.addItem(item)

                # Define the destination file path in the save directory
                destination_file = os.path.join(save_directory, os.path.basename(file))

                # Copy the file to the new directory and replace if it already exists
                shutil.copy(file, destination_file)

            with open(files[0], 'r') as f:
                content = f.read()

                # set the content of the file as its text
                self.textBrowser_showdata.setPlainText(content)

    # transfer raw data and show them in the text-browser
    def data_transfer(self):
        # input and output folder
        input_folder = './data'
        output_folder = './data'
        # loop for file chang
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
                    data = [line.strip().split() for line in lines[244:]]

                selected_data = []
                for row in data:
                    row_transformed = row.copy()
                    for i in [1, 2, 3, 4]:  # index of columns to transform
                        item = float(row[i])
                        if item >= 48:
                            row_transformed[i] = str(
                                int(item - 48))  # Subtract 48 and convert to string
                        else:
                            row_transformed[i] = str(
                                int(item))  # Convert to string without subtracting 48
                    selected_data.append([row_transformed[i] for i in
                                          [1, 2, 3, 4, 10]])  # Select the specific columns

                with open(output_file_path, 'w') as output_file:
                    for line in fixed_data:
                        output_file.write(line + "\n")

                    output_file.write("# a b m n rhoa\n")
                    for row in selected_data:
                        output_file.write("\t".join(row) + "\n")
                return output_file_path

    def data_show(self):
        output_file_path = self.data_transfer
        with open (output_file_path, 'r') as file:
            content = file.read()
        self.textBrowser_showdata.setPlainText(content)

    def jump_to_next_page(self):
        index_of_page = 1

        self.tabWidget_Importing.setCurrentIndex(index_of_page)

    def jump_to_next_visualisation(self):
        index_of_page = 4

        self.tabWidget_Importing.setCurrentIndex(index_of_page)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Import.setText(_translate("MainWindow", "Import"))
        self.pushButton_importfile.setText(_translate("MainWindow", "Choose your file"))
        self.tabWidget_Data.setTabText(self.tabWidget_Data.indexOf(self.Data), _translate("MainWindow", "Data"))
        self.pushButton_Transfer_Data.setText(_translate("MainWindow", "Transfer Data"))
        self.pushButton_next_to_visualisation.setText(_translate("MainWindow", "Next-multiple file"))
        self.pushButton_next_to_domain.setText(_translate("MainWindow", "Next-single file"))
        self.tabWidget_Data.setTabText(self.tabWidget_Data.indexOf(self.Pre_processing),
                                       _translate("MainWindow", "Pre_processing"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Importing),
                                            _translate("MainWindow", "Importing"))
        self.pushButton_4.setText(_translate("MainWindow", "Apply"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.textEdit_3.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Geometry:</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">start</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">end</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Mesh:</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Quality</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Area</span></p></body></html>"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Domain_Mesh),
                                            _translate("MainWindow", "Domain and Mesh"))
        self.textEdit_8.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">maxIter:</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Lam:</span></p></body></html>"))
        self.textEdit_10.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">dPhi:</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Apply"))
        self.pushButton_9.setText(_translate("MainWindow", "Save"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.Inversion),
                                            _translate("MainWindow", "Inversion"))
        self.textEdit_11.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temperture</p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.tab_5),
                                            _translate("MainWindow", "Water Content"))
        self.pushButton_7.setText(_translate("MainWindow", "Result"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Resistivity), _translate("MainWindow", "Resistivity"))
        self.pushButton_6.setText(_translate("MainWindow", "Convert"))
        self.pushButton_11.setText(_translate("MainWindow", "Save"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Water_content),
                                    _translate("MainWindow", "Water content"))
        self.tabWidget_Importing.setTabText(self.tabWidget_Importing.indexOf(self.visualisation),
                                            _translate("MainWindow", "visualisation"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionGuidline.setText(_translate("MainWindow", "Guidline"))
        self.actionContract.setText(_translate("MainWindow", "Contract"))


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
