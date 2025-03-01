import datetime
import os
import platform

from . import IO, extra, log, web, syntax


# a file to initialize the files and services needed to run the program
def init(directoriesReq, filesReq, onlineReq=False):
    global logID
    global sysDT
    logID = extra.keyGen(6)
    sysDT = getDT()

    fileSetup(directoriesReq, filesReq)

    if onlineReq:
        if not isOnline():
            quitKill()
        # IO.say("--- NOTICE Internet Capabilities Currently Disabled... NOTICE ---\n")


def fileSetup(directoriesReq, filesReq=""):
    slash = getSlash()

    for directory in directoriesReq:
        path = getCWD() + slash + directory + slash
        if not os.path.isdir(path):
            if not IO.mkDir(path):
                IO.say("Failed to create vital directory.")
                log.log("dir creation failed.", "err")
                quitKill()

    if filesReq != "":
        for file in filesReq:
            path = getCWD() + slash + file
            if not os.path.isfile(path):
                if not IO.mkFile(path):
                    IO.say("Failed to create vital files.")
                    log.log("dir creation failed.", "err")
                    quitKill()


# check for internet condition
def isOnline():
    if not web.ping():
        print("No internet discovered. Please establish an internet connection before running this program.")
        return False
    else:
        return True


def getOS():
    return platform.platform().lower()


def getSlash():
    OS = getOS()
    if OS.find("linux") or OS.find("mac"):
        return "/"
    elif getOS().find("win"):
        return "\\"
    else:
        return "/"


def getHomePath():
    return os.path.expanduser("~") + getSlash()


def getCWD():
    return os.getcwd()


def getConfigPath():
    return getCWD() + getSlash() + "config" + getSlash()


def getTmpPath():
    return f"{getCWD()}{getSlash()}tmp{getSlash()}"


def getDT(date=True, time=True):
    if date and time:
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    elif time and not date:
        return datetime.datetime.now().strftime('%H:%M:%S')
    elif date and not time:
        return datetime.datetime.now().strftime('%Y-%m-%d')


def getLogPath():
    return f"{getCWD()}{getSlash()}log{getSlash()}"


# deleting all files in the tmp directory
def clearCache():
    tmpPath = getTmpPath()
    tmpFiles = os.listdir(tmpPath)
    for file in tmpFiles:
        os.remove(f"{tmpPath}{file}")
        log.log(f"{tmpPath}{file}", "del")


def getLogInfo():
    logName = f"{sysDT}_{logID}.log.txt"
    logFile = f"{getLogPath()}{logName}"

    return [logID, logName, logFile, sysDT]

def getDataPath():
    return f"{getCWD()}{getSlash()}data{getSlash()}"

def getDownloadPath():
    return f"{getCWD()}{getSlash()}downloads{getSlash()}"

def getAssetsPath():
    return f"{getCWD()}{getSlash()}assets{getSlash()}"

# the quit function
def quitKill(preserve=False):
    if not preserve:
        clearCache()
    log.log("", "quit")
    exit()

def dumpHead():
    IO.say(['Created by: Calithos4136', f'Version: {IO.yamlRead(f"{getConfigPath()}local.yaml", "Version")}', f'SessionID: {logID}', '===========================================\n\n'], isLoop=True)

def mkConfig():
    OS = getOS()
    slash = getSlash()

    configFileP = f"{getConfigPath()}parent.yaml"
    configFileL = f"{getConfigPath()}local.yaml"
    sysPath = getCWD()
    homePath = getHomePath()
    logPath = getLogPath()

    web.fetchFTP(configFileP, "parent.yaml")

    if not os.path.isfile(configFileL):
        if IO.mkFile(configFileL):
            elements = ["OS", "CWD", "Home-Directory", "Program-SerialNo", "SendLogs", "Version"]
            values = [OS, sysPath, homePath, extra.keyGen(24), " ", "1.0.0 Alpha"]
            IO.yamlWrite(values, elements, configFileL, True)
        else:
            IO.say("Failed to create local configuration file.")
            log.log("local.config creation failed.", "err")
            quitKill()

    log.init(configFileL, logPath)

    sendLogs(configFileL)

def sendLogs(configFileL):

    if IO.yamlRead(configFileL, "SendLogs").__eq__(' '):
        response = IO.say("Would you like to opt into uploading log data? It IS anonymous. DEFAULT is no. (yes/no)", True, syntaxChk=True, synType="internal")
        if response.__eq__("yes") or response.__eq__("y"):
            IO.yamlWrite("True", "SendLogs", configFileL)
        else:
            IO.yamlWrite("False", "SendLogs", configFileL)
        IO.say("Thank you for using source.py!")
