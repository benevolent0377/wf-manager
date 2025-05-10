import requests


wfApiAddress = "https://api.warframestat.us/"
wikiApiAddress = "https://wf.snekw.com/"
marketApiAddress = "https://api.warframe.market/v1/"

def getState(item, autoParse=True):

    response = ""
    worldStates = ['alerts', 'arbitration', 'archonHunt', 'cambionCycle', 'cetusCycle', 'dailyDeals', 'earthCycle', 'events', 'fissures', 'flashSales', 'globalUpgrades', 'invasions', 'kuva', 'news', 'nightwave', 'persistentEnemies', 'simaris', 'sortie', 'steelPath', 'syndicateMissions', 'vallisCycle', 'voidTrader']
    for query in worldStates:

        if query == item:

            response = fetch(wfApiAddress + "pc/" + query)

    if response.status_code != 200:

        print(f"Error accessing file. Returned status code: {response.status_code}.")
        return {}

    if autoParse:

        return parse(response.json(), "state")

    else:

        return response.json()


def fetch(URL, auth=False):

    if not auth:
    
        return requests.get(URL)
    
    else:

        pass

def getItemData(item, itemType, isExactSearch=True, autoParse=True):

    apiParams = ""

    if itemType.lower() == "res":

        apiParams = "items/"
    
    elif itemType.lower() == "weapons":

        apiParams = "weapons/"

    elif itemType.lower() =="mods":

        apiParams = "mods/"

    elif itemType.lower() == "warframes":

        apiParams = "warframes/"

    if itemType.lower() != "riven":

        if not isExactSearch:

            apiParams = apiParams + "search/" + item

        else:

            apiParams = apiParams + item
    else:

        # code the section for riven mods
        pass

    
    response = fetch(wfApiAddress + apiParams)

    if response.status_code != 200:
        print(f"error: {response.json()}")

        if autoParse:

            if isExactSearch:

                
                return parse(response.json(), "item-search"), isExactSearch
            
            else:

                return parse(response.json(), "item"), isExactSearch

        else:
            
            return response.json(), isExactSearch
    else:

        if autoParse:

            parse(response.json(), "item")

        else:
            
            return response.json(), isExactSearch

def wikiQuery(query, queryType):

    apiParams = ""

    queryType = queryType.lower()

    if queryType == "weapons":

        apiParams = apiParams + "weapons-wiki"

    elif queryType == "warframes":

        apiParams = apiParams + "warframes-wiki"

    elif queryType == "mods":

        apiParams = apiParams + "mods-wiki"

    elif queryType == "arcane":

        apiParams = apiParams + "arcanes-wiki"

    elif queryType == "icon":

        apiParams = apiParams + "icon-wiki"

    elif queryType == "void":

        apiParams = apiParams + "void-wiki"

    elif queryType == "ability":

        apiParams = apiParams + "ability-wiki"

    elif queryType == "focus":

        apiParams = apiParams + "focus-wiki"

    elif queryType == "missions":

        apiParams = apiParams + "missions-wiki"

    elif queryType == "research":

        apiParams = apiParams + "research-wiki"

    elif queryType == "syndicate":

        apiParams = apiParams + "syndicate-wiki"

    response = fetch(wikiApiAddress + apiParams)

    return response.json()



def parse(data, operation):
    
    if operation == "item-search":

        pass

    elif operation == "item":

        pass

    elif operation == "state":

        pass
