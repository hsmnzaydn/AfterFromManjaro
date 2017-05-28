import BashCommands


UpdateCommands=["sudo pacman -S git","git fetch"]
def Update():
  BashCommands.RunCommands(UpdateCommands)
