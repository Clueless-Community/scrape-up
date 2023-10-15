import unittest
from src.scrape_up.academia import Academia

class TestAcademia(unittest.TestCase):
    def setUp(self):
        self.academia = Academia()

    def test_get_research_topics(self):
        academia = Academia()
        result = academia.get_research_topics(topic="Machine Learning")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for topic in result:
                self.assertIn("Title", topic)
                self.assertIn("Link", topic)
                self.assertIn("Number of Articles", topic)
                self.assertIn("Followers", topic)

                self.assertIsInstance(topic["Title"], str)
                self.assertIsInstance(topic["Link"], str)
                self.assertIsInstance(topic["Number of Articles"], str)
                self.assertIsInstance(topic["Followers"], str)

    def test_get_research_paper(self):
        academia = Academia()
        result = academia.get_research_papers(search="Machine Learning")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for paper in result:
                self.assertIn("Title", paper)
                self.assertIn("Summary", paper)
                self.assertIn("Link", paper)

                self.assertIsInstance(paper["Title"], str)
                if paper["Summary"] is not None:
                    self.assertIsInstance(paper["Summary"], str)
                self.assertIsInstance(paper["Link"], str)




