import re 
fh = open("regex-sum-42.txt")
intSum = 0
for line in fh:
    numbers=re.findall("[0-9]+", line)
    if not numbers: continue
    else:
        for number in numbers:
            intSum = intSum + int(number)

print(intSum)
