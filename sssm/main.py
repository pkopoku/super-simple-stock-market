from models.screen.Screen import DividendYieldScreen, PeRatioScreen, RecordTradeScreen, VolumeWeightedStockPrice, AllShareIndexScreen, ExitScreen, MainScreen, InvalidInputScreen
from models.screen import Banners 


if __name__ == "__main__":

    while(True):

        screen = MainScreen(Banners.MAIN_BANNER)
        choice = screen.run()

        if choice == '1':
            screen = DividendYieldScreen(Banners.DIVIDEND_YIELD_BANNER)
            screen.run()
        elif choice == '2':
            screen = PeRatioScreen(Banners.PE_RATIO_BANNER)
            screen.run()
        elif choice == '3':
            screen = RecordTradeScreen(Banners.RECORD_TRADE_BANNER)
            screen.run()
        elif choice == '4':
            screen = VolumeWeightedStockPrice(Banners.VOL_WEIGHT_BANNER)
            screen.run()
        elif choice == '5':
            screen = AllShareIndexScreen(Banners.ALL_SHARE_BANNER)
            screen.run()
        elif choice.upper() == 'X':
            screen = ExitScreen(Banners.EXIT_BANNER)
            screen.run()
            break
        else:
            screen = InvalidInputScreen(Banners.INVALID_BANNER)
            screen.run()

    exit(0)