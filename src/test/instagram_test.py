import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError
from scrape_up.instagram.users import Users


class InstagramWebScrapingTest(unittest.TestCase):
    def setUp(self):
        self.username = "example_username"
        self.user = Users(username=self.username)

    def test_followers_success(self):
        expected_followers = "100"
        mocked_data = (
            f'<meta name="description" content="{expected_followers}, 200 followers">'
        )
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = mocked_data
            result = self.user.followers()
            self.assertEqual(result["data"], expected_followers)
            self.assertEqual(
                result["message"], f"Followers found for user {self.username}"
            )

    def test_followers_index_error(self):
        mocked_data = '<meta name="description" content="Followers not found">'
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = mocked_data
            result = self.user.followers()
            self.assertIsNone(result["data"])
            self.assertEqual(
                result["message"],
                f"Failed to retrieve followers count for user {self.username}",
            )

    def test_followers_http_error(self):
        expected_error = "404 Not Found"
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 404
            mock_get.return_value.raise_for_status = lambda: HTTPError(expected_error)
            result = self.user.followers()
            self.assertIsNone(result["data"])
            self.assertEqual(
                result["message"],
                f"Failed to retrieve page for user {self.username}. Error: {expected_error}",
            )

    def test_followers_message(self):
        mocked_data = '<meta name="description" content="500, 500 followers">'
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = mocked_data
            result = self.user.followers()
            self.assertEqual(
                result["message"], f"Followers found for user {self.username}"
            )

    def test_followers_none(self):
        mocked_data = '<meta name="description" content="Followers not found">'
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = mocked_data
            result = self.user.followers()
            self.assertIsNone(result["data"])


if __name__ == "__main__":
    unittest.main()
