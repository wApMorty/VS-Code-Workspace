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

ema5 = []
ema10 = []
ema15 = []
ema20 = []
ema50 = []
ema100 = []
ema200 = []
macdValue = []
macdSignal = []

t = []

counter = 0

# Neural network model
inp = tf.keras.Input(shape=(20,))
dense1 = tf.keras.layers.Dense(10, activation=tf.keras.activations.relu)(inp)
dense2 = tf.keras.layers.Dense(5, activation=tf.keras.activations.relu)(dense1)
outp = tf.keras.layers.Dense(2, activation=tf.keras.activations.sigmoid)(dense2)
model = tf.keras.Model(inputs=inp, outputs=outp)

model.compile(optimizer='Adam', loss='meanSquaredError', metrics=['precision','recall','meaeenSquaredError'])

# main
while True:
    
    btc.append(getValue("BTC"))
    ema5 = ema(btc, 5)
    ema10 = ema(btc, 10)
    ema15 = ema(btc, 15)
    ema20 = ema(btc, 20)
    ema50 = ema(btc, 50)
    ema100 = ema(btc, 100)
    ema200 = ema(btc, 200)
    macdValue.append(macd(btc))
    macdSignal.append(ema(macd, 9)[-1])
    
    strTime = str(time.localtime()[2]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[0]) + " - " + str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
    
    t.append(strTime)

    while(time.localtime()[5] != 59):
        time.sleep(1)

    time.sleep(1)
    


