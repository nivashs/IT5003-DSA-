from collections import deque
import sys
input = sys.stdin.readline
r,c=map(int,input().split())
mygrid=[list(input()) for _ in range(r)]
t=int(input())
routes=[(-1,0,0),(-1,1,1),(0,1,2),(1,1,3),(1,0,4),(1,-1,5),(0,-1,6),(-1,-1,7)]#clock-wise order frm north
for _ in range(t):
    sx,sy,dx,dy=map(int,input().split())
    sx,sy,dx,dy=sx-1,sy-1,dx-1,dy-1
    if sx==dx and sy==dy:
        print(0)
        continue
    inf=int(1e9)
    visited=[[0 for _ in range(c)] for _ in range(r)]
    dist=[[inf for _ in range(c)] for _ in range(r)]
    dist[sx][sy]=0
    mydeq=deque()
    mydeq.append((sx,sy))
    while mydeq:
        i,j=mydeq.popleft()
        if i==dx and j==dy:
            break
        if visited[i][j]:
            continue
        visited[i][j]=1
        for ro in routes:
            x, y = i + ro[0], j + ro[1]
            if 0 <= x < r and 0 <= y < c and visited[x][y]!=1:
                new_dist = dist[i][j] + (int(mygrid[i][j]) != ro[2])#condition if in direction of current
                if new_dist < dist[x][y]:
                    dist[x][y] = new_dist
                    if (int(mygrid[i][j]) != ro[2]):#weight is 1
                        mydeq.append((x, y))
                    else:
                        mydeq.appendleft((x,y))#weight is zero
    print(dist[dx][dy])