def pali(s1):
    s2=s1[::-1]
    c=0
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            c=c+1
        else:
            c=0
            return 0
            break
    if c==len(s1):
        return 1
s=input().lower()
s=s.split()
c=0
for i in s:
    if pali(i):
        c=c+1
print(c)