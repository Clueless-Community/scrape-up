import unittest
from scrape_up.espncricinfo import Espncricinfo


class ESPNTest(unittest.TestCase):
    def test_connection(self):
        instance = Espncricinfo()
        self.assertTrue(
            instance,
            "ESPN:__init__ - connection failed",
        )

    def test_get_news(self):
        instance = Espncricinfo()
        method_response = instance.get_news()

        self.assertIsInstance(
            method_response,
            list,
            "ESPN:get_news - invalid response",
        )

    def test_get_livescores(self):
        instance = Espncricinfo()
        method_response = instance.get_livescores()

        self.assertIsInstance(
            method_response,
            list,
            "ESPN:get_livescores - invalid response",
        )


if __name__ == "__main__":
    unittest.main()
