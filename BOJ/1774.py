# import math
#
# n, m = map(int, input().split())
#
# pos = []
# parent = [i for i in range(n + 1)]
# graph = []
#
#
# def dist(a, b):
#     return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))
#
#
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     parent[max(a, b)] = min(a, b)
#
#
# for i in range(1, n + 1):
#     x, y = map(int, input().split())
#     pos.append((x, y))
# for _ in range(m):
#     x, y = map(int, input().split())
#     union(x, y)
#
# for i in range(1, n):
#     for j in range(i + 1, n + 1):
#         graph.append((i, j, dist(pos[i - 1], pos[j - 1])))
# ans = 0
# graph.sort(key=lambda x: x[2])
# for edge in graph:
#     if find(edge[0]) != find(edge[1]):
#         union(edge[0], edge[1])
#         ans += edge[2]
#
# print('%.2f' % (ans))
#
# import sys
# import math
# from collections import deque
# import copy
#
# input = sys.stdin.readline
# INF = sys.maxsize
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# di = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]],
#       [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]
#
# MIN = 9999999999999999
#
#
#
# def dfs(start, MAP, cctv):
#     global MIN
#     if start == len(cctv):
#         cnt = 0
#         for x in range(0, n):
#             for y in range(0, m):
#                 if MAP[x][y] == 0:
#                     cnt += 1
#         MIN = min(MIN, cnt)
#         return
#
#     num, x,y = cctv[start]
#     for dir in di[num]:
#         checked = [[False] for _ in range(n)] for in range(m)]
#         for i in dir:
#             ny, nx = y + dy[i], x + dx[i]
#             while m > ny >= 0 and n > nx >= 0:
#                 if tmp[nx][ny] == 6:
#                     break
#                 elif tmp[nx][ny] == 0:
#                     tmp[nx][ny] = '#'
#                 ny += dy[i]
#                 nx += dx[i]
#         dfs(start + 1, tmp, cctv)
#
# n, m = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(n)]
# cctv = []
# block_cnt = 0
# for x in range(0, n):
#     for y in range(0, m):
#         if MAP[x][y] not in [0, 6]:
#             cctv.append([MAP[x][y], x, y])
#         elif MAP[x][y] == 6:
#             block_cnt += 1
# dfs(0, MAP, cctv)
# print(MIN)

n, m, x, y, count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0] * 7


dx = [0,0,-1,1]
dy = [1,-1,0,0]


def change(d):
    if d == 1:
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    elif d == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif d == 3:
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
    else:
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]


for k in command:
    nx, ny = x + dx[k-1], y + dy[k-1]
    if 0 <= nx < n and 0 <= ny < m:
        change(k)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[6]
        else:
            dice[6] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(dice[1])


def dfs(start):
