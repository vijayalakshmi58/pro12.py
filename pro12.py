# pro12.py
vg1=int(input())
temp=vg1
revn1=0
while(vg1>0):
    d=vg1%10
    revn1=revn1*10+d
    vg1=vg1//10
if(temp==revn1):
    print("yes")
else:
    print("no")
