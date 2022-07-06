s=input()
s=s.lower()
k=""
for i in s:
    if s.count(i)==1 and i!=' ':
        k+=i
k=sorted(k)
l=''.join(k)
print(l)