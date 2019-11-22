# __Python Project Shell Automation__

This project is inspired by __Kalle Hallden__

- [Youtube](https://www.youtube.com/watch?v=7Y8Ppin12r4)
- [Github](https://github.com/KalleHallden/ProjectInitializationAutomation)

In this repo I've provided my version of shell automation for python projects, lets get started.

## Usage

### Requirements

- Install [VS Code](https://code.visualstudio.com/download)
- If you are using windows, download [Git](https://git-scm.com/download/win), which will install Git Bash as well. Then open Git Bash and run following commands
- Install PyGithub library for python

`$ pip install PyGithub`

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

1. __To create a project__

   `project create <project name> <description> <private (True/False)> <homepage url>`

 Example:

    $ project create "new project" "this is my description" "False"

    ============= Initiating project: new project =============

    Initialized empty Git repository in C:/Users/brain/Desktop/Projects/new project/.git/
    [master (root-commit) 3255f0d] Initial Commit
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 README.md
    Enumerating objects: 3, done.
    Counting objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 222 bytes | 222.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/braindotai/new-project.git
    * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.

    ============= Project initiated successfully =============

- This creates a project named "new project" in your "PROJECT_PATH"
- And sets that directory as github master repository
- Then create the Github repository with name "new project", description "this is my description", private setting (True/False) and homepage url as "https://mywebsitename.com"
- Then adds the Github remote url to the project directory
- Then creates the README.md file
- And commits an initial commit
- Then push the initial commit to master repo
- Then opens the VS Code through that project directory


__Now that's marvelous!!__

2. __To print names of projects existing in your PROJECT_PATH__

   `project list`
 
Example:
 
    $ project list
    1. Custom-Linux-Command-Creator
    2. Deep-Learning-Scratch-Arena
    3. Dr-Deep
    4. Kaggle-Exploratory-Data-Analysis
    5. Shell Python Project Automation

3. __To delete a project__

   `project delete <project name>`

Example:
 
    $ project delete new project
    Project "new project" is deleted successfully

4. __To print repository details__

   `project repo <repo name>`
 
Example:
 
    $ project repo dr deep

    =============== dr deep ===============
    Contents:
        .gitignore
        Blood Cells
        Breast Cancer
        Heart Attack
        LICENSE
        README.md
        Retinal OCT
        Skin Cancer
        Tuberculosis
        samples

    Branches:
        master

    Issues: 0
    Private: False
    Starts: 0
    Forked False
    Forks: 0
    Watchers: 0
    Language: Python
    Owner: braindotai
    URL: https://github.com/braindotai/Dr-Deep
    SSH URL: git@github.com:braindotai/Dr-Deep.git
    =======================================

5. __To list all repositories__

   `project repo list`
 
Example:
 
    $ project repo list
    1. Custom-Linux-Command-Creator
    2. Deep-Learning-Scratch-Arena
    3. Dr-Deep
    4. Dxeon
    5. incubator-mxnet
    6. Kaggle-Exploratory-Data-Analysis
    7. KDD18-Gluon
    8. MXNet-Gluon-Tutorials
    9. pandas-videos
    10. reinforcement-learning
    11. Reinforcement-Learning-Scratch-Arena
    12. Shell-Python-Project-Automation

6. __To delete a repository__

   `project repo delete <repository name>`
 
Example:
 
    $ project repo delete new project
    Repository "new project" is deleted successfully

7. __For help you can run__

   `project help`

# __Your Welcome__
