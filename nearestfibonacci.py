def fib(n):
    f3=0
    f1=0
    f2=1
    i=1
    while(i<=n):
        f3=f1+f2
        if(f3==n):
            print(n)
            break
        else:
            c1+=1
            i=i+1
        f1=f2
        f2=f3
    while(i):
        f3=f1+f2
        if(f3==n):
            print(n)
            break
        else:
            c2=c2+1
            
