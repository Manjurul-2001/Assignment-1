file=open("mbox.txt")
count=0
email_count={}
for line in file:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        if words[1] in email_count:
            email_count[words[1]]=email_count[words[1]]+1
        else:
            email_count[words[1]]=1
print(email_count) 
