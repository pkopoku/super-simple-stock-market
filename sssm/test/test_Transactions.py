import unittest
from sssm.models.Trade import Trade
import sssm.models.stock.Stock as stk
import sssm.models.Transactions as Transactions
import datetime

class TestTransactions(unittest.TestCase):
    def setUp(self):
        Transactions.data.clear()

    def test_getRecentTrades(self):
        #region test parameters
        now = datetime.datetime.utcnow()
        timestamp30MinutesAgo = now - datetime.timedelta(minutes=30)
        timestamp20MinutesAgo = now - datetime.timedelta(minutes=20)
        timestamp15MinutesAgo = now - datetime.timedelta(minutes=15)
        timestamp14MinutesAgo = now - datetime.timedelta(minutes=14)
        timestamp5MinutesAgo  = now - datetime.timedelta(minutes=5)

        trade1 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp30MinutesAgo)
        trade2 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp20MinutesAgo)
        trade3 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp15MinutesAgo)
        trade4 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp14MinutesAgo)
        trade5 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp5MinutesAgo)

        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=trade1)
        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=trade2)
        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=trade3)
        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=trade4)
        Transactions.addTransaction(stock=stk.STOCK_TICKER_ALE, trade=trade5)

        allTrades = [trade1, trade2, trade3, trade4, trade5]
        #endregion

        #region expected result
        result = [trade4, trade5]
        #endregion

        self.assertEqual(result, Transactions._getRecentTrades(trades=allTrades))
    
    def test_getRecentTradesNoTrades(self):
        self.assertEqual([], Transactions._getRecentTrades(trades=[]))