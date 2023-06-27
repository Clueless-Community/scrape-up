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

class RepositoryTest:

    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        #SetUp
        self.repository = github.Repository(self.username, repo)
    
    def test_fork_count(self):
        fork_count = self.repository.fork_count()
        return fork_count

    def test_get_contributors(self):
        contributors = self.repository.get_contributors()
        return contributors
    
    def test_topics(self):
        topics = self.repository.topics()
        return topics
    
    def test_pull_requests(self):
        pull_requests = self.repository.pull_requests()
        return pull_requests

    def test_last_updated_at(self):
        last_updated_at = self.repository.last_update_at()
        return last_updated_at

    def test_tags(self):
        tags = self.repository.tags()
        return tags

    def test_releases(self):
        releases = self.repository.releases()
        return releases

    def test_issues_count(self):
        issues_count = self.repository.issues_count()
        return issues_count        

    def test_readme(self):
        readme_path = self.repository.readme()
        return readme_path

    def test_get_pull_requests_ids(self):
        pull_requests_ids = self.repository.get_pull_requests_ids()
        return pull_requests_ids

    def test_get_issues(self):
        issues = self.repository.get_issues()
        return issues

    def test_commits(self):
        commits = self.repository.commits()
        return commits    

    def test_get_readme(self):
        readme = self.repository.get_readme()
        return readme

    def test_get_environment(self):
        environment = self.repository.get_environment()
        return environment    

    def test_watch_count(self):
        watch_count = self.repository.watch_count()
        return watch_count

    def test_all_watchers(self):
        watchers = self.repository.all_watchers()
        return watchers

class IssueTest:

    def __init__(self, username, repo, issue_no):
        self.username = username
        self.repo = repo
        self.issue_no = issue_no
        self.issue = github.Issue(self.username, self.repo, self.issue_no)

    def test_assignees(self):
        assignees = self.issue.assignees()
        return assignees

    def test_labels(self):
        labels = self.issue.labels()
        return labels

    def test_opened_by(self):
        opened_by = self.issue.opened_by()
        return opened_by

    def test_title(self):
        title = self.issue.title()
        return title

    def test_is_milestone(self):
        milestone = self.issue.is_milestone()
        return milestone

    def test_opened_at(self):
        opened_at = self.issue.opened_at()
        return opened_at

