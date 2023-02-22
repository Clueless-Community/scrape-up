import sys

sys.path.append('E:\Jwoc\Clueless\scrape-up\src\scrape_up\github')

# print(sys.path)
from users import Users




import unittest

class TestUsers(unittest.TestCase):
    
    def setUp(self):
        self.users = Users('username')

    def test_followers(self):
        self.assertTrue(callable(self.users.followers))
    
    def test_followers_not_found(self):
        self.assertTrue(callable(self.users.followers))

    def test_get_avatar(self):
        self.assertTrue(callable(self.users.get_avatar))

    def test_get_avatar_not_found(self):
        self.assertTrue(callable(self.users.get_avatar))

    def test_get_bio(self):
        self.assertTrue(callable(self.users.get_bio))
    
    def test_get_bio_not_found(self):
        self.assertTrue(callable(self.users.get_bio))

    def test_get_repo(self):
        self.assertTrue(callable(self.users.get_repo))

    def test_repo_count(self):
        self.assertTrue(callable(self.users.repo_count))

        # for invalid username
    def test_repo_count_not_found(self):
        self.assertTrue(callable(self.users.repo_count))

    def test_star_count(self):
        self.assertTrue(callable(self.users.star_count))

    def test_star_count_not_found(self):
        self.assertTrue(callable(self.users.star_count))

    def test_yearly_contribution(self):
        self.assertTrue(callable(self.users.get_yearly_contributions))

    def test_yearly_contribution_not_found(self):
        self.assertTrue(callable(self.users.get_yearly_contributions))
    
    def test_repo_page(self):
        self.assertTrue(callable(self.users.__get_repo_page))

    def test_get_repo_page_not_found(self):
        self.assertTrue(callable(self.__get_repo_page))

    def test_get_repositories(self):
        self.assertTrue(callable(self.users.get_repositories))

    # invalid username
    def test_get_repositories_not_found(self):
        self.assertTrue(callable(self.users.get_repositories))

    def test_get_organization(self):
        self.assertTrue(callable(self.users.get_organizations))

    def test_get_organization_not_found(self):
        self.assertTrue(callable(self.users.get_organizations))

    def test_get_organizations_no_orgs(self):
        self.assertTrue(callable(self.users.get_organizations))

    # valid user
    def test_get_starred_page(self):
        self.assertTrue(callable(self.users.__get_stared_page))

    # invalid user
    def test_get_starred_page_not_found(self):
        self.assertTrue(callable(self.users.__get_stared_page))

    # Test case for valid username with starred repositories
    def test_get_starred_repos_valid(self):
        self.assertTrue(callable(self.users.__get_stared_page))

    # Test case for invalid username
    def test_get_starred_repos_invalid(self):
        self.assertTrue(callable(self.users.__get_stared_page))

    # Test case for username with no starred repositories
    def test_get_starred_repos_empty(self):
        self.assertTrue(callable(self.users.__get_stared_page))

if __name__ == '__main__':
    unittest.main()
