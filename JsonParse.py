import urllib.request
import json

class JsonParse ():
    """
    Retrieves the latest version of Packages.json from github and parses the 
    json file into a form which Python can understand.
    
    Methods:
        getPackageCategories - Returns a list of categories which packages are
                                separated into.
        getAllProgramNames - Returns a list of package names in a given category
        getPackageBashCommands - Returns a list of bash commands to be executed
                                when a package is installed
        getVersion - Returns the version of the Packages.json
        getGithubRepo - Returns the URL of the application's github repository.
    """
    
    _URL = "https://raw.githubusercontent.com/hsmnzaydn/AfterFromManjaro/redoInstallation/Packages.json" #FIXME: Change back to master when merging back to master
    
    def __init__(self):
        """
        Constructor: Downloads the json file and parses
        @postcondition: _data is populated with the parsed json file
        """
        # Download the package list from github
        with urllib.request.urlopen(self._URL) as url:
            self._data = json.loads(url.read().decode())
        
    
    def getPackageCategories(self):
        """
        Returns a list of categories which packages are sorted by
        @precondition: Packages.json has a Categories key
        @postcondition: @return is a List of Strings of categories which
                        packages are sorted by.
        """
        return self._data["Categories"]


    def getAllProgramNames(self, category):
        """
        Get all package names from url
        
        @param category: a String representing the category of a set of packages
        @precondition: data["Packages"] has category as a key
        @postcondition: @return is a List of Strings containing package names which
                        are associated with Type.
        """
        Packages = []
    
        for packageName in self._data["Packages"][category]:
            Packages.append(packageName)
        return Packages
    
    
    def getPackageName(self, category, programName):
        """
        Returns the package name of a program
        @param category: A String containing the category the package is in
        @param programName: A String containing the name of the program as
                displayed in the GUI
        @precondition: category and programName must exist in the Packages.json
        @postcondition: @return is a String containing the package name of the 
                        program
        """
        return self._data["Packages"][category][programName]["PackageName"]
    
    
    def getPackageBashCommands(self, category, packageName):
        """
        Get bashCommands of Package from url
        
        @param category: a String representing the category of a set of packages
        @param packageName: a String representing the name of a package
        @precondition: data["Packages"] has category as a key and 
                        data["Packages"][category] has packageName as a key
        @postcondition: @return is a List of Strings of bash commands which
                        need to be run after a package is installed.
        """
        return self._data["Packages"][category][packageName]["PackageBashCommands"]
    
    
    def getVersion(self):
        """
        get version from url
        
        @precondition: data has a "Version" key
        @postcondition: @Return is a String containing the program version 
                        information
        """
        return self._data["Version"]
    
    
    def getGithubRepo(self):
        """
        get GithubRepo from url
        
        @precondition: data has a "GithubRepo" key
        @postcondition: @Return is a String containing the url of the github repo.
        """
        return self._data["GithubRepo"]
