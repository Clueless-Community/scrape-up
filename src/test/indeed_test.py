import unittest

from scrape_up.indeed import Indeed


class TestIndeed(unittest.TestCase):
    def test_get_jobs_with_valid_search_query(self):
        indeed = Indeed("python developer")
        jobs = indeed.get_jobs()
        self.assertTrue(len(jobs) > 0, "No jobs found for valid search query")

    def test_get_jobs_with_location_query(self):
        indeed = Indeed("java", "Mumbai")
        jobs = indeed.get_jobs()
        self.assertTrue(len(jobs) > 0, "No jobs found for valid location query")

    def test_get_jobs_with_min_jobs_limit(self):
        indeed = Indeed("python", min_jobs=5)
        jobs = indeed.get_jobs()
        self.assertTrue(
            len(jobs) >= 5, "Number of jobs retrieved is less then min jobs limit"
        )


if __name__ == "__main__":
    unittest.main()
