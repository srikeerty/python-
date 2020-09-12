n=int(input())
l=[i+1 for i in range(n)]
k=0
l1=[]
while True:
    if(len(l)==1):
        break
    l1.append(l[k])
    if(k==len(l)-1 or k==len(l)-2):
        if(k==len(l)-1):
            k=1
        else:
            k=0
        l=l1.copy()
        l1=[]
    else:
        k=k+2
print(l)
