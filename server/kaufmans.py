#---------------------------------------------------------
# The third algorithm is Kaufman's Adaptive Moving Average 
# (KAMA) algorithm. Works just regression but is more accurate
#---------------------------------------------------------
# IMPORTANT CONSTANTS:
#   # of periods for effiecny ratio (er): 10
#   # of periods for fastest era: 2
#   # of periods for slowest era: 30
# IMPORTANT FORMULAS:
#   effiecny ratio = change / vollatility
#   change = |close - close from 10 periods ago|
#   volatility = sigma[1 to 10](|close - piror close|)
#   smoothing constant = (effiency ratio * (2/(2 + 1) - 2(30 + 1)) + 2(30 + 1))^2
#   KAMA = prior KAMA + sc * (price - prior KAMA)
# for more information: 
#   https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average
#   https://www.youtube.com/watch?v=n_K643pELY8

def getVollatility(closes):
    closesSum = 0
    for i in range(1, len(closes)):
        if i == 0:
            closesSum += abs(closes[0] - 0)
        else:
            closesSum += abs(closes[i] - closes[i -1])
    return closesSum
    
def getEr(start, end, vollatility):
    change = abs(end - start)
    return change / vollatility

def getSC(closes, vollatility):
    sc = getEr(closes[0], closes[-1], vollatility) * ((2/(2 + 1))  - (2/(30 + 1))) + (2/(30 + 1))
    return (sc * sc)

def getCurrentKama(closes, piror, price, v):
    kama = piror + getSC(closes, v) * (price - piror)
    return kama

def getKamas(closes):
    price = closes[-1]
    v = getVollatility(closes)
    kamas = []
    piror = getCurrentKama(closes, 0, price, v)
    for i in range(1, len(closes)):
        kamas.append(piror)
        piror = getCurrentKama(closes, piror, price, v)
    return {'k': kamas}