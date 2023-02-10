from github import *

# print(dir(User))
# print(help(User))

user = User('pyguru123')
print(user.get_pinned_repos())