import sys

sys.path.append('E:\Jwoc\Clueless\scrape-up\src\scrape_up\github')

# print(sys.path)
from users import Users




import unittest

class TestUsers(unittest.TestCase):
    
    def setUp(self):
        self.users = Users('Laxmankohar')

    def test_followers(self):
        self.assertEqual(self.users.followers(), '1')
    
    def test_followers_not_found(self):
        self.assertEqual(self.users.followers(), f"{self.users.get_username()} not found !")

    def test_get_avatar(self):
        self.assertEqual(self.users.get_avatar(), 'https://avatars.githubusercontent.com/u/73365025?v=4')

    def test_get_avatar_not_found(self):
        self.assertEqual(self.users.get_avatar(), f'Avatar not found for {self.users.get_username()} ')

    def test_get_bio(self):
        self.assertEqual(self.users.get_bio(), 'Java || Data Structure And Algorithm || Front- End Developer || Final year Student || Open Source enthusiasts')
    
    def test_get_bio_not_found(self):
        self.assertEqual(self.users.get_bio(), f'Bio not found for {self.users.get_username()}')
        

    def test_get_repo(self):
        # self.assertEqual(users.get_repo(), ['test-repo'])
        self.assertEqual(self.users.get_repo(), ['NetflixClone'])

    def test_repo_count(self):
        self.assertEqual(self.users.repo_count(), '49')

        # for invalid username
    def test_repo_count_not_found(self):
        self.assertEqual(self.users.repo_count(), f'No. of Repos not found for {self.users.get_username()}: invalid_username')

    def test_star_count(self):
        self.assertEqual(self.users.star_count(), '28')

    def test_star_count_not_found(self):
        self.assertEqual(self.users.star_count(), f'Starred repo not found for {self.users.get_username()}')

    def test_yearly_contribution(self):
        self.assertEqual(self.users.get_yearly_contributions(), '742contributionsinthelastyear')

    def test_yearly_contribution_not_found(self):
        self.assertEqual(self.users.get_yearly_contributions(), f'Yearly contributions not found for {self.users.get_username()}: invalid_username')
    
    def test_repo_page(self):
        page = self.users.__get_repo_page()
        self.assertIsNotNone(page)
        self.assertEqual(page.status_code, 200)
        self.assertIn(f"https://github.com/{self.users.get_username()}?tab=repositories", page.url)

    def test_get_repo_page_not_found(self):
        page = self.users.__get_repo_page()
        self.assertIsNone(page)

    def test_get_repositories(self):
        repos = self.users.get_repositories()
        self.assertIsInstance(repos, list)
        self.assertGreater(len(repos), 0)

    # invalid username
    def test_get_repositories_not_found(self):
        repos = self.users.get_repositories()
        self.assertEqual(repos, f'Repositories not found for {self.users.get_username()}: thisusernamedoesnotexist')

    def test_get_organization(self):
        orgs = self.users.get_organizations()
        # Verify that the function returns a list of organization names
        self.assertIsInstance(orgs, list)
        self.assertGreater(len(orgs), 0)

    def test_get_organization_not_found(self):
        orgs = self.users.get_organizations()
        # Verify that the function returns an error message
        self.assertEqual(orgs, f"No organizations found for the {self.users.get_username()}: thisusernamedoesnotexist")

    def test_get_organizations_no_orgs(self):
        # Test with a valid username that is not part of any organization
        orgs = self.users.get_organizations()
        # Verify that the function returns an empty list
        self.assertIsInstance(orgs, list)
        self.assertEqual(len(orgs), 0)

    # valid user
    def test_get_starred_page(self):
        page = self.users.__get_starred_page()  #__get_stared_page is not acessible due to private method
        assert page.title.string.strip() == f"{'self.users'} - Overview, Repositories, Stars, Followers, Following · GitHub"

    # invalid user
    def test_get_starred_page_not_found(self):
        page = self.users.__get_starred_page()
        assert page is not None
        assert isinstance(page, BeautifulSoup)
        assert "Not Found" in page.title.string

    # Test case for valid username with starred repositories
    def test_get_starred_repos_valid(self):
        repos = self.users.get_starred_repos()
        assert type(repos) == list
        assert len(repos) > 0

    # Test case for invalid username
    def test_get_starred_repos_invalid(self):
        repos = self.users.get_starred_repos()
        assert repos == f"Starred repositories not found for {self.users.get_username()}: nonexistinguser"

    # Test case for username with no starred repositories
    def test_get_starred_repos_empty(self):
        repos = self.users.get_starred_repos()
        assert repos == f"Starred repositories not found for {self.users.get_username()}"

if __name__ == '__main__':
    unittest.main()
