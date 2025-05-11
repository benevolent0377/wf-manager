import requests
from source.core import syntax


wfApiAddress = "https://api.warframestat.us/"
wikiApiAddress = "https://wf.snekw.com/"
marketApiAddress = "https://api.warframe.market/v1/"
dropsApiAddress = "https://drops.warframestat.us/data/"

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

    queryType = syntax.adv(query, "internal")

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


def marketLookUp(item=""):

    item = syntax.adv(item, "nosymb")

    response = fetch(marketApiAddress + "items")

    responseData = response.json()['payload']['items']
    

    if response.status_code != 200:
        print("error")

    if item != "":

        matchedItems = []
        itemData = []
        
        for index in responseData:

            if index['item_name'].lower() == "item" or item in index['item_name'].lower():

                matchedItems.append(index)

        for obj in matchedItems:

            rawItemData = fetch(marketApiAddress + "items/" + obj["url_name"]).json()
            
            dataString = {'id': rawItemData['payload']['item']['id']}

            for index in rawItemData['payload']['item']['items_in_set']:

                for key in index:

                    valid = True
                
                    exclusions = ['ko', 'it', 'ku', 'sv', 'ru', 'fr', 'de', 'zh-hant', 'zh-hans', 'pt', 'es', 'pl', 'cs', 'uk']

                    for j in exclusions:
                    
                        if key == j:
                            valid = False
                            break
                    
                    if valid:
                        dataString.update({key: index[key]})

            itemData.append(dataString)

        return itemData

    return responseData


def getMarketOrders(item):

    itemData = marketLookUp(item)

    urlNames = getUrlNames(itemData)
    response = []
    data = []

    for index in range(len(urlNames)):

        response.append(fetch(marketApiAddress + "items/" + urlNames[index] + "/orders").json())
        data.append({'name': urlNames[index]})

        for u in range(len(response)):

            data[index].update({"orders": response[u]['payload']['orders']})

    return data

def getMarketStats(item):

    itemData = marketLookUp(item)

    urlNames = getUrlNames(itemData)

    itemStats = []
    data = []

    for index in range(len(urlNames)):

        itemStats.append(fetch(marketApiAddress + "items/" + urlNames[index] + "/statistics").json())
        data.append({'name': urlNames[index]})

        for u in range(len(itemStats)):

            data[index].update({'stats': itemStats[u]['payload']['statistics_live']})

    return data

def getUrlNames(data):

    urlNames = []

    for index in data:

        urlNames.append(index['url_name'])

    return urlNames


def parse(data, operation):
    
    if operation == "item-search":

        pass

    elif operation == "item":

        pass

    elif operation == "state":

        pass
