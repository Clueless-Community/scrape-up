from scrape_up import github

user = github.Users("PalaVenkiReddy")

print(user.get_repositories())