s=input()
s=s.split()
mini=0
maxi=0
for i in s:
    mini=mini+ord(min(i))
    maxi=maxi+ord(max(i))
print(maxi-mini)