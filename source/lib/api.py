import requests
from source.core import syntax

# api links
wfApiAddress = "https://api.warframestat.us/"
# wikiApiAddress = "https://wf.snekw.com/"
marketApiAddress = "https://api.warframe.market/v1/"
dropsApiAddress = "https://drops.warframestat.us/data/all.json"

# a function to get the state of the requested item, as it corresponds
# to the worldStates list


def getState(item, autoParse=True):
    response = ""
    worldStates = ['alerts', 'arbitration', 'archonHunt', 'cambionCycle', 'cetusCycle', 'dailyDeals', 'earthCycle', 'events', 'fissures', 'flashSales', 'globalUpgrades', 'invasions', 'kuva', 'news', 'nightwave', 'persistentEnemies', 'simaris', 'sortie', 'steelPath', 'syndicateMissions', 'vallisCycle', 'voidTrader']
    # checking to see if the query matches the approved list of world states
    for query in worldStates:

        if query == item:

            response = fetch(wfApiAddress + "pc/" + query)

    if response.status_code != 200:

        return response.status_code

    # if the data is intended to be parsed by a set algorithm
    # in the parse function
    if autoParse:

        return parse(response.json(), "state")
    # returns the unparsed data
    else:

        return response.json()


# this function returns the data requested by the server contacted
def fetch(URL, auth=False):

    response = ""

    # if there is not any kind of authentication required
    if not auth:
    
       response = requests.get(URL)
    
    else:

        # there is no functionality for authentication
        pass

    if response.status_code != 200:

        print(f"Request to {URL} returned status code {response.status_code}.")

    return response


# a function to return data on items by request (exact or broad search) from the warframe API
def getItemData(item, itemType, isExactSearch=True, autoParse=False):

    apiParams = ""

    itemType = syntax.adv(itemType, 'internal')
    
    # checking to see if the item type is valid and applying the correct link
    if itemType == "res":

        apiParams = "items/"
    
    elif itemType == "weapons":

        apiParams = "weapons/"

    elif itemType =="mods":

        apiParams = "mods/"

    elif itemType == "warframes":

        apiParams = "warframes/"

    # check specially to see if the request is a riven
    if itemType != "riven":
        
        # if it is a broad search
        if not isExactSearch:
            
            # search all items
            apiParams = apiParams + "search/" + item

        else:
            
            # otherwise look for the specific item
            apiParams = apiParams + item
    # if the item type is riven
    else:

        # code the section for riven mods
        pass

    # fetch the data from the link
    response = fetch(wfApiAddress + apiParams)

    # ensure the reponse was properly received
    if response.status_code == 200:

        # if the response is to be parsed by a preformatted algorithm
        if autoParse:
            
            # checking to see if the response was an exact search to ensure correct data parsing
            if isExactSearch:

                return parse(response.json(), "item-search"), isExactSearch
            
            else:

                return parse(response.json(), "item"), isExactSearch
        
        # return raw data
        else:
            
            return response.json(), isExactSearch
    # if there was a status code of anything other than 200, return the code to be handled
    else:

        return response.status_code


# a function to look up the data on a specific item on the market, and also search for items on the market
def marketLookUp(item=""):

    # run syntax on the request, since this will be by user input
    item = syntax.adv(item, "nosymb")
    
    # get all the items on the site
    response = fetch(marketApiAddress + "items")

    # ensure the data was properly accessed
    if response.status_code != 200:
        return response.status_code
    
    # breaking into the payload data
    responseData = response.json()['payload']['items']

    # if there was something specified, get specific data
    if item != "":

        matchedItems = []
        itemData = []
        
        # the loops below get the proper data from the api, sorting through multiple languages and extra data that is not used
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
        
        # return the specific item data built into a custom dict
        return itemData
    
    # returns all data if there was nothing specified
    return responseData


# a function to get the orders listed for a specific item
def getMarketOrders(item):
    
    # run a syntax check as this will be often user input
    item = syntax.adv(item, "nosymb")

    # get all the data for that item
    itemData = marketLookUp(item)

    # get all the site names of the items received in the search
    urlNames = getUrlNames(itemData)
    response = []
    data = []

    # for each item
    for index in range(len(urlNames)):
        # get the orders of the item specified
        response.append(fetch(marketApiAddress + "items/" + urlNames[index] + "/orders").json())
        
        # append the name of the item to a new dictionary
        data.append({'name': urlNames[index]})
        
        # for each item in the response
        for u in range(len(response)):
            
            # seperate the data from the raw responses and put it into the corresponding dict item
            data[index].update({"orders": response[u]['payload']['orders']})

    return data # return the item

    # how to read this data is as follows:
    #   data first is an array so access the different items queried in the search
    #       example: if my search returned 2 items, there would be 2 dictionaries (2 indexes) in this data variable
    #   inside each dictionary are two keys, 'name' and 'orders'
    #       name contains the name of the searched and served item
    #       orders contains another array of dictionaries containing all the orders for that item on the site
    #   if you want to access a specific order of an item type, inside the orders array, select an index, and then you will have access to all of the data to that specific order
    #
    # an example of how to use this data could be:
    #   to get all orders of all items: data
    #   to get orders of a specific item (in this case the first item in the results): data[0]
    #   to get the name of the item: data[0]['name']
    #   to get all orders of that item: data[0]['orders']
    #   to get a specific order of that item: data[0]['orders'][0]
    #   to get the id of a specific order of the requested item: data[0]['orders'][0]['id']


# get the statistics for the queried item
# this function acts the exact same as the getMarketOrders() function
def getMarketStats(item):

    item = syntax.adv(item, 'nosymb')

    itemData = marketLookUp(item)

    urlNames = getUrlNames(itemData)

    itemStats = []
    data = []

    for index in range(len(urlNames)):

        itemStats.append(fetch(marketApiAddress + "items/" + urlNames[index] + "/statistics").json())
        data.append({'name': urlNames[index]})

        for u in range(len(itemStats)):

            data[index].update({'stats': itemStats[u]['payload']['statistics_live'], 'oldStats': itemStats[u]['payload']['statistics_closed']})

    return data

    # the way data can be accessed and parsed is the same here as it is for the getMarketOrders() function
    # BUT instead of using 'orders', use 'stats'


# a function to get the site specific names of the data parssed into the function
def getUrlNames(data):

    urlNames = []

    for index in data:

        urlNames.append(index['url_name'])

    return urlNames


def getDropTables():

    response = fetch(dropsApiAddress)
    rawData = response.json()

    dropTables = []

    for key in rawData.keys():

        dropTables.append(key)

    return response, dropTables

# the drop tables functions below are incomplete, and will not work if called (except for getMissionDropData(), queryDropTables(), and getRelicDropData(), these work)


def getItemDropData(item, itemType):

    itemType = syntax.adv(itemType, "nosymb")

    match itemType:

        case 'prime':

            return getRelicDropData(item)

        case 'relic':

            return getRelicDropData(item)

        case 'mod':

            return getModDropData(item)

        case 'resource':

            return getResourceDropData(item)

        case 'spResource':

            return getSpEntityDropData(item)

    return "end"


def queryDropTables(tables):

    data = []
    response, dropTables = getDropTables()

    for table in tables:

        data.append(response.json()[dropTables[table]])

    return data


# works
def getMissionDropData(query):

    query = syntax.adv(query, "nosymb").lower()

    tablesReq = [0, 2]

    tables = queryDropTables(tablesReq)

    output = {'query': query, 'results': [], 'missions': []}
    data = []

    for table in range(len(tables)):

        if table == 0:

            planets = tables[table]

            for planet in planets:

                for mission in planets[planet]:
                    
                    if query in mission.lower() or query == mission.lower():
                        output['missions'].append({'name': mission, 'data': planets[planet][mission]})

                    for rotation in planets[planet][mission]['rewards']:
                    
                        if rotation != 'A' and rotation != 'B' and rotation != 'C':

                            for reward in range(len(planets[planet][mission]['rewards'])):
                            
                                if query.replace(' ', '') in planets[planet][mission]['rewards'][reward]['itemName'].lower().replace(' ', '') or query.replace(' ', '') == planets[planet][mission]['rewards'][reward]['itemName'].lower().replace(' ', '') or query == planets[planet][mission]['rewards'][reward]['_id']:
                                
                                    data.append({'location': planet, 'mission': mission, 'rotation': 'None', 'reward': planets[planet][mission]['rewards'][reward]})

                        else:

                            for reward in range(len(planets[planet][mission]['rewards'][rotation])):

                                if query.replace(' ', '') in planets[planet][mission]['rewards'][rotation][reward]['itemName'].lower().replace(' ', '') or query.replace(' ', '') == planets[planet][mission]['rewards'][rotation][reward]['itemName'].lower().replace(' ', '') or query == planets[planet][mission]['rewards'][rotation][reward]['_id']:
                                
                                    data.append({'location': planet, 'mission': mission, 'rotation': rotation, 'reward': planets[planet][mission]['rewards'][rotation][reward]})
                                
        else:

            missionTypes = tables[table]

            for missionType in range(len(missionTypes)):

                for rewardList in missionTypes[missionType]['rewards']:

                    if query in rewardList['itemName'].lower():

                        data.append({'objectiveName': missionTypes[missionType]['objectiveName'], 'reward': rewardList})
    

    output.update({'results': data})

    return output


# works
def getRelicDropData(query):

    query = syntax.adv(query, "nosymb").lower()

    tablesReq = [1]

    tables = queryDropTables(tablesReq)

    output = {'query': query, 'results': []}
    data = []

    for table in range(len(tables)):

        if table == 0:

            for relic in tables[0]:

                if query == relic['tier'].lower():
                    data.append({'data': relic, 'sources': False})

                elif query == relic['relicName'].lower() or query.replace(" ", "") == relic['tier'].lower() + relic['relicName'].lower() or query == relic['_id']:

                    relicID = relic['tier']+relic['relicName']
                    data.append({'data': relic, 'sources': getMissionDropData(relicID)['results']})

    output.update({'results': data})

    return output


def getEnemyDropData(query):

    query = syntax.adv(query, 'nosymb')

    tablesReq = [4, 6]

    tables = queryDropTables(tablesReq)

    output = {'query': query, 'results': []}
    data = []
    enemyData = []

    query = query.lower().replace(' ', '')

    for table in range(len(tables)):
        # access the enemy mod tables
        if table == 0:

            for enemy in tables[0]:

                if query in enemy['enemyName'].lower().replace(' ', ''):

                    enemyData.append({'enemyName': enemy['enemyName'], 'enemyModDropChance': enemy['enemyModDropChance'], 'mods': enemy['mods'], 'items': None, 'blueprints': None})

        # access the blueprint drop tables by enemy name
        elif table == 1:

            for enemy in tables[1]:

                if query in enemy['enemyName'].lower().replace(' ', ''):

                    for dataPoint in enemyData:

                        if enemy['enemyName'] == dataPoint['enemyName']:
                            dataPoint['blueprints'] = enemy['items']

    data = enemyData

    output.update({'results': data})
    return output


def getModDropData(query):

    output = {'query': query, 'results': []}

    query = syntax.adv(query, "nosymb").lower()

    tablesReq = [3]

    tables = queryDropTables(tablesReq)

    data = []

    query = query.lower().replace(' ', '')

    for mod in tables[0]:

        if query in mod['modName'].lower().replace(" ", ""):

            data.append({'modName': mod['modName'], 'sources': mod['enemies']})

    output.update({'results': data})
    return output


# there's so many more functions to write
def getSortieDropData(query):

    output = {'query': query, 'results': []}
    query = syntax.adv(query, 'nosymb').lower()
    data = []

    table = queryDropTables([7])

    data = table[0]

    output.update({'results': data})
    return output


def getBountyDropData(syndicate):

    output = {'query': syndicate, 'results': []}
    data = []

    # defining syndicate table codes
    CETUS = 9
    SOLARIS = 10
    DEIMOS = 11
    ZARIMAN = 12
    ENTRATI = 13
    HEX = 14
    ALL = [CETUS, SOLARIS, DEIMOS, ZARIMAN, ENTRATI, HEX]

    match syndicate:

        case "*":
            tablesReq = ALL

        case "Cetus":
            tablesReq = [CETUS]

        case "Solaris":
            tablesReq = [SOLARIS]

        case "Deimos":
            tablesReq = [DEIMOS]

        case "Zariman":
            tablesReq = [ZARIMAN]

        case "Entrati":
            tablesReq = [ENTRATI]

        case "Hex":
            tablesReq = [HEX]

    if tablesReq == ALL:

        tables = queryDropTables(tablesReq)

        iteration = 9

        for table in tables:

            match iteration:
                case 9:
                   data.append({'syndicateName': 'Cetus', 'data': table})
                case 10:
                    data.append({'syndicateName': 'Solaris', 'data': table})
                case 11:
                    data.append({'syndicateName': 'Deimos', 'data': table})
                case 12:
                    data.append({'syndicateName': 'Zariman', 'data': table})
                case 13:
                    data.append({'syndicateName': 'Entrati', 'data': table})
                case 14:
                    data.append({'syndicateName': 'Hex', 'data': table})
            iteration += 1
    else:

        table = queryDropTables(tablesReq)

        data = table  # no loop needed

    output.update({'results': data})
    return output


def getSyndicateDropData(query):

    output = {'query': query, 'results': []}
    tablesReq = [15]
    data = []

    table = queryDropTables(tablesReq)

    for syndicate in table[0].keys():

        if syndicate == query:

            data.append(table[0][syndicate])

        elif query == "*":

            data.append({syndicate: table[0][syndicate]})

        else:
            query = syntax.adv(query, "nosymb").lower()

            for item in table[0][syndicate]:

                if query in item['item'].lower().replace(" ", ""):
                    data.append(item)

    output.update({'results': data})
    return output


def getSpEntityDropData(query):

    output = {'query': query, 'results': []}
    query = syntax.adv(query, "nosymb").lower()
    data = {'entities': [], 'items': []}
    tablesReq = [17, 18]
    tables = queryDropTables(tablesReq)

    for table in tables:
        for entity in table:

            if query in entity['source'].lower().replace(" ", ""):
                data['entities'].append(entity)
            else:
                for item in entity['items']:
                    if query in item['item'].lower().replace(" ", ""):
                        data['items'].append(item)

    output.update({'results': data})
    return output


def getResourceDropData(query):

    output = {'query': query, 'results': []}
    query = syntax.adv(query, "nosymb").lower()
    data = {'source': [], 'resources': []}
    tablesReq = [16]

    table = queryDropTables(tablesReq)
    for tab in table:

        for entity in tab:

            if query in entity['source'].lower().replace(" ", ""):
                data['source'].append(entity['source'])
                data['resources'].append(entity['items'])

            else: 
                for item in entity['items']:

                    if query in item['item'].lower().replace(" ", ""):
                        data['source'].append(entity['source'])
                        data['resources'].append(item)

    output.update({'results': data})
    return output


def parse(data, operation):

    if operation == "item-search":

        pass

    elif operation == "item":

        pass

    elif operation == "state":

        pass

