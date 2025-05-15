# this is a core updater file to update the core files through python, and will be builtin to all programs
# I no longer wanted to make installers for the core files, so the program will build it automatically through this file

import requests, platform, os, hashlib, sys

def selfUpdate():

    updaterURL = "https://api.github.com/repositories/806174201/contents/update"
    slash = getSlash()
    corePATH = getCWD() + slash + "source" + slash + "update" + slash

    updaterData = requests.get(updaterURL).json()

    altered = False

    sortedContent = {}

    for item in updaterData:

        sortedContent.update({item['name']: item['download_url']})

    for fileName, URL in sortedContent.items():
        
        try:

            outputArray = fileRead(corePATH + fileName)
            outputString = ""
            
            for line in outputArray:
                outputString += line
        except:
            outputString = ""

        outputString = outputString.encode()

        localmd5 = hashlib.md5(outputString).hexdigest()
        remotemd5 = hashlib.md5(requests.get(URL).content).hexdigest()

        if localmd5 != remotemd5:
            rmFile(corePATH + fileName)
            mkFile(corePATH + fileName)
            fileWrite(requests.get(URL).text, corePATH + fileName, overwrite=True)
            altered = True

    return altered

def update():

    coreURL = "https://api.github.com/repositories/806174201/contents/files"
    slash = getSlash()
    corePATH = getCWD() + slash + "source" + slash + "core" + slash

    if not os.path.exists(corePATH):
        mkDir(corePATH)


    data = requests.get(coreURL)
    data = data.json()

    sortedContent = {}

    for item in data:
        sortedContent.update({item["name"]:item["download_url"]})

    altered = False

    for fileName, URL in sortedContent.items():

        try:
            outputArray = fileRead(corePATH+ fileName)
            outputString = ""
            for line in outputArray:
                outputString += line
        except:
            outputString = ""

        outputString = outputString.encode()

        localmd5 = hashlib.md5(outputString).hexdigest()
        remotemd5 = hashlib.md5(requests.get(URL).content).hexdigest()

        if localmd5 != remotemd5:
            rmFile(corePATH + fileName)
            mkFile(corePATH + fileName)
            fileWrite(requests.get(URL).text, corePATH + fileName, overwrite=True)
            altered = True

    return altered

def exists(File):

    if os.path.isfile(File):

        return True

    return False

def mkFile(File):
        with open(File, "x") as file:
            return os.path.isfile(File)

def rmFile(File):
    try:
        os.remove(File)
        return True
    except:
        return False

def fileWrite(value, File, isLoop=False, overwrite=False, update=False):
    
    if exists(File):
        if overwrite and not update:
            if isLoop:
                count = 0
                with open(File, "w") as file:
                    while len(value) > count:
                        file.write(value[count] + "\n")
                        count += 1
            else:
                with open(File, "w") as file:
                    file.write(value)
        elif not overwrite and not update:
            if isLoop:
                count = 0
                with open(File, "a") as file:
                    while len(value) > count:
                        file.write(value[count] + "\n")
                        count += 1
            else:
                with open(File, "a") as file:
                    file.write(value)
                

        if update:
            print()
    else:
        return False

def getOS():
    return str(platform.system().lower())


def getSlash():
    OS = getOS()
    if OS.find("linux") != -1 or OS.find("mac") != -1:
        return "/"
    elif OS.find("win") != -1:
        return "\\"

def mkDir(path):
    try:
        os.makedirs(path)
    except:
        return False

    return True

def getCWD():
    return os.getcwd()

# reads a file and outputs an array
def fileRead(File):
    if exists(File):
        with open(File, "r") as file:
            out = []
            for line in file:
                out.append(line)
    else:
        out = []
    
    return out

def get():
    print("Checking for updates.")
    if selfUpdate() or update():
        print("Program files have been updated. Please restart the program.")
        exit()
