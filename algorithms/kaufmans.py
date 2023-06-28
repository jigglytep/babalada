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

# !NOTE! -> API ONLY ALLOWS 5 CALLS A MINUTE SO KAMAS MIGHT BE CALCUALTED SLOWLY

import requests
import json
from datetime import date, timedelta

# this function get the information for the first kama calculation
# it is just like getData() in main.py, but returns more info
# this makes it so further calls dont need user input for information
def getInitDataKAMA():
    data = configUrlKAMA()
     # params are set up for GET
    url = data["url"]
    respoce = requests.get(url)
    # if everything went all right, return json data
    if (respoce.status_code == 200):
        reply = json.loads(respoce.text)
        # returns a dict of info of the stock needed for 
        # next functions
        return { 
            'request': data,
            'results': reply["results"],
            'code': respoce.status_code
        }
    
# configures the URL and reutrn info about user input
def configUrlKAMA():
    # a ticker symbol identifies a stock
    ticker = input("Enter the ticker: ")
    # api needs it in uppercase, so if may be converted
    if (not ticker.isupper()):
        ticker = ticker.upper()
    # url is partly configed
    url = "https://api.polygon.io/v2/aggs/ticker/" + ticker
    # the start and end date are gotten - note they can be same day
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end day (YYYY-MMM-DD): ")
    # the last parts are added to the url to complete it
    url += "/range/25/minute/" + start + "/" + end +"?apiKey=KAwpTRBlsFOLCDCJLV4p8dbYeUnCphMQ"
    return {
        'url': url,
        'ticker': ticker,
        'start': start,
        'end': end
    }

# this get the data for every call after the frist one, in this one
# no user input is need becasue all info is povided in data
def getKAMAData(data, start):
    url = "https://api.polygon.io/v2/aggs/ticker/" + data["ticker"]
    url += "/range/25/minute/" + str(start) + "/" + data["end"] +"?apiKey=KAwpTRBlsFOLCDCJLV4p8dbYeUnCphMQ"
    respoce = requests.get(url)
    # if everything went all right
    if (respoce.status_code == 200):
        reply = json.loads(respoce.text)
        # returns data and code
        return { 
            'results': reply["results"],
            'code': respoce.status_code
        }
    # else returns error code
    else:
        return {
            'code': respoce.status_code
        }

# Get the data needed for a single KAMA
def getCloseAndPrice(data):
    # get last price
    price = data[len(data) - 1]["o"]
    # kData = 11 last closes + price
    kData = []
    #last 11 closes are added
    for i in range (0, 11):
        kData.append(data[len(data) - 1 - i]["c"])
    kData.append(price)
    return kData

# calculates the efficeny ratio
def calculateER(kdata):
    change = abs(kdata[10] - kdata[1])
    volatilty = 0
    for i in range (1, 11):
        volatilty += abs(kdata[i] - kdata[i - 1])
    return (change/volatilty)

# calculates smooty constant
def caluclateSC(kData):
    er = calculateER(kData)
    return (er * ((2/3) - (2/31)) + (2/31))

# get a single KAMA (prior = prior KAMA)
def getCurrentKAMA(kData, prior):
    return (prior + calculateER(kData) * (kData[-1] - prior))

# this finds KAMA value for data over from two date given by user
def getKAMAs():
    # this get the initalial information needed
    init = getInitDataKAMA()
    # data will hold data form next calls
    data = {}
    # kData = 11 last closes and currnet price
    kData = getCloseAndPrice(init["results"])
    # currKama = current kama, and 0 is used prior kama
    currKama = getCurrentKAMA(kData, 0)
    # kamaList will hold all kamas gotten
    kamaList =[]
    # the frist kama is added
    kamaList.append(currKama)
    # all data from kData is cleared to avoid problems
    kData.clear()
    # start = starting data, which is gotten from init call data
    # end is same thing for end
    start = date.fromisoformat(init['request']['start'])
    end = date.fromisoformat(init["request"]["end"])
    # td = a timedelta object, which helps add days to start date
    td = timedelta(days = 1)
    # while start data != end stat
    while (start != end):
        # a day is added to start
        start += td
        # data = data gotten from next call to api using info form init call
        data = getKAMAData(init["request"], start)
        # if everything went ok, then caluate kama, and add it to list
        if (data["code"] == 200):
            kData = getCloseAndPrice(data["results"])
            currKama = getCurrentKAMA(kData, currKama)
            kData.clear()
            kamaList.append(currKama)
        # else if something went wrong, substract the day that was added
        else:
            start -= td
    return kamaList