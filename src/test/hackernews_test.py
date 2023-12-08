import unittest
from scrape_up.hackernews import Articles


class HackerNewsTest(unittest.TestCase):
    '''
    HackerNews module test.\n
    | Methods             | Details                                                                                                                   |
    | ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
    | `articles_list()`   | Returns the latest articles along with their score, author, author URL, time, comment count, and link.                    |
    | `new_articles()`    | Returns the latest new articles along with their score, author, author URL, time, comment count, and link.                |
    | `past_articles()`   | Returns the past articles along with their score, author, author URL, time, comment count, and link.                      |
    | `ask_articles()`    | Returns the asked articles along with their score, author, author URL, time, comment count, and link.                     |
    | `show_articles()`   | Returns the show articles along with their score, author, author URL, time, comment count, and link.                      |
    | `jobs()`            | Returns the jobs along with their time and link.                                                                          |
    '''

    def setUp(self):
        self.instance = Articles()


    def test_articles_list(self):
        articles_list = self.instance.articles_list()

        self.assertIsNotNone(articles_list)
        self.assertIsInstance(articles_list, list)

        for item in articles_list:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                ['title', 'score', 'author', 'author_url', 'time', 'comment_count', 'link']
            )

            for value in item.values():
                self.assertIsInstance(value, str)


    def test_new_articles(self):
        new_articles = self.instance.new_articles()

        self.assertIsNotNone(new_articles)
        self.assertIsInstance(new_articles, list)

        for item in new_articles:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                ['title', 'score', 'author', 'author_url', 'time', 'comment_count', 'link']
            )

            for value in item.values():
                self.assertIsInstance(value, str)


    def test_past_articles(self):
        past_articles = self.instance.past_articles()

        self.assertIsNotNone(past_articles)
        self.assertIsInstance(past_articles, list)
        
        for item in past_articles:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                ['title', 'score', 'author', 'author_url', 'time', 'comment_count', 'link']
            )

            for value in item.values():
                self.assertIsInstance(value, str)


    def test_ask_articles(self):
        ask_articles = self.instance.ask_articles()

        self.assertIsNotNone(ask_articles)
        self.assertIsInstance(ask_articles, list)

        for item in ask_articles:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                ['title', 'score', 'author', 'author_url', 'time', 'comment_count', 'link']
            )

            for value in item.values():
                self.assertIsInstance(value, str)


    def test_show_articles(self):
        show_articles = self.instance.show_articles()

        self.assertIsNotNone(show_articles)
        self.assertIsInstance(show_articles, list)

        for item in show_articles:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                ['title', 'score', 'author', 'author_url', 'time', 'comment_count', 'link']
            )

            for value in item.values():
                self.assertIsInstance(value, str)


    def test_jobs(self):
        jobs = self.instance.jobs()

        self.assertIsNotNone(jobs)
        self.assertIsInstance(jobs, list)

        for item in jobs:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                ['title', 'time', 'link']
            )

            for value in item.values():
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
