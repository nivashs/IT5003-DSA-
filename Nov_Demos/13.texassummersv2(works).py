# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
shady=[]
all_cordinates=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    shady.append((x,y))
sx,sy=map(int,input().split())
dx,dy=map(int,input().split())
all_cordinates.append((sx,sy))
for x,y in shady:
    all_cordinates.append((x,y))
all_cordinates.append((dx,dy))
n=len(all_cordinates)
inf=int(1e9)
dist=[inf for _ in range(n)]
par=[p for p in range(n)]
dist[0]=0
visited=[0]*n
for i in range(n):
    u_min=-1
    d_min=inf
    for u in range(n):
        if visited[u]!=1:
            if(dist[u]<d_min):
                d_min=dist[u]
                u_min=u
    u=u_min
    visited[u]=1
    ux=all_cordinates[u][0]
    uy=all_cordinates[u][1]
    for v in range(n):
        p=all_cordinates[v][0]
        q=all_cordinates[v][1]
        w=(ux-p)**2+(uy-q)**2
        if dist[u]+w<dist[v]:
            dist[v]=dist[u]+w
            par[v]=u
path=[]
node=n-1
path.append(node)
while(par[node]!=node):
    path.append(par[node])
    node=par[node]
if len(path)==2:
    print('-')
else:
    k=len(path)
    for i in range(k-2,0,-1):
        print(path[i]-1)
#print(dist)