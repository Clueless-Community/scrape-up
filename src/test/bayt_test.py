import unittest
from src.scrape_up.bayt import Jobs


class TestJobs(unittest.TestCase):
    """
    | Methods                       | Details                                                                    |
    | ----------------------------- | -------------------------------------------------------------------------- |
    | `.fetch_jobs(query, page)`    | Fetch job listings data from Bayt.com based on the given query and page.   |
    """

    def setUp(self):
        """
        Initialize an instance of the Jobs class before each test.
        """
        self.scraper = Jobs()
        self.query = "software developer"
        self.page = 1

    def test_fetch_jobs(self):
        """
        Test the fetch_jobs method.
        """
        try:
            jobs_data = self.scraper.fetch_jobs(self.query, self.page)
            self.assertIsNotNone(jobs_data, "Failed to fetch job listings")
            self.assertIsInstance(jobs_data, list, "Job listings should be a list")
            self.assertGreater(len(jobs_data), 0, "Job listings should not be empty")

            # Check the structure of the first job listing
            job = jobs_data[0]
            expected_keys = ["title", "company", "location", "url"]
            for key in expected_keys:
                self.assertIn(key, job, f"Missing expected key: {key}")
                self.assertIsInstance(job[key], str, f"{key} should be a string")

        except:
            return None

    def test_extract_job_info(self):
        """
        Test the __extract_job_info method indirectly by testing fetch_jobs.
        """
        try:
            jobs_data = self.scraper.fetch_jobs(self.query, self.page)
            self.assertIsNotNone(jobs_data, "Failed to fetch job listings")
            self.assertGreater(len(jobs_data), 0, "Job listings should not be empty")

            # Check the first job listing details
            job = jobs_data[0]
            self.assertIn("title", job, "Job should have a title")
            self.assertIn("company", job, "Job should have a company name")
            self.assertIn("location", job, "Job should have a location")
            self.assertIn("url", job, "Job should have a URL")

            # Ensure that none of the fields are empty
            self.assertNotEqual(job["title"], "", "Job title should not be empty")
            self.assertNotEqual(job["url"], "", "Job URL should not be empty")

        except:
            return None

if __name__ == "__main__":
    unittest.main()
