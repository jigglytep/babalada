import requests
import json

# api: https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to

# get the data from the api
def getData():
    # configUrl returns complete url
    url = configUrl()
    # params are set up for GET
    respoce = requests.get(url)
    # if everything went all right, return json data
    if (respoce.status_code == 200):
        data= json.loads(respoce.text)
        # returns just the list of number
        return data["results"]
    # else returns code   
    else:
        respoce.status_code

# configures the url with the correct params
def configUrl():
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
    return url