import sys
sys.setrecursionlimit(10**6)
v,e=map(int,input().split())
c=v
adj=[[] for i in range(v)]
visited=[0 for _ in range(v)]
army_size={}
for _ in range(e):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    adj[u].append(v)
    adj[v].append(u)
for d in range(c):
    army_size[d]=int(input())
lst=[army_size[0]]
for i in range(c):
    adj[i]=sorted(adj[i], key=lambda x: army_size[x])
def dfs(v,adj,army_size,lst):
    visited[v]=1
    for neigh in adj[v]:
        if(lst[0]>army_size[neigh] and visited[neigh]!=1):
            lst[0]+=army_size[neigh]
            dfs(neigh,adj,army_size,lst)
dfs(0,adj,army_size,lst)
print(lst[0])