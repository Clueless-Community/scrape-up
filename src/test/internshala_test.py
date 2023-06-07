import unittest
from scrape_up.internshala.internships import Internships

class InternshipsTest(unittest.TestCase):
    def scrape_internships(self):
        scraper = Internships()  
        internships = scraper.scrape_internships()
        self.assertTrue(isinstance(internships, list))
        

if __name__ == '__main__':
    unittest.main()
