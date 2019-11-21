#!/usr/bin/env python
import os
import sys
from github import Github

project_path = os.environ.get("PROJECT_PATH")

args = sys.argv
SPACE = " " * 5

def rmspace(name):
	return name.replace(" ", "-")

def git():
	return Github(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_PASSWORD"))

def get_repos():
	return [repo.name for repo in git().get_user().get_repos()]


if len(args) == 1:
	print("Command name is required")

elif args[1] == "help":
	print("\nproject create: To create a new project")
	print(" Example:")
	print(' project create "project name" "description" "private(True/False)" "homepage(url)"')
	
	print("\nproject list: To print names of existing projects")
	print(" Example:")
	print(' project list')
	
	print("\nproject delete: To delete a project")
	print(" Example:")
	print(' project delete "project name"')

	print("\nproject repo: To print repository details")
	print(" Example:")
	print(' project repo "repo name"')

	print("\nproject repo list: To list all repositories")
	print(" Example:")
	print(' project repo list')

	print("\nproject repo delete: To delete a repository")
	print(" Example:")
	print(' project repo delete "repository name"')


elif args[1] == "create":
	try:
		name = args[2]
	except:
		raise ValueError("Project name is required")
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

	user = git().get_user()
	user.create_repo(name = name, description = description, homepage = homepage, private = private)
	print("")
	os.system(f"echo ============= Initiating project: {name} =============")
	print("")
	os.chdir(project_path)
	os.mkdir(name)
	os.chdir(project_path + name)
	os.system('git init')
	os.system('git remote add origin https://github.com/braindotai/' + name.replace(" ", "-") + '.git')
	open("README.md", "w")
	os.system('git add .')
	os.system('git commit -m "Initial Commit"')
	os.system('git push -u origin master')
	os.system('code .')
	print("")
	os.system(f"echo ============= Project initiated successfully =============")

elif args[1] == "list":
	projects = os.listdir(project_path)
	for i, project in enumerate(projects):
		print(f"{i + 1}. {project}")

elif args[1] == "repo":
	if len(args) == 2:
		raise ValueError("Repository name is required")
	elif args[2] == "list":
		for i, repo in enumerate(git().get_user().get_repos()):
			print(f"{i + 1}. {repo.name}")
	elif args[2] == "delete":
		if len(args) == 3:
			raise ValueError("Repository name is required")
		else:
			repos = get_repos()
			name = ' '.join(args[3:])
			if rmspace(name) not in repos:
				print('Repository "' + rmspace(name) + '" not found')
			else:
				repo = git().get_repo(os.environ.get("GITHUB_USERNAME") + "/" + rmspace(name))
				repo.delete()
				print('Repository "' + name.replace("-", " ") + '" is deleted successfully')
	else:
		name = ' '.join(args[2:])
		repo = git().get_repo(os.environ.get("GITHUB_USERNAME") + "/" + rmspace(name))
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
		print("Forked", repo.fork)
		print("Forks:", repo.forks)
		print("Watchers:", repo.watchers_count)
		print("Language:", repo.language)
		print("Owner:", str(repo.owner).split('"')[1])
		print("URL:", repo.url.replace("api.", "").replace("repos/", ""))
		print("SSH URL:", repo.ssh_url)

		print("=" * len("=============== " + name + "===============\n"))

		

elif "delete" in args:
	name = ' '.join(args[2:])
	projects = os.listdir(project_path)
	if name in projects or rmspace(name) in projects:
		print(name)
		os.system('rm -rf "' + project_path + name + '"')
		os.system('rm -rf "' + project_path + rmspace(name) + '"')
		repos = get_repos()
		if rmspace(name) not in repos:
			print('Repository "' + rmspace(name) + '" not found...... skipping repository deletion')
		else:
			repo = git().get_repo(os.environ.get("GITHUB_USERNAME") + "/" + rmspace(name))
			repo.delete()
		print('Project "' + name.replace("-", " ") + '" is deleted successfully')
	else:
		print('Project "' + name + '" is not found')

else:
	print("Envalid command")
	print('Run "project help" for more info')