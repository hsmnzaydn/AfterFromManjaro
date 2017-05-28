import urllib.request, json
import BashCommands

#get data from url
with urllib.request.urlopen("https://raw.githubusercontent.com/hsmnzaydn/AfterFromManjaro/master/Packages.json") as url:
    data = json.loads(url.read().decode())

#get all packagename from url
def getPackageName(Type):
    Packages=[]

    for row in data[Type]:
        Packages.append(row["PackageName"])
    return Packages
#get choosed bashCommands of Package from url
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
#get version from url
def getVersion():
    return data["Version"]
#get GithubRepo from url
def getGithubRepo():
    return data["GithubRepo"]





