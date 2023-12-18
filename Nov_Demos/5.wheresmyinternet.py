import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
houses,m=map(int,input().split())
adj=defaultdict(list)
visited=[0]*(houses+1)
visited[0]=1
for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
def dfs(v,adj,visited):
    visited[v]=1
    for neigh in adj[v]:
        if visited[neigh]!=1:
            visited[neigh]=1
            dfs(neigh,adj,visited)
dfs(1,adj,visited)
if all(visited):
    print('Connected')
else:
    for i in range(1, houses + 1):
        if visited[i] == 0:
            print(i)

# atleast1=False
# for i in range(1, houses + 1):
#     if visited[i] == 0:
#         atleast1=True
#         print(i)
# if not atleast1:
#     print('Connected')

