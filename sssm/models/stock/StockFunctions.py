import models.Exchange as exchange
import models.Transactions as Transactions
from models.screen import Banners
from models.stock.StockTypes import TYPE_COMMON, TYPE_PREFERRED
from models.stock.Stock import STOCK_TICKER_TEA, STOCK_TICKER_POP, STOCK_TICKER_ALE, STOCK_TICKER_GIN, STOCK_TICKER_JOE
from models.Trade import Trade

def _getExchangeData(stock):
    if stock in exchange.data:
        return exchange.data[stock]
    raise KeyError

def dividendYield(stock, price):
    def commonDividendYield(stock, price):
        if price > 0:
            stockData = _getExchangeData(stock)
            dividendYield = stockData.getLastDividend() / price
            return round(dividendYield, 2)
        return -1

    def preferredDividendYield(stock, price):
        if price > 0:
            stockData = _getExchangeData(stock)
            dividendYield = (stockData.getFixedDividend() * stockData.getParValue()) / price
            return round(dividendYield, 2)
        return 0

    if price > 0:
        stockData = _getExchangeData(stock)

        if stockData.type == TYPE_COMMON:
            return commonDividendYield(stock, price)
        elif stockData.type == TYPE_PREFERRED:
            return preferredDividendYield(stock, price)

    return 0

def peRatio(stock, price):
    stockData = _getExchangeData(stock)
    dividend = stockData.getLastDividend()
    if dividend > 0:
        return round(price / dividend, 2)
    return 0

def volumeWeightedStockPrice(stock):
    return Transactions.getVolumeWeightedStockPrice(stock)

def allShareIndex():
    return Transactions.getAllShareIndex()

#region helper Functions
def getStock():
    print(Banners.PROMPT_STOCK_TICKER)
    stock = None

    while stock is None:

        choice = input()

        if choice == '1':
            stock = STOCK_TICKER_TEA
            break
        elif choice == '2':
            stock = STOCK_TICKER_POP
            break
        elif choice == '3':
            stock = STOCK_TICKER_ALE
            break
        elif choice == '4':
            stock = STOCK_TICKER_GIN
            break
        elif choice == '5':
            stock = STOCK_TICKER_JOE
            break
        else:
            print(Banners.INVALID_BANNER)
    
    return stock

def getPrice():
    print(Banners.PROMPT_PRICE)
    # price = float(input())
    price = None

    while price is None:

        userInput = input()

        try:
            price = float(userInput)
        except ValueError:
            print(Banners.INVALID_NUMBER)

    return price

def getTrade(stock):
    def getInt(prompt, validityRange=(float('-inf'), float('inf'))):
        print(prompt)
        num = None
        minimum = validityRange[0]
        maximum = validityRange[1]

        while num is None:

            userInput = input()

            try:
                num = int(userInput)
                
                if not (minimum <= num <= maximum):
                    num = None
                    raise ValueError
            
            except ValueError:
                print(Banners.INVALID_NUMBER)

        return num

    quantity = getInt(Banners.RECORD_TRADE_PROMPT_QUANTITY)
    indicator = getInt(Banners.RECORD_TRADE_PROMPT_INDICATOR, validityRange=(1, 2))
    price = getPrice()

    return Trade(quantity, indicator, price, stock)
#endregion