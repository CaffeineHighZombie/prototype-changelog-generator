# Syntax for changelog generator
The Syntax is a subset of and is heavily based on [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) and [the Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

## Structure of Commit Message
The commit message should be structured as follows:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
## Structural Elements of Commit Message
The commit contains the following structural elements:
1. fix: a commit of the type fix patches a bug in your codebase (this correlates with PATCH in semantic versioning).
2. feat: a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in semantic versioning).
3. chore: a commit of the type chore involves no production code change and deals with updating grunt tasks such as:
    * implementation (of an existing feature, which doesn't involve a fix)
    * configuration (like the .gitignore or .gitattributes)
    * private internal methods

## Examples of Commit Messages
Following are the examples of the commit messages the prototype changelog generator works on \(the examples are actual commit messages from [Angular repository's commit history](https://github.com/angular/angular/commits/master) which was used during development and testing\):

