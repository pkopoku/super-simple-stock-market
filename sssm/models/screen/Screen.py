"""For the family of Screen classes"""
from abc import ABC, abstractmethod
from models.stock.StockFunctions import dividend_yield, pe_ratio
from models.stock.StockFunctions import volume_weighted_stock_price
from models.stock.StockFunctions import all_share_index, get_stock
from models.stock.StockFunctions import get_price, get_trade
from models.screen import Banners
import models.Transactions as Transactions


class Screen(ABC):
    """
    Abstract Screen template class

    Attributes:
        banner (str): The main display banner
    """
    def __init__(self, banner):
        super().__init__()
        self.banner = banner

    @abstractmethod
    def display_screen(self):
        """override to display main screen"""
        raise NotImplementedError()

    @abstractmethod
    def run(self):
        """override to implement screen logic"""
        raise NotImplementedError()


#region NavigationScreens
class MainScreen(Screen):
    """
    Concrete implementation of main screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()

        print(Banners.MAIN_MENU)
        choice = input()

        return choice


class InvalidInputScreen(Screen):
    """
    Concrete implementation of invalid input screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()


class ExitScreen(Screen):
    """
    Concrete implementation of exit screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()
#endregion


#region Function Screens
class DividendYieldScreen(Screen):
    """
    Concrete implementation of div yield screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()
        stock, price = get_stock(), get_price()
        div_yield = dividend_yield(stock, price)

        print("{0} : {1}"
              .format(Banners.DIVIDEND_YIELD_PROMPT_RESULT, div_yield))


class PeRatioScreen(Screen):
    """
    Concrete implementation of p/e ratio screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()
        stock, price = get_stock(), get_price()
        ratio = pe_ratio(stock, price)

        print("{0} : {1}".format(Banners.PE_RATIO_PROMPT_RESULT, ratio))


class RecordTradeScreen(Screen):
    """
    Concrete implementation of trading screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()
        stock = get_stock()
        trade = get_trade(stock)
        Transactions.add_transaction(stock, trade)

        print(Banners.RECORD_TRADE_RESULT_COMPLETE)


class VolumeWeightedStockPrice(Screen):
    """
    Concrete implementation of vol. weighted stock screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()
        stock = get_stock()
        vol_weight_stock_price = volume_weighted_stock_price(stock)

        print("{0} : {1}".format(Banners.VOL_WEIGHT_RESULT, vol_weight_stock_price))


class AllShareIndexScreen(Screen):
    """
    Concrete implementation of All Share Index screen

    Attributes:
        banner (str): The main display banner
    """
    def display_screen(self):
        print(self.banner)

    def run(self):
        self.display_screen()
        as_index = all_share_index()

        print("{0} : {1}".format(Banners.ALL_SHARE_RESULT, as_index))
#endregion
