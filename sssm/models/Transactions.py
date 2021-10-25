import datetime

data = {}

_CummulativePriceProduct = 1
_NumberOfTransactions = 0

def _getRecentTrades(trades, timeDeltaInMinutes=15):
    def getIndexAtDeltaStart(trades, key):
        left, right = 0, len(trades) - 1
        boundaryIndex = -1
        while left <= right:
            mid = (left + right) // 2
            if trades[mid] >= key:
                boundaryIndex = mid
                right = mid - 1
            else:
                left = mid + 1
        return boundaryIndex

    key = datetime.datetime.utcnow() - datetime.timedelta(minutes=timeDeltaInMinutes)

    startIndex = getIndexAtDeltaStart(trades, key)
    return trades[startIndex:]

def addTransaction(stock, trade):
    global _CummulativePriceProduct
    global _NumberOfTransactions

    if stock in data:
        data[stock].append(trade)
    else:
        data[stock] = [trade]

    _CummulativePriceProduct *= trade.tradePrice
    _NumberOfTransactions += 1

def getAllShareIndex():
    if _NumberOfTransactions:
        return round(_CummulativePriceProduct ** (1 / _NumberOfTransactions), 2)
    return 0

def getVolumeWeightedStockPrice(stock):
    if stock in data:
        stockTransactions = data[stock]
        recentTrades = _getRecentTrades(stockTransactions)

        cummulativePrice = sum([trade.tradePrice * trade.quantity for trade in recentTrades])
        cummulativeQuantity = sum([trade.quantity for trade in recentTrades])
        return round(cummulativePrice/cummulativeQuantity, 2)
    return 0