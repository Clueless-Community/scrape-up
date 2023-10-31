import unittest
from scrape_up.covidinfo import covidinfo


class CovidInfoTest(unittest.TestCase):
    def setUp(self):
        self.instance = covidinfo.CovidInfo()

    """
    CovidInfo module test.\n
    | Methods | Details |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.covid_data()` | Returns the list of all the covid data scraped from the website |
    | `.total_cases()` | Returns the count of total covid cases all over the world |
    | `.total_deaths()` | Returns the count of deaths covid cases all over the world |
    | `.total_recovered()` | Returns the count of recovered covid cases all over the world |
    | `.latest_news()` | Return the lastest news of the day |
    """

    def test_covid_data(self):
        covid_data_response = self.instance.covid_data()
        self.assertIsInstance(covid_data_response, list)
        if covid_data_response is not None:
            for data in covid_data_response:
                self.assertIsInstance(data, dict)
                self.assertIn("Country", data)
                self.assertIn("Number of Cases", data)
                self.assertIn("Deaths", data)
                self.assertIn("Continent", data)
                self.assertIsInstance(data["Country"], str)
                self.assertIsInstance(data["Number of Cases"], int)
                self.assertIsInstance(data["Deaths"], int)
                self.assertIsInstance(data["Continent"], str)

    def test_total_cases(self):
        total_cases_response = self.instance.total_cases()
        self.assertIsInstance(total_cases_response, str)

    def test_total_deaths(self):
        total_deaths_response = self.instance.total_deaths()
        self.assertIsInstance(total_deaths_response, str)

    def test_total_recovered(self):
        test_total_response = self.instance.total_recovered()
        self.assertIsInstance(test_total_response, dict)

    def test_latest_news(self):
        latest_news_response = self.instance.latest_news()
        self.assertIsInstance(latest_news_response, (list, type(None)))
        if latest_news_response is not None:
            for news in latest_news_response:
                self.assertIsInstance(news, dict)
                self.assertIn("news", news)
                self.assertIn("source", news)
                self.assertIsInstance(news["news"], str)
                self.assertIsInstance(news["source"], str)


if __name__ == "__main__":
    unittest.main()
