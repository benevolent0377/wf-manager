# this is a core updater file to update the core files through python, and will be builtin to all programs
# I no longer wanted to make installers for the core files, so the program will build it automatically through this file

import requests, platform, os, hashlib


def update():
    
    coreURL = "https://api.github.com/repositories/806174201/contents/files"
    slash = getSlash()
    corePATH = getCWD() + slash + "source" + slash + "core" + slash
    data = requests.get(coreURL)
    data = data.json()

    sortedContent = {}

    for item in data:
        sortedContent.update({item["name"]:item["download_url"]})

    altered = False

    for fileName, URL in sortedContent.items():

        outputArray = fileRead(corePATH + fileName)
        outputString = ""
        for line in outputArray:
            outputString += line

        outputString = outputString.encode()

        localmd5 = hashlib.md5(outputString).hexdigest()
        remotemd5 = hashlib.md5(requests.get(URL).content).hexdigest()

        if localmd5 != remotemd5:
            rmFile(corePATH + fileName)
            mkFile(corePATH + fileName)
            fileWrite(requests.get(URL).text, corePATH + fileName, overwrite=True)
            altered = True

    return altered

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

def getOS():
    return str(platform.system().lower())


def getSlash():
    OS = getOS()
    if OS.find("linux") != -1 or OS.find("mac") != -1:
        return "/"
    elif OS.find("win") != -1:
        return "\\"


def getCWD():
    return os.getcwd()

# reads a file and outputs an array
def fileRead(File):
    with open(File, "r") as file:
        out = []
        for line in file:
            out.append(line)

    return out

def get():
    print("Checking for updates.")
    if update():
        print("Successfully updated core files. Please restart the program.")
        exit() 
