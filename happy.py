'''n=int(input())
while(True):
    s=0
    if(n>1 and n<=9):
        print("not possible")
        break
    elif(n>=10):
        
        while(n>0):
            r=n%10
            n=n//10
            s=s+r*r
        if(s==1 or s==7):
            print("s")
            break
        else:
            n=s'''
def happy(n):
    s=0
    while(n):
            r=n%10
            n=n//10
            s=s+r*r
            if(n==0 and s<10 and (s==1 or s==7)):
                s=1
                return s
                
            elif(n==0):
                n=s
                s=0

n=int(input())
c=happy(n)
if(c==1):
        print("happy")
        
else:
    print("sad")
            






            
