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
│   
└───📂src
│   │   └───📂scrape_up 
|   |       |   📄__init__.py
|   |       | 
│   │       └───📂github 
|   |       |   └───📄__init__.py
|   |       |
│   │       └───📂twitter
|   |       |   └───📄__init__.py
|   |       |
|   |
📄.gitignore
📄contribution.md
📄documentation.py
📄LICENCE
📄pyproject.toml
📄README.md
📄requirements.txt
📄setup.cfg
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

Now you are done with the project setup, now you can make the changes you want or assigned.


Once you are done with the changes you wanted to add. Follow the steps to make the pull request.
## Create and checkout to the new branch.
```powershell
git checkout -b <branch_name>
```
## Add the changes
```
git add .
```

## Commit your change with a proper messagge
```
git commit -m "Enter your message here"
```

## Make the Pull Request
```
git push origin <branch_name>
```
---