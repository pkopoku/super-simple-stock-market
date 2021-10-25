import unittest
import sssm.models.stock.StockFunctions as sf
import sssm.models.stock.Stock as stk
import sssm.models.stock.StockTypes as stype
from sssm.models.Exchange import ExchangeData
import models.Transactions as Transactions
from sssm.models.Trade import Trade


class TestStockFunctions(unittest.TestCase):
    def setUp(self):
        Transactions.DATA.clear()


    def test_get_exchange_data(self):
        self.assertEqual(
            ExchangeData(stock_type=stype.TYPE_COMMON, last_dividend=0,
                         fixed_dividend=None, par_value=100),
            sf._get_exchange_data(stock=stk.STOCK_TICKER_TEA))

        with self.assertRaises(KeyError):
            sf._get_exchange_data(stock="invalid_stock")
            sf._get_exchange_data(stock=None)
            sf._get_exchange_data(stock=42)


    def test_common_dividend_yield(self):
        self.assertEqual(0.4, sf.dividend_yield(stock=stk.STOCK_TICKER_POP, price=20))
        self.assertEqual(0, sf.dividend_yield(stock=stk.STOCK_TICKER_POP, price=0))
        self.assertEqual(0, sf.dividend_yield(stock=stk.STOCK_TICKER_POP, price=-10))

        with self.assertRaises(TypeError):
            sf.dividend_yield(stock=stk.STOCK_TICKER_POP, price="s")
            sf.dividend_yield(stock=stk.STOCK_TICKER_POP, price=None)


    def test_preferred_dividend_yield(self):
        self.assertEqual(0.1, sf.dividend_yield(stock=stk.STOCK_TICKER_GIN, price=20))
        self.assertEqual(0, sf.dividend_yield(stock=stk.STOCK_TICKER_GIN, price=0))
        self.assertEqual(0, sf.dividend_yield(stock=stk.STOCK_TICKER_GIN, price=-10))

        with self.assertRaises(TypeError):
            sf.dividend_yield(stock=stk.STOCK_TICKER_GIN, price="s")
            sf.dividend_yield(stock=stk.STOCK_TICKER_GIN, price=None)


    def test_pe_ratio(self):
        self.assertEqual(1, sf.pe_ratio(stock=stk.STOCK_TICKER_ALE, price=23))
        self.assertEqual(0, sf.pe_ratio(stock=stk.STOCK_TICKER_ALE, price=0))

        # dividend of 0
        self.assertEqual(0, sf.pe_ratio(stock=stk.STOCK_TICKER_TEA, price=0))


    def test_volume_weighted_stock_price(self):
        # no existing transactions
        self.assertEqual(0, sf.volume_weighted_stock_price(stock=stk.STOCK_TICKER_ALE))

        # single transaction
        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE,
                                     trade=Trade(quantity=10, indicator=stk.STOCK_BUY_CODE,
                                                 price=50, stock=stk.STOCK_TICKER_ALE))
        self.assertEqual(50, sf.volume_weighted_stock_price(stock=stk.STOCK_TICKER_ALE))

        # multiple transactions
        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE,
                                     trade=Trade(quantity=5, indicator=stk.STOCK_SELL_CODE,
                                                 price=60, stock=stk.STOCK_TICKER_ALE))
        self.assertEqual(53.33, sf.volume_weighted_stock_price(stock=stk.STOCK_TICKER_ALE))


    def test_geometric_mean(self):
        # no existing transactions
        self.assertEqual(0, sf.all_share_index())

        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE,
                                     trade=Trade(quantity=10, indicator=stk.STOCK_BUY_CODE,
                                                 price=2, stock=stk.STOCK_TICKER_ALE))
        Transactions.add_transaction(stock=stk.STOCK_TICKER_GIN,
                                     trade=Trade(quantity=15, indicator=stk.STOCK_SELL_CODE,
                                                 price=2, stock=stk.STOCK_TICKER_GIN))

        # added transactions
        self.assertEqual(2, Transactions.get_all_share_index())

if __name__ == "__main__":
    unittest.main()