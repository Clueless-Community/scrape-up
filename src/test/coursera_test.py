import unittest
from scrape_up.coursera import Coursera

class TestCoursera(unittest.TestCase):
    def setUp(self, topic="Machine Learning"):
        self.scraper = Coursera(topic)

    def test_get_courses(self):
        result = self.scraper.get_courses()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for topic in result:
                self.assertIn("title", topic)
                self.assertIn("taught_by", topic)
                self.assertIn("skills", topic)
                self.assertIn("rating", topic)
                self.assertIn("review_count", topic)
                self.assertIn("img_url", topic)
                self.assertIn("link", topic)

                self.assertIsInstance(topic["title"], str)
                self.assertIsInstance(topic["taught_by"], str)
                self.assertIsInstance(topic["skills"], str)
                self.assertIsInstance(topic["rating"], str)
                self.assertIsInstance(topic["review_count"], str)
                self.assertIsInstance(topic["img_url"], str)
                self.assertIsInstance(topic["link"], str)

    def test_fetch_modules_with_modules(self):
        result = self.scraper.fetch_modules(course="Machine Learning with Python")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

        if result is not None:
            for key, value in result.items():
                self.assertIsInstance(value, str)
                

    def test_fetch_modules_with_specializations(self):
        result = self.scraper.fetch_modules(course="Machine Learning")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

        if result is not None:
            for key, value in result.items():
                self.assertIsInstance(value, dict)
                self.assertIn("Title", value)
                self.assertIn("Link", value)
                self.assertIsInstance(value["Title"], str)
                self.assertIsInstance(value["Link"], str)


if __name__ == "__main__":
    unittest.main()
