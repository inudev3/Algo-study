import collections

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

n = int(input())
board = [[0 for _ in range(n)]for _ in range(n)]
dist = [[-1 for _ in range(n)] for _ in range(n)]
r1,c1,r2,c2 = map(int, input().split())
queue= collections.deque()
queue.append((r1,c1))
dist[r1][c1] = 0
while queue:
    x,y = queue.popleft()
    for k in range(6):
        nx, ny =x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if dist[nx][ny]==-1:
                dist[nx][ny] = dist[x][y]+1
                queue.append((nx,ny))

print(dist[r2][c2])

