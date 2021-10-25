from datetime import datetime
from models.stock.Stock import STOCK_BUY, STOCK_BUY_CODE, STOCK_SELL, STOCK_SELL_CODE

class Trade:
    _indicatorMap = {STOCK_BUY_CODE: STOCK_BUY, STOCK_SELL_CODE:STOCK_SELL}

    def __init__(self, quantity, indicator, price, stock, timestamp=datetime.utcnow()):
        self.timestamp = timestamp
        self.quantity = quantity
        self.indicator = self._indicatorMap[indicator]
        self.tradePrice = price
        self.stock = stock

    def __ge__(self, other):#indicate datetime?
        return self.timestamp >= other

    def __repr__(self):
        return ','.join([str(self.timestamp), str(self.quantity), self.indicator, str(self.tradePrice), self.stock])