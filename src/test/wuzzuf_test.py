import unittest
from unittest.mock import patch
from scrape_up.wuzzuf import Jobs
import requests

class JobsTest(unittest.TestCase):
    """
    Jobs module test.
    | Methods             | Details                                                                                      |
    | ------------------- | -------------------------------------------------------------------------------------------- |
    | `filter_job()`      | Apply filters to the job search using parameters like title, country, city, min/max years of experience. |
    | `fetch_jobs()`      | Fetch job listings based on the applied filters, with an optional maximum number of pages to scrape.    |
    """

    def setUp(self):
        self.scraper = Jobs()

    def test_filter_job(self):
        self.scraper.filter_job(
            title="software engineer", country="Egypt", city="Cairo", min_years_of_experience=2, max_years_of_experience=5
        )
        expected_url = "https://wuzzuf.net/search/jobs/?q=software+engineer&filters[country][0]=Egypt&filters[city][0]=Cairo&filters[years_of_experience_min][0]=2&filters[years_of_experience_max][0]=5"
        self.assertEqual(self.scraper.url, expected_url)

    @patch('requests.get')
    def test_fetch_jobs(self, mock_get):
        # Mock the get response
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"""
        <div class="css-1gatmva e1v1l3u10">
            <h2 class="css-m604qf"><a href="/job/1">Software Engineer</a></h2>
            <div class="css-d7j1kk"><a href="#">Company Name</a></div>
            <span class="css-5wys0k">Cairo, Egypt</span>
            <div class="css-4c4ojb">3 days ago</div>
            <span class="eoyjyou0">Full Time</span>
            <span class="eoyjyou0">Senior</span>
        </div>
        """
        mock_get.return_value = mock_response

        jobs = self.scraper.fetch_jobs(max_page_number=1)
        expected_job = {
            "name": "Software Engineer",
            "url": "/job/1",
            "company": "Company Name",
            "location": "Cairo, Egypt",
            "published_time": "3 days ago",
            "properties": "Full Time ,Senior"
        }

        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0], expected_job)

if __name__ == "__main__":
    unittest.main()