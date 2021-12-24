dx = [0, 0, -1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().spllit())
a = [input() for _ in range(n)]
check = [[False] * m for _ in range(n)]



def go(x, y, cnt, color): #cnt는 방문한 칸의 개수
    if check[x][y]:
        return (cnt - dist[x][y]) >= 4
    check[x][y] = True
    dist[x][y] = cnt
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == color:
                if go(nx, ny, cnt + 1, color):
                    return True

for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        dist = [[0] * m for _ in range(n)] ## 시작점으로부터의 길이 초기화
        if go(i, j , 1, a[i][j] ):
            print('Yes')
else:
    print('No')
