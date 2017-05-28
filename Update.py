import os


UpdateCommands=["sudo pacman -S git"]
def Update():
  for Command in UpdateCommands:
   os.system(Command)
