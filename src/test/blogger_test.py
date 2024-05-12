import unittest
from scrape_up import blogger  

class BloggerTest(unittest.TestCase):

    """
    Test cases for the Blogger module.

    | Methods                        | Details                                                                              |
    | ------------------------------ | ------------------------------------------------------------------------------------ |
    | `.test_get_articles()`        | Returns Item_Name, Link, Author for articles related to a given topic.               |
    | `.test_get_articles_invalid_topic()` | Tests retrieval of articles for an invalid topic. 
                                                                |
    """

    def setUp(self):
        self.blogger = blogger()

    def test_get_articles(self):
        topic = "python programming"
        articles = self.blogger.get_articles(topic)
        self.assertIsNotNone(articles)
        for article in articles:
            self.assertIn('title', article)
            self.assertIn('link', article)
            self.assertIn('author', article)

    def test_get_articles_invalid_topic(self):
        topic = "invalid topic"
        articles = self.blogger.get_articles(topic)
        self.assertIsNone(articles)
  
if __name__ == '__main__':
    unittest.main()