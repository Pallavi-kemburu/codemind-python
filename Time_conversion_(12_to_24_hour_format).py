a=input().split(":")
#print(a)
if a[1][3]=="A":
    if (int(a[0])==12):
        print("00:00")
    else:
        print(str(a[0])+":"+str(a[1][0:2]))
else:
    if (int(a[0])==12):
        print("12:00")
    else:
        print(str(int(a[0])+12)+":"+str(a[1][0:2]))