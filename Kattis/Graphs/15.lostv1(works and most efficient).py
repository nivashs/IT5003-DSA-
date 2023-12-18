from collections import defaultdict
from collections import deque
n,e=map(int,input().split())
target_langs=input().split()
my_graph=defaultdict(list)
inf=int(1e9)
dist=defaultdict(lambda: inf)
cdist=defaultdict(lambda: inf)
for _ in range(e):
    u,v,w=input().split()
    w=int(w)
    my_graph[u].append((v,w))
    my_graph[v].append((u,w))
my_DQ=deque()
dist['English']=0
cdist['English']=0
my_DQ.append('English')
while my_DQ:
    u=my_DQ.popleft()
    for v,w in my_graph[u]:
        if dist[u]+1<dist[v] or (dist[v] == dist[u]+1 and cdist[v]>w):
            dist[v] = dist[u] + 1
            cdist[v]=w
            my_DQ.append(v)
ans=sum(cdist.values())
for lang in target_langs:
    if dist[lang]==inf:
        ans='Impossible'
        break
print(ans)
'''
done using bfs
'''