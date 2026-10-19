# Setup Day! 🥳

* Terminal reminder
* If checking out laptop, ask to be made an admin (they will do this if it is for a class or thesis)

## 1. Conda and Python
* Open Terminal
* Check if conda is already installed `conda -V`
* If that returns "zsh: command not found: conda" (overwhelmingly likely) that means that we will now install conda
* Open a web browser and search for "conda install"
* Ignore the AI Overview
* Click the first link
* Select "install miniconda"
* Select "skip to download" (it's in the small text, annoying)
* Click "Graphical installer" under "Miniconda"
* Open the package that downloads and follow the instructions
* Run conda -V again, you'll get a version number. Skip to here if you already had conda.
* Run python -V, you'll get a version number.

### 1a. Make environment
* Run command `conda create -n ev228 python=3.12`
* Press `y` when prompted
* `conda activate ev228`
* You can now see that this is activated

## 2. VSCode
* Open your browser and search for "vscode install"
* Ignore the AI Overview. Click the first link.
* Select Download
* Open the package and follow the instructions.
* Drag VSCode to Applications
* Open VSCode
* Add to Dock (options, keep in dock) or Desktop 

## 3. GitHub
* Open your browser and search for "github desktop install"
* Drag GitHub Desktop to Applications
* Make a GitHub account if you do not have one already
* Sign in to your GitHub account
* If prompted to "Move and Restart" select "Move and Restart"

## 4. Project repository
* Create new repository on local drive
* Name it something relevant; EV228 is a good name
* Select initialize with README
* Note path of repository
* Create repository
* Publish repository
* Go to your browser and bring up your github page
* Settings
* Collaborators
* Add `dmhuehol`
* Open in Visual Studio Code
* Allow if prompted
### 4a. "Hello world!" and practice push
#### "Hello world!"
* Select new file
* Call the file `hello.py` or `Hello.py`
* Create file
* Click button to bring up terminal
* `print("Hello world!")`
* Save (file-save or command-S)
* Run code with "python Hello.py"
* Change string to anything of your choice; save it; run it again
#### Practice push
* Pull up GitHub Desktop
