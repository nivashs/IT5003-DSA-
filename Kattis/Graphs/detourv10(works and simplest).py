from collections import defaultdict
from heapq import heappop,heappush
import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
adj=defaultdict(dict)
for i in range(m):
    u,v,w=map(int,input().split())
    adj[u][v]=w
    adj[v][u]=w

inf=int(1e9)
dist=[inf for _ in range(n)]
p=[-1 for _ in range(n)]
dist[1]=0

my_PQ=[]
shortes_path=[]
heappush(my_PQ,(0,1))
while my_PQ:
    d,u=heappop(my_PQ)
    if (d <= dist[u]):
        for v,w in adj[u].items():
            if(dist[u]+w<dist[v]):
                dist[v]=dist[u]+w
                p[v]=u
                heappush(my_PQ,(dist[v],v))

###Backtrack and getting path,Can do interative way
def mypath(n,x):
    if n==-1:
        return
    mypath(x[n],x)
    shortes_path.append(n)

###deleting all edges pointing to shortest path from (0-->1):
for i in range(n):
    if p[i] != -1:
        del adj[i][p[i]]


p1=[-1 for _ in range(n)]

from collections import deque
mylst = deque()
mylst.append(0)
visited=[0 for _ in range(n)]

###Doing BFS to get path from 0 to 1 with least vertices as Kattis is checking path with only least number of vertices
while(mylst):
    u=mylst.popleft()
    if visited[u] == 1:
        continue
    visited[u]=1
    for v in adj[u]:
        if(visited[v]!=1):
            mylst.append(v)
            p1[v]=u
if not visited[1]:
    print("impossible")
else:
    shortes_path = []
    mypath(1,p1)
    print(str(len(shortes_path)) + ' ' + ' '.join(map(str, shortes_path)))