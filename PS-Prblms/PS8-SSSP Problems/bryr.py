from heapq import heappush,heappop
n,e=map(int,input().split())
adj=[[] for _ in range(n)]
for _ in range(e):
    u,v,w=map(int,input().split())
    u,v=u-1,v-1
    adj[u].append((v,w))
    adj[v].append((u,w))
inf=int(1e9)
dist=[inf for _ in range(n)]
dist[0]=0
myPQ=[]
heappush(myPQ,(0,0))
while myPQ:
    d,u=heappop(myPQ)
    if(d<=dist[u]):
        for v,w in adj[u]:
            if(dist[u]+w<dist[v]):
                dist[v]=dist[u]+w
                heappush(myPQ,(dist[v],v))
print(dist[n-1])