import unittest

from src.scrape_up.flexjobs import FlexJobs


class TestFlexJobs(unittest.TestCase):
    def test_get_jobs_with_valid_search_query(self):
        flexjobs = FlexJobs("python developer")
        jobs = flexjobs.get_jobs()
        self.assertTrue(len(jobs) > 0, "No jobs found for valid search query")

    def test_get_jobs_with_location_query(self):
        flexjobs = FlexJobs("python developer", "New York")
        jobs = flexjobs.get_jobs()
        self.assertTrue(len(jobs) > 0, "No jobs found for valid location query")

    def test_get_jobs_with_min_jobs_limit(self):
        flexjobs = FlexJobs("python developer", min_jobs=5)
        jobs = flexjobs.get_jobs()
        self.assertTrue(len(jobs) >= 5, "Number of jobs retrieved exceeds max jobs limit")


if __name__ == '__main__':
    unittest.main()
