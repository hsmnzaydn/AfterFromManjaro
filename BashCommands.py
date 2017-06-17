import os


def RemoveFile(File):
    """
    Removes a file from the filesystem
    
    @precondition: File is a String which contains the path to a file to remove.
                    The program has the correct permissions to remove the file.
    @postcondition: The file at that path is removed.
    """
    os.remove(File)


def RunSingleCommand(Command):
    """
    Runs a single bash command
    
    @precondition: Command is a String with a valid bash command
    @postcondition: The command is executed
    """
    os.system(Command)

# This file is used in the script to use bash commands
# Bu dosya programda bash komutlarını kullanmak için kullanılıyor


def Wget(url):
    """
    Uses wget to download a file from the url and places it in the working
    directory.
    
    @precondition: url is a String and must be formatted as a valid url
    @postcondition: The file at the url is downloaded to the working directory
    """
    os.system("wget " + url)


def RunSh(fileDirectory):
    """
    Run bash file
    
    @precondition: fileDirectory is a String representing the directory path to
                    a bash file.
    @postcondition: The bash file at that path is executed
    """
    os.system("sh " + fileDirectory)


def RunCommands(Commands):
    """
    Run bash commands
    
    @precondition: Commands is a List of Strings containing legal bash commands
    @postcondition: Each command is executed in the order they are in the List
    """
    for Command in Commands:
        os.system(Command)

def StartRun():
    """
    Run when installing a package
    
    @postcondition: wget, base-devel, yaourt are installed. Refreshes pacman
    mirrors.
    """
    Commands = ["sudo pacman -S wget --noconfirm", 
                "sudo pacman -S base-devel --noconfirm",
                "sudo pacman -S yaourt --noconfirm", "sudo pacman-mirrors -g", 
                "sudo pacman -Syy --noconfirm"]
    RunCommands(Commands)

# You can edit the install.sh with this functions


def EchoMulti(Commands):
    """
    Appends multiple commands to an install.sh file for execution
    """
    os.system("echo -e" + Commands + ">install.sh")


def EchoSingle(Commands):
    """
    Appends a single command to an install.sh file for execution
    """
    os.system("echo " + Commands + ">install.sh")


def EchoPass(Text):
    """
    Appends some text to pass.txt
    """
    os.system("echo " + Text + ">pass.txt")
