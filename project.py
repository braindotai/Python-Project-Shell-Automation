#!/usr/bin/env python
import os
import sys
import socket
import time
import pyautogui as auto
from github import Github

project_path = os.environ.get("PROJECT_PATH")
backup_path = os.environ.get("BACKUP_PATH")
args = sys.argv
SPACE = " " * 5

def rmspace(name):
	return name.replace(" ", "-")

def git():
	if check_connected("www.google.com"):
		return Github(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_PASSWORD"))
	print("Github connection failed..... system is not connected to internet")
	sys.exit(1)

def get_repos():
	return [repo.name for repo in git().get_user().get_repos()]

def check_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
    	pass
    return False

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f"{num:.2f} {x}"
        num /= 1024.0

def get_size(file):    
    path = project_path + file
    
    if os.path.isfile(path):
        return convert_bytes(os.path.getsize(path))

    total_size = 0.0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
            	try:
            		total_size += os.path.getsize(fp)
            	except:
            		pass
    return convert_bytes(total_size)

def spaceprint(name, size):
    space = SIZE - len(name)
    print(name, end = "")
    print(" " * space, size)
    
if len(args) == 1:
	print("Command name is required")
	print('For help run "project help"')

elif args[1] == "help":
	print("\n1. project create: To create a new project")
	print("   Example:")
	print('   project create "project name" "description" "private(True/False)" "official url"')
	
	print("\n2. project list: To print names of existing projects")
	print("   Example:")
	print('   project list')

	print("\n3. project <project name>: To view directories in a project")
	print("   Example:")
	print('   project "project name"')

	print("\n4. project open: To open the project in VS Code")
	print("   Example:")
	print('   project open "project name"')

	print("\n5. project backup: To backup the project")
	print("   Example:")
	print('   project backup "project name"')
	
	print("\n6. project delete: To delete a project")
	print("   Example:")
	print('   project delete "project name"')

	print("\n7. project repo: To print repository details")
	print("   Example:")
	print('   project repo "repo name"')

	print("\n8. project repo list: To list all repositories")
	print("   Example:")
	print('   project repo list')

	print("\n9. project repo delete: To delete a repository")
	print("   Example:")
	print('   project repo delete "repository name"')


elif args[1] == "create":
	if len(args) > 2:
		name = args[2]
	else:
		print("Project name is required")
		sys.exit(1)
	try:
		description = args[3]
	except:
		description = ""
	try:
		private = args[4]
		if private == "True": private = True
		else: private = False
	except:
		private = False
	try:
		homepage = args[5]
	except:
		homepage = ""

	if os.path.exists(project_path + name):
		print(f'Project with name "{name}" already exists')
		name = input("Enter new name: ").replace('"', "")

	print("")
	print(f"[============= Initiating project: {name} =============]")
	print("")
	os.chdir(project_path)
	os.mkdir(name)
	os.chdir(project_path + name)
	
	print("Creating Readme file ....")
	open("README.md", "w")
	
	print("Creating Environment Variables ....")
	open(".vars", "w")
	
	print("Creating Virtual Environment ....")
	os.system("python -m venv venv")

	print("Initiating Git Integration ....")
	os.system('git init')

	gitignore = open(".gitignore", "w")
	gitignore.write("venv\n")
	gitignore.write(".vars\n")
	gitignore.write("*.pyc")
	gitignore.write("__pycache__")
	gitignore.close()

	if check_connected("www.google.com"):
		github = Github(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_PASSWORD"))
	else:
		github = False

	os.system('git add .')
	os.system('git commit -m "Initial Commit"')

	if github:
		github.get_user().create_repo(name = name, description = description, homepage = homepage, private = private)
		print("Adding remote URL")
		os.system('git remote add origin https://github.com/braindotai/' + name.replace(" ", "-") + '.git')
		print("Pushing initial commit ....")
		os.system('git push -u origin master')
	else:
		print("Skipping remote URL integration")

	print("Opening project")
	os.system('code .')
	print("")
	print(f"[============= Project initiated successfully =============]")

	time.sleep(4)
	auto.keyDown('shift')
	auto.press('space')
	auto.keyUp('shift')
	time.sleep(1.5)
	auto.typewrite('source venv/scripts/activate')
	auto.press('enter')

	if github:
		time.sleep(1)
		auto.typewrite('python -m pip install --upgrade pip')
		auto.press('enter')


elif args[1] == "list":
	projects = os.listdir(project_path)
	for i, project in enumerate(projects):
		print(f"{i + 1}. {project}")

elif args[1] == "repo":
	if len(args) == 2:
		print("Repository name is required")
		sys.exit(1)
	elif args[2] == "list":
		for i, repo in enumerate(git().get_user().get_repos()):
			print(f"{i + 1}. {repo.name}")
	elif args[2] == "delete":
		if len(args) == 3:
			print("Repository name is required")
			sys.exit(1)
		else:
			repos = get_repos()
			name = ' '.join(args[3:])
			if rmspace(name) not in repos:
				print('Repository "' + rmspace(name) + '" not found')
				print('Type "$ project repo list" to see all available repositories')
			else:
				repo = git().get_repo(os.environ.get("GITHUB_USERNAME") + "/" + rmspace(name))
				repo.delete()
				print('Repository "' + name.replace("-", " ") + '" is deleted successfully')
	else:
		name = ' '.join(args[2:])
		try: 
			repo = git().get_repo(os.environ.get("GITHUB_USERNAME") + "/" + rmspace(name))
		except:
			print(f'Repository with name "{name}" is not found')
			print('Type "$ project repo list" to see all available repositories')
			sys.exit(1)
		print("\n===============", name, "===============")
		
		print("Contents:")
		for content in repo.get_contents(""):
			print(SPACE, str(content).split('"')[1])
		
		print("\nBranches:")
		for branch in repo.get_branches():
			print(SPACE, str(branch).split('"')[1])

		i = 0
		for _ in repo.get_issues(state = "open"):
			i += 1
		print("\nIssues:", i)
		for issue in enumerate(repo.get_issues(state = "open")):
			print(SPACE, str(issue).split('"')[1])


		print("Private:", repo.private)
		print("Starts:", repo.stargazers_count)
		print("Forked:", repo.fork)
		print("Forks:", repo.forks)
		print("Watchers:", repo.watchers_count)
		print("Language:", repo.language)
		print("Owner:", str(repo.owner).split('"')[1])
		print("URL:", repo.url.replace("api.", "").replace("repos/", ""))
		print("SSH URL:", repo.ssh_url)

		print("=" * len("=============== " + name + "===============\n"))

		

elif "delete" == args[1]:
	name = ' '.join(args[2:])
	projects = os.listdir(project_path)
	if name in projects or name.title() in projects or rmspace(name) in projects:
		print(f'Deleting project "{name}" from Projects directory')
		os.system('rm -rf "' + project_path + name + '"')
		os.system('rm -rf "' + project_path + rmspace(name) + '"')
		repos = get_repos()
		if rmspace(name.title()) not in repos and rmspace(name) not in repos:
			print('Repository "' + rmspace(name) + '" not found...... skipping repository deletion')
		else:
			print(f'Deleting project "{name}" from Github')
			repo = git().get_repo(os.environ.get("GITHUB_USERNAME") + "/" + rmspace(name))
			repo.delete()
		print('Project "' + name.replace("-", " ") + '" is deleted successfully')
	else:
		print('Project "' + name + '" is not found')
		print('Run "$ project list" to see all available projects')

elif "backup" == args[1]:
	name = ' '.join(args[2:])
	projects = os.listdir(project_path)
	if name in projects or name.title() in projects:
		os.system(f'rm -rf "{backup_path + name.title()}"')
		os.system(f'cp -r "{project_path + name.title()}" "{backup_path}"')
		print('Project "' + name + '" is backuped successfully')
	else:
		print('Project "' + name + '" is not found')
		print('Run "$ project list" to see all available projects')

elif "open" == args[1]:
	name = ' '.join(args[2:])
	projects = os.listdir(project_path)
	if name in projects or name.title() in projects:
		os.system(f'code "{project_path + name.title()}"')
		time.sleep(3)
		if 'venv' in os.listdir(project_path + name.title()):
			auto.keyDown('shift')
			auto.press('space')
			auto.keyUp('shift')
			time.sleep(1.5)
			auto.typewrite('source venv/scripts/activate')
			auto.press('enter')

	else:
		print('Project "' + name + '" is not found')
		print('Run "$ project list" to see all available projects')

else:
	name = ' '.join(args[1:])
	projects = os.listdir(project_path)
	if name in projects or name.title() in projects:
		SIZE = 30
		PLUS = 0
		dirs = os.listdir(project_path + name)
		files = []
		folders = []

		for file in dirs:
			if os.path.isfile(project_path + name + "/" + file):
				files.append(file)
			else:
				folders.append(file)
			if len(file) > SIZE:
			    PLUS += 4
			    SIZE += PLUS

		print("============= FOLDERS =============")
		for file in folders:
			spaceprint(file, get_size(name + "/" + file))
		print("")

		print("============== FILES ==============")
		for file in files:
		    spaceprint(file, get_size(name + "/" + file))


	else:
		print("Envalid command")
		print('Run "project help" for more info')