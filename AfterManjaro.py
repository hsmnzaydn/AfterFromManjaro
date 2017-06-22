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
            self._packages[category] = self._jsonParse.getAllProgramNames(category)
            
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
        packages to be installed.
        @precondition: UI is initialised 
        @postcondition: @result is a Dictionary which maps Strings to a List of
                        Strings. Each key in @result is a category
                        in Packages.json, and each string in the mapped list is
                        a selected program in the GUI list views.
        """
        selectedItems = {}
        selectedItems["Developer"] = (
            self._ui.Developer_listWidget.selectedItems())
        selectedItems["Tools"] = self._ui.Tools_listWidget.selectedItems()
        selectedItems["Personal"] = self._ui.Personal_listWidget.selectedItems()
        selectedItems["System"] = self._ui.System_listWidget.selectedItems()
        return selectedItems
    
    def _getPackagesToInstall(self, selectedItems):
        """
        Takes a dictionary of selectedItems and returns the list of package 
        names to install.
        @param selectedItems: A Dictionary which maps Strings to a List of 
                Strings. Maps the category of the programs to a list of all
                selected programs which are in that category. 
        @postcondition: @return is a List of Strings of valid package names 
                        which are selected for installation
        """
        packagesToInstall = []
        for category in selectedItems:
            for selectedProgram in selectedItems[category]:
                packageName = self._jsonParse.getPackageName(category, 
                                                             selectedProgram)
                if packageName:
                    packagesToInstall.append(packageName)
            
        return packagesToInstall
    
    
    def _getPostCommands(self, selectedItems):
        """
        Takes a dictionary of selectedItems and returns the list of any commands
        to run after packages have been installed.
        @param selectedItems: A Dictionary which maps Strings to a List of 
                Strings. Maps the category of the programs to a list of all
                selected programs which are in that category. 
        @postcondition: @return is a List of Strings of bash commands to be
                        executed after packages are installed
        """
        postCommands = []
        for category in selectedItems:
            for selectedProgram in selectedItems[category]:
                postCommands.extend(
                    self._jsonParse.getPackageBashCommands(category, 
                                                           selectedProgram))
        
        return postCommands
        
            
    def handleInstall(self):
        """
        Runs when the install button is clicked. Handles installing the selected
        packages.
        """
        self.showInformation("Information", 
                             "Your programs are being installed.Please wait")
        
        # Get selected packages and commands to run
        selectedItems = self._getItems()
        packagesToInstall = self._getPackagesToInstall(selectedItems)
        postCommands = self._getPostCommands(selectedItems)
        
        # Run the installation and post commands
        self._installThread = installation.installThread(packagesToInstall, 
                                                        postCommands)
        self._installThread.start()
        
        self.showInformation("Information", "Your programs installed")
        
    def handleUpdate(self):
        """
        Runs when the update button is clicked. Handles updating the program.
        """
        Update.Update()
        self.showInformation("Updated", 
                             "The software has updated to the latest version")
        
    def about(self):
        """
        Opens a browser to the github page when the about button is clicked
        """
        webbrowser.open('http://www.github.com/hsmnzaydn/afterfrommanjaro', 
                        new=2)
        
    
    def showInformation(self, title, message):
        """
        Opens a window which displays information to the UI.
        @param title: A String which will be the window title for the message
        @param message: A String which is the information which will be
                displayed in the window.
        @postcondition: A QMessageBox() appears displaying the information.
        """
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText(message)
        infoBox.setWindowTitle(title)
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()
        
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

