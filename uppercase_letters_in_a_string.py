s=input()
s2=s.upper()
c=0
for i in s:
    if i is ' ':
        continue
    if i in s2:
        c=c+1
print(c)