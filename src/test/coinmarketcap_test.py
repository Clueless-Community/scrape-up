import unittest
from scrape_up import coinmarketcap

# sys.path.insert(0, "..")


class CoinMarketCapTest(unittest.TestCase):
    """
    CoinMarketCap module test.\n
    | Method                       | Details                                                  |
    | ---------------------------- | -------------------------------------------------------- |
    | `get_top_cryptocurrencies()` | Fetches and returns data about the top cryptocurrencies. |
    """

    def test_get_top_cryptocurrencies(self):
        instance = coinmarketcap.Crypto()
        top_cryptocurrencies = instance.get_top_cryptocurrencies()

        self.assertIsInstance(top_cryptocurrencies, list)

        for item in top_cryptocurrencies:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "Name",
                    "Symbol",
                    "Link",
                    "Price",
                    "1h%",
                    "24h%",
                    "7d%",
                    "MarketCap",
                    "Volume(24h)",
                    "Circulating Supply",
                ],
            )

            for value in item.values():
                self.assertIsInstance(value, str)


if __name__ == "__main__":
    unittest.main()
