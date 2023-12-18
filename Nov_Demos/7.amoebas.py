import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
my_disp=[[] for _ in range(n)]
for i in range(n):
    my_disp[i]=list(input())
def dfs(v,my_disp):
    if my_disp[v[0]][v[1]]=='#':
        my_disp[v[0]][v[1]] = '.'
        row = [-1, -1, 0, 1, 1, 1, 0, -1]  # top,top-right,right...
        col = [0, 1, 1, 1, 0, -1, -1, -1]
        for k in range(8):
            i = v[0] + row[k]
            j = v[1] + col[k]
            if(i<n and i>=0 and j<m and j>=0 and my_disp[i][j]=='#'):
                dfs((i, j), my_disp)
total_amoeba=0
for i in range(n):
    for j in range(m):
        if my_disp[i][j]=='#':
            dfs((i,j),my_disp)
            total_amoeba+=1
print(total_amoeba)