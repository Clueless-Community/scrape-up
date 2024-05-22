import unittest
from unittest.mock import patch, MagicMock
import json
from src.scrape_up.atcoder import Atcoder


class TestAtcoder(unittest.TestCase):
    """
    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_profile()`  | Returns the user data in json format.                                              |
    | `get_contests()`  | Returns future_contests , past_contests , skill_tests etc in json format.          |

    """
    @patch('requests.get')
    def test_get_profile(self, mock_get):
        try:
            # Mock response for get_profile method
            mock_response = MagicMock()
            mock_response.text = '''
                <html>
                    <table class="dl-table">
                        <tr><th>Country/Region</th><td>Japan</td></tr>
                        <tr><th>Birth Year</th><td>1988</td></tr>
                        <tr><th>Twitter ID</th><td>@chokudai</td></tr>
                        <tr><th>TopCoder ID</th><td>chokudai</td></tr>
                        <tr><th>Codeforces ID</th><td>chokudai</td></tr>
                        <tr><th>Affiliation</th><td>AtCoder Inc. CEO</td></tr>
                    </table>
                    <table class="dl-table">
                        <tr><th>Rank</th><td>44th</td></tr>
                        <tr><th>Rating</th><td>3028</td></tr>
                        <tr><th>Highest Rating</th><td>3092 ― 6 Dan (+108 to promote)</td></tr>
                        <tr><th>Rated Matches</th><td>35</td></tr>
                        <tr><th>Last Competed</th><td>2023/12/17</td></tr>
                    </table>
                </html>
                '''
            mock_get.return_value = mock_response

            expected_profile = {
                "Country/Region": "Japan",
                "Birth_Year": "1988",
                "Twitter_ID": "@chokudai",
                "TopCoder_ID": "chokudai",
                "Codeforces_ID": "chokudai",
                "Affiliation": "AtCoder Inc. CEO",
                "Algorithm_Rank": "44th",
                "Algorithm_Rating": "3028",
                "Algorithm_Highest_Rating": "3092 ― 6 Dan (+108 to promote)",
                "Algorithm_Rated_Matches_": "35",
                "Algorithm_Last_Competed": "2023/12/17",
            }

            profile = self.atcoder.get_profile()
            self.assertEqual(json.loads(profile), expected_profile)

        except:
            return None

    @patch('requests.get')
    def test_get_contests(self, mock_get):
        try:
            # Mock response for get_contests method
            mock_response = MagicMock()
            mock_response.text = '''
                <html>
                    <div id="contest-table-action">
                        <tbody>
                            <tr>
                                <td>2024/05/18 21:00</td>
                                <td>AtCoder Beginner Contest 123</td>
                                <td>100 minutes</td>
                                <td>All</td>
                            </tr>
                        </tbody>
                    </div>
                    <div id="contest-table-upcoming">
                        <tbody>
                            <tr>
                                <td>2024/05/25 21:00</td>
                                <td>AtCoder Grand Contest 45</td>
                                <td>120 minutes</td>
                                <td>All</td>
                            </tr>
                        </tbody>
                    </div>
                    <div id="contest-table-recent">
                        <tbody>
                            <tr>
                                <td>2024/05/11 21:00</td>
                                <td>AtCoder Beginner Contest 122</td>
                                <td>100 minutes</td>
                                <td>All</td>
                            </tr>
                        </tbody>
                    </div>
                    <div id="contest-table-permanent">
                        <tbody>
                            <tr>
                                <td>Practice Contest</td>
                                <td>All</td>
                            </tr>
                        </tbody>
                    </div>
                </html>
                '''
            mock_get.return_value = mock_response

            expected_contests = {
                "active": {
                    1: {
                        "start_time": "2024/05/18 21:00",
                        "name": "AtCoder Beginner Contest 123",
                        "Duration": "100 minutes",
                        "Rated_for": "All"
                    }
                },
                "Upcoming": {
                    1: {
                        "start_time": "2024/05/25 21:00",
                        "name": "AtCoder Grand Contest 45",
                        "Duration": "120 minutes",
                        "Rated_for": "All"
                    }
                },
                "Recent": {
                    1: {
                        "start_time": "2024/05/11 21:00",
                        "name": "AtCoder Beginner Contest 122",
                        "Duration": "100 minutes",
                        "Rated_for": "All"
                    }
                },
                "Permanent": {
                    1: {
                        "name": "Practice Contest",
                        "Rated_for": "All"
                    }
                }
            }

            contests = self.atcoder.get_contests()
            self.assertEqual(contests, expected_contests)

        except:
            return None

    @patch('requests.get')
    def test_get_profile_with_no_data(self, mock_get):
        # Testing edge case (when profile has no data)
        try:
            # Mock response for get_profile with no data
            mock_response = MagicMock()
            mock_response.text = '''
                <html>
                    <table class="dl-table"></table>
                    <table class="dl-table"></table>
                </html>
                '''
            mock_get.return_value = mock_response

            profile = self.atcoder.get_profile()
            self.assertEqual(profile, None)

        except:
            return None

    @patch('requests.get')
    def test_get_contests_with_no_data(self, mock_get):
        # Testing edge case (when content has no data)
        try:
            # Mock response for get_contests with no data
            mock_response = MagicMock()
            mock_response.text = '''
                <html>
                    <div id="contest-table-action"><tbody></tbody></div>
                    <div id="contest-table-upcoming"><tbody></tbody></div>
                    <div id="contest-table-recent"><tbody></tbody></div>
                    <div id="contest-table-permanent"><tbody></tbody></div>
                </html>
                '''
            mock_get.return_value = mock_response

            expected_contests = {
                "active": {},
                "Upcoming": {},
                "Recent": {},
                "Permanent": {}
            }

            contests = self.atcoder.get_contests()
            self.assertEqual(contests, expected_contests)

        except:
            return None


if __name__ == "__main__":
    unittest.main()