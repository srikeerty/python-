n=int(input())
n1=n2=n
c=0
s=0
f=0
g=0
while(n>0):
    r=n%10
    n=n//10
    c+=1
for i in range(1,c+1):
    r=n1%10
    n1=n1//10
    while(n1>0):
        su=n%10
        s+=1
        n1=n1//10
        if(s%2!=0):
            if(r<su):
                f=f+1
            else:
                g=g+1
if(f>c//2):
    print("boue")
else:
    print("no")
        
        
