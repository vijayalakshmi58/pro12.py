# pro12.py
cccd=int(input())
temp=cccd
revn=0
while(cccd>0):
    d=cccd%10
    revn=revn*10+d
    cccd=cccd//10
if(temp==revn):
    print("yes")
else:
    print("no")
