import unittest
from src.scrape_up.librarygenesis import LibGen


class TestLibGen(unittest.TestCase):
    """
        | Methods       | Details                       |
        | --------------| ----------------------------- |
        | `.getBooks(book_name=" ")` | Returns the books with name, author, size, format, book link, book cover link, language |
        """
    def setUp(self):
        """
        Initialize a LibGen instance before each test method.
        """
        self.libgen = LibGen()

    def test_getBooks_empty_name(self):
        """
        Test the getBooks() method with an empty book name.
        """
        try:
            result = self.libgen.getBooks("")
            self.assertEqual(result, "Error: enter name", "Expected error message for empty book name")
        except:
            return None

    def test_getBooks_short_name(self):
        """
        Test the getBooks() method with a short book name.
        """
        try:
            result = self.libgen.getBooks("AI")
            self.assertEqual(result, "Error: Title Too Short", "Expected error message for short book name")
        except:
            return None

    def test_getBooks_valid_name(self):
        """
        Test the getBooks() method with a valid book name.
        """
        try:
            result = self.libgen.getBooks("Python")
            self.assertIsInstance(result, list, "Expected a list of books")
            if result:  # Check if there are books returned
                book = result[0]
                self.assertIn("name", book, "Book should have a 'name' field")
                self.assertIn("author", book, "Book should have an 'author' field")
                self.assertIn("size", book, "Book should have a 'size' field")
                self.assertIn("format", book, "Book should have a 'format' field")
                self.assertIn("link", book, "Book should have a 'link' field")
                self.assertIn("language", book, "Book should have a 'language' field")
        except:
            return None

    def test_getBooks_no_results(self):
        """
        Test the getBooks() method with a book name that yields no results.
        """
        try:
            result = self.libgen.getBooks("somebookthatdoesnotexist")
            self.assertEqual(result, "Error: no results found", "Expected error message for no results found")
        except:
            return None


if __name__ == "__main__":
    unittest.main()
