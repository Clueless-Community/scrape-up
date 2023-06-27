from scrape_up import github

class UserTest():

    def __init__(self, username):
        self.username = username
        #SetUp
        self.user = github.Users(username=self.username)

    def test_followers(self):
        followers = self.user.followers()
        return followers

    def test_following(self):
        following = self.user.following()
        return following

    def test_get_avatar(self):
        avatar = self.user.get_avatar()
        return avatar  

    def test_get_bio(self):
        bio = self.user.get_bio()
        return bio

    def test_get_repo(self):
        repos = self.user.get_repo()
        return repos

    def test_repo_count(self):
        repo_count = self.user.repo_count()
        return repo_count

    def test_star_count(self):
        star_count = self.user.star_count()
        return star_count

    def test_get_yearly_contributions(self):
        contributions = self.user.get_yearly_contributions()
        return contributions

    def test_get_repositories(self):
        repositories = self.user.get_repositories()
        return repositories

    def test_get_starred_repos(self):
        starred_repos = self.user.get_starred_repos()
        return starred_repos
        
    def test_pull_requests(self):
        pull_requests = self.user.pul_requests()
        return pull_requests

    def test_get_followers(self):
        followers = self.user.get_followers()
        return followers

    def test_get_following_users(self):
        following_users = self.user.get_following_users()
        return following_users

    def test_get_achievements(self):
        achievements = self.user.get_achievements()
        return achievements

    def test_get_status(self):
        status = self.user.get_status()
        return status
        
    def test_get_contribution_streak(self):
        contribution_streak = self.user.get_contribution_streak()
        return contribution_streak
        
    def test_get_repository_details(self):
        repository_details = self.user.get_repository_details()
        return repository_details
        
    def test_get_branch(self):
        branches = self.user.get_branch()
        return branches
