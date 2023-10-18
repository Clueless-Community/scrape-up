import unittest
from scrape_up import github_education


class GitHubEducationTest(unittest.TestCase):
    """
    CodeChef module test.\n
    | Methods        | Details                                                                                                             |
    | -------------- | ------------------------------------------------------------------------------------------------------------------- |
    | `get_events()` | Returns the latest events along with their title, image_url, description, date, location, language, tags, and link. |
    """

    def test_get_events(self):
        instance = github_education.Events()
        method_response = instance.get_events()

        self.assertIsInstance(
            method_response, list, "GitHubEducation:get_events - return type mismatch"
        )
        self.assertTrue(all(isinstance(event, dict) for event in method_response))

        for event in method_response:
            self.assertEqual(
                list(event.keys()),
                [
                    "title",
                    "image_url",
                    "description",
                    "date",
                    "location",
                    "language",
                    "tags",
                    "link",
                ],
                "GitHubEducation:get_events - keys mismatch",
            )


if __name__ == "__main__":
    unittest.main()
