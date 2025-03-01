from . import IO, system
import os

data = []
def init(configFileL, logPath):
    logID, logName, fileLog, sysDT = system.getLogInfo()

    if not os.path.isdir(logPath):
        if not IO.mkDir(logPath):
            IO.say("Failed to make log directory.")
            system.quitKill()

            # comment chunk for log creation, remove when you want logs
        else:
            if not os.path.isfile(fileLog):

                if IO.mkFile(fileLog):
                    IO.fileWrite(
                        [" ", f"Serial: {IO.yamlRead(configFileL, 'Program-SerialNo')}", f"LogID: {logID}", sysDT,
                         logName, " "], fileLog, isLoop=True)

                else:
                    IO.say("Log file creation failed.")
                    log("Log file creation failed.", "err")

    else:
        if not os.path.isfile(fileLog):

            if IO.mkFile(fileLog):
                IO.fileWrite(
                    [" ", f"Serial: {IO.yamlRead(configFileL, 'Program-SerialNo')}", f"LogID: {logID}", sysDT,
                     logName, " "], fileLog, isLoop=True)

            else:
                IO.say("Log file creation failed.")
                log("Log file creation failed.", "err")

    return fileLog

def log(value, action, element=""):
    match action:
        case "output":
            data.append(f"[{system.getDT(date=False)}]: Printed: \'{value}\'")
        case "mkfile":
            data.append(f"[{system.getDT(date=False)}]: File \'{value}\' created")
        case "mkdir":
            data.append(f"[{system.getDT(date=False)}]: Directory \'{value}\' created")
        case "input":
            data.append(f"[{system.getDT(date=False)}]: Read \'{value}\'")
        case "err":
            data.append(f"[{system.getDT(date=False)}]: Error Occurred: {value}")
            system.quitKill()
        case "rfile":
            data.append(f"[{system.getDT(date=False)}]: Read \'{value}\' from file \'{element}\'")
        case "wfile":
            data.append(f"[{system.getDT(date=False)}]: Wrote \'{value}\' to file \'{element}\'")
        case "rand":
            data.append(f"[{system.getDT(date=False)}]: Generated new random key.")
        case "ftpconnect":
            data.append(f"[{system.getDT(date=False)}]: Connected to \'{value}\' via FTP as \'{element}\'")
        case "ftpD":
            data.append(f"[{system.getDT(date=False)}]: Fetched \'{value}\' from \'{element}\' via FTP")
        case "ftpU":
            data.append(f"[{system.getDT(date=False)}]: Uploaded \'{value}\' to \'{element}\' via FTP")
        case "del":
            data.append(f"[{system.getDT(date=False)}]: Deleted \'{value}\'")
        case "quit":
            data.append(f"[{system.getDT(date=False)}]: Exit Code 0")
            close()

def close(flush=True):
    a, b, fileLog, c = system.getLogInfo()
    IO.fileWrite(data, fileLog, True, isLog=True, overwrite=False)
