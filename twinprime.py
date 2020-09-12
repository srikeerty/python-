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
c=0
while(True):
    
    if(prime(n1) and(prime(n1+2) or prime(n1-2))):
        c+=1
    if(c==x):
        print(n1,n1+2)
        break
    n1+=1
