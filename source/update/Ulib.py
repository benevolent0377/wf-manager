# this file will update the source code of the whole project (not including this file)
# this file will most likely be small, only passing variables to the core function that is more specified to update the source files

import requests, hashlib
from source.core import IO, system, web

def update(projName):
    
    reposURL = "https://api.github.com/users/benevolent0377/repos"
    slash = system.getSlash()
    localPATH = system.getCWD() + slash + "source" + slash + "lib" + slash
    projectID = ""
    repos = requests.get(reposURL).json()

    repoData = {}

    for repo in repos:
        repoData.update({repo["name"]:repo["id"]})

    for name in repoData.keys():
        if name.lower() == projName.lower():
            projectID = repoData[name]
            break
    projectURL = "https://api.github.com/repositories/" + str(projectID) + "/contents/source/lib"

    projectDataRaw = requests.get(projectURL).json()

    projectDataParsed = {}

    for item in projectDataRaw:
        projectDataParsed.update({item["name"]: item["download_url"]})

    altered = False
    for fileName, URL in projectDataParsed.items():

        outputArray = IO.fileRead(localPATH + fileName)
        outputString = ""
        for line in outputArray:
            outputString += line

        outputString = outputString.encode()

        localmd5 = hashlib.md5(outputString).hexdigest()
        remotemd5 = hashlib.md5(requests.get(URL).content).hexdigest()
        
        if localmd5 != remotemd5:

            IO.rmFile(localPATH + fileName)
            IO.mkFile(localPATH + fileName)
            IO.fileWrite(requests.get(URL).text, localPATH + fileName, overwrite=True)
            altered = True

    return altered

def get(projName):

    if update(projName):
        IO.say("Program files have been updated. Please restart the program.")
        system.quitKill()


