from collections import defaultdict
from heapq import heappush,heappop
n,e=map(int,input().split())
target_langs=input().split()
my_graph=defaultdict(list)
inf=int(1e9)
visited=defaultdict(int)
for _ in range(e):
    u,v,w=input().split()
    w=int(w)
    my_graph[u].append((v,w))
    my_graph[v].append((u,w))
my_PQ=[]
heappush(my_PQ,(0,0,'English'))
ans=0
while my_PQ:
    x=heappop(my_PQ)
    e = x[0]
    d = x[1]
    u = x[2]
    if(visited[u]!=1):
        visited[u]=1
        ans+=d
        for v,w in my_graph[u]:
            if(visited[v]!=1):
                heappush(my_PQ,(e+1,w,v))
for lang in target_langs:
    if not visited[lang]:
        ans='Impossible'
        break
print(ans)
'''
done using PQ
'''