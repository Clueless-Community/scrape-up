import unittest
from scrape_up import flyrobu


class FlyrobuTest(unittest.TestCase):
    """
    Flyrobu module test.\n
    | Methods             | Details                                                                                                         |
    | ------------------- | --------------------------------------------------------------------------------------------------------------- |
    | `.search(keyword)`  | Returns the json data of all the details related to search with informing about the total amount of items found |
    | `.get_product_details(product_name)` | Returns the json data of the product details based on the given `product_name`                 |
    """

    def test_search(self):
        """
        Test the search method of the Flyrobu class.

        This test case ensures that the method returns valid search results for a given query.

        1. It creates an instance of the Flyrobu class.
        2. Calls the search method with the query 'arduino'.
        3. Asserts that the search results are not None.
        4. Asserts that the search results are a list.
        5. Asserts that the search results contain at least one item (length > 0).
        6. Asserts that the first item in the search results is a dictionary.

        If all these assertions pass, it confirms that the search method is functioning as expected.
        """

        instance = flyrobu.Flyrobu()
        search_results = instance.search('arduino')
        self.assertIsNotNone(search_results, 'FLyrobu:search - search results are None')
        self.assertIsInstance(search_results, list, 'Flyrobu:search - search results are not a list')
        self.assertGreater(len(search_results), 0, 'Flyrobu:search - search results are empty')
        self.assertIsInstance(search_results[0], dict, 'Flyrobu:search - search results are not a list of dictionaries')
        first_search_result = search_results[0]
        expected_keys = [
            "title",
            "price",
            "brand_name",
            "image",
            "description",
            "rating",
            "model_id",
            "link"
        ]

        # Check if all expected keys exist in the product_data dictionary
        for key in expected_keys:
            self.assertIn(key, first_search_result, f"Key '{key}' is missing in the first search result")

    def test_search_url_is_incorrect(self):
        """
        Test for incorrect search URL handling in the Flyrobu class.

        This test case verifies the behavior of the Flyrobu class when an incorrect base URL is provided.

        1. It creates an instance of the Flyrobu class.
        2. Sets the base URL to an incorrect, malformed URL ('malformed:/www.search-url.com').
        3. Calls the search method with the query 'arduino'.
        4. Asserts that the search results are None, indicating a failed request due to the incorrect URL.

        This test ensures that the Flyrobu class handles incorrect URL scenarios and returns the expected None result.

        """
        instance = flyrobu.Flyrobu()
        instance.base_url = 'malformed:/www.search-url.com'
        search_results = instance.search('arduino')
        self.assertIsNone(search_results, 'Flyrobu:search - search results are not None')
    
    def test_get_product_details(self):
        """
        Test the 'get_product_details' method of the Flyrobu class.

        This test case checks the behavior of the 'get_product_details' method in the Flyrobu class.

        1. It creates an instance of the Flyrobu class.
        2. Specifies a 'product_name' for a product to be retrieved ('chain_for_6.35mm_pitch_sprocket_ebike_scooter').
        3. Calls the 'get_product_details' method with the specified product name.
        4. Asserts that 'product_details' is not None.
        5. Asserts that 'product_details' is of type 'dict'.
        6. Defines a list of expected keys that should be present in the 'product_details' dictionary.
        7. Iterates through the expected keys and checks if each key exists in the 'product_details' dictionary.
        If any key is missing, an error message is displayed.

        This test ensures that the 'get_product_details' method retrieves product details, and that the resulting
        'product_details' dictionary contains the expected keys, making it suitable for further processing.

        """
        instance = flyrobu.Flyrobu()
        product_name = 'chain_for_6.35mm_pitch_sprocket_ebike_scooter'
        product_details = instance.get_product_details(product_name)
        self.assertIsNotNone(product_details, 'Flyrobu:get_product_details - product details are None')
        self.assertIsInstance(product_details, dict, 'Flyrobu:get_product_details - product details are not a dictionary')
        expected_keys = [
            "Description",
            "Features",
            "Technical Details",
            "Current Price",
            "Original Price",
            "Image",
        ]

        # Check if all expected keys exist in the product_data dictionary
        for key in expected_keys:
            self.assertIn(key, product_details, f"Key '{key}' is missing in the product details")
    
    def test_product_details_url_is_incorrect(self):
        """
        Test for incorrect product details URL handling in the Flyrobu class.

        This test case verifies the behavior of the Flyrobu class when an incorrect base URL is provided for fetching
        product details.

        1. It creates an instance of the Flyrobu class.
        2. Sets the base URL to an incorrect, malformed URL ('malformed:/www.product-details-url.com').
        3. Specifies a 'product_name' for a product to be retrieved ('chain_for_6.35mm_pitch_sprocket_ebike_scooter').
        4. Calls the 'get_product_details' method with the specified product name.
        5. Asserts that 'product_details' is None, indicating a failed request due to the incorrect URL.

        This test ensures that the Flyrobu class correctly handles scenarios where the product details URL is malformed
        and returns the expected None result.

        """
        instance = flyrobu.Flyrobu()
        instance.base_url = 'malformed:/www.product-details-url.com'
        product_name = 'chain_for_6.35mm_pitch_sprocket_ebike_scooter'
        product_details = instance.get_product_details(product_name)
        self.assertIsNone(product_details, 'Flyrobu:get_product_details - product details are not None')

