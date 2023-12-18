###Bubble sort XD
l=list(map(int,input().split()))
n=len(l)-1
while(n-1>=0):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            print(' '.join(map(str,l)))
    n-=1