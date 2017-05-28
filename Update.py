import BashCommands

#This class is being used to update the program
#Bu class programın güncellenmesi için kullanıyor

UpdateCommands=["sudo pacman -S git","git pull"]
def Update():
  BashCommands.RunCommands(UpdateCommands)
