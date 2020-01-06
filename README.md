# Prototype Changelog Generator
Prototype changelog generator leveraging git commit messages.
## Instructions for environment setup 
### Creating and setting up python virtual environment with required python modules
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## Instructions for running the tool
Running the tool with -h / --help option will list all the current available options in the tool. 
```bash
$ ./changelog-generator.py -h
```
Running the tool without any options will generate CHANGELOG.md with commit history spanning from the first commit to current HEAD of the active branch. The default name of the version will be "1.0.0" if none given, else version name given via option -v / --version will be used.
```bash
$ ./changelog-generator.py
```
```bash
$ ./changelog-generator.py --version 2.0.0
```
To create changelog upto a commit in the current active branch use -e / --end option
```bash
$ ./changelog-generator.py --end 989a977 
```
To create changelog from a commit to current HEAD in the current active branch use -s / --start option
```bash
$ ./changelog-generator.py --start 989a977 
```
To create changelog upto between two commits in the current active branch combine -e / --end and -s / --start option
```bash
$ ./changelog-generator.py --start d6c61c8 --end 989a977 
```
To create changelog from a sample commit file for validation or debugging purposes use -f / --filename option
```bash
$ ./changelog-generator.py --filename sample-commit-files/sample-commits-10
```
## Current functionality of the tool
* Interface directly with the git commit
* Create changelog based on the git commit messages
* Automatic Versioning
* 

## Feature Roadmap
* Refactor code. Mostly to improve modularity and readability.
* Interactive git rebase within the tool to help with incorrectly formatted commits
* Automatic Versioning
* 

## Known Issues
* If the proper commit version is not given the tool fails catastrophically
* 

## Reasons for Choosing Python for Implementing this tool
* The language I am confortable with
* Good support for git input with gitpython, cli tool
* 

## The approach to the assessment
* Research on the various forms of changelog by digging through various repositories and projects download page.
* Reading up on the different commit formats such Conventional Commits, Angular Convention, gitmoji to analyse and choose a syntax to develop the tool on. 
* Choosing a subset of the syntax and writing [SYNTAX.md](./SYNTAX.md) to codify it.
* Getting a project that follows . In my case it was Angular project. Cloned it in on my machine and generated various types and sizes of sample commits from it.
    * Sample commits of various were generated with -n and --skip options. The option --format option was used to format it as "%H--HASH--%s" to create delimited formated commit for our specific module and usage.
* Designing and developing Parser module which would read in commits (provided to it as a files based on sample commits from above) and generate hierarchical hashmap (python dictionary) of the changelog
    * Testing against the couple of sample commits generated from the angular project with output visualized on stdout
* Designing and developing Markdown Writer module, and combining it with Parser module to write CHANGELOG.md based on the changelog in the form of hierarchical hashmap from the Parser module
    * Testing against the couple of sample commits generated from the angular project with output in the CHANGELOG.md
* Designing and developing Git Interface module which would talk the git repository to extract commits (and in future couple of more actions like rebase and etc.). Integrating with Parser and Markdown Write module.
* Designing and developing CLI module with argparser to read in arguments passed to the program from the cli and enable more options with tool usage. Integrating with main core tool.


