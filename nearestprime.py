'''n=int(input())
c=0
n1=n
c1=0
c2=0
while(n,n1):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
    
            break
    else:
        c1+=1
        n=n+1
    c=0
    for i in range(1,n1+1):
        if(n1%i==0):
            c=c+1
    if(c==2):
            
            break
    else:
        c2+=1
        n1=n1-1
    
if(c2<c1):
    print(n1)
elif(c2==c1):
    print(n,n1)
else:
    print(n)'''
t=int(input())
c1=0
c2=0
for i in range(t):
    n=int(input())
    c=0
    n1=n
    
    while(n,n1):
        c=0
        for i in range(1,n+1):
            if(n%i==0):
                c=c+1
        if(c==2):
    
            break
        else:
            c1+=1
            n=n+1
        c=0
        for i in range(1,n1+1):
            if(n1%i==0):
                c=c+1
        if(c==2):
            
            break
        else:
            c2+=1
            n1=n1-1
    
    if(c2<c1):
        print(n1)

    elif(c1<c2):
        print(n)
    

    
