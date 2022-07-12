# s = list(input().rstrip())
# t = list(input().rstrip())
#
#
# def check(word):
#     if word == s:
#         return 1
#     else:
#         return 0
#
#
# for i in range(len(t)-1, len(s)-1, -1):
#     if t[i] == 'A':
#         t.pop()
#     else:
#         t.pop()
#         t.reverse()
#
# print(check(t))
#
#
#
import sys
sys.setrecursionlimit(1000000)
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
D = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, color):
    D[x][y] = color
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1 and D[nx][ny] == 0:
                dfs(nx, ny, color)


color = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and D[i][j] == 0:
            color += 1
            dfs(i, j, color)
print(color)
for i in range(1,color+1):
    cnt=0
    for j in range(n):
        for k in range(n):
            if D[j][k] == i:
                cnt += 1
    print(cnt)
