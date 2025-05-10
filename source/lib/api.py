import requests


wfApiAddress = "https://api.warframestat.us/pc/"
wikiApiAddress = "https://wf.snekw.com/"
marketApiAddress = "https://api.warframe.market/v1/"

def getState(item):

    response = ""
    worldStates = ['alerts', 'arbitration', 'archonHunt', 'cambionCycle', 'cetusCycle', 'dailyDeals', 'earthCycle', 'events', 'fissures', 'flashSales', 'globalUpgrades', 'invasions', 'kuva', 'news', 'nightwave', 'persistentEnemies', 'simaris', 'sortie', 'steelPath', 'syndicateMissions', 'vallisCycle', 'voidTrader']
    for query in worldStates:

        if query == item:

            response = fetch(wfApiAddress + query)

    if response.status_code != 200:

        print(f"Error accessing file. Returned status code: {response.status_code}.")
        return {}

    return response.json()


def fetch(URL, auth=False):

    if not auth:
    
        return requests.get(URL)
    
    else:

        pass

def 

