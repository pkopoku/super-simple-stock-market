import unittest
from unittest.mock import patch
from models.screen.Screen import DividendYieldScreen, PeRatioScreen
from models.screen.Screen import RecordTradeScreen
from models.screen.Screen import VolumeWeightedStockPrice, AllShareIndexScreen
from models.screen.Screen import ExitScreen, MainScreen, InvalidInputScreen
from models.screen import Banners

class TestScreens(unittest.TestCase):

    # mock user choice
    @patch('models.screen.Screen.MainScreen.run', return_value=1)
    def test_main_menu_choice(self, input):
        screen = MainScreen(Banners.MAIN_BANNER)
        choice = screen.run()
        self.assertEqual(screen.run(), 1)
