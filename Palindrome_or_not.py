s1=input().lower()
s2=s1[::-1]
c=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        c=c+1
    else:
        c=0
        print(False)
        break
if c>0:
    print(True)