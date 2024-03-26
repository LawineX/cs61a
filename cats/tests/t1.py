import random

count=0
lst=list(range(2**16))
for _ in range(100):

    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i]^lst[j]==68:
                count+=1
print(count/100)