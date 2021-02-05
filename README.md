# ds-squad-project

Welcome to the DS Squad project repository. 

# Getting started

- Get acquainted with the Slack workspace and the various channels

- Get acquainted with the Trello board (link in the #important-links Slack channel).

# Clone the repository from GitHub

Follow these instructions to start using Git and this GitHub repository effectively.

- [Download Git](https://git-scm.com/downloads)
- Create a [GitHub account](https://github.com/)
- Clone the project by opening Git Bash (or your preferred Git tool) and enter the following:

```
cd path_to_your_preferred_local_folder
git clone https://github.com/dannymorris/ds-squad-project.git
```

# Simple workflow for collaborating on GitHub

- Each member will have "push" access to the main branch. While this is typically not recommended, I believe it is appropriate given the nature of the project. Since each of you will most likely be working on your own set of files, we are unlikely to have many conflicts. 

- Each day you work on the project, get in the habit of "pulling" the latest copy of the GitHub repo to your local machine. As your work progresses, you'll want to keep the habit of pulling frequently to ensure that everyone's local Git repository is up-to-date. Look out for communications from team members in new files are added to the GitHub repo that you may need to pull. Use the following code to pull the latest copy of the GitHub repo to your local machine.

```
cd path_to_your_preferred_local_folder
git pull
```

- Develop the habit of "adding", "committing", and "pushing" your work frequently. For example, if you create a new Python script use the following code:

```
git add my_new_script.py
git commit -m "adding my new Python script containing crime summary statistics"
git push
```

- If you push a file that may impact other team members, be sure to send out a communication on Slack.