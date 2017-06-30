import os
import subprocess


def RemoveFile(File):
    os.remove(File)
def RunSingleCommand(Command):
    os.system(Command)

#This file is used in the script to use bash commands
#Bu dosya programda bash komutlarını kullanmak için kullanılıyor
def Wget(url):
    os.system("wget "+url)

#Run bash file
def RunSh(fileDirectory):

    os.system("sh "+fileDirectory)
#
#Run bash commands
def RunCommands(Commands):
    for Command in Commands:
        os.system(Command)

#Run when installing a package
def StartRun():
 Commands=["sudo pacman -S wget --noconfirm;sudo pacman -S base-devel --noconfirm;sudo pacman -S yaourt --noconfirm;sudo pacman-mirrors -g;sudo pacman -Syy --noconfirm"]
 RunCommands(Commands)

#You can edit the install.sh with this functions
def EchoMulti(Commands):
    os.system("echo -e"+Commands+">install.sh")

def EchoSingle(Commands):
    os.system("echo "+Commands+">install.sh")

def EchoPass(Text):
    os.system("echo "+Text+">pass.txt")