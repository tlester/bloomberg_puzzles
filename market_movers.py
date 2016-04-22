#!/usr/bin/python

def marketMovers(lst, n):
    topCount = n
    stocks = {}
    results = []
    for tick in lst:
        if tick[0] in stocks.keys():
            stocks[tick[0]].append(tick[1])
        else:
            stocks[tick[0]] = [tick[1]]

    for stock in stocks:
        low = sorted(stocks[stock])[0]
        high = sorted(stocks[stock])[-1]
        results.append([high - low, stock])
    results = sorted(results, reverse=True)
    for e in range(0, n):
        print "{} => {}".format(results[e][1], results[e][0])


# The following example should print:
# goog => 3
# appl => 9

movers = marketMovers([("ibm",  100),
                       ("appl", 500),
                       ("appl", 502),
                       ("hp",    34),
                       ("msft", 212),
                       ("goog", 405),
                       ("ibm",   99),
                       ("goog", 408),
                       ("msft", 211),
                       ("appl", 509)],
                       2)
