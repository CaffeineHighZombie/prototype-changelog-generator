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
    
