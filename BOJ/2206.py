import collections

n, m = map(int, input().split())

a = [list(map(int, list(input().rstrip()))) for _ in range(n+1)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dist = [[-1] * (m+1) for _ in range(n+1)]
def bfs(a,b):
    q = collections.deque()
    dist[a][b] = 0
    broke = False
    q.append((a, b, broke))
    while q:
        x, y, broke = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k]+ y+dy[k]
            if 0<=nx<=n and 0<=ny<=m and dist[nx][ny]==-1:
                if a[nx][ny]==1 and broke:
                    continue
                elif a[nx][ny] ==1 and not broke:
                    dist[nx][ny] = dist[x][y] +1
                    broke = True
                    q.append((nx,ny, broke))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny, broke))
bfs(1,1)
print(-1 if dist[n][m]==-1 else dist[n][m])
