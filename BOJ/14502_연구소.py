import collections



# 벽을 3개 세우는 경우의 수 (NM)^3
# BFS, DFS 실행 시간복잡도 NM. 따라서 벽을 세개 세우고 BFS, DFS를 수행하는데 걸리는 시간복잡도 NM^4
# NM의 최대값이 64이므로 2^64으로 1677만 정도. 시간 복잡도 충족

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board):
    a = [[0 for _ in range(m)] for _ in range(n)]
    n= len(a)
    m = len(a[0])
    queue = collections.deque()
    for i in range(n):
        for j in range(m):
            a[i][j] = board[i][j]
            if board[i][j] == 2:
                queue.append((i, j))
    ## 바이러스 퍼뜨리기 BFS수행
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    a[ny][ny] = 2
                    queue.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                cnt += 1
    return cnt
n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for x1 in range(n):
    for y1 in range(m):
        if board[x1][y1] != 0: continue
        for x2 in range(n):
            for y2 in range(m):
                if board[x2][y2] != 0: continue
                for x3 in range(n):
                    for y3 in range(m):
                        if board[x3][y3] != 0: continue
                        if x1 == x2 and y1 == y2: continue
                        if x2 == x3 and y2 == y3: continue
                        if x1 == x3 and y1 == y3: continue
                        board[x1][y1] = 1
                        board[x2][y2] = 1
                        board[x3][y3] = 1
                        cur = bfs(board)
                        if ans < cur: ans = cur
                        board[x1][y1] = 0
                        board[x2][y2] = 0
                        board[x3][y3] = 0
