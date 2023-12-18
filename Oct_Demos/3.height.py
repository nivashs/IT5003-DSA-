###Insertion sort// Calculate number of shifts:
n=int(input())
for inp in range(n):
    l=list(map(int,input().split()))
    l,count=l[1:],0
    for i in range(1,len(l)):
        x=l[i]
        j=i-1
        while(j>=0 and x<l[j]):
            l[j+1]=l[j]
            count+=1
            j-=1
        l[j+1]=x
    print(str(inp+1)+' '+str(count))