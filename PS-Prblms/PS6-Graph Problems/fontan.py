from collections import deque
r,c=map(int,input().split())
visited=[[0 for _ in range(c)] for _ in range(r)]
my_disp=[0 for _ in range(r)]
strt_points=deque()
for i in range(r):
    my_disp[i]=list(input())
    for j in range(c):
        if my_disp[i][j]=='V':
            strt_points.append((i,j))
            visited[i][j]=1
while strt_points:#bfs approach used
    i,j=strt_points.popleft()
    if i+1<r and my_disp[i+1][j]!='#':
        if(visited[i+1][j]!=1):
            strt_points.append((i+1,j))
            my_disp[i+1][j] = 'V'
            visited[i+1][j]=1
    elif i+1<r and my_disp[i+1][j]=='#':
        row=[0,0]
        col=[1,-1]
        for k in range(2):
            p=i+row[k]
            q=j+col[k]
            if(p>=0 and q>=0 and p<r and q<c and visited[p][q]!=1 and my_disp[p][q]!='#'):
                strt_points.append((p,q))
                visited[p][q]=1
                my_disp[p][q]='V'
for row in my_disp:
    print(''.join(row))