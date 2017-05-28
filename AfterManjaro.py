# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import uic
import JsonParse
import BashCommands
import Update

Developer_list = []
Tool_list=[]
Personal_list=[]
System_list=[]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 740)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 818, 572))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 193, 552))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Developer_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Developer_label.setFont(font)
        self.Developer_label.setObjectName("Developer_label")
        self.verticalLayout.addWidget(self.Developer_label)
        self.Developer_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.Developer_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Developer_listWidget.setObjectName("Developer_listWidget")
        self.verticalLayout.addWidget(self.Developer_listWidget)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 194, 552))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Tools_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Tools_label.setFont(font)
        self.Tools_label.setObjectName("Tools_label")
        self.verticalLayout_2.addWidget(self.Tools_label)
        self.Tools_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_3)
        self.Tools_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Tools_listWidget.setObjectName("Tools_listWidget")
        self.verticalLayout_2.addWidget(self.Tools_listWidget)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.addWidget(self.scrollArea_3)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 193, 552))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Personal_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Personal_label.setFont(font)
        self.Personal_label.setObjectName("Personal_label")
        self.verticalLayout_3.addWidget(self.Personal_label)
        self.Personal_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_4)
        self.Personal_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Personal_listWidget.setObjectName("Personal_listWidget")
        self.verticalLayout_3.addWidget(self.Personal_listWidget)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout.addWidget(self.scrollArea_4)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 194, 552))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.System_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.System_label.setFont(font)
        self.System_label.setObjectName("System_label")
        self.verticalLayout_4.addWidget(self.System_label)
        self.System_listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_5)
        self.System_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.System_listWidget.setObjectName("System_listWidget")
        self.verticalLayout_4.addWidget(self.System_listWidget)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout.addWidget(self.scrollArea_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.Install_Button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Install_Button.setFont(font)
        self.Install_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Install_Button.setObjectName("Install_Button")
        self.gridLayout_2.addWidget(self.Install_Button, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Update_group = QtWidgets.QGroupBox(self.groupBox)
        self.Update_group.setGeometry(QtCore.QRect(0, 0, 825, 624))
        self.Update_group.setObjectName("Update_group")
        self.label_2 = QtWidgets.QLabel(self.Update_group)
        self.label_2.setGeometry(QtCore.QRect(580, 290, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.CurrentVersion_label = QtWidgets.QLabel(self.Update_group)
        self.CurrentVersion_label.setGeometry(QtCore.QRect(750, 290, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CurrentVersion_label.setFont(font)
        self.CurrentVersion_label.setText("")
        self.CurrentVersion_label.setObjectName("CurrentVersion_label")
        self.label_4 = QtWidgets.QLabel(self.Update_group)
        self.label_4.setGeometry(QtCore.QRect(650, 260, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Version_label = QtWidgets.QLabel(self.Update_group)
        self.Version_label.setGeometry(QtCore.QRect(740, 260, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Version_label.setFont(font)
        self.Version_label.setText("")
        self.Version_label.setObjectName("Version_label")
        self.Update_button = QtWidgets.QPushButton(self.Update_group)
        self.Update_button.setEnabled(False)
        self.Update_button.setGeometry(QtCore.QRect(370, 150, 85, 71))
        self.Update_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Update_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Update_button.setIcon(icon1)
        self.Update_button.setIconSize(QtCore.QSize(50, 50))
        self.Update_button.setObjectName("Update_button")
        self.AboutUs_groub = QtWidgets.QGroupBox(self.Update_group)
        self.AboutUs_groub.setGeometry(QtCore.QRect(30, 350, 651, 68))
        self.AboutUs_groub.setObjectName("AboutUs_groub")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.AboutUs_groub)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.AboutUs_groub)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.GithubRepo_label = QtWidgets.QLabel(self.AboutUs_groub)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.GithubRepo_label.setFont(font)
        self.GithubRepo_label.setObjectName("GithubRepo_label")
        self.horizontalLayout_2.addWidget(self.GithubRepo_label)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        global Developer_list, Tool_list, Personal_list
        global System_list


        Developer_list = JsonParse.getPackageName("Developer")
        Tool_list = JsonParse.getPackageName("Tools")
        Personal_list = JsonParse.getPackageName("Personal")
        System_list = JsonParse.getPackageName("System")


        Version_no="1.0.0"
        self.Version_label.setText(Version_no)


        self.GithubRepo_label.setText(JsonParse.getGithubRepo())
        self.CurrentVersion_label.setText(JsonParse.getVersion())

        #Adds incoming package names to the list
        for Package_Developer in Developer_list:
            self.Developer_listWidget.addItem(Package_Developer)
        for Package_Tools in Tool_list:
            self.Tools_listWidget.addItem(Package_Tools)
        for Package_Personal in Personal_list:
            self.Personal_listWidget.addItem(Package_Personal)
        for Package_System in System_list:
            self.System_listWidget.addItem(Package_System)

        #If the version number does not match the version number in the repository, the update button opens.
        if Version_no != JsonParse.getVersion():
            self.Update_button.setEnabled(True)

        #to install and update functions
        self.Install_Button.clicked.connect(self.install)
        self.Update_button.clicked.connect(self.update)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Developer_listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "After From Manjaro"))
        self.Developer_label.setText(_translate("MainWindow", "Developer"))
        self.Tools_label.setText(_translate("MainWindow", "Tools"))
        self.Personal_label.setText(_translate("MainWindow", "Personal"))
        self.System_label.setText(_translate("MainWindow", "System"))
        self.Install_Button.setText(_translate("MainWindow", "Install"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Software"))
        self.Update_group.setTitle(_translate("MainWindow", "Update"))
        self.label_2.setText(_translate("MainWindow", "Current Version:"))
        self.label_4.setText(_translate("MainWindow", "Version:"))
        self.AboutUs_groub.setTitle(_translate("MainWindow", "About Us"))
        self.label.setText(_translate("MainWindow", "Github Repo:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Others"))

    #Get name of choosed package
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

    #When clicked install button
    def install(self):
        BashCommands.StartRun()
        self.getItems()

    #When clicked update button
    def update(self):

        Update.Update()




if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = QMainWindow()

        ui = Ui_MainWindow()
        ui.setupUi(window)

        window.show()
        sys.exit(app.exec_())