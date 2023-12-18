from collections import defaultdict
n=int(input())
my_graph=defaultdict(list)
visited=defaultdict(int)
for _ in range(n):
    line=input().split(':')
    line[1]=line[1].split()
    for file in line[1]:
        my_graph[file].append(line[0])
        visited[file]=0
print(my_graph)
source=input()
# print(visited)
# print(my_graph)#To understand the graph structure
ans=[]
def dfs(v,adj,visited):
    visited[v]=1
    for neigh in adj[v]:
        if visited[neigh]!=1:
            dfs(neigh,adj,visited)
    ans.append(v)
dfs(source,my_graph,visited)
#print(visited)
while ans:
    print(ans.pop())