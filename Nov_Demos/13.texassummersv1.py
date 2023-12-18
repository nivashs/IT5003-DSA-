# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
from heapq import heappush,heappop
all_cordinates=[]
src_no=int(input())
for _ in range(src_no):
    x,y=map(int,input().split())
    all_cordinates.append((x,y))
sx,sy=map(int,input().split())
dx,dy=map(int,input().split())
all_cordinates.append((sx,sy))
all_cordinates.append((dx,dy))
n=len(all_cordinates)
inf=int(1e9)
dist=[inf for _ in range(n)]
par=[p for p in range(n)]
dist[src_no]=0
my_PQ=[]
heappush(my_PQ,(0,(sx,sy),src_no))
while my_PQ:
    d,u,node=heappop(my_PQ)
    ux=u[0]
    uy=u[1]
    if(d<=dist[node]):
        for v in range(n):
            if(v!=node):
                p,q=all_cordinates[v]
                value=(ux-p)**2+(uy-q)**2
                if(dist[node]+value<dist[v]):
                    dist[v]=dist[node]+value
                    par[v]=node
                    heappush(my_PQ,(dist[v],(p,q),v))
path=[]
node=n-1
path.append(src_no+1)
while(par[node]!=node):
    path.append(par[node])
    node=par[node]
if len(path)==2:
    print('-')
else:
    k=len(path)
    for i in range(k-2,0,-1):
        print(path[i])
print(dist)