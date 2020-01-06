#!/usr/bin/env python3

import os
import datetime
import argparse
 
# def feat_commit(commit_msg, commit_hash):
#     print(commit_msg, commit_hash)
    
# def fix_commit(commit_msg, commit_hash):
#     print(commit_msg, commit_hash)
    
# def chore_commit(commit_msg, commit_hash):
#     print(commit_msg, commit_hash)

def main(args):
    commit_information = list()
    if args.filename:
        filename = args.filename
        try:
            f = open(filename)
        except FileNotFoundError as e:
            print("FileNotFoundError: ", e)
            return None
        for line in f:
            commit_hash, commit_message = line.rstrip().split('--HASH--')
            commit_information.append((commit_hash, commit_message))
        f.close()
    else:
        return None

    ## Declaring list to hold each of the feat, fix, chore and syntax exception commits
    feat_list = list()
    fix_list = list()
    chore_list = list()
    exception_list = list()
    
    ## Grunt Commit Message. This will not be part of the changelog and also, won't to
    ## syntax violations
    grunt_messages = ('refactor', 'docs')

    for commit_hash, commit_message in commit_information:
        if commit_message.startswith('feat:'):
            feat_string = '* {} ({})'.format(commit_message.replace('feat:', '', 1), commit_hash[:7])
            feat_list.append(feat_string)
        elif commit_message.startswith('fix:'):
            fix_string = '* {} ({})'.format(commit_message.replace('fix:', '', 1), commit_hash[:7])
            fix_list.append(fix_string)
        elif commit_message.startswith('chore:'):
            chore_string = '* {} ({})'.format(commit_message.replace('chore:', '', 1), commit_hash[:7])
            chore_list.append(chore_string)
        elif commit_message.startswith(grunt_messages):
            pass
        else:
            exception_string = 'Commit Hash: {} | Subject: {}'.format(commit_hash, commit_message)
            exception_list.append(exception_string)

    ## Checking to see if there are any syntax violating commits for the current changelog
    ## if so, then writing it to a reference file with commit hash and subject for the 
    ## relase manage to git rebase and squah them. Else, writing the changelog.
    if len(exception_list) != 0:
        with open('Syntax-Violations', 'w') as filehand:
            for line in exception_list:
                filehand.write(line + os.linesep)
    # else:
    ## Checking if the CHANGELOG.md exists. If so, then temporarily rename it
    ## write the entry for each of the feat, fix and chore, and then append earlier
    ## CHANGELOG text now in a temp file into it and clean up. Else, write completly 
    ## new Changelog entry
    if os.path.isfile('CHANGELOG.md'):
        os.rename('CHANGELOG.md', 'TEMP.md')
    changelog_filehand = open('CHANGELOG.md', 'w')
    version_number = "1.0.0"
    current_datetime = datetime.datetime.now()
    ## Writing current version number and date of the version creation
    changelog_filehand.write('# {} ({})'.format(version_number, current_datetime.strftime('%Y-%m-%d')) + os.linesep)
    
    if len(fix_list) > 0:
        changelog_filehand.write('### Bug Fixes' + os.linesep)
        for line in fix_list:
            changelog_filehand.write(line + os.linesep)

    if len(feat_list) > 0:
        changelog_filehand.write('### Features' + os.linesep)
        for line in feat_list:
            changelog_filehand.write(line + os.linesep)

    if len(chore_list) > 0:
        changelog_filehand.write('### Improvements' + os.linesep)
        for line in chore_list:
            changelog_filehand.write(line + os.linesep)

    if os.path.isfile('TEMP.md'):
        with open('TEMP.md') as filehand:
            for line in filehand:
                changelog_filehand.write(line)
        os.remove('TEMP.md')
    
    changelog_filehand.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prototype Changelog Generator')
    parser.add_argument('-f', '--filename', help='Filename of the commit file (For debugging purpose)')
    parser.add_argument('-v', '--version', help='Version of the current build. Default "1.0.0"')
    parser.add_argument('-s', '--start', help='Hash of the first commit for the current build. If none provided very first commit of the repo will be default.')
    parser.add_argument('-e', '--end', help='Hash of the last commit for the current build. If none provided very last commit of the repo will be default.')
    args = parser.parse_args()
    main(args)
