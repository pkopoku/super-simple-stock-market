import unittest
from sssm.models.Trade import Trade
import sssm.models.stock.Stock as stk
import sssm.models.Transactions as Transactions
import datetime

class TestTransactions(unittest.TestCase):
    def setUp(self):
        Transactions.DATA.clear()

    def test_get_recent_trades(self):
        #region test parameters
        now = datetime.datetime.utcnow()
        timestamp_30_Minutes_Ago = now - datetime.timedelta(minutes=30)
        timestamp_20_Minutes_Ago = now - datetime.timedelta(minutes=20)
        timestamp_15_Minutes_Ago = now - datetime.timedelta(minutes=15)
        timestamp_14_Minutes_Ago = now - datetime.timedelta(minutes=14)
        timestamp_5_Minutes_Ago  = now - datetime.timedelta(minutes=5)

        trade1 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp_30_Minutes_Ago)
        trade2 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp_20_Minutes_Ago)
        trade3 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp_15_Minutes_Ago)
        trade4 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp_14_Minutes_Ago)
        trade5 = Trade(quantity=10, indicator=stk.STOCK_BUY_CODE, price=2, stock=stk.STOCK_TICKER_ALE, timestamp=timestamp_5_Minutes_Ago)

        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE, trade=trade1)
        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE, trade=trade2)
        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE, trade=trade3)
        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE, trade=trade4)
        Transactions.add_transaction(stock=stk.STOCK_TICKER_ALE, trade=trade5)

        all_trades = [trade1, trade2, trade3, trade4, trade5]
        #endregion

        recent_trades = Transactions._get_recent_trades(trades=all_trades)
        self.assertTrue(2 <= len(recent_trades) <= len(all_trades))
        self.assertTrue(trade4 in recent_trades and trade5 in recent_trades)


    def test_get_recent_tradesNoTrades(self):
        self.assertEqual([], Transactions._get_recent_trades(trades=[]))
