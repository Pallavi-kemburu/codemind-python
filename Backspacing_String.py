s=input()
t=input()
s=list(s)
t=list(t)
sz=[]
tz=[]
for i in s:
    if i=='#':
        sz.pop()
    else:
        sz.append(i)
for i in t:
    if i=='#':
        tz.pop()
    else:
        tz.append(i)
if sz==tz:
    print('True')
else:
    print('False')