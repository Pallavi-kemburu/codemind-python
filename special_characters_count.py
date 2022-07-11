s=input()
l=len(s)
c=0
for i in s:
    if i.isalnum():
        c=c+1
    if i is ' ':
        c=c+1
print(l-c)