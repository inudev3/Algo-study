from collections import deque

possible = [(-2,1),(-1,2),(1,2),(2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
T = int(input())
INF = int(1e9)

def bfs(cur, dest):
    q = deque()
    q.append((cur[0], cur[1]))

    while q:
        x,y = q.popleft()
        if x==dest[0] and y==dest[1]:
            print(dist[x][y])
            return
        for dx, dy in possible:
            if 0<=x+dx and x+dx<L and 0<=y+dy and y+dy<L:
                if not dist[y+dy][x+dx]:
                    q.append((x+dx, y+dy))
                    dist[y+dy][x+dx] = dist[y][x] +1

for _ in range(T):
    L = int(input())
    cur = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    dist = [[0] * L for _ in range(L)]
    bfs(cur, dest)






