# creator-computer-literacy
In becoming a data science researcher, we shift from using computers as a *consumer* to using them as a *creator*. When you use a computer, tablet, or smartphone as a consumer, there are thousands of highly-trained (and highly-paid!) software engineers, designers, hardware engineers, and other professionals whose jobs are to keep you from encountering friction in the user experience.

![xkcd 1349](/images/xkcd-1349.png)  
*Credit: [xkcd 1349](xkcd.com/1349/), licensed under a Creative Commons Attribution-NonCommercial 2.5 License.*

When you use a computer as a creator, there is no longer anyone to protect you from the whims of the sand! Thus, learning *computer literacy skills*--fundamental knowledge about how computers operate and are structured--is a necessary first step.  

The duck-exclamation symbol 🦆:heavy_exclamation_mark: denotes items that are key parts of "creator" computer literacy that are very different from how you interact with technology as a "consumer." These are marked because I've found them to be common pain points for new researchers as they shift from consumer to creator.  

Depending on your prior experience, much or all of this material may be review. That's okay: it will still help to refresh your memory, and it's important to build a common language from the start.

## Computer literacy
### CL.1 - Computers as a physical object
* A computer has a finite amount of *storage*, that is, space to hold data.
  * The hardware that contains data in a computer is called a "drive."
  * Storage is measured in a unit called "bytes." A typical laptop from the last five years will have between 128 gigabytes (GB; equal to 1 billion bytes) and 1 terabyte (TB; equal to 1 trillion bytes) of storage on its drive.
  * Storage is usually the major constraint for our type of projects. Large environmental datasets are often multiple terabytes, or even petabytes in scale!
  * *External drives* can be physically connected to your computer to provide additional storage. Our group has external drives which can be used to support research purposes.  
* A computer has a finite amount of *computational power* (or "*compute*")--the hardware that allows the computer to carry out operations.
* In data science, we often link to remote resources (for example, when downloading data) to access more storage and compute than we have available on our machines.
* **All computing resources exist in the real world somewhere, and computing resources are always finite.**
##### CL.1 Exercises
* Look up the total storage and available storage on the computer you use for research. If you don't know how to do this, review Section CL.4 of this document and then search the Internet for instructions for how to check storage space on your computer.

### CL.2 - File and folder structure
* Information is stored on computers in discrete *files*.
  * Example: a Word document is a file
  * Example: data is usually contained in one or more files
* These files are contained in *folders*. Folders are also referred to as *directories*.  
* A *path* uniquely describes the location of a file or folder within a sequence of other folders. The folders are separated by forward slashes ("/").
  * For example, `/Users/joharding/Data/toto_obs_19960510.dat` is a path to a file named `toto_obs_19960510.dat` located within the `Data` folder inside the `joharding` folder in the `Users` folder.
  * *Windows works differently:* On Windows, paths are separated by backslashes ("\\").
  * The `*` symbol denotes a wildcard that will match any character. For example, `/Users/joharding/Data/toto*` denotes any file starting in `toto` located within the `Data` folder inside the `joharding` folder in the `Users` folder.
* Your computer's *file system* organizes all of the data on your computer into different directories.
* A folder within another folder is called a *subfolder* or *subdirectory*.
* The *root directory* is the top folder in the file system: that is, all other folders are subfolders of the root directory.
  * On a Mac or Linux system, the root directory is denoted as `/`.
  * *Windows works differently:* On Windows, the root directory is usually denoted as `C:\`.
* The *user directory* is the top folder within your user account on a computer. All other folders within your user account are subfolders of the user directory.
  * On a Mac or Linux system, the user directory is found at `/Users/[username]`, where `[username]` is your username. For example, `/Users/joharding/` would be the user directory for a user named `joharding`.
  * *Windows works differently:* On Windows, the user directory is usually, but not always, denoted as `C:\Users\[username]\`.
* When working with a computer as a creator, it is important to think in terms of files having a specific location on your computer, familiarizing yourself with those locations, and keeping track of the folders where you store data and code. In particular, accessing data when writing code requires knowing the path where the data is stored.
  * 🦆:heavy_exclamation_mark: This is very different than how consumer interactions with computers typically work: mobile/tablet apps (e.g., TikTok, Snapchat) rarely involve continuity in workflow and cloud systems (e.g., Google Drive) queue most recently used items.

#### CL.2.1 - Navigating file structure
![finder-example](/images/finder-example.png)  
*Example of a Finder window showing different folders. Each folder in the left column contains code and documentation for a different project. The files and folders for a project named coding-computers-edsg is displayed in the right column. The full path for the folder is displayed at the bottom, with `>` symbols between the directories.*
* On a Mac, use the Finder to browse your file system.
* New folders can be created by selecting "New Folder" from the "File" menu within a Finder window.
* *Windows works differently:* On Windows, the File Explorer is the program used to browse the file system. See Microsoft's documentation [here](https://support.microsoft.com/en-us/windows/file-explorer-in-windows-ef370130-1cca-9dc5-e0df-2f7416fe1cb1) for more information.
##### CL.2.1 Exercises
* Create a folder called `Data` within your user directory on your computer, and take note of the path. **Use this to store data throughout the Block.**

#### CL.2.2 - File formats
* Files have a format that tells programs how to interact with them
* The format is denoted by a set of numbers, symbols, and letters after the `.` symbol in the filename
    * For example, the file `toto_obs_19960510.dat` is of the `.dat` file format
* Common file formats include: `.pdf` ("Portable Document Format," usually for typeset documents), `.docx` (Microsoft Word), `.pages` (Apple Pages), `.txt` (plain text without formatting), `.HEIC` (iPhone photos)
* `.py` files denote Python programs

### CL.3 - Locations and saving
* *Local* refers to files and folders located physically on your computer or an external drive physically attached to it. Local locations are always accessible.
* *Remote* files and folders are located physically elsewhere and accessible through networking. Accessing remote locations requires an Internet signal.
* Moving data from remote to local is called *downloading*, while moving data from local to remote is *uploading*. Obtaining data for research generally involves searching the Web (see CL.4) to find the data, then downloading it to your local machine.
#### CL.3.1 - Local
* Local locations are accessible using Finder (Mac) or File Explorer (Windows); see CL.2.1
* Most of our data and code will be stored locally.
#### CL.3.2 - Cloud
* *Cloud* locations refer to remote locations used for storage that are distributed across many individual remote servers (computers specialized to store and provide data).
* There are many services that provide cloud storage, including: Google Drive, Apple iCloud, Microsoft OneDrive, and Proton Drive.
* Google Drive is accessible through your web browser; see CL.4.
* Cloud storage makes it easy to share files remotely and is hard to physically destroy: If campus is obliterated in a wildfire, for example, all of our local storage is gone but the cloud will be unaffected. However, cloud storage is slow to access relative to local storage, expensive in large amounts, and not reliably private (frequent concerns include: changes in legal terms, use for corporate language model training, government surveillance).
#### CL.3.2 - Saving
* *Saving* a file refers to the process of storing a file at a location, or storing the changes to an already-existing file.
* Unsaved changes are lost when the open program is closed--including if it is closed accidentally, or violently (e.g., a power surge, crash).
* 🦆:heavy_exclamation_mark: Deliberately saving files is usually necessary when working locally. Online systems for consumers typically save changes automatically (e.g., Google Docs)--so it's important to get in the habit of saving manually!
### CL.3.3 - Odd rules of file systems
* File systems have many odd rules that can often trip up new users. Here are a few that are worth being aware of as you begin to intentionally choose file and folder names.
* 🦆:heavy_exclamation_mark: Computers care a *lot* about exact filenames. `/Users/joharding/` and `/Users/johording/` look very similar to us, but are completely different to a computer. When you get an error while coding, it is often due to a small error in the command you entered.
* 🦆:heavy_exclamation_mark: Due to intricacies of how computers developed over time, they retain many arcane rules for acceptable file and folder names. A few general rules that are often surprising: 
  * File and folder names are case sensitive: that is, `/Users/Joharding/` is different from `/Users/joharding/`. For this reason, it is often recommended to use all lowercase letters in file and folder names.
  * Space characters are almost never desirable in filenames. Use the `_` or `-` symbols instead of spaces. For example, instead of calling a folder `data analysis`, it should be named `data_analysis` or `data-analysis`. Otherwise, it may be difficult to access items within this folder later on.
  * Never put a space at the end of a filename. For example, a folder name of `data ` should never be used; it should be named `data` instead. We often have a habit of putting a space at the end due to the presence of autocomplete on smartphones and tablets, where pressing the space key triggers the most likely suggestion. But extraneous space at the end of a folder often renders a path inaccessible when writing code.

### CL.4 - The Internet and information retrieval
* The Web is the worldwide system for sharing information over the Internet.
* Individual *pages* on a *website* are located at an *internet address*, analogous to how local files and folders are located at specific paths.
   * For example, our `creator-computer-literacy` page is located on the website `github.com` accessible with the complete address `https://github.com/dmhuehol/ev228-analysis-of-environmental-data/blob/main/coding-ide-iterating-github.md`
* *Web browsers* allow you to visit different websites. Common web browsers are below.
   * [Firefox](https://www.firefox.com/en-US/)
   * [Google Chrome](https://www.google.com/chrome/)
   * [Microsoft Edge](https://www.microsoft.com/en-us/edge/)
   * [Safari](https://www.apple.com/safari/) - included by default on Macs
   * [Vivaldi](https://vivaldi.com)
* You can visit a specific website by typing its address into the address bar in your web browser. An example is shown below.
![address-bar](/images/address-bar.png)  
*Example of a Web browser (Vivaldi) open to a specific website--here, the National Hurricane Center. The address is the highlighted text at the top of the screen inside the address bar.*
* *Search engines* refer to tools that are designed for retrieving information on the Web related to a specific query. Search engines usually return a block of synthetic text ("AI Overview") generated in response to your query followed by a list of links to websites with relevant information. Common search engines are below. Search engines marked with the 🐈‍⬛ symbol allow the synthetic text response to be disabled.
   *  [Google](https://www.google.com)
   *  [Startpage](https://www.startpage.com) - 🐈‍⬛
   *  [Brave](https://search.brave.com) - 🐈‍⬛
   *  [Ecosia](https://www.ecosia.org) - 🐈‍⬛
   *  [Bing](https://www.bing.com/) - 🐈‍⬛
* Some search engines may serve a specific purpose, for example, searching images.
   * [Google Images](https://www.google.com/imghp) - search images
   * [Wikimedia Commons Search](https://commons.wikimedia.org/wiki/Special:Search) - search freely-available images
   * [Google Scholar](https://scholar.google.com) - search academic literature
   * [Colorado College Library Search](https://www.coloradocollege.edu/library/) - search academic holdings of the CC library
* Other information retrieval services operate on a more abstract level. For example, [ResearchRabbit](https://www.researchrabbit.ai) uses a graph neural network model to retrieve relevant academic references by tracing citations, authors, and concepts between papers.
* Chatbots (e.g., ChatGPT, Claude) generate plausible text based on the distribution of strings in their training data. *This function is not the same as information retrieval.*
  * If you are interested, watch Emily Bender and Chirag Shah's video "Situating Search" (start-4:05) to learn more about distinctions between synthetic text generation and information retrieval. [link](https://www.youtube.com/watch?v=VY1GHbU_FYs)
  * Plausible text in present-generation chatbots is often incorrect or misleading (for example, 35% frequency on average for news information from leading chatbots in 2025 [link](https://www.newsguardtech.com/wp-content/uploads/2025/09/August-2025-One-Year-Progress-Report-3.pdf); nearly half of environmental news stories [link](doi.org/10.1371/journal.pclm.0000799)) but presented as authoritative instead of as one potential source among many.
* 🦆:heavy_exclamation_mark: Data science research extensively involves retrieving information to find data, diagnose problems, and contextualize a topic. This is in contrast to most consumer interactions with technology, which involve an algorithmically-mediated feed of information with minimal user agency in the process of obtaining information (for example, the TikTok "For You" page or the Instagram feed).
##### CL.4 Exercises
* Use Google Scholar to find the paper titled: "The community earth system model: a framework for collaborative research"
* Use the CC Library Search to find this same paper
* Use a search engine you have not used before to search some topic that you know well. How would you rate the results? Why?

### CL.5 - Operating System (OS)
* Your OS refers to the system software that manages the hardware, programs, and their interactions on your computer.
* On desktop/laptop computers, there are two major classes of OS: Microsoft Windows and Unix-based systems (macOS and Linux).
* While Windows is most commonly used globally, Unix-based systems--particularly macOS--are much more widely used in research. This is because Unix-based systems are nearly exclusively used for the large-scale systems that underpin data hosting and networking infrastructure.
* Windows and Unix-based systems have subtle differences between how they interact with Python code that make it difficult to port code and environments between the two systems.

### CL.6 - Shell/Terminal
* The shell provides a text-based method of accessing the file system. It allows more control over operations than the Finder.
* At any given state, the shell has access to a single path which we call the *working directory*. When you open a new shell, the working directory will typically be your user directory.
* Interacting with the shell involves typing commands and entering them by pressing "Enter" on your keyboard.
#### CL.6.1 - Shell commands
##### CL.6.1.1 - Fundamentals
Three commands are fundamental to moving around the file system in the shell:
   * `pwd` -- "print working directory", prints the path of the current directory (think of this as "where am I?")
   * `ls` -- "list", prints the contents of the working directory (think of this as "what's here?")
   * `cd [path]` -- "change directory", change to the location specified by `[path]` (think of this as "go somewhere else")
      * `cd ..` moves up one folder. `..` can be chained, for example, `cd ../..` moves up two folders.
      * `cd` on its own will change directory to the user directory
      * Commands from within the working directory inherit the path of the working directory. For example, if your working directory is `/Users/joharding/` and you want to change directory into `/Users/joharding/Data/`, you can simply type `cd Data`. This will be interpreted the same as `cd /Users/joharding/Data/`, because the working directory path `/Users/joharding/` is assumed.
##### CL.6.1.2 - Other frequent commands
Some other commands are also frequently useful:
   * `mkdir [path]` -- "make directory", makes a new directory at the location specified by `[path]`
   * `touch [path/filename]` -- make a new empty file called `[filename]` at the location specified by `[path]`
   * `cat [path/filename]` -- print the contents of `[filename]` at the location specified by `[path]`
   * `open [path/filename]` -- open the file called `[filename]` at the location specified by `[path]` using the system default program for that type of file
   * `rm [filename]` -- "remove", deletes the file at `[filename]`. **WARNING: Deletions using `rm` cannot be undone. Use this carefully!**
* 🦆:heavy_exclamation_mark: The shell is how we run Python code and is often necessary to download large datasets. This is the final step of the creator computer literacy: as a consumer, you will likely never interact with the shell!
* *Windows works differently:* On Windows, the equivalent to the shell is called the "Command Line". While it may look similar, the underlying software and hardware engineering is *completely different*. This is a major reason why it is difficult to move code between Windows and Unix-based systems. Thus, it's best to choose just one to work in (although it is not impossible to work around this). For the reasons described in CL.5, most researchers (including myself) choose Unix-based systems.
   * If using Windows, watch [this video](https://www.youtube.com/watch?v=QBWX_4ho8D4) for a tutorial of using the Windows shell.
##### CL.6.2 Exercises
These exercises are written with Unix-based systems in mind. If using Windows, substitute their equivalent (watch the video above for help).

Remember: You will get comfortable with the shell with practice. It will feel unfamiliar--and then suddenly it will be second nature!
* Open your shell. What is the working directory?
* Use `cd` and `ls` to navigate to your Data directory from CL.2.1
* Use `mkdir` to make a new directory called `test` within your Data directory
* Use `touch` to make a new empty file called `test.txt`
* Use `ls` to verify that the file exists

### CL.7 - Shortcut keys
* Shortcut keys refer to certain key combinations that trigger a more complex behavior when held. On macOS, they usually involve the command (⌘), option (⌥), or control (^) keys on your keyboard.
    * *Windows works differently:* On Windows, shortcut keys usually involve the control key, alt key, or windows key, respectively.
* Shortcuts are written by the symbol of the key with a + symbol between them to denote the keys that must be held. To trigger a shortcut, the keys must be pressed in order and held.
##### CL.7.1 Exercises
* In all web browsers, the command ⌘+T opens a new tab and ⌘+W closes one. Use these shortcuts to open and close a tab.
* When typing in the shell, the up-arrow key repeats the previous command that you typed. Use the up-arrow to scroll through your command history.
* When typing in the shell, ⌥+left or right arrow moves backward/forward one word at a time. Test this shortcut out.
* When typing in the shell, ⌘+left or right arrow moves to the start or end of the entire line. Test this shortcut out.
* The shortcut ^+⌘+spacebar opens the screen to type emojis in almost any program. Open the Notes app and type a parrot emoji in a new note.

### CL.8 - 🦆:heavy_exclamation_mark: A general principle: Read what is in front of you :)
* Because the experience of using modern technology as a consumer is relatively frictionless, it is very easy to get in the habit of assuming that any friction is unsolvable and any error messages produced are gibberish. But this is not the case!
* If the computer isn't doing what you want (particularly in the shell) take a closer look at what the computer is saying to you, and what you've typed.
* Can you express what you did to get into the current situation, and what the error is telling you?

### CL.9 - Synthesis exercises
That's it! 🎉 The following exercises helps tie some of these skills together. They are deliberately written in natural language as practice interpreting written notes. These exercises are written with Unix-based systems in mind. If using Windows, substitute their equivalent (watch the video linked in CL.6.2 for help).

#### CL.9.1 ☁️
Search Wikimedia Commons for a cloud picture that you like. Save the photo to the `test` folder in your `Data` folder. Open the shell and use the commands to navigate to this directory, then open the image.

#### CL.9.2 Applications
The Applications folder is located within the root directory. Use the shell to navigate to this folder, and use `ls` to view all of the installed programs. Look up one program that you are not familiar with online to see what it does.

#### CL.9.3 Text edit / Reading what is in front of you
Open your terminal and navigate to the `test` folder in your `Data` folder. The command `nano [filename]` opens a simple text editor inside the command line. Use `nano` to open the blank `test.txt` file that you made in CL.6.1. Type any text that you want--I suggest "The five boxing wizards jump quickly." With `nano` open, the bottom of the screen will display shortcut keys for various commands. Use the shortcut for "Exit", then follow the prompt to "Save modified buffer" to save your changes. Use `cat` to print the change to your shell screen.

### Authorship and Acknowledgments
This document was written by Daniel Hueholt.




