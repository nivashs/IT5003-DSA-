from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
mygrid = [ch for _ in range(r) for ch in input().rstrip()]
t = int(input())
routes = [(-1, 0, 0), (-1, 1, 1), (0, 1, 2), (1, 1, 3), (1, 0, 4), (1, -1, 5), (0, -1, 6), (-1, -1, 7)]  # clock-wise order from north

def flatten(i, j):
    return i * c + j

# def get_neighbors(i, j):
#     return [(i + ro[0], j + ro[1]) for ro in routes if 0 <= i + ro[0] < r and 0 <= j + ro[1] < c]

for _ in range(t):
    sx, sy, dx, dy = map(int, input().split())
    sx, sy, dx, dy = sx - 1, sy - 1, dx - 1, dy - 1
    if sx == dx and sy == dy:
        print(0)
        continue
    inf = float('inf')
    dist = [inf] * (r * c)
    visit=[0]*(r*c)
    start_index = flatten(sx, sy)
    end_index = flatten(dx, dy)
    dist[start_index] = 0
    mydeq = deque([start_index])
    while mydeq:
        current_index = mydeq.popleft()
        if current_index==end_index:
            break
        if visit[current_index]:
            continue
        visit[current_index]=1
        i, j = divmod(current_index, c)
        grid_value = int(mygrid[current_index])
        for ro in routes:
            neighbor_i, neighbor_j = i + ro[0], j + ro[1]
            if 0 <= neighbor_i < r and 0 <= neighbor_j < c:
                neighbor_index = flatten(neighbor_i, neighbor_j)
                if visit[neighbor_index]:
                    continue
                new_dist = dist[current_index] + (grid_value != ro[2])
                if new_dist < dist[neighbor_index]:
                    dist[neighbor_index] = new_dist
                    if grid_value != ro[2]:
                        mydeq.append(neighbor_index)
                    else:
                        mydeq.appendleft(neighbor_index)
    print(dist[end_index])
