import requests


wfApiAddress = "https://api.warframestat.us/"
wikiApiAddress = "https://wf.snekw.com/"
marketApiAddress = "https://api.warframe.market/v1/"

def getState(item):

    response = ""
    worldStates = ['alerts', 'arbitration', 'archonHunt', 'cambionCycle', 'cetusCycle', 'dailyDeals', 'earthCycle', 'events', 'fissures', 'flashSales', 'globalUpgrades', 'invasions', 'kuva', 'news', 'nightwave', 'persistentEnemies', 'simaris', 'sortie', 'steelPath', 'syndicateMissions', 'vallisCycle', 'voidTrader']
    for query in worldStates:

        if query == item:

            response = fetch(wfApiAddress + "pc/" + query)

    if response.status_code != 200:

        print(f"Error accessing file. Returned status code: {response.status_code}.")
        return {}

    return response.json()


def fetch(URL, auth=False):

    if not auth:
    
        return requests.get(URL)
    
    else:

        pass

def getItemData(item, itemType, isExactSearch=True):

    apiParams = ""

    if itemType.lower() == "res":

        apiParams = "items/"
    
    elif itemType.lower() == "weapon":

        apiParams = "weapons/"

    elif itemType.lower() =="mod":

        apiParams = "mods/"

    elif itemType.lower() == "warframes":

        apiParams = "warframes/"

    if not isExactSearch:

        apiParams = apiParams + "search/" + item

    else:

        apiParams = apiParams + item

    
    response = fetch(wfApiAddress + apiParams)

    if response.status_code != 200:
        print(f"error: {response.json()}")
        return response.json(), isExactSearch
    else:
        return response.json(), isExactSearch

