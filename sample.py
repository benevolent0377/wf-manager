import requests


StatAPIHost = "https://api.warframestat.us/"
WikiAPIHost = "https://wf.snekw.com/"

response = requests.get(StatAPIHost + "drops/search/oxium")

if response.status_code == 200:

    data = response.json()
    print(data)
    # print(((data['data'])['Mods'])['Necramech Vitality'])
    print("success")

else:
    print("bummer")
