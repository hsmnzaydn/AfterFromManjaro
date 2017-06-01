import BashCommands

#This class is being used to update the program
#Bu class programın güncellenmesi için kullanıyor

UpdateCommands=["sudo git stash save --keep-index","sudo pacman -S git","sudo git pull"]
def Update():
  BashCommands.RunCommands(UpdateCommands)
