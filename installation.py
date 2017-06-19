'''
Created on 19Jun.,2017

@author: jonathan
'''
from PyQt5.QtCore import QThread
import os

class installThread(QThread):
    """
    A QThread which will spawn a terminal and run the installation commands
    """
    
    def __init__(self, packages, terminal="konsole"): #FIXME: Remove default terminal
        """
        Constructor:
        @param packages: A List of Strings of package names
        @param terminal: A String which contains the name of the terminal to use
        @precondition: Each package name in the list of packages must exist in 
                        the standard repository or the AUR.
        @postcondition: A new QThread is created, and when set to run it opens a
                        terminal which executes the command
        """
        QThread.__init__(self)
        self._command = self._getInstallCommand(packages)
        self._terminal = terminal
        
    def _getInstallCommand(self, packages):
        """
        Takes a list of package names creates a yaourt command to install them
        @param packages: A List of Strings of package names
        @precondition: len(packages) > 0
        @postcondition: Returns a String which is a valid yaourt command that
                        will install the packages specified
        """
        # Convert packages into a string which yaourt can interpret
        packageNames = ""
        for package in packages:
            packageNames += package + " "
            
        # Create command to pass to yaourt
        return "yaourt -S {}--noconfirm".format(packageNames)
    
    def run(self):
        """
        Overrides the function in QtCore.Qthread
        @postcondition: Spawns the terminal and sets the command running
        """
        #FIXME: Create options to select which terminal to use and expand to
        # support most common terminals
        if self._terminal == "konsole":
            refreshCommand = self._terminal + " -e \"yaourt -Syyu\""
            installCommand = self._terminal + " -e " + '"{}"'.format(self._command)
        
        os.system(refreshCommand)
        os.system(installCommand)
        
        
        
        
        
        
        