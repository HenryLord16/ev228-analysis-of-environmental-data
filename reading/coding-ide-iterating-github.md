# coding-ide-iterating-github

### 0.1. Goals
* I can define and give examples of IDEs and use an IDE to write, run, and edit code
* I can define version control, explain how Git and GitHub work to carry out version control, and use GitHub Desktop to commit and push changes to code

### 0.2. Prerequisites
These materials assume: 
* You have set up Python and an environment
* You have downloaded VSCode
* You have a GitHub account
* You have GitHub Desktop installed on your computer
* GitHub is already set up with a repository for your onboarding project.
We will go over all of these processes in our initial meeting on Day 1.

## 1. Coding in an Integrated Development Environment (IDE)
* An IDE is software that provides a comprehensive environment to carry out software development: that is, to write, run, and test code.
* Examples of IDEs:
    * VSCode -- this is the one we use in EV228
    * Zed
    * Spyder
    * PyCharm
    * Kate
    * Notepad++
* Code you write in an IDE is saved to a local project folder on the computer where the IDE is running.
* Keep code for different projects in different folders. For example, your onboarding code should be in a separate project folder from the code you write as we begin to do data analysis.

### 1.1. VSCode
* There are three main panels in the VSCode window. The figure below describes this layout.
![vscode-window](images/vscode-window.jpeg)
*Example VSCode window showing the Editor, Explorer, and Terminal.*

### 1.2. Running code
* Python code is run from the shell using the command `python [name of file.py]`
  * For example, we ran our `utensils_script_demo.py` Python program on Day 1 by entering the command `python utensils_script_demo.py` into the shell
* The output from the code is printed to the Terminal

### 1.3. Example: Writing and running code
* From within your onboarding project folder, make a new file (⌘ + N, or select "New Text File" from the "File" menu)
* Add the following code to your blank file: `print("Hello world!")`
* Save the file within your project folder (⌘ + S, or select "Save" from the "File" menu) and name it `hello_world.py`.
   * The `.py` at the end of the file designates the file as containing Python code
* Run your program by typing `python hello_world.py` in the Terminal panel
* This should yield the output: "Hello world!"

*Link to video: [link](https://drive.google.com/file/d/1woTGqYPr772jzUVwURcVUfkdXtcFDGPK/view?usp=drive_link). Screen recording of this example. Shell commands used to show that the working directory is the project folder.*

#### 1.3.1 Printing and program state
* In general, any variable can be printed by typing `print(variable)`.
* In class, we often use a function called `ic()` from the package `icecream` to do this instead as it uses clearer formatting.
* Printing variables is used to track the *program state*: the set of objects accessible to the program at a given moment.
* Tracking the program state is critical to troubleshooting code as it is how we understand exactly where the program goes awry.

### 1.4. Stopping at a certain line
* It is often useful to stop code from running past a certain point, especially when troubleshooting a longer program.
* The `sys` package (installed with Python by default) includes a function `exit` that stops a program. With `sys` imported, `sys.exit('STOP')` will stop the program at that line and print the message "STOP".

*Link to video: [link](https://drive.google.com/file/d/1dvht2JliBUASHiJhIVTKQp6WfNVVQcX5/view?usp=drive_link). Screen recording of this example, illustrating stopping output at a certain line.*

#### 1.4.1. Exercises
* Change your code to print "Sphinx of the black quartz, heed my vow" and "The quick brown fox jumps over the lazy dog" after it prints "Hello, world!"
* Edit the code from the previous exercise to stop execution before "The quick brown fox jumps over the lazy dog"
* Edit the code from the previous exercise so that the message from `sys.exit()` reads `NOW` instead of `STOP`

### 1.5. Useful shortcut keys
* Save: ⌘ + S (Windows equivalent: Control + S)
* Undo: ⌘ + Z (Windows equivalent: Control + Z)
* Comment or uncomment current line, or multiple selected lines: ⌘ + / (Windows equivalent: Control + /)
* Autocomplete command in terminal: Tab
* Open new file: ⌘ + N (Windows equivalent: Control + N)
* Close current tab: ⌘ + W (Windows equivalent: Control + W)

### 1.6. A Note About Jupyter Notebooks
**You can ignore this section if you never learned Jupyter Notebooks or if you have already worked with free-form Python code.**
* Jupyter Notebooks provide a single script organized in "cells" consisting of either natural language (written in Markdown) or code (Python).
* Most new Python learners (since ~2020) begin with Jupyter Notebooks, due to their ability to run cell by cell and the way that they hide certain complexities of the underlying Python installation.
* Our approach of writing Python code free-form within an IDE may seem unintuitive if you are familiar with Jupyter Notebooks.
* Jupyter Notebooks are terrific in classroom situations where learning code is not the emphasis! I use Jupyter Notebooks extensively in EV128 "Introduction to Global Climate Change" and my First-Year Program version of this course.
* However, in research and professional development they raise **three major challenges:**
    1. Notebooks encourage thinking about workflows as a single process, often with lots of repeated code. This usually yields inefficient code which is difficult for others (including your future self!) to reuse.
    2. The cell-by-cell workflow of Notebooks make it difficult to reliably track the program state. This makes troubleshooting challenging because edits made in one place interact unpredictably with other parts of the script. These errors are difficult to catch, particularly under deadline pressure. Meta-scientific analyses show that most Jupyter Notebooks in the published literature cannot run to completion because of bugs introduced by program state errors!
    3. Most careers with a data science element in industry, the nonprofit sector, or government do not consider knowledge of Jupyter Notebooks alone to be sufficient experience for hiring.


## 2. Version control with Git and GitHub
* Version control refers to tracking changes to code in an organized way that allows changes to be browsed and managed after they are made.
* Git and GitHub refers to systems that manages version control through a combination of local (Git) and remote (GitHub) *repositories*. Repositories are like folders, except they retain the revision history of each item contained within in addition to the items themselves. (Think of this like the document history in a Google Doc.)
* GitHub Desktop manages the local and remote repositories seamlessly in one place.

### 2.1. Git and GitHub theory
* The *project folder* on your computer is the actual folder where you are working and making changes to your code, for example, in VSCode
    * Saving a file saves the changes to your drive
* Git adds a *local repository* which tracks the version history (all changes over time) of the items within the repository.
    * Making a *commit* involves logging all of the changes since your last commit into your local repository
    * The local repository is essentially a folder that "shadows" the contents of your project folder. It can't normally be seen because it's deliberately hidden from the file system.
        * To see the local repository from within the shell, navigate your working directory to a folder with a Git repository and use `ls -a` (Mac) or `dir /a:h` (Windows). You will see an invisible folder called `.git`. This is the local repository!
* GitHub hosts a *remote repository* on the cloud which additionally logs the changes to serve as an off-site backup and enable easy sharing
    * *Fetching* checks whether there are any differences between the remote and local repositories without making any changes
    * If there are no changes on the remote repository, *pushing* your code updates the remote repository to match your local repository at its last commit
        * If there are already changes on the remote repository, these conflicts need to be resolved before your code can be pushed. This is common when multiple people are collaborating on the same project, but is extremely rare in our situation where an individual is working alone and using Git/GitHub to track their own changes over time.
    * *Pulling* updates your local repository and project folder to match the remote repository
* The standard Git/GitHub workflow involves making some set of changes within your project folder, committing those changes to your local repository, then pushing them to the remote repository.
    * This archives your changes such that you can go back later and check on what you've done--and revert changes if necessary. (Think of this as analogous to checkpoints in a video game.)
    * GitHub has many more complex features than this. Depending on what direction our work goes, we may explore some of these later in the project. But, these pieces of logging iterative changes by committing and pushing individual commits are sufficient for now.

![git-github-theory](images/git-github-theory.jpeg)
*This schematic illustrates the relationship between the local project folder where you make changes, the local Git repository, and the remote repository hosted on GitHub. Saving (does not involve Git) saves changes within the project folder. Committing logs changes within the local repository (moves from project folder to local repository). Fetching checks whether the remote and local repositories are different. Pushing updates the remote repository to match the local repository (moves from local to remote repository). Pulling updates the local repository to match the remote repository (moves from remote to local repository).*

#### 2.1.1. Why do we use Git?
  * *For the code author:* 
      * Git/GitHub ensures you never lose an important step in your work by overwriting it with a new change, without having to manually maintain different versions of your code. (That is, it averts the phenomenon described in [this comic](https://phdcomics.com/comics.php?f=1531).)
      * Git/GitHub encourages you to think in terms of making individual, discrete updates to your code. This is helpful to keep track of your project development as it becomes more complex.
      * Use of Git/GitHub is a key transferable skill to many professional jobs that involve code or collaborative work, especially in industry, government, and the nonprofit sector.
  * *For collaborators*: 
      * Git/GitHub facilitates sharing code and its revision history together.
      * Git/GitHub ensures that users always have access to the most up-to-date version of your code.
      * Git/GitHub makes it easy for other researchers to "fork" off of your code and continue development in another direction.

#### 2.1.2. Limitations of Git
  * Git/GitHub is not meant as a data storage solution and restricts individual file sizes. **Do not keep data in your repository; this will prevent you from pushing to GitHub.** Your data should be kept in the data folder that you created as part of completing the [creator-computer-literacy](https://github.com/dmhuehol/coding-computers-edsg/blob/main/creator-computer-literacy.md) materials.

### 2.2. Using GitHub Desktop to manage version control
* GitHub Desktop manages all stages of version control: committing, fetching, pushing, pulling, etc.

![github-desktop](images/github-desktop.jpeg)
*Example GitHub Desktop window showing major panels.*

* The Changes panel displays all files in the project folder with changes from the previous commit
* The Difference panel displays changes between the previous commit and current state for a selected file within the Changes panel.
* The Commit panel allows you to make a single commit and add necessary metadata to describe what changed in this commit.
    * The *Summary* is essentially the title for your changes, and it is required to make a commit. By convention, the summary message should be as brief as possible and written in the imperative mood (that is, "Add demo files", rather than "This update is adding demo files").
    * The *Description* allows you to make longer-form prose comments about the changes in the commit. Personally, I like to add a list for each file with changes from the previous commit with a brief description of what changed. These descriptions are often valuable when resuming work on a project after a long pause.
        * The summary and description are always included and visible on your remote repository.
    * Clicking the blue Commit button makes a commit to your local repository
* The button at the top (labeled "Fetch origin" in the screenshot above) may fetch, push, or pull changes to/from the remote repository depending on context. The label will change depending on what operation it is ready to do.
    * In order to push once a commit has been made: 
        * After the commit has been made, the button will change to read "Push origin"
        * Click "Push origin" to push to GitHub

*Link to video: [link](https://drive.google.com/file/d/1S79gFr3qlHGu8T6utf2fPBWW7rI5fCYj/view?usp=sharing). Screen recording of committing and pushing to a remote repository. The video opens by showing the current remote repository on GitHub. I then add a commit summary, description, and click the commit button. Then, I push these changes to the remote repository. The remote repository online has now updated to include the changes from my local repository.*

### 2.3. When should I commit and push?
* There's no hard and fast rule for this!
* The guidelines document includes explicit instructions for when to push changes to your onboarding repository during the first few days of onboarding tasks. This will help you to get in the habit of pushing changes. It will also help to share code when we meet virtually.
* When starting out on our research project, I recommend the following general rules:
    * *Commit and push at least once per day.* It's often best to make this the last thing you do before signing off for the day. Writing the commit description then helps summarize to yourself what you did today, and this may help you identify where to pick things up the next day!
    * *Commit and push when you make a very concrete change that you are about to iterate on.* For example, if you've successfully written some new code and are about to start editing it to make it work better--commit and push the code *before* you start making new changes! This ensures that you don't overwrite anything that is important.
* Remember:
    * There's no penalty for committing and pushing "too often." Err on the side of committing and pushing more frequently, particularly as you get used to Git/GitHub.
    * Your code doesn't have to work when you commit and push it! In fact, writing your commit message can sometimes help to clarify why your code isn't working. I often find that this works as a kind of ["rubber duck debugging"](https://www.youtube.com/shorts/jB085P7ktMc).

### 2.4. Exercises
* Commit and push your changes from the exercises in the previous section. Be sure to include a commit summary and description.


## 3. Authorship and Acknowledgments
This document was written by Daniel Hueholt.




