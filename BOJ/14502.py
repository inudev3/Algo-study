import collections

n, m = map(int, input().split())
##DFS, BFS의 목적: 한 정점에서 시작해 연결된 모든 정점을 방문하는것
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
dist = [[-1] * m for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
b = [[0] * m for _ in range(n)]
def dfs(x,y):
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny <m:
            if b[nx][ny] ==0:
                b[nx][ny]=2
                dfs(nx, ny)
def go():
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
    for i in range(n):
        for j in range(m):
            if b[i][j] ==2:
                dfs(i,j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt
# def bfs(a):
#     q = collections.deque()
#     for i in range(n):
#         for j in range(m):
#             b[i][j] = a[i][j]
#             if b[i][j] == 2:
#                 q.append((i, j))
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
#                 b[nx][ny] = 2
#                 q.append((nx, ny))
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if b[i][j] == 0:
#                 cnt += 1
#     return cnt


#  전체 보드판 위에 들어갈 수 있는 3개의 벽의 경우에 대해 전부 bfs를 해준다.

ans = 0
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0: continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0: continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0: continue
                        if x1 == x2 and y1 == y2: continue
                        if x2 == x3 and y2 == y3: continue
                        if x1 == x3 and y1 == y3: continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        cur = go()
                        if ans < cur: ans = cur
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)
