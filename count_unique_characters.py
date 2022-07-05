s=input()
s=s.lower()
k=[]
for i in s:
    if s.count(i)==1 and i!=' ':
        k.append(i)
print(len(k))