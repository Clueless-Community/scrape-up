import unittest
from scrape_up import flyrobu

class FlyrobyTest(unittest.TestCase):
    def test_get_html_content(self):
        instance = flyrobu.Flyrobu()
        self.assertIsNotNone(instance.search('arduino'))

