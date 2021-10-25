import datetime

DATA = {}


class Cummulation:
    """Class to circumvent managing global accumulation variables"""
    def __init__(self, cummulative_pp, num_trans):
        self.cpp = cummulative_pp
        self.num_transactions = num_trans


    def accumulate(self, price):
        """For the running accumulation of p1 . p2 ... . pn

        Args:
            price (float): the security price
        """
        self.cpp *= price
        self.num_transactions += 1

    def get_cummulative_price_product(self):
        """returns cummulative price product"""
        return self.cpp
    
    def get_number_of_transactions(self):
        """returns number of transactions"""
        return self.num_transactions


ACCUMULATOR = Cummulation(1, 0)

def _get_recent_trades(trades, time_delta_in_minutes=15):
    def get_index_at_delta_start(trades, key):
        left, right = 0, len(trades) - 1
        boundary_index = -1
        while left <= right:
            mid = (left + right) // 2
            if trades[mid] >= key:
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return boundary_index

    key = datetime.datetime.utcnow() - datetime.timedelta(minutes=time_delta_in_minutes)

    start_index = get_index_at_delta_start(trades, key)
    return trades[start_index:]


def add_transaction(stock, trade):
    """Record Transaction

    Args:
        stock (str): The ticker
        trade (models.Trade): the trade object
    """
    if stock in DATA:
        DATA[stock].append(trade)
    else:
        DATA[stock] = [trade]

    ACCUMULATOR.accumulate(trade.trade_price)


def get_all_share_index():
    """Calculates All Share Index

    Args:
        None

    Returns:
        All Share Index
    """
    number_of_transactions = ACCUMULATOR.get_number_of_transactions()
    if number_of_transactions:
        return round(
            ACCUMULATOR.get_cummulative_price_product() 
            ** (1 / number_of_transactions), 2)
    return 0

def get_volume_weighted_stock_price(stock):
    """Calculates Volume Weighted Stock Price

    Args:
        stock (str): The ticker

    Returns:
        Volume Weighted Stock Price
    """
    if stock in DATA:
        stock_transactions = DATA[stock]
        recent_trades = _get_recent_trades(stock_transactions)

        cummulative_price = sum([trade.trade_price * trade.quantity for trade in recent_trades])
        cummulative_quantity = sum([trade.quantity for trade in recent_trades])
        return round(cummulative_price/cummulative_quantity, 2)
    return 0
