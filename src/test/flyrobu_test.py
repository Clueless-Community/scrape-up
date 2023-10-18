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
        instance = flyrobu.Flyrobu()
        search_results = instance.search("arduino")
        self.assertIsNotNone(search_results, "FLyrobu:search - search results are None")
        self.assertIsInstance(
            search_results, list, "Flyrobu:search - search results are not a list"
        )
        self.assertGreater(
            len(search_results), 0, "Flyrobu:search - search results are empty"
        )
        self.assertIsInstance(
            search_results[0],
            dict,
            "Flyrobu:search - search results are not a list of dictionaries",
        )
        first_search_result = search_results[0]
        expected_keys = [
            "title",
            "price",
            "brand_name",
            "image",
            "description",
            "rating",
            "model_id",
            "link",
        ]

        # Check if all expected keys exist in the product_data dictionary
        for key in expected_keys:
            self.assertIn(
                key,
                first_search_result,
                f"Key '{key}' is missing in the first search result",
            )

    def test_search_url_is_incorrect(self):
        instance = flyrobu.Flyrobu()
        instance.base_url = "malformed:/www.search-url.com"
        search_results = instance.search("arduino")
        self.assertIsNone(
            search_results, "Flyrobu:search - search results are not None"
        )

    def test_get_product_details(self):
        instance = flyrobu.Flyrobu()
        product_name = "chain_for_6.35mm_pitch_sprocket_ebike_scooter"
        product_details = instance.get_product_details(product_name)
        self.assertIsNotNone(
            product_details, "Flyrobu:get_product_details - product details are None"
        )
        self.assertIsInstance(
            product_details,
            dict,
            "Flyrobu:get_product_details - product details are not a dictionary",
        )
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
            self.assertIn(
                key, product_details, f"Key '{key}' is missing in the product details"
            )

    def test_product_details_url_is_incorrect(self):
        instance = flyrobu.Flyrobu()
        instance.base_url = "malformed:/www.product-details-url.com"
        product_name = "chain_for_6.35mm_pitch_sprocket_ebike_scooter"
        product_details = instance.get_product_details(product_name)
        self.assertIsNone(
            product_details,
            "Flyrobu:get_product_details - product details are not None",
        )


if __name__ == "__main__":
    unittest.main()
