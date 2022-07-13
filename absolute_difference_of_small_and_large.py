s=input()
s=s.split()
mini=0
maxi=0
for i in s:
    print(abs(ord(min(i))-ord(max(i))),end=' ')