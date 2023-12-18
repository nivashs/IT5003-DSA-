#More optimized using BFS compared to dijsktra's
from collections import deque
t,r,c=map(int,input().split())
my_disp=[0 for _ in range(r)]
visted=[[0 for _ in range(c)] for _ in range(r)]
mydeque=deque()
inf=1e9
ans=inf
for i in range(r):
    my_disp[i]=list(input())
    for j in range(c):
        if my_disp[i][j]=='S':
            mydeque.append((0,(i,j)))
            visted[i][j]=1
while mydeque:
    d,u=mydeque.popleft()
    i,j=int(u[0]),int(u[1])
    if (i==0 or i==r-1 or j==0 or j==c-1):
        ans=d
        break
    row=[0,1,0,-1]
    col=[1,0,-1,0]#[right,down,left,up]
    for k in range(4):
        p=i+row[k]
        q=j+col[k]
        if(p>=0 and p<r and q>=0 and q<c and my_disp[p][q]=='0' and visted[p][q]!=1):
            mydeque.append((d+1,(p,q)))
            visted[p][q]=1
        elif(p>=0 and p<r and q>=0 and q<c and my_disp[p][q]=='U' and i==p-1 and j==q and visted[p][q]!=1):
            mydeque.append((d+1, (p, q)))
            visted[p][q] = 1
        elif (p >= 0 and p < r and q >= 0 and q < c and my_disp[p][q] == 'D' and i==p+1 and j==q and visted[p][q]!=1):
            mydeque.append((d+1, (p, q)))
            visted[p][q] = 1
        elif (p >= 0 and p < r and q >= 0 and q < c and my_disp[p][q] == 'L' and i==p and j==q-1 and visted[p][q]!=1):
            mydeque.append((d+1, (p, q)))
            visted[p][q] = 1
        elif (p >= 0 and p < r and q >= 0 and q < c and my_disp[p][q] == 'R' and i==p and j==q+1 and visted[p][q]!=1):
            mydeque.append((d+1, (p, q)))
            visted[p][q] = 1
if ans<=t:
    print(ans)
else:
    print('NOT POSSIBLE')