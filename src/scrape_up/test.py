import github

user = github.User('pyguru123')

print(user)
# print(dir(user))
# print(help(user))

print(user.username)
print(user.fullname)
print(user.followers)
print(user.following)
print(user.bio)
print(user.location)
print(user.repositories)
print(user.readme)
print(user.contributions)
print(user.get_pinned_repos())