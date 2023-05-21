<h1 align=center> For the contributors 🫂 </h1>

### Haven't made your first-contribution yet? 😢

Do check our [First Contribution](https://github.com/Clueless-Community/first-contribution) repository, where we have provided the guidelines to set up Git and how to make a pull request !

# Project setup 

## Fork and clone the repository
Copy the URL of the forked repository and clone it.
```bash
https://github.com/<your_username>/scrape-up
```

## Change the directory
```bash
cd scrape-up
```

> Folder Structure
```
scrape-up
 ├── 📄  LICENSE  
 ├── 📄  README.md  
 ├── 📄  contribution.md  
 ├── 📄  documentation.md  
 ├── 📄  pyproject.toml  
 ├── 📄  requirements.txt  
 ├── 📄  setup.cfg  
 └── 📂  src/ 
 │  └──── 📂  scrape_up/ 
 │  │  ├──── 📄  __init__.py  
 │  │  └──── 📂  github/ 
 │  │  │  ├──── 📄  __init__.py  
 │  │  │  ├──── 📄  respository.py  
 │  │  │  └──── 📄  users.py  
 │  │  └──── 📂  twitter/ 
 │  │  │  └──── 📄  __init__.py  

```


## Create a virtual environment
```bash
python -m venv env
```
## Activate the virtual environment
> For windows
```bash
env\scripts\activate
```
> For Linux
```bash
source env/scripts/activate
```

## Install the dependencies
```powershell
pip install -r requirements.txt
```

Now you are done with the project setup, now you can make the changes you want or assign.

### Let say you want to scrape the avatar url of and user. Steps applying which we can do this

- At first we have to scrape the profile page of a user. For that we have defined a function in the user class as
```python
- scrape-up/src/scrape_up/github/users.py
class Users:

    def __init__(self, username):
        self.username = username

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://github.com/{username}")
        data = BeautifulSoup(data.text, "html.parser")
        return data
```

+ The `__scrape_page` is a private function defined to scrape any page. 
+ Now we have to create a function with an approporiate name, in this case `get_avatar`.
```python
def followers(self):
        page = self.__scrape_page()
        try:
            followers = page.find(class_ = "avatar avatar-user width-full border color-bg-default")
            return followers["src"]
        except:
            message = f"{self.username} not found !"
            return message
```
+ When you do inspect element of the page, you will get to know class named `avatar avatar-user width-full border color-bg-default` contains the avatar url.

Once you are done with the changes you wanted to add,follow the steps to make the pull request.
## Create and checkout to the new branch.
powershell
git checkout -b <branch_name>

## Add the changes

git add .


## Commit your change with a proper messagge

git commit -m "Enter your message here"


## Make the Pull Request

git push origin <branch_name>



## Writing Tests ✍️

- Ensure that your code changes are accompanied by relevant tests.

- Write test cases that cover different scenarios and edge cases.


- Follow the existing test structure and naming conventions.

### Documentation 📑

- Document any significant changes or additions to the codebase.
- Provide clear and concise explanations of the functionality, usage, and any relevant considerations.
- Update the `README.md` file to reflect the changes made and provide instructions on how to use the project.

### ✅ Code Reviews 

- Be open to feedback and constructive criticism from other contributors.
- Participate in code reviews by reviewing and providing feedback.

### ✅ Bug Fixes and Issue Reporting 

- Help identify and fix bugs in the project.
- Report any issues or bugs you encounter during your contribution by creating a new issue in the GitHub repository.

### 🚀🚀Feature Requests

- Suggest new features or improvements that you believe would enhance the project.

### ☘️ Spread the Word

- Share your experience and the project with others.
- Spread the word about the project on social media, developer forums, or any relevant community platforms.

Thank you for your valuable contribution and for being a part of the Clueless Community! Together, we can make a difference. 🚀
