n,k=map(int,input().split())
a=[]
c=0
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    if i<k:
        c=c+a[i]
print(c)
