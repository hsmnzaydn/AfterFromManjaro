from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import BashCommands, indexnew, JsonParse, Update, sys, installation, os
import webbrowser
from urllib.error import URLError

class Application():
    """
    Class containing the main application logic. 
    """
    
    def __init__(self, mainWindow):
        """
        Constructor
        @param mainWindow: QMainWindow - The main window of the application
        """
                
        #Set up UI
        self._mainWindow = mainWindow
        self._ui = indexnew.Ui_MainWindow()
        self._ui.setupUi(mainWindow)
        
        #Load the packages
        self._loadPackages()
        
        #Add packages to the UI
        self._addPackagesToUi()
        
        # Connect install and update functions
        self._ui.Install_button.clicked.connect(self.handleInstall)
        self._ui.Update_button.triggered.connect(self.handleUpdate)
        self._ui.About_button.triggered.connect(self.about)
        
        
    def _loadPackages(self):
        """
        Loads the packages from Packages.json and adds them to a dictionary of
        packages.
        @postcondition: _packages contains a list of packages keyed by category 
        """
        self._packages = {}
        
        try:
            self._jsonParse = JsonParse.JsonParse()
        except URLError:
            self.showError("Error Downloading Package List", 
                           "There was an error loading the package list. " + 
                            "Please check your internet connection")
            #FIXME: Need to disable or exit the program here
        
        for category in self._jsonParse.getPackageCategories():
            self._packages[category] = self._jsonParse.getPackageName(category)
            
    def _addPackagesToUi(self):
        """
        Adds the packages to the list widgets in the UI.
        @precondition: self._ui is initialised and self._packages contains a 
                        List for the keys "Developer", "Tools", "System" and
                        "Personal"
        @postcondition: Each list view in the ui contains the package names of
                        the loaded packages
        """
        for Package_Developer in self._packages["Developer"]:
            self._ui.Developer_listWidget.addItem(Package_Developer)
        for Package_Tools in self._packages["Tools"]:
            self._ui.Tools_listWidget.addItem(Package_Tools)
        for Package_Personal in self._packages["Personal"]:
            self._ui.Personal_listWidget.addItem(Package_Personal)
        for Package_System in self._packages["System"]:
            self._ui.System_listWidget.addItem(Package_System)
            
    def _getItems(self):
        """
        Gets the selected items from the list widgets in the UI and sets those
        packages to be installed. FIXME: This method is needlessly complicated
        """
        selected_package_Developer = ""
        items = self._ui.Developer_listWidget.selectedItems()
        Developer_Selected = []
        for x in range(len(items)):
            Developer_Selected.append(self.Developer_listWidget.selectedItems()[x].text())
        selected_package_Developer = selected_package_Developer + "-".join(Developer_Selected)
        selected_install_Developer = selected_package_Developer.split("-") #???
        for install in selected_install_Developer:
            JsonParse.getPackageBashCommands("Developer", install)



        selected_package_Tools = ""
        items = self._ui.Tools_listWidget.selectedItems()
        Tool_Selected = []
        for x in range(len(items)):
            Tool_Selected.append(self.Tools_listWidget.selectedItems()[x].text())

        selected_package_Tools = selected_package_Tools + "-".join(Tool_Selected)
        selected_install_Tools = selected_package_Tools.split("-") #???
        for install in selected_install_Tools:
            JsonParse.getPackageBashCommands("Tools", install)


        selected_package_Personal = ""
        items = self._ui.Personal_listWidget.selectedItems()
        Personal_Selected = []
        for x in range(len(items)):
            Personal_Selected.append(self.Personal_listWidget.selectedItems()[x].text())
        selected_package_Personal = selected_package_Developer + "-".join(Personal_Selected)
        selected_install_Personal = selected_package_Personal.split("-") #???
        for install in selected_install_Personal:
            JsonParse.getPackageBashCommands("Personal", install)

        selected_package_System = ""
        items = self._ui.System_listWidget.selectedItems()
        System_Selected = []
        for x in range(len(items)):
            System_Selected.append(self.System_listWidget.selectedItems()[x].text())
        selected_package_System = selected_package_Developer + "-".join(System_Selected)
        selected_install_System = selected_package_System.split("-") #???
        for install in selected_install_System:
            JsonParse.getPackageBashCommands("System", install)
            
    def handleInstall(self):
        """
        Runs when the install button is clicked. Handles installing the selected
        packages.
        """
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Your programs are being installed.Please wait")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()
        BashCommands.StartRun()
        self._getItems()
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Your programs installed  ")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()
        
    def handleUpdate(self):
        """
        Runs when the update button is clicked. Handles updating the program.
        """
        Update.Update()
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Updated")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()
        
    def about(self):
        """
        Opens a browser to the github page when the about button is clicked
        """
        webbrowser.open('http://www.github.com/hsmnzaydn/afterfrommanjaro', 
                        new=2)
        
    def showError(self, title, errorMessage):
        """
        Opens a window which displays an error message if an error occurs.
        @param title: A String which will be the window title for the error 
                message
        @param errorMessage: A String which is the error message to display.
        @postcondition: A QMessageBox() appears displaying errorMessage as a 
                        message.
        """
        errorBox = QMessageBox()
        errorBox.setIcon(QMessageBox.Critical)
        errorBox.setText(errorMessage)
        errorBox.setWindowTitle(title)
        errorBox.setStandardButtons(QMessageBox.Ok)
        errorBox.exec_()
        

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    window = QMainWindow()
    app = Application(window)
    window.show()
    sys.exit(qApp.exec_())

