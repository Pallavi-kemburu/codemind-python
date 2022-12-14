from itertools import permutations
s=input()
k=permutations(s)
for i in k:
    z="".join(i)
    print(z)