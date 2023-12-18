n,m=map(int,input().split())
my_lst=[i for i in range(1,n+1)]
sums_set=set()
pairs=[]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        check=i+j
        if check not in sums_set:
            sums_set.add(check)
            pairs.append((i,j))
t=len(pairs)
print(t)
if m>t or m<n-1:
    print(-1)
else:
    for ans in range(m):
        print(' '.join(map(str,pairs[ans])))