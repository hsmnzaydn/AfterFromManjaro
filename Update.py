import BashCommands


UpdateCommands=["sudo pacman -S git","git pull"]
def Update():
  BashCommands.RunCommands(UpdateCommands)
