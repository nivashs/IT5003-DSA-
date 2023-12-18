# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
from heapq import heappush,heappop
while True:
    n, m, q, s = map(int, input().split())
    if(n==m==q==s==0):
        break
    my_adj = [[] for _ in range(n)]
    inf = int(1e9)
    dist = [inf for _ in range(n)]
    dist[s]=0
    for _ in range(m):
        u, v, w = map(int, input().split())
        my_adj[u].append((v,w))
    my_PQ=[]
    heappush(my_PQ,(0,s))
    while my_PQ:
        d,u=heappop(my_PQ)
        if(d<=dist[u]):
            for v, w in my_adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v]=dist[u]+w
                    heappush(my_PQ,(dist[v],v))
    for _ in range(q):
        z=int(input())
        print(dist[z]) if dist[z]!=inf else print('Impossible')
    print()