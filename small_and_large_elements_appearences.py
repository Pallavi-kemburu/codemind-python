s=input()
s=s.split()
s=''.join(s)
print(min(s),s.count(min(s)),max(s),s.count(max(s)),end=' ')