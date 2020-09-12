s=input()
a=list(input())
a.insert(0,0)
j=0
k=[]
for i in range(1,len(a)):
    if (a[i] not in k):
        k.append(0)
    else:
        print(index(a[i]))
        k.append(index(a[i]))
print(k)
'''
for i in  range(len(s)):
    if(s[i]==a[j+1]):
        i=i+1
        j=j+1
    elif'''
    
    

