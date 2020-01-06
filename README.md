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
* Ability to interface directly with the git repo and commit object of current git repository.
* Ability to work on both git commits directly and sample commit files.
* Able to generate changelog for all, starting from, ending at or between different commits. 
* Changelog appended in chronological order to the existing one.
* Tool being accessible as CLI with various options passed as command line arguments.

## Feature Roadmap
* Interactive git rebase within the tool to help with incorrectly formatted commits or other syntactic violations as such.
* Refactor code. Mostly to improve modularity and readability.
* More options to be able to choose which branch to generate release and changelog on.
* Automatic versioning (if none provided) probably based on versioning scheme provided via a configuration file.
* Syntax itself being ingested as a configuration rather than coded in the tool. Probably even something simple as a hashmap (json file) with key-value pair of message element and actions.
* Provide harness / endpoints to be able to integrate into CI/CD systems say Jenkins build system for better deployment.

## Known Issues
* Have to manually keep track of the commits and versioning for each release for which changelog had been generated.
* In case of syntax violations have to manually rebase the commits based on the information provided by the tool generated Syntax-Violation file and the process can resume only after the corrections.

## Reasons for choosing python for tool implementation
* To start with it is a language I am more confortable with for developing tools and scripts.
* It has good string sequence methods which itself could be used directly to develop parser module.
* Has support for various modules such as GitDB, GitPython, etc. which could be used to inferace with git repo and commit objects directly, and thereby allowing greater flexibility to with tool development.
* It also has good argparser module which help quickly prototype the tool and cli interface for it.

## The approach to the assessment
* Research on the various forms of changelog by digging through various repositories and projects download page.
* Reading up on the different commit formats such Conventional Commits, Angular Convention, gitmoji to analyse and choose a syntax to develop the tool on. 
* Choosing a subset of the syntax and writing [SYNTAX.md](./SYNTAX.md) to codify it.
* Getting a project that follows chosen syntax. In my case it was Angular project. Cloned it in on my machine and generated various types and sizes of sample commits from it.
    * Sample commits of various were generated with -n and --skip options. The option --format option was used to format it as "%H--HASH--%s" to create delimited formated commit for our specific module and usage.
* Designing and developing Parser module which would read in commits (provided to it initially as a files based on sample commits from above) and generate nested data containers (list of tuples) of the parsed changelog messages.
    * Testing against the couple of sample commits generated from the angular project with output visualized on stdout
* Designing and developing Markdown Writer module, and combining it with Parser module to write CHANGELOG.md based on the changelog in the form of nested data containers from the Parser module.
    * Testing against the couple of sample commits generated from the angular project with output in the CHANGELOG.md
* Designing and developing Git Interface module which would talk the git repository to extract commits (and in future couple of more actions like rebase and etc.). Integrating with Parser and Markdown Write module.
* Designing and developing CLI module with argparser to read in arguments passed to the program from the cli and enable more options with tool usage. Integrating with main core tool.


