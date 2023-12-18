from collections import deque
my_deq=deque()
c,p,x,l=map(int,input().split())
x,l=x-1,l-1
my_deq.append(l)
adj=[[] for _ in range(c)]
for _ in range(p):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    adj[u].append(v)
    adj[v].append(u)
degree_lst=[0 for _ in range(c)]
for i in range(c):
    degree_lst[i]=len(adj[i])
def reduce_degree(n,degree_list):
    for x in adj[n]:
        degree_list[x]-=1
visited=[0 for _ in range(c)]
while my_deq:
    u=my_deq.popleft()
    reduce_degree(u,degree_lst)
    visited[u]=1
    for neigh in adj[u]:
        if visited[neigh]!=1 and degree_lst[neigh]<=len(adj[neigh])//2:
            visited[neigh]=1
            my_deq.append(neigh)
if(visited[x]==1):
    print('leave')
else:
    print('stay')