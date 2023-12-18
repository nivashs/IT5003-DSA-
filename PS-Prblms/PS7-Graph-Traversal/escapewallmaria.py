from heapq import heappush,heappop
t,r,c=map(int,input().split())
my_disp=[0 for _ in range(r)]
inf=1e9
dist=[[inf for _ in range(c)] for _ in range(r)]
myPQ=[]
for i in range(r):
    my_disp[i]=list(input())
    for j in range(c):
        if my_disp[i][j]=='S':
            heappush(myPQ,(0,(i,j)))
            dist[i][j]=0
while myPQ:
    d,u=heappop(myPQ)
    i,j=int(u[0]),int(u[1])
    row=[0,1,0,-1]
    col=[1,0,-1,0]#[right,down,left,up]
    for k in range(4):
        p=i+row[k]
        q=j+col[k]
        if(p>=0 and p<r and q>=0 and q<c and my_disp[p][q]=='0'):
            if(d+1<dist[p][q]):
                dist[p][q]=d+1
                heappush(myPQ,(dist[p][q],(p,q)))
        elif(p>=0 and p<r and q>=0 and q<c and my_disp[p][q]=='U' and i==p-1 and j==q):
            if (d+1<dist[p][q]):
                dist[p][q] = d + 1
                heappush(myPQ, (dist[p][q], (p, q)))
        elif (p >= 0 and p < r and q >= 0 and q < c and my_disp[p][q] == 'D' and i==p+1 and j==q):
            if (d + 1 < dist[p][q]):
                dist[p][q] = d + 1
                heappush(myPQ, (dist[p][q], (p, q)))
        elif (p >= 0 and p < r and q >= 0 and q < c and my_disp[p][q] == 'L' and i==p and j==q-1):
            if (d + 1 < dist[p][q]):
                dist[p][q] = d + 1
                heappush(myPQ, (dist[p][q], (p, q)))
        elif (p >= 0 and p < r and q >= 0 and q < c and my_disp[p][q] == 'R' and i==p and j==q+1):
            if (d + 1 < dist[p][q]):
                dist[p][q] = d + 1
                heappush(myPQ, (dist[p][q], (p, q)))
#Iterating through borders of dist list:
time_taken=inf
for a in range(c):
    time_taken = min(time_taken,dist[0][a])
for a in range(c):
    time_taken = min(time_taken,dist[r-1][a])
for i in range(1,r-1):
    time_taken = min(time_taken,dist[i][c - 1])
for i in range(r-2,0,-1):
    time_taken= min(time_taken,dist[i][0])
if time_taken <=t:
    print(time_taken)
else:
    print('NOT POSSIBLE')