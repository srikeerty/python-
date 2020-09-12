def prime(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
           
    if(c==2):
        return 1
    else:
        return 0        

x=int(input())
n1=2
c1=0
c2=0
while(True):
    if(prime(n1)):
        if(prime(n1+2)):
            a=n1+2
            c1+=1
        elif(prime(n1-2)):
            b=n1-2
            c2+=1
        
    if(c1==x):
        print(n1,a)
        break
    elif(c2==x):
        print(n1,b)
        break
    n1+=1
        
