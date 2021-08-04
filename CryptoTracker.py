import requests, time, json

APIKey = "d852d06372cc0ae5e9a575a83ee535913a73c5886f64df3504009124a301caa3"

timeResolution = 5 # Unite : minutes
sleepTimer = timeResolution*60

BTC = []
ETH = []
LTC = []
XRP = []
ADA = []

t = []

pairs = ["BTC","ETH","LTC","XRP","ADA"]

while True:

    requestURL = "https://min-api.cryptocompare.com/data/pricemulti?fsyms="
    for pair in pairs:
        requestURL += pair + ","
    requestURL += "&tsyms=USD&api_key=" + APIKey

    requestResponse = requests.get(requestURL).json()
    
    BTC.append(requestResponse["BTC"]["USD"])
    ETH.append(requestResponse["ETH"]["USD"])
    LTC.append(requestResponse["LTC"]["USD"])
    XRP.append(requestResponse["XRP"]["USD"])
    ADA.append(requestResponse["ADA"]["USD"])
    
    t.append(time.localtime)

    time.sleep(sleepTimer)

# TO DO : Ajouter des tracés de courbes