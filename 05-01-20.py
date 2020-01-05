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
        
