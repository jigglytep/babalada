#---------------------------------------------------------
# The frist algorithm is the use of a regression line, whi- 
# ch is form the book. This line will measure if the stock
# price is going up or down, based on slope of the line
#---------------------------------------------------------
# IMPORTANT FORMULAS:
#   y = mx + b (for line itself)
#   m = (mean of (xy) - mean of (x) * mean of (y)) /
#       (mean of (x^2) - (mean of (x)^2))
#   b = mean of (y) - m * mean of (x)

from functools import reduce
import main

def meanOf(nums):
    # reduce adds all the element in nums together
    return (reduce(lambda x, y: x + y, nums)/ len(nums))

# finds the slope given two list of numbers
def getSlope(xs, ys):
    # map apply the same funciton to the a list, list then turns it into a list
    #map(lambda x, y: x * y, xs, ys) mutliplies xs[i] and ys[i] together
    numerator =  meanOf(list(map(lambda x, y: x * y, xs, ys))) - (meanOf(xs) * meanOf(ys))
    denominator = meanOf(list(map(lambda x: x * x, xs))) - (pow(meanOf(xs), 2)) 
    return (numerator / denominator)

# finds the y-intercept, which is b
def getYIntercept(xs, ys):
    return (meanOf(ys) - (getSlope(xs, ys) * meanOf(xs)))

# finds the equation for the reggression line
# returns it as a string
def getReggressionLine():
    data = main.getData()
    if (type(data) == list):
          # xs is the list of x values and y is the list of y values
        xs = []
        ys = []
        # the open price for a stock is added into ys
        for el in data:
            ys.append(el["o"])
        #then 1 to len(data) are added into xs
        for x in range(len(data)):
            xs.append(x)
        # the slope and y-intercept are found and then rounded to 3 places
        slope = round(getSlope(xs, ys), 3)
        b = round(getYIntercept(xs, ys), 3)
        # the if statment makes sure the correct sign are added to b
        # it also coverts slope and b to strings so it can concatenated
        if (b > 0):
            return ("y = " + str(slope) + "x + " + str(b))
        elif (b == 0):
            return ("y = " + str(slope) + "x")
        else:
            return ("y = " + str(slope) + "x " + str(b))
    else:
        # if nothing was returned (possibly becasue user gave
        # a nonexsisting stock name) then data's type is none
        if (type(data) == None):
            print("Error: No data was returned")
        else:
            print(f"Error code: {data}")