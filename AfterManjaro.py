# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indexnew.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import sys
import BashCommands
from PyQt5 import uic
import JsonParse
import BashCommands
import Update
import os
import webbrowser
Developer_list = []
Tool_list=[]
Personal_list=[]
System_list=[]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 481)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Install_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Install_button.setFont(font)
        self.Install_button.setObjectName("Install_button")
        self.gridLayout.addWidget(self.Install_button, 2, 0, 1, 1)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 157, 315))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.Developer_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_11)
        self.Developer_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Developer_listWidget.setObjectName("Developer_listWidget")
        self.gridLayout_4.addWidget(self.Developer_listWidget, 1, 0, 1, 1)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_11)
        self.gridLayout_3.addWidget(self.scrollArea_7, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 157, 315))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.Tools_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_6)
        self.Tools_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Tools_listWidget.setObjectName("Tools_listWidget")
        self.verticalLayout_4.addWidget(self.Tools_listWidget)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 157, 315))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.Personal_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_8)
        self.Personal_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Personal_listWidget.setObjectName("Personal_listWidget")
        self.verticalLayout_6.addWidget(self.Personal_listWidget)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_3.addWidget(self.scrollArea_4, 0, 2, 1, 1)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 157, 315))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.System_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_9)
        self.System_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.System_listWidget.setObjectName("System_listWidget")
        self.verticalLayout_7.addWidget(self.System_listWidget)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_3.addWidget(self.scrollArea_5, 0, 3, 1, 1)
        self.scrollArea_2.raise_()
        self.scrollArea_4.raise_()
        self.scrollArea_5.raise_()
        self.scrollArea_7.raise_()
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_2.raise_()
        self.Install_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Update_button = QtWidgets.QAction(MainWindow)
        self.Update_button.setObjectName("Update_button")
        self.About_button = QtWidgets.QAction(MainWindow)
        self.About_button.setObjectName("About_button")
        self.menuSettings.addAction(self.Update_button)
        self.menuSettings.addAction(self.About_button)
        self.menubar.addAction(self.menuSettings.menuAction())
        global Developer_list, Tool_list, Personal_list
        global System_list

        Developer_list = JsonParse.getPackageName("Developer")
        Tool_list = JsonParse.getPackageName("Tools")
        Personal_list = JsonParse.getPackageName("Personal")
        System_list = JsonParse.getPackageName("System")

        # Adds incoming package names to the list
        for Package_Developer in Developer_list:
            self.Developer_listWidget.addItem(Package_Developer)
        for Package_Tools in Tool_list:
            self.Tools_listWidget.addItem(Package_Tools)
        for Package_Personal in Personal_list:
            self.Personal_listWidget.addItem(Package_Personal)
        for Package_System in System_list:
            self.System_listWidget.addItem(Package_System)

        # If the version number does not match the version number in the repository, the update button opens.


        # to install and update functions
        self.Install_button.clicked.connect(self.install)
        self.Update_button.triggered.connect(self.update)
        self.About_button.triggered.connect(self.about)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "After From Manjaro"))
        self.Install_button.setText(_translate("MainWindow", "Install"))
        self.label_9.setText(_translate("MainWindow", "Developer"))
        self.label_4.setText(_translate("MainWindow", "Tools"))
        self.label_6.setText(_translate("MainWindow", "Personal"))
        self.label_7.setText(_translate("MainWindow", "System"))
        self.menuSettings.setTitle(_translate("MainWindow", "Help"))
        self.Update_button.setText(_translate("MainWindow", "Update"))
        self.About_button.setText(_translate("MainWindow", "About "))

        # Get name of choosed package

    def getItems(self):
        selected_package_Developer = ""
        items = self.Developer_listWidget.selectedItems()
        Developer_Selected = []
        for x in range(len(items)):
            Developer_Selected.append(self.Developer_listWidget.selectedItems()[x].text())
        selected_package_Developer = selected_package_Developer + "-".join(Developer_Selected)
        selected_install_Developer = selected_package_Developer.split("-")
        for install in selected_install_Developer:
            JsonParse.getPackageBashCommands("Developer", install)



        selected_package_Tools = ""
        items = self.Tools_listWidget.selectedItems()
        Tool_Selected = []
        for x in range(len(items)):
            Tool_Selected.append(self.Tools_listWidget.selectedItems()[x].text())

        selected_package_Tools = selected_package_Tools + "-".join(Tool_Selected)
        selected_install_Tools = selected_package_Tools.split("-")
        for install in selected_install_Tools:
            JsonParse.getPackageBashCommands("Tools", install)


        selected_package_Personal = ""
        items = self.Personal_listWidget.selectedItems()
        Personal_Selected = []
        for x in range(len(items)):
            Personal_Selected.append(self.Personal_listWidget.selectedItems()[x].text())
        selected_package_Personal = selected_package_Developer + "-".join(Personal_Selected)
        selected_install_Personal = selected_package_Personal.split("-")
        for install in selected_install_Personal:
            JsonParse.getPackageBashCommands("Personal", install)

        selected_package_System = ""
        items = self.System_listWidget.selectedItems()
        System_Selected = []
        for x in range(len(items)):
            System_Selected.append(self.System_listWidget.selectedItems()[x].text())
        selected_package_System = selected_package_Developer + "-".join(System_Selected)
        selected_install_System = selected_package_System.split("-")
        for install in selected_install_System:
            JsonParse.getPackageBashCommands("System", install)

    # When clicked Install button
    def install(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Your programs are being installed.Please wait")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()
       # BashCommands.StartRun()
        self.getItems()
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Your programs installed  ")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()


        # When clicked update button

    def update(self):
        Update.Update()
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Updated")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()

    # When clicked about button
    def about(self):
        webbrowser.open('http://www.github.com/hsmnzaydn/afterfrommanjaro', new=2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())

