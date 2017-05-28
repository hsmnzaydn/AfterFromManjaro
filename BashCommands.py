import os

def Wget(url):
    os.system("wget "+url)

def RunSh(fileDirectory):
    os.system("sh "+fileDirectory)

def RunCommands(Commands):
    for Command in Commands:
        os.system(Command)

def StartRun():
    Commands=["sudo pacman -S wget","sudo pacman -S yaourt","sudo pacman-mirrors -g","sudo pacman -Syy"]
    RunCommands(Commands)


def EchoMulti(Commands):
    os.system("echo -e"+Commands+">install.sh")

def EchoSingle(Commands):
    os.system("echo "+Commands+">install.sh")




EchoSingle("sudo pacman -S wget")
