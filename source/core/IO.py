# a file of local inout functions making the process easy and keeping the main file decluttered
import os.path
from . import syntax, log
import yaml
import json


# simply prints the string output or creates a query in the terminal, also returns the inputted values
def say(output="", isQuestion=False, isLoop=False, syntaxChk=False, synType="", end="\n", ):
    # checking if the program wants a response, aka: question = yes
    if isQuestion:

        # seeing if the program wants to ask multiple queries
        if isLoop:
            loopVector = len(output)
            count = 0
            usrSay = []  # this is the returned list
            while loopVector > count:  # while the # of questions is greater than the responses, ask a question
                usrSay.append(input(output[count]))
                log.log(output[count], "output")
                log.log(usrSay[count], "input")
                count += 1

            if syntaxChk:
                return syntax.adv(usrSay, synType, isLoop)
            else:
                return usrSay

        else:
            log.log(output, "output")

            if syntaxChk:
                response = syntax.adv(input(output), synType, isLoop)  # says the output and returns the prompt
                log.log(response, "input")
                return response
            else:
                response = input(output)
                log.log(response, "input")
                return response
    # if the program does not want a response, aka: not a question
    else:

        # if the program has multiple statements to print out
        if isLoop:
            count = 0
            loopVector = len(output)
            while loopVector > count:  # while the number of statements is less than the number already stated, speak
                log.log(output[count], "output")
                # say more
                if syntaxChk:
                    print(syntax.adv(output[count], synType), end=end)
                else:
                    print(output[count], end=end)
                count += 1

        # if the program does not want a loop
        else:
            log.log(output, "output")
            if syntaxChk:
                print(syntax.adv(output, synType), end=end)
            else:
                print(output, end=end)


# WRITE TO A YAML FILE
def yamlWrite(value, element, File, isLoop=False):
    data = yamlRead(File, element, True)
    if data is None:
        data = {}
        if isLoop and len(element) == len(value):
            count = 0
            while len(element) > count:
                data.update({element[count]: value[count]})
                count += 1

        else:
            data.update({element: value})
    else:
        if isLoop:
            count = 0
            while len(element) > count:
                data.update({element[count]: value[count]})
                count += 1

        else:
            data.update({element: value})

    with open(File, "w") as file:
        log.log(element, "wfile", File)
        yaml.dump(data, file)


# read from a yaml file
def yamlRead(File, element, update=False, elements=1):
    with open(File, "r") as file:
        data = yaml.safe_load(file)
        log.log(element, "rfile", File)
        if data is None:
            return None

        else:
            if update:
                count = 0
                while elements > count:
                    data.update({element: data[element]})
                    count += 1

                return data
            else:
                return data[element]


# write into an element(s) of a json file
def jsonWrite(value, element, File, isLoop=False):
    # blah blah blah
    data = jsonRead(File, element, True)
    if data is None:
        data = {}
        if isLoop and len(element) == len(value):
            count = 0
            while len(element) > count:
                data.update({element[count]: value[count]})
                count += 1

        else:
            data.update({element: value})
    else:
        if isLoop:
            count = 0
            while len(element) > count:
                data.update({element[count]: value[count]})
                count += 1

        else:
            data.update({element: value})

    with open(File, "w") as file:
        log.log(element, "wfile", File)
        json.dump(data, file)


# read from a json file
def jsonRead(File, element, update=False, elements=1):
    # more blah
    with open(File, "r") as file:
        data = yaml.safe_load(file)
        log.log(element, "rfile", File)
        if data is None:
            return None

        else:
            if update:
                count = 0
                while elements > count:
                    data.update({element: data[element]})
                    count += 1

                return data
            else:
                return data[element]


def mkFile(File):
    with open(File, "x") as file:
        log.log(File, "mkfile")
        return os.path.isfile(File)


def mkDir(dir):
    os.mkdir(dir)
    log.log(dir, "mkdir")
    return os.path.isdir(dir)


def fileWrite(value, File, isLoop=False, overwrite=False, update=False, isLog=False):
    
    if fileExists(File):

        if overwrite and not update:
            if isLoop:
                count = 0
                with open(File, "w") as file:
                    while len(value) > count:
                        file.write(value[count] + "\n")
                        if not isLog:
                            log.log(value[count], "wfile", File)
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
                        if not isLog:
                            log.log(value[count], "wfile", File)
                        count += 1
            else:
                with open(File, "a") as file:
                    file.write(value)
                    if not isLog:
                        log.log(value, "wfile", File)

        if update:
            print()


# reads a file and outputs an array
def fileRead(File):
    if fileExists(File):
        with open(File, "r") as file:
            out = []
            for line in file:
                out.append(line)

        log.log(File, "rfile")
        return out
    else:
        return []

def fileExists(File):
        
    exists = os.path.isfile(File)

    if not exists:
        IO.say("File does not exist.")
        log.log(f"Nonexistent file: {File}", "err")

def checksum(localFile, remoteFile):

    match = True

    if fileExists(localFile):

        dataArray = fileRead(localFile)
        localData = ""

        for line in dataArray:
            localData += line

    else:

        localData = ""

    localData.encode()

    remoteData = requests.get(remoteFile)

    localmd5 = hashlib.md5(localData).hexdigest()
    remotemd5 = hashlib.md5(remoteData.content).hexdigest()

    if localmd5 != remotemd5:
        match = False

    return match
