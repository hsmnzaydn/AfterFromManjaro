import urllib.request
import json
import BashCommands

# Download the package list from github
with urllib.request.urlopen("https://raw.githubusercontent.com/hsmnzaydn/AfterFromManjaro/master/Packages.json") as url:
    data = json.loads(url.read().decode())
#FIXME: A network connection should have error checking


def getPackageName(Type):
    """
    Get all package names from url
    
    @param Type: a String representing the category of a set of packages
    @precondition: data has Type as a key
    @postcondition: @return is a List of Strings containing package names which
                    are associated with Type.
    """
    Packages = []

    for row in data[Type]:
        Packages.append(row["PackageName"])
    return Packages


def getPackageBashCommands(Type, PackageName):
    """
    Get bashCommands of Package from url
    
    @param Type: a String representing the category of a set of packages
    @param PackageName: a String representing the name of a package
    @precondition: data has Type as a key and data[Type] has a dictionary 
                    containing PackageName as a value for the "PackageName" key
    @postcondition: The bash command to install the package is added to be
                    executed.
    """
    for row in data[Type]:
        command = ""
        if row["PackageName"] == PackageName:
            for packageCommand in row["PackageBashCommands"]:
                if len(packageCommand) == 1:
                    command = command + "" + packageCommand
                else:
                    command = command + "\n" + packageCommand
            if len(packageCommand) == 1:
                BashCommands.RunSingleCommand(command)
            else:
                BashCommands.EchoMulti(command)


def getVersion():
    """
    get version from url
    
    @precondition: data has a "Version" key
    @postcondition: @Return is a String containing the program version 
                    information
    """
    return data["Version"]


def getGithubRepo():
    """
    get GithubRepo from url
    
    @precondition: data has a "GithubRepo" key
    @postcondition: @Return is a String containing the url of the github repo.
    """
    return data["GithubRepo"]
