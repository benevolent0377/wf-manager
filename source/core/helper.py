from . import IO, system


# a file to handle all help requests

def request(command=""):
    cmdData = IO.yamlRead(f'{system.getConfigPath()}parent.yaml', 'cmdList')
    aMsg = {}
    bMsg = {}

    for item in cmdData:
        aMsg.update({item["secondaryName"]: item["helpMsg"]})
        bMsg.update({item["name"]: item["helpMsg"]})

    if command.__eq__(""):
        for item in cmdData:
            IO.say(f"{item['name']}  {item['secondaryName']}  {item['helpMsg']}")
    if aMsg.__contains__(command):
        IO.say(f"{command} {aMsg[command]}")
    elif  bMsg.__contains__(command):
        IO.say(f"{command} {bMsg[command]}")