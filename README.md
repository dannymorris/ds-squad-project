# ds-squad-project

Welcome to the DS Squad project repository. 

# Getting started

- Get acquainted with the Slack workspace and the various channels

- Get acquainted with the Trello board (link in the #important-links Slack channel).

- Follow the Git and GitHub workflow described below.

# Download Git and GitHub

- [Download Git](https://git-scm.com/downloads)
- Create a [GitHub account](https://github.com/)

# Simple workflow for using Git and GitHub

Follow these instructions to start using Git and this GitHub repository effectively.

- Clone the project by opening Git Bash (or your preferred Git tool) and entering the following:

```
cd documents # or some other local folder to store the project
git clone https://github.com/dannymorris/ds-squad-project.git
```

- Create your own branch to isolate your work and protect the main branch. Replace `my_branch_name` with something unique, e.g. `firstname_lastname`.

```
git checkout -b my_branch_name
```

- Create a new file, stage it, and commit it.

```
git add my_new_file.py
git commit -m "adding my_new_file.py"
```

- Push your file to your branch in GitHub

```
git push origin my_branch_name
```

- If you need to grab a file from another branch (e.g. another team member's branch), use the following:

```
git checkout some_other_branch another_file.py
git add another_file.py
git commit -m "adding another_file.py from some_other_branch"
```

# When and how to move files to the main branch

The main branch is now a "protected" branch, meaning no team member has direct access to push files directly to the main branch. This branch is reserved for "production" code. For this project, that may include the final Jupyter notebook for reproducing the machine learning model, a complete Python script for sourcing new features, and code for the final dashboard. 

Team members are expected to use their branches while the work is being developed. To move files to the main branch, a "pull request" must be submitted and reviewed by the repo administrator. This can be done by logging in to GitHub and going to the "Pull Requests" tab. If the pull request passes the code review by the administrator, it will be accepted into the main branch.

