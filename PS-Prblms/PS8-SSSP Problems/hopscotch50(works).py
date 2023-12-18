from heapq import heappush,heappop
n,k=map(int,input().split())
myPQ=[]
art=[[] for _ in range(n)]
adj=[[] for _ in range(k)]
inf=int(1e9)
dist=[[inf for _ in range(n)] for _ in range(n)]
check,ans=[],inf
for i in range(n):
    art[i]=list(map(int,input().split()))
    for j in range(n):
        if (art[i][j] - 1 == k - 1):
            check.append((i, j))
        if art[i][j]-1==0:
            heappush(myPQ,(0,(i,j)))
            dist[i][j]=0
        else:
            x = art[i][j] - 1
            adj[x - 1].append((i, j))
while myPQ:
    d,u=heappop(myPQ)
    i=u[0]
    j=u[1]
    if(d<=dist[i][j]):
        for x,y in adj[art[i][j]-1]:
            w=abs(x-i)+abs(y-j)
            if(dist[i][j]+w<dist[x][y]):
                dist[x][y]=dist[i][j]+w
                heappush(myPQ,(dist[x][y],(x,y)))
for i,j in check:
    ans=min(ans,dist[i][j])
if ans==inf:
    print(-1)
else:
    print(ans)