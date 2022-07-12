s=input()
s=s.split()
c=0
v='aeiouAEIOU'
for i in s:
    if i[0] in v and i[-1] not in v:
        c=c+1
print(c)