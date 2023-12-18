# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
from heapq import heappush,heappop
n,s,x=map(int,input().split())
am=[[] for _ in range(n)]
for i in range(n):
    am[i]=list(map(int,input().split()))
my_adj=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i!=j):
            my_adj[i].append((j,am[i][j]))
inf=int(1e9)
dist=[inf for _ in range(n)]
my_PQ=[]
dist[s]=0
heappush(my_PQ,(0,s))
while my_PQ:
    d,u=heappop(my_PQ)
    if(d<=dist[u]):
        for v,w in my_adj[u]:
            if(dist[u]+w<dist[v]):
                dist[v]=dist[u]+w
                heappush(my_PQ,(dist[v],v))
print(dist[x])