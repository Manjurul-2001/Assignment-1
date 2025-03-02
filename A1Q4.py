
file=open("mbox.txt")
count=0
total_confidence=0
for line in file:
    line=line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        print(line)
        words=line.split()
        confidence=float(words[1])
        total_confidence=total_confidence+confidence
        count=count+1
print(count)
if count>0:
    avg=total_confidence/count
    print("Average sum", avg)
else:
    print("NO file is X-DSPAM-Confidence found")
