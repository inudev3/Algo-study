from collections import deque

N, M = map(int, input.split())
a = [list(map(int, list(input()))) for _ in range(N)]
check = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1, 0,0]
q = deque()
q.append((0, 0))
check[0][0] = True
dist[0][0] = 1
while q:
    x,y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if check[nx][ny] ==False and a[nx][ny] == 1:
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y]+1
                check[nx][ny] = True
print(dist[N-1][M-1])