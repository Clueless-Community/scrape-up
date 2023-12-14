import unittest
from scrape_up.dribbble import Dribbble


class DribbbleTest(unittest.TestCase):
    """
    Dribbble module test.\n
    | Methods              | Details                                                                                                                         |
    | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
    | `get_shots()`        | Returns the latest shots along with their title, designer and designer url like and view count and link.                        |
    | `search(topic)`      | Returns the latest shots along with their title, designer and designer url like and view count and link for the searched topic. |
    | `get_animations()`   | Returns the latest animation along with their title, designer and designer url like and view count and link.                    |
    | `get_branding()`     | Returns the latest branding along with their title, designer and designer url like and view count and link.                     |
    | `get_illustration()` | Returns the latest illustration along with their title, designer and designer url like and view count and link.                 |
    | `get_mobile()`       | Returns the latest mobile shots along with their title, designer and designer url like and view count and link.                 |
    | `get_webdesign()`    | Returns the latest web-design shots along with their title, designer and designer url like and view count and link.             |
    """
    
    def setUp(self):
        self.instance = Dribbble()

    def test_get_shots(self):
        shots = self.instance.get_shots()

        self.assertIsNotNone(shots)
        self.assertIsInstance(shots, list)

        for item in shots:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)

    def test_search(self):
        search = self.instance.search(topic="christmas")

        self.assertIsNotNone(search)
        self.assertIsInstance(search, list)

        for item in search:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)

    def test_get_animations(self):
        animations = self.instance.get_animations()

        self.assertIsNotNone(animations)
        self.assertIsInstance(animations, list)

        for item in animations:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)

    def test_get_branding(self):
        branding = self.instance.get_branding()

        self.assertIsNotNone(branding)
        self.assertIsInstance(branding, list)

        for item in branding:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)

    def test_get_illustration(self):
        illustration = self.instance.get_illustration()

        self.assertIsNotNone(illustration)
        self.assertIsInstance(illustration, list)

        for item in illustration:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)

    def test_get_mobile(self):
        mobile = self.instance.get_mobile()

        self.assertIsNotNone(mobile)
        self.assertIsInstance(mobile, list)

        for item in mobile:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)
        
    def test_get_webdesign(self):
        webdesign = self.instance.get_webdesign()

        self.assertIsNotNone(webdesign)
        self.assertIsInstance(webdesign, list)

        for item in webdesign:
            self.assertIsInstance(item, dict)

            self.assertEqual(
                list(item.keys()),
                [
                    "title",
                    "image_url",
                    "designer",
                    "designer_url",
                    "like_count",
                    "views_count",
                    "link"
                ]
            )

            for value in item.values():
                self.assertIsInstance(value, str)


if __name__ == "__main__":
    unittest.main()