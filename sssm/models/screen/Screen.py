from abc import ABC, abstractmethod
from models.stock.StockFunctions import dividendYield, peRatio, volumeWeightedStockPrice, allShareIndex, getStock, getPrice, getTrade
from models.screen import Banners 
from models.Trade import Trade
import models.Transactions as Transactions

class Screen(ABC):
    def __init__(self, banner):
        super().__init__()
        self.banner = banner
    
    @abstractmethod
    def displayScreen(self):
        print(self.banner)
    
    @abstractmethod
    def run(self):
        raise NotImplementedError()

#region NavigationScreens
class MainScreen(Screen):
    def displayScreen(self):
        return super().displayScreen()
    
    def run(self):
        self.displayScreen()

        print(Banners.MAIN_MENU)
        choice = input()

        return choice

class InvalidInputScreen(Screen):
    def displayScreen(self):
        return super().displayScreen()

    def run(self):
        self.displayScreen()

class ExitScreen(Screen):
    def displayScreen(self):
        return super().displayScreen()
    
    def run(self):
        self.displayScreen()
#endregion

#region Function Screens
class DividendYieldScreen(Screen):
    
    def displayScreen(self):
        return super().displayScreen()

    def run(self):
        self.displayScreen()
        
        stock, price = getStock(), getPrice()

        dy = dividendYield(stock, price)

        print("{0} : {1}".format(Banners.DIVIDEND_YIELD_PROMPT_RESULT, dy))

class PeRatioScreen(Screen):
    
    def displayScreen(self):
        return super().displayScreen()

    def run(self):
        self.displayScreen()
        
        stock, price = getStock(), getPrice()

        pe = peRatio(stock, price)

        print("{0} : {1}".format(Banners.PE_RATIO_PROMPT_RESULT, pe))

class RecordTradeScreen(Screen):
    def displayScreen(self):
        return super().displayScreen()

    def run(self):
        self.displayScreen()
        
        stock = getStock()
        trade = getTrade(stock)
        Transactions.addTransaction(stock, trade)

        print(Banners.RECORD_TRADE_RESULT_COMPLETE)

class VolumeWeightedStockPrice(Screen):
    def displayScreen(self):
        return super().displayScreen()
    
    def run(self):
        self.displayScreen()

        stock = getStock()
        vwsp = volumeWeightedStockPrice(stock)

        print("{0} : {1}".format(Banners.VOL_WEIGHT_RESULT, vwsp))

class AllShareIndexScreen(Screen):
    def displayScreen(self):
        return super().displayScreen()
    
    def run(self):
        self.displayScreen()

        asi = allShareIndex()

        print("{0} : {1}".format(Banners.ALL_SHARE_RESULT, asi))
#endregion

