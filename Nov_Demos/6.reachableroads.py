t=int(input())
def dfs(v,adj,visited):
    visited[v] = 1
    for neigh in adj[v]:
        if (visited[neigh] != 1):#mistake made here
            dfs(neigh, adj, visited)
for _ in range(t):
    nodes=int(input())
    adj=[[] for _ in range(nodes)]
    for _ in range(int(input())):
        a,b=map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited=[0]*nodes
    connected_comps=0
    for i in range(nodes):
        if(visited[i]!=1):
            dfs(i,adj,visited)
            connected_comps+=1
    print(connected_comps-1)