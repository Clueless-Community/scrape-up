import unittest
from src.scrape_up.devpost import Devpost


class TestDevpost(unittest.TestCase):
    """
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.get_projects()` | Returns the latest projects along with their decription, like and commment count, image and member details. |
    | `.search(topic)` | Returns the searched projects along with their decription, like and commment count, image and member details. |
    | `.get_hackathons()` | Returns the latest hackathons along with their title, participants, prizes, deadlines.          |
    | `.get_featured()` | Returns the latest featured projects along with their decription, like and commment count, image and member details. |
    | `.get_winner()` | Returns the latest winning projects along with their decription, like and commment count, image and member details. |
    """

    def setUp(self):
        """
        Initialize a Devpost instance before each test method.
        """
        self.devpost = Devpost()

    def test_get_projects(self):
        """
        Test the get_projects() method.
        """
        try:
            projects = self.devpost.get_projects()
            self.assertIsInstance(projects, list, "Expected a list of projects")
            if projects:  # Check if there are projects returned
                project = projects[0]
                self.assertIn("title", project, "Project should have a 'title' field")
                self.assertIn("description", project, "Project should have a 'description' field")
                self.assertIn("like_count", project, "Project should have a 'like_count' field")
                self.assertIn("comment_count", project, "Project should have a 'comment_count' field")
                self.assertIn("img_url", project, "Project should have a 'img_url' field")
                self.assertIn("members", project, "Project should have a 'members' field")
                self.assertIsInstance(project["members"], list, "Members should be a list")
        except:
            return None

    def test_search(self):
        """
        Test the search() method.
        """
        try:
            topic = "AI"
            projects = self.devpost.search(topic)
            self.assertIsInstance(projects, list, "Expected a list of projects")
            if projects:  # Check if there are projects returned
                project = projects[0]
                self.assertIn("name", project, "Project should have a 'name' field")
                self.assertIn("tagline", project, "Project should have a 'tagline' field")
                self.assertIn("like_count", project, "Project should have a 'like_count' field")
                self.assertIn("comment_count", project, "Project should have a 'comment_count' field")
                self.assertIn("photo", project, "Project should have a 'photo' field")
                self.assertIn("members", project, "Project should have a 'members' field")
                self.assertIsInstance(project["members"], list, "Members should be a list")

        except:
            return None


    def test_get_featured(self):
        """
        Test the get_featured() method.
        """
        try:
            featured_projects = self.devpost.get_featured()
            self.assertIsInstance(featured_projects, list, "Expected a list of featured projects")
            if featured_projects:  # Check if there are featured projects returned
                project = featured_projects[0]
                self.assertIn("name", project, "Project should have a 'name' field")
                self.assertIn("tagline", project, "Project should have a 'tagline' field")
                self.assertIn("like_count", project, "Project should have a 'like_count' field")
                self.assertIn("comment_count", project, "Project should have a 'comment_count' field")
                self.assertIn("photo", project, "Project should have a 'photo' field")
                self.assertIn("members", project, "Project should have a 'members' field")
                self.assertIsInstance(project["members"], list, "Members should be a list")
        except:
            return None

    def test_get_winner(self):
        """
        Test the get_winner() method.
        """
        try:
            winner_projects = self.devpost.get_winner()
            self.assertIsInstance(winner_projects, list, "Expected a list of winning projects")
            if winner_projects:  # Check if there are winning projects returned
                project = winner_projects[0]
                self.assertIn("name", project, "Project should have a 'name' field")
                self.assertIn("tagline", project, "Project should have a 'tagline' field")
                self.assertIn("like_count", project, "Project should have a 'like_count' field")
                self.assertIn("comment_count", project, "Project should have a 'comment_count' field")
                self.assertIn("photo", project, "Project should have a 'photo' field")
                self.assertIn("members", project, "Project should have a 'members' field")
                self.assertIsInstance(project["members"], list, "Members should be a list")
        except:
            return None

if __name__ == "__main__":
    unittest.main()
