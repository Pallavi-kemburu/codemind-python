s=input()
c=0
z=[]
v='aeiouAEIOU'
for i in s:
    if i in v:
        c=c+1
    else:
        z.append(c)
        c=0
z.append(c)
print(max(z))