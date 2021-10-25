import models.Exchange as exchange
import models.Transactions as Transactions
from models.screen import Banners
from models.stock.StockTypes import TYPE_COMMON, TYPE_PREFERRED
from models.stock.Stock import STOCK_TICKER_TEA, STOCK_TICKER_POP
from models.stock.Stock import STOCK_TICKER_ALE, STOCK_TICKER_GIN
from models.stock.Stock import STOCK_TICKER_JOE
from models.Trade import Trade


def _get_exchange_data(stock):
    if stock in exchange.DATA:
        return exchange.DATA[stock]
    raise KeyError


def dividend_yield(stock, price):
    """Calculates Dividend Yield

        Args:
            stock (str): The ticker
            price (float): the security price

        Returns:
            dividend yield
        """
    def common_dividend_yield(stock, price):
        if price > 0:
            stock_data = _get_exchange_data(stock)
            div_yield = stock_data.get_last_dividend() / price
            return round(div_yield, 2)
        return 0

    def preferred_dividend_yield(stock, price):
        if price > 0:
            stock_data = _get_exchange_data(stock)
            div_yield = (stock_data.get_fixed_dividend() * stock_data.get_par_value()) / price
            return round(div_yield, 2)
        return 0

    if price > 0:
        stock_data = _get_exchange_data(stock)

        if stock_data.type == TYPE_COMMON:
            return common_dividend_yield(stock, price)
        if stock_data.type == TYPE_PREFERRED:
            return preferred_dividend_yield(stock, price)

    return 0


def pe_ratio(stock, price):
    """Calculates P/E Ratio

        Args:
            stock (str): The ticker
            price (float): the security price

        Returns:
            p/e ratio
    """
    stock_data = _get_exchange_data(stock)
    dividend = stock_data.get_last_dividend()
    if dividend > 0:
        return round(price / dividend, 2)
    return 0


def volume_weighted_stock_price(stock):
    """Calculates vol. weighted stock price

        Args:
            stock (str): The ticker

        Returns:
            volume weighted stock price
    """
    return Transactions.get_volume_weighted_stock_price(stock)


def all_share_index():
    """Calculates All Share Index

        Args:
            None

        Returns:
            all share index
    """
    return Transactions.get_all_share_index()


#region helper Functions
def get_stock():
    """Reads stock ticker from user input

        Args:
            None

        Returns:
            stock ticker
    """
    print(Banners.PROMPT_STOCK_TICKER)
    stock = None

    while stock is None:

        choice = input()

        if choice == '1':
            stock = STOCK_TICKER_TEA
        elif choice == '2':
            stock = STOCK_TICKER_POP
        elif choice == '3':
            stock = STOCK_TICKER_ALE
        elif choice == '4':
            stock = STOCK_TICKER_GIN
        elif choice == '5':
            stock = STOCK_TICKER_JOE
        else:
            print(Banners.INVALID_BANNER)

    return stock


def get_price():
    """Reads stock price from user input

        Args:
            None

        Returns:
            stock price
    """
    print(Banners.PROMPT_PRICE)
    price = None

    while price is None:

        user_input = input()

        try:
            price = float(user_input)
        except ValueError:
            print(Banners.INVALID_NUMBER)

    return price


def get_trade(stock):
    """Records transaction from user input

        Args:
            None

        Returns:
            models.Trade
    """
    def get_int(prompt, validity_range=(float('-inf'), float('inf'))):
        print(prompt)
        num = None
        minimum = validity_range[0]
        maximum = validity_range[1]

        while num is None:

            user_input = input()

            try:
                num = int(user_input)

                if not minimum <= num <= maximum:
                    num = None
                    raise ValueError

            except ValueError:
                print(Banners.INVALID_NUMBER)

        return num

    quantity = get_int(Banners.RECORD_TRADE_PROMPT_QUANTITY)
    indicator = get_int(Banners.RECORD_TRADE_PROMPT_INDICATOR,
                        validity_range=(1, 2))
    price = get_price()

    return Trade(quantity, indicator, price, stock)
#endregion
