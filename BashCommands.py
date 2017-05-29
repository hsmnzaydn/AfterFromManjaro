import os

#This file is used in the script to use bash commands
#Bu dosya programda bash komutlarını kullanmak için kullanılıyor
def Wget(url):
    os.system("wget "+url)

#Run bash file
def RunSh(fileDirectory):

    os.system("sh "+fileDirectory)

#Run bash commands
def RunCommands(Commands):
    for Command in Commands:
        os.system(Command)

#Run when installing a package
def StartRun():
    Commands=["sudo pacman -S wget","sudo pacman -S base-devel","sudo pacman -S yaourt","sudo pacman-mirrors -g","sudo pacman -Syy"]
    RunCommands(Commands)

#You can edit the install.sh with this functions
def EchoMulti(Commands):
    os.system("echo -e"+Commands+">install.sh")

def EchoSingle(Commands):
    os.system("echo "+Commands+">install.sh")
