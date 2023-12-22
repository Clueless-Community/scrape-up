import unittest
from scrape_up import github


class GithubTest(unittest.TestCase):
    """
    | Methods                       | Details                                                                                            |
    | ----------------------------- | -------------------------------------------------------------------------------------------------- |
    | `.followers()`                | Returns the number of followers of a user.                                                         |
    | `.following()`                | Returns the number of following of a user.                                                         |
    | `.get_avatar()`               | Returns the avatar URL of a user.                                                                  |
    | `.get_bio()`                  | Returns the bio of a user.                                                                         |
    | `.get_repo()`                 | Returns the list of pinned repositories for a user.                                                |
    | `.repo_count()`               | Returns the number of Repositories of a user.                                                      |
    | `.star_count()`               | Returns the number of stars of a user.                                                             |
    | `.get_yearly_contributions()` | Returns the number of contributions made in 365 days frame.                                        |
    | `.get_repositories()`         | Returns the list of repositories of a user.                                                        |
    | `.get_starred_repos()`        | Return the list of starred repositories of a user.                                                 |
    | (NA) `.pul_requests()`             | Return the number of pull requests opened in a repository.                                         |
    | `.get_followers()`            | Returns the list of followers of a user.                                                           |
    | `.get_following_users()`      | Returns the list of users followed by a user.                                                      |
    | `.get_achievements()`         | Returns the list of achievements of a user.                                                        |
    | `.get_status()`               | Returns the status of a user.                                                                      |
    | `.get_contribution_streak()`  | Returns the maximum contribution streak of a user in the past year starting from the current date. |
    | `.get_repository_details()`   | Returns the list of repositories with their details.                                               |
    | (NA) `.get_branch()`               | Returns the list of branches in a repository.                                                      |
    | `.get_merged_pull_requests()` | Returns the list of merged pull requests                                                           |
    | `.get_open_issues()`          | Returns the list of open issues                                                                    |
    | `.get_years_active()`         | Returns the number of years that user have been active on github.                                  |
    """
    """
    | Methods            | Details                                                                    |
    | ------------------ | -------------------------------------------------------------------------- |
    | `.commits()`       | Returns the number of commits made in a pull request.                      |
    | `.title()`         | Returns the title of a pull request.                                       |
    | `.labels()`        | Returns all the labels of a pull request, empty list in case of no labels. |
    | `.files_changed()` | Returns the number of files changed in a pull request.                     |
    | `.reviewers()`     | Return the list of reviewers assigned in a pull request.                   |
    """
    """
    | Methods                    | Details                                                                                                                                                        |
    | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `.fork_count()`            | Returns the number of forks of a repository.                                                                                                                   |
    | `.get_contributors()`      | Returns the number of contributors of a repository.                                                                                                            |
    | `.topics()`                | Returns the topics of a repository.                                                                                                                            |
    | `.pull_requests()`         | Returns the number of pull requests opened in a repository.                                                                                                    |
    | `.last_updated_at()`       | Returns the last updated date of a repository.                                                                                                                 |
    | `.tags()`                  | Returns the last ten tags of a repository.                                                                                                                     |
    | `.releases()`              | Returns the last ten releases of a repository.                                                                                                                 |
    | `.issues_count()`          | Returns number of issues in a repository                                                                                                                       |
    | `.readme`                  | Saves the readme.md file of the given user to the current working directory. To view the readme.md with a live server, change ".md" to ".html" in "readme.md". |
    | `.get_pull_requests_ids()` | Returns all ids of opened pull requests in a repository.                                                                                                       |
    | `.get_issues()`            | Returns the list of all open issues in a repository.                                                                                                           |
    | `.commits()`               | Returns the number of commits in a repository.                                                                                                                 |
    | `.get_readme()`            | Returns & saves README.md file of the special repository (if exists)                                                                                           |
    | `.get_environment()`       | Returns the latest deployed link of a repository (if exists).                                                                                                  |
    | `.watch_count()`           | Returns the number of watchers of a repository                                                                                                                 |
    | `.all_watchers()`          | Returns the username of all watches of a repository                                                                                                            |
    | `.get_insights(period)`    | Returns the active pr count, active issue count, merged pr count, open pr count, closed issue count, new issue count, list of recent merged prs,
                                   list of recent open prs, list of recent closed issues, list of recent open issues for a specified period                                                                           |
    """
    """
    | Methods                     | Details                                                         |
    | --------------------------- | --------------------------------------------------------------- |
    | `.top_topics()`             | Returns a list of the most used topics in an organization.      |
    | `.followers()`              | Returns the number of followers of an organization.             |
    | `.top_languages()`          | Returns the top languages used in an organization.              |
    | `.followers()`              | Returns the number of followers of an organization.             |
    | `.avatar()`                 | Returns the avatar URL of an organization.                      |
    | `.repositories()`           | Returns the list of repositories of an organization.            |
    | `.people()`                 | Returns the list of people in an organization.                  |
    | `.peoples() `               | Returns the number of people in an organization.                |
    | `.get_location() `          | Returns the location of an organization.                        |
    | `.repository_details()`     | Returns the list of repositories with their details.            |
    | `.pinned_repository()`      | Returns the list of pinned repositories with their details.     |
    | `.get_organization_links()` | Returns a dictionary of important website links of a community. |
    """
    """
    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.assignees()`    | Returns the assignees of an issue.                                                 |
    | `.labels()`       | Returns the labels of an issue.                                                    |
    | `.opened_by()`    | Returns the name of the user, who opened the issue.                                |
    | `.title()`        | Returns the title of an issue.                                                     |
    | `.is_milestone()` | Returns the milestone, if the issue is part of one or 'No milestone', if it's not. |
    | `.opened_at()`    | Returns a string containing the time when the issue was opened in ISO format.      |
    """

    def test_followers(self):
        test_instance_user = github.Users("nikhil25803")
        method_response  =  test_instance_user.followers()
        self.assertIsInstance(method_response, str)
        self.assertEqual(method_response.isdigit(), True)

    def test_following(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.following()
        self.assertIsInstance(method_response, str)
        self.assertEqual(method_response.isdigit(), True)

    def test_get_avatar(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_avatar()
        self.assertIsInstance(method_response, str)
        self.assertIn("https://avatars.githubusercontent.com/u/", method_response)

    def test_get_bio(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_bio()
        self.assertIsInstance(method_response, str)

    def test_get_repo(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_repo()
        self.assertIsInstance(
            method_response, list, "Return type mismatch [Github Users: get_repo()]"
        )

    def test_get_repo_count(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.repo_count()
        self.assertIsInstance(
            method_response,
            str,
            "Return type mismatch [Github Users: get_repo_count()]",
        )
        self.assertEqual(method_response.isdigit(), True)

    def test_star_count(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.star_count()
        self.assertIsInstance(
            method_response, str, "Return type mismatch [Github Users: star_count()]"
        )
        self.assertEqual(method_response.isdigit(), True)

    def test_get_yearly_contributions(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_yearly_contributions()
        self.assertIsInstance(method_response, str)
        str_portion  =  method_response.split(" ", 1)[1]
        self.assertEqual("contributions in the last year", str_portion)

    def test_get_repositories(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_repositories()
        self.assertIsInstance(method_response, list)

    def test_get_starred_repos(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_starred_repos()
        self.assertIsInstance(method_response, list)

    def test_get_followers(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_followers()
        self.assertIsInstance(method_response, list)
        for item in method_response:
            self.assertIsInstance(item, str)

    def test_get_following_users(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_following_users()
        self.assertIsInstance(method_response, list)
        for item in method_response:
            self.assertIsInstance(item , str)

    def test_get_achievements(self):
        test_instance_user  =  github.Users("nikhil25803")
        method_response  =  test_instance_user.get_achievements()
        self.assertIsInstance(method_response, list)

    def test_get_status(self):
        test_instance_user = github.Users("nikhil25803")
        method_response = test_instance_user.get_status()
        self.assertIsInstance(method_response, str)
    
    def test_get_contribution_streak(self):
        test_instance_user = github.Users("nikhil25803")
        method_response = test_instance_user.get_contribution_streak()
        self.assertIsInstance(method_response, int)

    def test_get_repository_details(self):
        test_instance_user = github.Users("havoksahil")
        method_response = test_instance_user.get_repository_details()
        self.assertIsInstance(method_response, list)
        for items in method_response:
            self.assertAlmostEqual(
                list(items.keys()), 
                ['name', 'url', 'description', 'language', 'forks', 'stars', 'issues', 'pull_requests']
            )


    def test_get_merged_pull_requests(self):
        test_instance_user = github.Users("nikhil25803")
        method_response = test_instance_user.get_merged_pull_requests()
        self.assertIsInstance(method_response, list)

    
    def test_get_open_issues(self):
        test_instance_user = github.Users("nikhil25803")
        method_response = test_instance_user.get_open_issues()
        self.assertIsInstance(method_response, list)

    def test_get_years_active(self):
        test_instance_user = github.Users("nikhil25803")
        method_response = test_instance_user.get_years_active()
        self.assertIsInstance(method_response, int)

    def test__pull_commits(self):
        pull_request = github.PullRequest(username = "anoma", repository_name = "namada", pull_request_number = 2294)
        method_response = pull_request.commits()
        self.assertIsInstance(method_response, str)
        self.assertTrue(method_response.isdigit())
    
    def test_title(self):
        pull_request = github.PullRequest(username = "anoma", repository_name = "namada", pull_request_number = 2294)
        method_response = pull_request.title()
        self.assertIsInstance(method_response, str)

    def test_labels(self):
        pull_request = github.PullRequest(username = "chromium", repository_name = "chromium", pull_request_number = 206)
        method_response = pull_request.labels()
        self.assertIsInstance(method_response, list)
    
    def test_files_changed(self):
        pull_request = github.PullRequest(username = "chromium", repository_name = "chromium", pull_request_number = 206)
        method_response = pull_request.files_changed()
        self.assertIsInstance(method_response, str)
        self.assertTrue(method_response.isdigit())
    
    def test_reviewers(self):
        pull_request = github.PullRequest(username = "anoma", repository_name = "namada", pull_request_number = 2294)
        method_response = pull_request.reviewers()
        self.assertIsInstance(method_response, list)


    def test_fork_count(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.fork_count()
        self.assertIsInstance(method_response, str)


    def test_get_contributors(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.get_contributors()
        self.assertIsInstance(method_response, str)
        self.assertIn('Contributors', method_response)


    def test_get_topics(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.topics()
        self.assertIsInstance(method_response, list)


    def test_pull_requests(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.pull_requests()
        self.assertIsInstance(method_response, int)


    def test_last_updated_at(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.last_update_at()
        self.assertIsInstance(method_response, str)


    def test_tags(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.tags()
        self.assertIsInstance(method_response, list)


    def test_releases(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.releases()
        self.assertIsInstance(method_response, list)


    def test_issues_count(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.issues_count()
        self.assertIsInstance(method_response, str)
        self.assertTrue(method_response.isdigit())
    
    # def test_readme(self): can't test for readme as there is no return value


    def test_get_pull_requests_id(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.get_pull_requests_ids()
        self.assertIsInstance(method_response, list)


    def test_get_issues(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.get_issues()
        self.assertIsInstance(method_response, list)


    def test_repo_commits(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.commits()
        self.assertIsInstance(method_response, int)

 
    def test_get_readme(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.get_readme()
        self.assertIsInstance(method_response, str)


    def test_get_environment(self):
        repository = github.Repository(username = "bobheadxi", repository_name = "deployments")
        method_response = repository.get_environment()
        self.assertIsInstance(method_response, str)


    def test_watch_count(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.watch_count()
        self.assertIsInstance(method_response, dict)
        self.assertIsInstance(method_response['data'], int)


    def test_all_watchers(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.all_watchers()
        self.assertIsInstance(method_response, list)

    def test_get_insights(self):
        repository = github.Repository(username = "Clueless-Community", repository_name = "scrape-up")
        method_response = repository.get_insights('monthly')
        self.assertIsInstance(method_response, list)

    def test_topics(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.top_topics()
        self.assertIsInstance(method_response, list)


    def test_org_followers(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.followers()
        self.assertIsInstance(method_response, str)
        self.assertTrue(method_response.isdigit())

    def test_top_languages(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.top_languages()
        self.assertIsInstance(method_response, list)

    def test_org_avatar(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.avatar()
        self.assertIsInstance(method_response, str)

    def test_org_repositories(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.repositories()
        self.assertIsInstance(method_response, list)

    def test_people(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.people()
        self.assertIsInstance(method_response, list)

    def test_peoples(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.peoples()
        self.assertIsInstance(method_response, int)

    def test_get_location(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.get_location()
        self.assertIsInstance(method_response, str)

    def test_respository_details(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.repository_details()
        self.assertIsInstance(method_response, list)
        for items in method_response:
            self.assertAlmostEqual(
                list(items.keys()), 
                ['name', 'url', 'description', 'language', 'forks', 'stars', 'issues', 'pull_requests']
            )

    def test_pinned_repository(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.pinned_repository()
        self.assertIsInstance(method_response, list)
        for items in method_response:
            self.assertAlmostEqual(
                list(items.keys()),
                [   
                    "name",
                    "link",
                    "detail",
                    "top_lang",
                    "stars",
                    "forks"
                ]
            )

    def test_org_links(self):
        organization = github.Organization(organization_name = "Clueless-Community")
        method_response = organization.get_organization_links()
        self.assertIsInstance(method_response, dict)

    def test_assignees(self):
        issue = github.Issue(username = "Shreya111111", repository_name = "Linkscrape", issue_number = 1)
        method_response = issue.assignees()
        self.assertIsInstance(method_response, list)

    def test_issue_labels(self):
        issue = github.Issue(username = "Shreya111111", repository_name = "Linkscrape", issue_number = 1)
        method_response = issue.labels()
        self.assertIsInstance(method_response, list)

    def test_opened_by(self):
        issue = github.Issue(username = "Shreya111111", repository_name = "Linkscrape", issue_number = 1)
        method_response = issue.opened_by()
        self.assertIsInstance(method_response, str)

    def test_issue_title(self):
        issue = github.Issue(username = "Shreya111111", repository_name = "Linkscrape", issue_number = 1)
        method_response = issue.title()
        self.assertIsInstance(method_response, str)

    def test_opened_at(self):
        issue = github.Issue(username = "Shreya111111", repository_name = "Linkscrape", issue_number = 1)
        method_response = issue.opened_at()
        self.assertIsInstance(method_response, str)

    # def test_is_milestone(self): need to find a milestone issue
    #     issue = github.Issue(username = "", repository_name = "", issue_number = )
    #     method_response = issue.is_milestone()
    #     self.assertIsInstance(method_response, str)

    

if __name__ == '__main__':
    unittest.main()