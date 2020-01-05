#!/usr/bin/env python3

import sys

 
def feat_commit(commit_msg, commit_hash):
    print(commit_msg, commit_hash)
    
def fix_commit(commit_msg, commit_hash):
    print(commit_msg, commit_hash)
    
def chore_commit(commit_msg, commit_hash):
    print(commit_msg, commit_hash)

def main(filename):
    try:
        f = open(filename)
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
        return None
    for line in f:
        commit_hash, commit_message = line.rstrip().split('--HASH--')
        print(line)
        print(commit_hash)
        print(commit_message)
    f.close()

if __name__ == '__main__':
    if len(sys.argv)==2:
        filename = sys.argv[1]
    else:
        filename = 'sample-commits-10'
    main(filename)
