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

        pass

    elif queryType == "warframes":

        pass

    elif queryType == "mods":

        pass

    elif queryType == "arcane":

        pass

    elif queryType == "icon":

        pass

    elif queryType == "void":

        pass 

    elif queryType == "ability":

        pass

    elif queryType == "focus":

        pass

    elif queryType == "missions":

        pass

    elif queryType == "research":

        pass

    elif queryType == "syndicate":

        pass



def parse(data, operation):
    
    if operation == "item-search":

        pass

    elif operation == "item":

        pass

    elif operation == "state":

        pass
