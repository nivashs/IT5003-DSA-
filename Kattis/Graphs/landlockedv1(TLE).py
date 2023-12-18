from collections import deque
import sys
input = sys.stdin.readline
r,c=map(int,input().split())
visited=[[0 for _ in range(c)] for _ in range(r)]
countries= {}
graph = [list(input()) for _ in range(r)]

mydeq=deque()
for i in range(r):
    for j in range(c):
        if graph[i][j]=='W':
            mydeq.append(((i, j),-1))#Storing co-ordinates of Ocean with initial dist -1
while mydeq:
    co_ord,dist=mydeq.popleft()
    x,y=co_ord[0],co_ord[1]
    if(visited[x][y]):
        continue
    visited[x][y]=1
    if graph[x][y] not in countries:
        countries[graph[x][y]]=dist
    row = [-1, -1, 0, 1, 1, 1, 0, -1]# top,top-right,right...
    col = [0, 1, 1, 1, 0, -1, -1, -1]
    for k in range(8):
        i=x+row[k]
        j=y+col[k]
        if(i<r and j<c and i>=0 and j>=0 and visited[i][j]!=1):
            if graph[i][j]==graph[x][y]:#moving to same country so dont increase dist,or ocean to ocean
                mydeq.appendleft(((i,j),dist))
            else:# reached another country,so increase dist
                mydeq.append(((i,j),dist+1))
del countries['W']
for i in range(26):
    if chr(65+i) in countries:
        print(chr(65+i),end=' ')
        print(countries[chr(65+i)])