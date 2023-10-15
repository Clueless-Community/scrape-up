import unittest
from scrape_up.healthgrades import HealthGrades # Import your original module

class TestHealthGrades(unittest.TestCase):

    def test_get_best_hospitals(self):

        # Define the expected result
        expected_result = [{'Name': 'Banner Estrella Medical Center', 'Location': '9201 W Thomas RdPhoenix, AZ 85037', 'Link': 'https://www.healthgrades.com/hospital-directory/arizona-az/banner-estrella-medical-center-hgstd12b8315030115', 'Awards': ["America's 250 Best Hospitals Award™ For the years (2023, 2022, 2021)", "America's 100 Best Pulmonary Care™ For the years (2023, 2022, 2021)"]}, {'Name': 'Banner Thunderbird Medical Center', 'Location': '5555 W Thunderbird RdGlendale, AZ 85306', 'Link': 'https://www.healthgrades.com/hospital-directory/arizona-az/banner-thunderbird-medical-center-hgst750b7b36030089', 'Awards': ["America's 100 Best Hospitals Award™ For the years (2023)", "America's 100 Best Critical Care™ For the years (2023, 2022, 2021)"]}, {'Name': 'Mayo Clinic Hospital', 'Location': '5777 E Mayo BlvdPhoenix, AZ 85054', 'Link': 'https://www.healthgrades.com/hospital-directory/arizona-az/mayo-clinic-hospital-hgst460b7b36030103', 'Awards': ["America's 50 Best Hospitals Award™ For the years (2023, 2022, 2021)", 'Outstanding Patient Experience Award™ For the years (2023, 2022, 2021)']}]

        # Create an instance of the HealthGrades class
        healthgrades = HealthGrades()

        # Call the method under test
        result = healthgrades.get_best_hospitals(state="bihar")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()