s1=input().lower()
s2=input().lower()
a=''
c=0
for i in s1:
    if i is ' ':
        continue
    if i in s2 and i not in a:
        c=c+1
        a=a+i
a=sorted(a)
a=''.join(a)
if c==0:
    print(-1)
else:
    print(a)        