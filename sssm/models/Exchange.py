from models.stock.StockTypes import TYPE_COMMON, TYPE_PREFERRED

class ExchangeData:
    def __init__(self, stockType, lastDividend, fixedDividend, parValue):
        self.type = stockType
        self.lastDividend = lastDividend
        self.fixedDividend = fixedDividend
        self.parValue = parValue
    
    def getLastDividend(self):
        return self.lastDividend
    
    def getParValue(self):
        return self.parValue
    
    def getFixedDividend(self):
        return self.fixedDividend

    def __eq__(self, other):
        return self.type == other.type and self.lastDividend == other.lastDividend and self.fixedDividend == other.fixedDividend and self.parValue == other.parValue

    def __repr__(self):
        return ','.join([self.type, str(self.lastDividend), str(self.fixedDividend), str(self.parValue)])

data = {
    "TEA" : ExchangeData(stockType=TYPE_COMMON, lastDividend=0, fixedDividend=None, parValue=100),
    "POP" : ExchangeData(stockType=TYPE_COMMON, lastDividend=8, fixedDividend=None, parValue=100),
    "ALE" : ExchangeData(stockType=TYPE_COMMON, lastDividend=23, fixedDividend=None, parValue=100),
    "GIN" : ExchangeData(stockType=TYPE_PREFERRED, lastDividend=8, fixedDividend=0.02, parValue=100),
    "JOE" : ExchangeData(stockType=TYPE_COMMON, lastDividend=13, fixedDividend=None, parValue=100)
}