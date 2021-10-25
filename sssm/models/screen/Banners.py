"""A collection of string prompts"""

#region
MAIN_BANNER = """
    Welcome to the Global Beverage Corporation Exchange (GBCE)
"""
MAIN_MENU = """
    1 - Calculate Dividend Yield
    2 - Calclulate P/E Ratio
    3 - Record Trade
    4 - Calculate Volume Weighted Stock Price
    5 - Calculate GBCE All Share Index
    X - Exit
"""
#endregion

#region
INVALID_BANNER = """
    Please enter a valid Menu Item
"""
INVALID_NUMBER = """
    Please enter a valid number
"""
#endregion

# region Dividend Yield Strings
DIVIDEND_YIELD_BANNER = """
    Calculate Dividend Yield
"""
DIVIDEND_YIELD_PROMPT_RESULT = "Dividend Yield"
#endregion

#region PE Ratio Strings
PE_RATIO_BANNER = """
    Calculate P/E Ratio
"""
PE_RATIO_PROMPT_RESULT = "P/E Ratio"
#endregion

#region Record Trade Strings
RECORD_TRADE_BANNER = """
    Record Trade
"""
RECORD_TRADE_RESULT_COMPLETE = """
    Transaction Complete
"""
RECORD_TRADE_PROMPT_QUANTITY = "number of shares:"
RECORD_TRADE_PROMPT_INDICATOR = "indicator (1 - Buy, 2 - Sell):"
RECORD_TRADE_PROMPT_PRICE = "traded price:"
#endregion

#region Volume Weighted Stock Strings
VOL_WEIGHT_BANNER = """
    Calculate Volume Weighted Stock
"""
VOL_WEIGHT_RESULT = "Volume Weighted Stock Price"
#endregion

#region All Share Index Strings
ALL_SHARE_BANNER = """
    Calculate GBCE All Share Index
"""
ALL_SHARE_RESULT = "GBCE All Share Index"
#endregion

#region Exit Strings
EXIT_BANNER = "Exiting The Stock Market. See you again!"
#endregion

#region generic prompt strings
PROMPT_STOCK_TICKER = """
    Please Select a Ticker.
    1 - TEA
    2 - POP
    3 - ALE
    4 - GIN
    5 - JOE
"""
PROMPT_PRICE = "price:"
#endregion
