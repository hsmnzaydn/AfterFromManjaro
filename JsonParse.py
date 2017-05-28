import urllib.request, json
import BashCommands

with urllib.request.urlopen("https://raw.githubusercontent.com/hsmnzaydn/AfterFromManjaro/master/Packages.json") as url:
    data = json.loads(url.read().decode())
def getPackageName(Type):
    Packages=[]

    for row in data[Type]:
        Packages.append(row["PackageName"])
    return Packages

def getPackageBashCommands(Type,PackageName):
    for row in data[Type]:
        Com = ""
        if row["PackageName"]==PackageName:
            for Command in row["PackageBashCommands"]:
                if len(Command)==1:
                    Com = Com + "" + Command
                else:
                    Com = Com + "\n" + Command
            if len(Command) == 1:
               BashCommands.EchoSingle(Com)
               BashCommands.RunSh("./install.sh")
            else:
                BashCommands.EchoMulti(Com)

def getVersion():
    return data["Version"]
def getGithubRepo():
    return data["GithubRepo"]





