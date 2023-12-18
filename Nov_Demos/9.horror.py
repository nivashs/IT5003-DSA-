from collections import deque
my_deq=deque()
n,h,l=map(int,input().split())
adj=[[] for _ in range(n)]
horror_lst=list(map(int,input().split()))
visited=[0 for _ in range(n)]
for i in range(h):
    my_deq.append((horror_lst[i],0))
    visited[horror_lst[i]]=1
inf=1e9
weight_vertices=[inf for _ in range(n)]
for _ in range(l):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
while my_deq:
    ele,d=my_deq.popleft()
    visited[ele]=1
    weight_vertices[ele]=d
    for neigh in adj[ele]:
        if visited[neigh]!=1:
            visited[neigh]=1
            my_deq.append((neigh,d+1))
print(weight_vertices.index(max(weight_vertices)))