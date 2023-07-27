#---------------------------------------------------------
# The second algorithm is Mean Reversion. This finds the 
# current mean of a segment of time, and also the current
# high and lows
#---------------------------------------------------------
import yfinance as yf

def getRange(ticker):
    responce = yf.Ticker(ticker)
    return {
        "high": responce.info["regularMarketDayHigh"],
        "low": responce.info["regularMarketDayLow"]
    }