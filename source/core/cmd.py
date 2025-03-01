from . import IO, syntax, helper, log, system

# a file to parse all commands

def parse(values, req):
    cmdData = IO.yamlRead(f'{system.getConfigPath()}parent.yaml', 'cmdList')
    cmds = []
    loopVectorB = 0
    for command in cmdData:
        loopVectorA = 0
        while len(values) > loopVectorA:
            if command["name"].__eq__(values[loopVectorA]) or command["secondaryName"].__eq__(values[loopVectorA]):
                if command["takesParams"] >= 0:
                    if loopVectorA + 1 < len(values):
                        if values[loopVectorA + 1].startswith("-") and command["takesParams"] != 1:
                            IO.say(f"{values[loopVectorA + 1]} is not a valid option for {command['name']}")
                            log.log(f"{values[loopVectorA + 1]} is not a valid option for {command['name']}", "err")
                            loopVectorA += 1
                        else:
                            if values[loopVectorA + 1].find(",") != -1:
                                command.update({"args": values[loopVectorA + 1].split(",")})
                                cmds.append(command)
                            else:
                                command.update({"args": values[loopVectorA + 1]})
                                cmds.append(command)

                            loopVectorA += 2
                    else:
                        command.update({"args": ""})
                        cmds.append(command)
                        loopVectorA += 1
                else:
                    loopVectorA += 1
            else:
                loopVectorA += 1

        loopVectorB += 1

    read(cmds, req)


def read(pData, req, mode=0, chk="", regexStr="", isLoop=False):
    varsIn = {}

    if mode == 0:

        for item in pData:
            varsIn.update({item['secondaryName'].replace("--", ""): ""})
            varsIn.update({item['secondaryName'].replace("--", ""): item["args"]})
    else:
        varsIn = pData

    if mode == 0:
        return varsIn

    else:
        if isLoop:
            count = 0
            while len(chk) > count:
                if not syntax.adv(varsIn[chk[count]], regex=True, regexStr=regexStr[count]):
                    IO.say(f"'{varsIn[chk[count]]} is not valid.'")
                count += 1
        else:
            if not syntax.adv(varsIn[chk], regex=True, regexStr=regexStr):
                IO.say(f"'{varsIn[chk]} is not valid.'")

        varsIn.update({"stor": syntax.adv(varsIn["stor"], "dir")})

