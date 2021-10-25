import unittest
import sssm.models.stock.StockFunctions as sf
import sssm.models.stock.Stock as stk
import sssm.models.stock.StockTypes as stype
from sssm.models.Exchange import ExchangeData
import models.Transactions as Transactions
from sssm.models.Trade import Trade

class TestStockFunctions(unittest.TestCase):
    def setUp(self):
        Transactions.data.clear()

    def test_getExchangeData(self):
        self.assertEqual(ExchangeData(stockType=stype.TYPE_COMMON, lastDividend=0, fixedDividend=None, parValue=100),
        sf._getExchangeData(stock=stk.STOCK_TICKER_TEA))

        with self.assertRaises(KeyError):
            sf._getExchangeData(stock="invalid_stock")
            sf._getExchangeData(stock=None)
            sf._getExchangeData(stock=42)

    def test_commonDividendYield(self):
        self.assertEqual(0.4, sf.dividendYield(stock=stk.STOCK_TICKER_POP, price=20))
        self.assertEqual(0, sf.dividendYield(stock=stk.STOCK_TICKER_POP, price=0))
        self.assertEqual(0, sf.dividendYield(stock=stk.STOCK_TICKER_POP, price=-10))

        with self.assertRaises(TypeError):
            sf.dividendYield(stock=stk.STOCK_TICKER_POP, price="s")
            sf.dividendYield(stock=stk.STOCK_TICKER_POP, price=None)
    
    def test_preferredDividendYield(self):
        self.assertEqual(0.1, sf.dividendYield(stock=stk.STOCK_TICKER_GIN, price=20))
        self.assertEqual(0, sf.dividendYield(stock=stk.STOCK_TICKER_GIN, price=0))
        self.assertEqual(0, sf.dividendYield(stock=stk.STOCK_TICKER_GIN, price=-10))

        with self.assertRaises(TypeError):
            sf.dividendYield(stock=stk.STOCK_TICKER_GIN, price="s")
            sf.dividendYield(stock=stk.STOCK_TICKER_GIN, price=None)

    def test_peRatio(self):
        self.assertEqual(1, sf.peRatio(stock=stk.STOCK_TICKER_ALE, price=23))
        self.assertEqual(0, sf.peRatio(stock=stk.STOCK_TICKER_ALE, price=0))

        # dividend of 0
        self.assertEqual(0, sf.peRatio(stock=stk.STOCK_TICKER_TEA, price=0))
    
    def test_volumeWeightedStockPrice(self):
        # no existing transactions
        self.assertEqual(0, sf.volumeWeightedStockPrice(stock=stk.STOCK_TICKER_ALE))

        # single transaction
        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=50, stock=stk.STOCK_TICKER_ALE))
        self.assertEqual(50, sf.volumeWeightedStockPrice(stock=stk.STOCK_TICKER_ALE))

        # multiple transactions
        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=Trade(quantity=5, indicator=stk.STOCK_SELL_CODE, price=60, stock=stk.STOCK_TICKER_ALE))
        self.assertEqual(53.33, sf.volumeWeightedStockPrice(stock=stk.STOCK_TICKER_ALE))

    def test_geometricMean(self):
        # no existing transactions
        self.assertEqual(0, sf.allShareIndex())

        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE))
        Transactions.addTransaction(stock=stk.STOCK_TICKER_GIN, trade=Trade(quantity=15, indicator=stk.STOCK_SELL_CODE, price=2, stock=stk.STOCK_TICKER_GIN))

        # added transactions
        self.assertEqual(2, Transactions.getAllShareIndex())

if __name__ == "__main__":
    unittest.main()