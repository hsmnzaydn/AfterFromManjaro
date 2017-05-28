import BashCommands


UpdateCommands=["sudo pacman -S git"]
def Update():
  BashCommands.RunCommands(UpdateCommands)
