a=input().lower()
c=[]
for i in a:
    if i is ' ':
        continue
    if i not in c:
        c.append(i)
c=sorted(c)
c=''.join(c)
print(c)