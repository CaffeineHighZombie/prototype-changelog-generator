# Prototype Changelog Generator
Prototype changelog generator leveraging git commit messages.
## Build/Configure Instructions
### Creating and setting up python virtual environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## Tool running instructions
### Running the changelog generator CLI
```bash
$ changelog-generator.py
```
## Current functionality of the tool
* Interface directly with the git commit
* Create changelog based on the git commit messages
* Automatic Versioning
* 

## Feature Roadmap
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
* Choosing a subset of the syntax and writing SYNTAX.md to codify it.
* Getting a project that follows . In my case it was Angular project. Cloned it in on my machine and generated various types and sizes of sample commits from it.
* Designing and developing Parser module which would read in commits (provided to it as a files based on sample commits from above) and generate hierarchical hashmap (python dictionary) of the changelog
    * Testing against the couple of sample commits generated from the angular project with output visualized on stdout
* Designing and developing Markdown Writer module, and combining it with Parser module to write CHANGELOG.md based on the changelog in the form of hierarchical hashmap from the Parser module
    * Testing against the couple of sample commits generated from the angular project with output in the CHANGELOG.d
* Designing and developing Git Interface module which would talk the git repository to extract commits (and in future couple of more actions like rebase and etc.). Integrating with Parser and Markdown Write module.
* Designing and developing CLI module with argparser to read in arguments passed to the program from the cli and enable more options with tool usage. Integrating with main core tool.


