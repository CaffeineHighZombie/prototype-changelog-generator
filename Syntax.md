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
Following are the examples of the commit messages the prototype changelog generator works on \(the examples are based on actual commit messages from [Angular repository's commit history](https://github.com/angular/angular/commits/master) which was used during development and testing\):
### 1. fix
```
fix(ngcc): use the correct identifiers when updating typings files (#34254)

Previously the identifiers used in the typings files were the same as
those used in the source files.

When the typings files and the source files do not match exactly, e.g.
when one of them is flattened, while the other is a deep tree, it is
possible for identifiers to be renamed.

This commit ensures that the correct identifier is used in typings files
when the typings file does not export the same name as the source file.

Fixes https://github.com/angular/ngcc-validation/pull/608

PR Close #34254
```
```
fix(language-service): Proper completions for properties and events (#34445)

This commit fixes autocompletions for properties and events bindings.

The language service will no longer provide bindings like (click) or [id].
Instead, it'll infer the context based on the brackets and provide suggestions
without any brackets.

This fix also adds support for alternative binding syntax such as
`bind-`, `on-`, and `bindon`.

PR closes https://github.com/angular/vscode-ng-language-service/issues/398
PR closes https://github.com/angular/vscode-ng-language-service/issues/474

PR Close #34445
```
### 2. feat
```
feat(language-service): Append symbol type to hover tooltip (#34515)

Now that https://github.com/angular/angular/pull/34177 fixed the `TypeWrapper`
to have a proper name, we have the information needed to show the type
name in a hover tooltip.

PR Close #34515
```
```
feat(ivy): throw compilation error when providing undecorated classes (#34460)

Adds a compilation error if the consumer tries to pass in an undecorated class into the `providers` of an `NgModule`, or the `providers`/`viewProviders` arrays of a `Directive`/`Component`.

PR Close #34460
```
### 3. chore
```
chore: add products.ts file on getting started page (#34301)

in the getting started page (first tutorial) file products.ts which was not shown and was only present in the StackBlitz examples. So added a refrence that it is present in the example and also added a note that examples may carry filenames not present please look at StackBliz examples for details

Fixes #34291

PR Close #34301
```
```
chore: add products.ts file on getting started page (#34301)

in the getting started page (first tutorial) file products.ts which was not shown and was only present in the StackBlitz examples. So added a refrence that it is present in the example and also added a note that examples may carry filenames not present please look at StackBliz examples for details

Fixes #34291

PR Close #34301
```
