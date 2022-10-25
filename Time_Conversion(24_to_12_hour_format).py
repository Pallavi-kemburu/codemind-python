a=input().split(":")
if int(a[0])<12:
    if int(a[0])==0:
        print("12:00 AM")
    else:
        print(str(a[0])+":"+str(a[1])+" AM")
    
else:
    if(int(a[0])==12):
        print("12:00 PM")
    else:
        k=int(a[0])-12
        if(len(str(k))==1):
            print("0"+str(k)+":"+str(a[1])+" PM")
        else:
            print(str(k)+":"+str(a[1])+" PM")