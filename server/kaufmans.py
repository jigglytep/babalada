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

def getEr(closes):
    change = abs(closes[9] - closes[0])
    closesSum = 0
    for i in range(1, len(closes)):
        if i == 0:
            closesSum += abs(closes[0] - 0)
        else:
            closesSum += abs(closes[i] - closes[i -1])
    return change / closesSum

def getSC(closes):
    sc = getEr(closes) * ((2/(2 + 1))  - (2/(30 + 1))) + (2/(30 + 1))
    return (sc * sc)

def getCurrentKama(closes, piror, price):
    kama = piror + getSC(closes) * (price - piror)
    return kama
