import unittest
from scrape_up import codechef


class CodeChefTest(unittest.TestCase):
    """
    CodeChef module test.\n
    | Methods         | Details                                                          |
    | --------------- | ---------------------------------------------------------------- |
    | `get_profile()` | Returns name, username, profile_image_link, rating, details etc. |
    """

    def test_get_profile(self):
        instance = codechef.User(id="heltion")
        method_response = instance.get_profile()

        self.assertEqual(
            list(method_response.keys()),
            ["name", "username", "profile_image_link", "rating", "details"],
            "Codechef:get_profile - keys mismatch",
        )


if __name__ == "__main__":
    unittest.main()  
