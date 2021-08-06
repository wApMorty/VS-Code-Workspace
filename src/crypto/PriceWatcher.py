import requests, time, json
import tensorflow as tf

# Constants
APIKey = "d852d06372cc0ae5e9a575a83ee535913a73c5886f64df3504009124a301caa3"

# Functions
def getValue(coin):
    requestURL = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + coin + "&tsyms=USD&api_key=" + APIKey
    requestResponse = requests.get(requestURL).json()
    return (requestResponse[coin]["USD"])

def ema(s, n):
    """
    returns an n period exponential moving average for
    the time series s

    s is a list ordered from oldest (index 0) to most
    recent (index -1)
    n is an integer

    returns a numeric array of the exponential
    moving average
    """
    ema = []
    j = 1

    if len(s) > n :
        #get n sma first and calculate the next n period ema
        sma = sum(s[:n]) / n
        multiplier = 2 / float(1 + n)
        for i in range(n):
            ema.append(sum(s[:n+1])/(n+1))

        #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
        ema.append(( (s[n] - sma) * multiplier) + sma)

        #now calculate the rest of the values
        for i in s[n+1:]:
            tmp = ( (i - ema[j]) * multiplier) + ema[j]
            j = j + 1
            ema.append(tmp)
    
    else :
        for i in range(len(s)):
            ema.append(sum(s[:i+1])/(i+1))

    return ema

def macd(s):
    shortEMA = ema(s, 12)[-1]
    longEMA = ema(s, 26)[-1]
    return (shortEMA - longEMA)

# Parameters
timeResolution = 1 # Unite : minutes
sleepTimer = timeResolution*60

# Variables initialization
btc = []