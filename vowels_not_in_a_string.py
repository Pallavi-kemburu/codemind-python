s=input()
v='aeiou'
c=""
f=0
for i in s:
    if i in v:
        c=c+i
for i in v:
    if i not in c:
        f+=1
        print(i,end=' ')
if f==0:
    print('0')