# __Shell Python Project Automation__

This project is inspired by __Kalle Hallden__

- [Youtube](https://www.youtube.com/watch?v=7Y8Ppin12r4)
- [Github](https://github.com/KalleHallden/ProjectInitializationAutomation)

In this repo I've provided my version of that shell python project automation, lets get started.

## Usage

### Requirements

- Install VS Code
- If you are using windows, download [Git](https://git-scm.com/download/win), which will install Git Bash as well. Then open Git Bash and run following commands

### Step 1.
You need to set 3 environment variables:

- `GITHUB_USERNAME`: Your github username
- `GITHUB_PASSWORD`: Your github password
- `PROJECT_PATH`: Path where you want to store all your projects

Checkout these tutorials to get it done

[For Mac/Linux](https://www.youtube.com/watch?v=5iWhQWVXosU)

[For Windows](https://www.youtube.com/watch?v=IolxqkL7cD8)

### Step 2.

In the shell run:
- `$ git clone https://github.com/braindotai/Shell-Python-Project-Automation.git`
- `$ cd Shell-Python-Project-Automation`
- `$ mv project.py project`
- `$ chmod +x project`
- `$ mkdir ~/bin`
- `$ cp project ~/bin"`
- `$ echo 'export PATH=$PATH":$HOME/bin"' >> .profile`
Then go back to working directory
- `$ cd ..`

### Step 3.

__To create a project__
1. `project create`: To create a new project

 Example:

 project create "new project" "this is my description" "private(True or False)" "homepage(https://mywebsitename.com)"

- This creates a project named "new project" in your "PROJECT_PATH"
- And sets that directory as github master repository
- Then create the Github repository with name "new project", description "this is my description", private setting (True/False) and homepage url as "https://mywebsitename.com"
- Then adds the Github remote url to the project directory
- Then creates the README.md file
- And commits an initial commit
- Then push the initial commit to master repo
- Then opens the VS Code through that project directory

__Now that's marvelous!!__

__2.__ `project list`: To print names of projects existing in your PROJECT_PATH
 
Example:
 
    `project list`

__3.__ `project delete`: To delete a project

Example:
 
    `project delete project name`

__4.__ `project repo`: To print repository details
 
Example:
 
    `project repo repo name`

__5.__ `project repo list`: To list all repositories
 
Example:
 
    `project repo list`

__6.__ `project repo delete`: To delete a repository
 
Example:
 
    `project repo delete repository name`

__7.__ For help you can run

    `project help`

# __Your Welcome__
