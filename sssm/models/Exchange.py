"""module to encapsulate exchange data"""
from models.stock.StockTypes import TYPE_COMMON, TYPE_PREFERRED


class ExchangeData:
    """
    Class of exchange data and functions

    Attributes:
        type (str): Stock Type
        last_dividend (float): Last Dividend
        fixed_dividend (float): Fixed Dividend
        par_value (float): Par Value
    """
    def __init__(self, stock_type, last_dividend, fixed_dividend, par_value):
        self.type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value

    def get_last_dividend(self):
        """Get Last Dividend

        Args:
            None

        Returns:
            dividend
        """
        return self.last_dividend

    def get_par_value(self):
        """Get Par Value

        Args:
            None

        Returns:
            par value
        """
        return self.par_value

    def get_fixed_dividend(self):
        """Get Fixed Dividend

        Args:
            None

        Returns:
            fixed dividend
        """
        return self.fixed_dividend

    def __eq__(self, other):
        return self.type == other.type \
            and self.last_dividend == other.last_dividend \
            and self.fixed_dividend == other.fixed_dividend \
            and self.par_value == other.par_value

    def __repr__(self):
        return ','.join([self.type, str(self.last_dividend),
                         str(self.fixed_dividend), str(self.par_value)])


DATA = {
    "TEA": ExchangeData(
        stock_type=TYPE_COMMON, last_dividend=0,
        fixed_dividend=None, par_value=100),
    "POP": ExchangeData(
        stock_type=TYPE_COMMON, last_dividend=8,
        fixed_dividend=None, par_value=100),
    "ALE": ExchangeData(
        stock_type=TYPE_COMMON, last_dividend=23,
        fixed_dividend=None, par_value=100),
    "GIN": ExchangeData(
        stock_type=TYPE_PREFERRED, last_dividend=8,
        fixed_dividend=0.02, par_value=100),
    "JOE": ExchangeData(
        stock_type=TYPE_COMMON, last_dividend=13,
        fixed_dividend=None, par_value=100)
}
