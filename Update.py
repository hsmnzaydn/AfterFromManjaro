import BashCommands

#This class is being used to update the program
#Bu class programın güncellenmesi için kullanıyor

UpdateCommands=["sudo git stash save --keep-index --noconfirm","yaourt -S git --noconfirm","sudo git pull -noconfirm"]
def Update():
  BashCommands.RunCommands(UpdateCommands)
