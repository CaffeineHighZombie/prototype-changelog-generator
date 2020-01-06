get_ipython().run_line_magic('logstart', '05-01-20.py append')
f = open('sample-commits-10')
for line in f:
    print(line)
    type(line)
    
for line in f:
    print(line)
    type(line)
    
f = open('sample-commits-10')
for line in f:
    print(line)
    type(line)
    
for line in f:
    commit_hash, commit_message = line.split('--HASH--')
    print(line)
    print(commit_hash)
    print(commit_message)
    
f = open('sample-commits-10')
for line in f:
    commit_hash, commit_message = line.split('--HASH--')
    print(line)
    print(commit_hash)
    print(commit_message)
    
for line in f:
    commit_hash, commit_message = line.rstrip('\n\r').split('--HASH--')
    print(line)
    print(commit_hash)
    print(commit_message)
    
f = open('sample-commits-10')
for line in f:
    commit_hash, commit_message = line.rstrip('\n\r').split('--HASH--')
    print(line)
    print(commit_hash)
    print(commit_message)
    
def feat_commit(commit_msg, commit_hash):
    print(commit_msg, commit_hash)
    
def fix_commit(commit_msg, commit_hash):
    print(commit_msg, commit_hash)
    
def chore_commit(commit_msg, commit_hash):
    print(commit_msg, commit_hash)
    
def chore_commit(commit_msg, commit_hash):
    print("chore_commit:", commit_msg, commit_hash)
    
def fix_commit(commit_msg, commit_hash):
    print("fix_commit:", commit_msg, commit_hash)
    
def feat_commit(commit_msg, commit_hash):
    print("feat_commit: ", commit_msg, commit_hash)
    
def else_commit(commit_msg, commit_hash):
    print("ELSE_commit: ", commit_msg, commit_hash)
    
for line in f:
    commit_hash, commit_message = line.rstrip('\n\r').split('--HASH--')
    if commit_message.lower().startswith('feat:'):
        feat_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('fix:'):
        fix_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('chore:'):
        chore_commit(commit_message, commit_hash)
    else:
        else_commit(commit_message, commit_hash)
        
f = open('sample-commits-10')
for line in f:
    commit_hash, commit_message = line.rstrip('\n\r').split('--HASH--')
    if commit_message.lower().startswith('feat:'):
        feat_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('fix:'):
        fix_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('chore:'):
        chore_commit(commit_message, commit_hash)
    else:
        else_commit(commit_message, commit_hash)
        
def else_commit(commit_msg, commit_hash):
    print("##ELSE_commit##", commit_msg, commit_hash)
    
def feat_commit(commit_msg, commit_hash):
    print("##feat_commit##", commit_msg, commit_hash)
    
def fix_commit(commit_msg, commit_hash):
    print("##fix_commit##", commit_msg, commit_hash)
    
def chore_commit(commit_msg, commit_hash):
    print("##chore_commit##", commit_msg, commit_hash)
    
f = open('sample-commits-10')
for line in f:
    commit_hash, commit_message = line.rstrip('\n\r').split('--HASH--')
    if commit_message.lower().startswith('feat:'):
        feat_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('fix:'):
        fix_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('chore:'):
        chore_commit(commit_message, commit_hash)
    else:
        else_commit(commit_message, commit_hash)
        
f = open('sample-commits-10')
for line in f:
    commit_hash, commit_message = line.rstrip('\n\r').split('--HASH--')
    if commit_message.lower().startswith('feat:'):
        feat_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('fix:'):
        fix_commit(commit_message, commit_hash)
    elif commit_message.lower().startswith('chore:'):
        chore_commit(commit_message, commit_hash)
    else:
        else_commit(commit_message, commit_hash)
        
get_ipython().run_line_magic('logstart', '05-01-20.py append')
import git
repo = git.Repo()
commits = list(repo.iter_commits("master", max_counts=5))
dir(repo)
dir(repo.iter_commits)
dir(repo.iter_commits())
dir(repo.active_branch)
repo.active_branch
repo.active_branch.name
repo.active_branch.log
repo.active_branch.log()
dir(repo.active_branch)
dir(repo.active_branch.log)
dir(repo.active_branch.log())
commits = list(repo.iter_commits())
commits
len(commits)
commit = commits[0]
commit
commit.author
commit.message
dir(commit)
commit.list_items()
commit.list_items(repo)
commit.summary
type(commit.summary)
type(commit.hexsha)
commit.hexsha
commit.summary
c1 = list(repo.iter_commits())
len(c)
len(c1)
c2 = list(repo.iter_commits('3138d17'))
len(c2)
c2 = list(repo.iter_commits('3138d17..HEAD'))
len(c2)
c2 = list(repo.iter_commits('3138d17..da86039'))
len(c2)
s1 = "fix: don't produce template diagnostics when scope is invalid (#34460)"
s1
l1 = s1.lsplit(':', max_count=1)
l1 = s1.split(':', max_count=1)
l1 = s1.split(':', maxsplit=1)
l1
s2 = "fix(ivy): don't produce template diagnostics when scope is invalid (#34460)"
s2 = "fix(ivy): don't produce template diagnostics when scope is invalid so:54  (#34460)"
l2 = s2.split(':', maxsplit=1)
l2
l3 = l2[0].replace('fix','')
l3
l4 = l3.strip('()')
l4
s2
l3
l4
l2
exit()
