from itertools import permutations
l=list(map(str,input().split()))
p=list(permutations(l))
max=0
for i in p:
    s=""
    for j in i:
        s=s+j
    if int(s)>max:
        max=int(s)
print(max)
