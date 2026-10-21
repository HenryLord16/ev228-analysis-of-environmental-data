# Software Development Principles

There are several general principles from software engineering that are beneficial for applications in environmental data science research.
These are ones which are especially important in my experience and are a focus in this class.

## 1. Iterative refinement
* Iterative refinement refers to aiming for continuous improvement based on testing, rather than attempting to go from design to deployment in a single step
* This takes the pressure off of attempting to write “perfect” code, which is unattainable, and emphasizes useful real-world feedback (usually from error messages!) over attempting to pre-plan for every eventuality
* Always start with a *pretotype*—the minimum example that will allow you to check that your idea is on the right track—rather than attempting to build everything in one go.
    * (This document is an example of a pretotype! I wanted to write something much more detailed about each of these principles, but decided the bullet-point version would allow me to see if this was a useful concept for a reading.)

## 2. Version control
* Version control refers to any system that keeps track of different versions of a piece of software as you develop it
* In our class, we use GitHub as a version control system
* Version control makes it impossible to lose your work, facilitates reversing changes that prove unfruitful, aids in reproducibility, and makes synchronous collaborative work on the same piece of software possible
* Experience with version control is vital in careers where software design involves direct teamwork, particularly in corporations, nonprofits, and many federal labs

## 3. Documentation
* Documentation is natural language text that accompanies computer code (in-line comments and docstrings within code, READMEs in your GitHub repository) or datasets
* The computer is not your only audience--you are writing for other people who may use your code, including yourself in the future!
* When publishing a result, the workflow to reproduce all results should always be completely documented
### 3a. Documentation guidelines
* *Docstrings:* Programs, including each function within a module, should always have a docstring.
* *In-line comments:* As you begin to learn code, it is often helpful to document each line with a comment to help you check your understanding. As you become more comfortable with code, you will use comments more sparingly.
* *READMEs:* In professional practice, readme formats are different from enterprise to enterprise. In our class, READMEs should always include a code index (list of each program and brief description of what it does) and a Generative AI Statement.

## 4. Modularity
* Modularity describes writing code in discrete, general functions that can be recombined for different purposes
* Results in more thoughtful software design and facilitates more complex tasks that involve chaining different operations together
* Often yields much more efficient code which is easier for others to use when compared to a scripting approach
* When code is intended to serve multiple purposes, modular code is much easier to document than a script

## 5. Style
* There are styles for code to codify practice, similar to how there are style guides for written natural language (e.g., MLA, APA, Chicago).
* Style guides describe conventions for everything from variable names to the number of spaces in an indent
* In industry, [PEP8](https://peps.python.org/pep-0008/) is a commonly-used standard for Python code. (We do not use this in EV228, but it is linked in case it is of interest.)
### 5a. Style guidelines
* Variables should have descriptive names, i.e., names should provide information about their contents.
    * For example, in `ic_world`, we named the variable containing the first stanza `stanza_1` rather than `variable1` or `x`
    * It is acceptable for variables to be fairly long: in the context of this course, I would rather variable names be long and descriptive than short and inscrutable (i.e., `stanza_1` is better than `sz1`)
* Files should have descriptive names, i.e., names that provide information about their contents.
    * For example, we used the name `ic_world` rather than `day1_program`
* Extended written prose in documentation (docstrings and readmes) should be thoughtful and expressed clearly (including basic proofreading).
* Documentation should be kept current in code: make sure that when you change your code, you change your documentation as well!
* I may update this list as the course continues

## 6. Optimization (introduced in Week 2)
* Optimization refers to improving the speed of code
* Tic/toc profiling — using paired tic/toc commands (which time the duration of sections of code) to check performance of different parts of software
* Bottlenecks — operations that disproportionately impact overall performance of a piece of software. Common bottlenecks include:
    * Nested loops (i.e., an operation on each point of a gridded dataset that requires looping through latitude, longitude, and time)
    * Data in/out commands unnecessarily placed within loops
    * Looping forwards through data structures that are recreated on each iteration
* Be thoughtful about when to carry out a calculation once and save a derived dataset as opposed to recalculating a quantity and holding it in memory
* Don’t overly optimize code—it is important to be aware of when optimization itself can become a bottleneck!

## 7. Review (introduced in Week 2)
* Code review involves sharing code with another person who tests the code and provide feedback. This serves a similar purpose as peer review in any English writing course.
* Code review helps to identify improvements in the code itself, silent bugs, and gaps in documentation
* Review is important even when your code is in a partially-completed state!
* Feedback from other people is a key part of iterative refinement.
