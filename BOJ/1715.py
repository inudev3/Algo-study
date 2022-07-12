# # #1715
# # import heapq
# #
# # n= int(input())
# #
# # a = [0 for _ in range(n)]
# # for i in range(n):
# #     a[i] = int(input())
# #
# # heapq.heapify(a)
# # if n==1:
# #     print(0)
# # else:
# #     sum=0
# #     while len(a)>1:
# #         temp = heapq.heappop(a)+heapq.heappop(a)
# #         heapq.heappush(a, temp)
# #         sum+=temp
# #     print(sum)
# n = int(input())
# D = [[0 for _ in range(10)] for _ in range(100)]
# mod = 1000000000
# for i in range(1, 10):
#     D[0][i] = 1
# for i in range(1, n):
#     for j in range(10):
#         if j >= 1:
#             D[i][j] += D[i - 1][j - 1]
#         if j <= 8:
#             D[i][j] += D[i - 1][j + 1]
#         D[i][j] %= mod
# print(sum(D[n - 1])%mod)
# #

r, c = map(int, input().split())
board = [[[0 for _ in range(2)] for _ in range(c)] for _ in range(r)]  ##0은 A, 1은 B
##0은 아래쪽, 1은 위쪾
for i in range(r):
    items = list(input().split())
    for j in range(len(items)):
        if items[j][0] == 'B':
            board[i][j][1] = int(items[j][1])
        else:
            board[i][j][0] = int(items[j][1])
D = [[0 for _ in range(c)] for _ in range(r)]
a = [[0 for _ in range(c)] for _ in range(r)]
b = [[0 for _ in range(c)] for _ in range(r)]
total = [[0 for _ in range(c)] for _ in range(r)]
for j in range(1, c):
    for i in range(r-1):
        b[i + 1][j] = b[i][j] + board[i][j][1]
for j in range(c):
    for i in range(r - 1, 0, -1):
        a[i - 1][j] = a[i][j] + board[i][j][0]

for i in range(r):
    for j in range(c):
        total[i][j] = a[i][j] + b[i][j]
for i in range(r):
    for j in range(c):
        if i == 0:
            D[i][j] = D[i][j - 1] + total[i][j]
        else:
            D[i][j] = max(D[i][j - 1] + total[i][j], D[i - 1][j - 1] + total[i][j], D[i - 1][j] - board[i][j][0])

print(D[r - 1][c - 1])
