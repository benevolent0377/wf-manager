from source.core import system, IO, log

class FileSystem:

    def __init__(self, directoriesReq, filesReq=""):
        self.onlineReq = True
        system.init(directoriesReq, filesReq, self.onlineReq)
        self.directories = directoriesReq
        self.files = filesReq
        self.CWD = system.getCWD()
        self.logID = system.logID
        self.instanceID = system.logID
        self.sysDT = system.sysDT
        self.slash = system.getSlash()
        self.OS = system.getOS()
        self.homePath = system.getHomePath()
        self.configPath = f"{self.CWD}{self.slash}config{self.slash}"
        self.cachePath = f"{self.CWD}{self.slash}cache{self.slash}"
        self.tmpPath = f"{self.CWD}{self.slash}tmp{self.slash}"
        self.logPath = f"{self.CWD}{self.slash}log{self.slash}"
        self.userdataPath = f"{self.CWD}{self.slash}.userdata{self.slash}"
        self.pgmdataPath = f"{self.CWD}{self.slash}.pgmdata{self.slash}"
        self.logName = system.getLogInfo()[1]
        self.file = system.getLogInfo()[2]

    
    def isOnline(self):
        return system.isOnline()

    def clearCache(self):
        system.clearCache()

    def getLogInfo(self):
        return system.getLogInfo()

    def buildConfig(self, fileNames, fileData=[]):

        defData = {'OS': self.OS, 'CWD': self.CWD, 'Home-Directory': self.homePath, 'Program-SerialNo': self.logID, 'SendLogs': False, 'Version': "v0 DEV-ALPHA"}

        if len(fileData) > 0:
            #  develop this
            pass
        else:
            fileData.append(defData)

        for fileName in fileNames:
            if IO.fileExists(f"{self.configPath}{fileName}"):
                pass
            else:
                if not IO.mkFile(f"{self.configPath}{fileName}"):
                    log.log(f"{fileName} creation failed.", "err")
                    system.quitKill()
        
        for file in range(len(fileData)):
            if IO.fileExists(f"{self.configPath}{fileNames[file]}"):
                elements = []
                values = []

                for key, data in fileData[file].items():
                    elements.append(key)
                    values.append(data)

                IO.yamlWrite(values, elements, f"{self.configPath}{fileNames[file]}", True)
                log.log(fileData[file], "wfile", f"{self.configPath}{fileNames[file]}")
        
        log.init(f"{self.configPath}{fileNames[0]}", self.logPath)