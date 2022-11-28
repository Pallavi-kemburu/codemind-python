for _ in range(int(input())):
    a=input()
    mi=min(a)
    ma=max(a)
    i=0
    while i<len(a):
        if str(int(mi)+int(i)) not in a:
            print("NO")
            break
        i=i+1
    else:
        print("YES")
            
    