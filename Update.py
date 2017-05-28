import BashCommands


UpdateCommands=["sudo pacman -S git","cd .."]
def Update():
  BashCommands.RunCommands(UpdateCommands)
