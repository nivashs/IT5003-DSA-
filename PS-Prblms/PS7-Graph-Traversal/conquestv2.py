from heapq import heappush,heappop
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
myheap=[]
ans=army_size[0]
heappush(myheap,(army_size[0],0))
visited[0]=1
while myheap:
    arm_size,u=heappop(myheap)
    if ans>arm_size:
        ans+=arm_size
    elif arm_size>=ans and u!=0:
        break
    for neigh in adj[u]:
        if(visited[neigh]!=1):
            heappush(myheap,(army_size[neigh],neigh))
            visited[neigh]=1
print(ans)