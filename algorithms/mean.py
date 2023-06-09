#---------------------------------------------------------
# The second algorithm is Mean Reversion. This finds the 
#current mean of a segment of time, and also the current
# high and lows
#---------------------------------------------------------
import main

# gets all the high and lows from a certain time period
# if highestAndLowest is set to true, it just hets highest and lowest
def getHighsAndLows(highestAndLowest: bool):
    # gets that data
    data = main.getData()
    if(type(data) == list):
        if (not highestAndLowest):
            # h = highest list, l = lowest list
            h = []
            l = []
            # complete wil hold both list later
            complete = []
            # highs get put in h and lows in l
            for result in data:
                h.append(result["h"])
                l.append(result["l"])
            # list added in complete and returned
            complete.append(h)
            complete.append(l)
            return complete
        else: 
            # init val (not low is 1000 just make sure it gets val
            # it's val doesn't matter as long as it's high)
            high = 0
            low = 1000
            # highest and lowest is found
            for result in data:
                if (high < result["h"]):
                    high = result["h"]
                if (low > result["l"]):
                    low = result["l"]
            # they are returned in a dict
            return dict(highest = high, lowest = low)
    else:
        print("Error")