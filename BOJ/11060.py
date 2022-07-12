# # n = int(input())
# #
# # a = list(map(int, input().split()))
# # D = [-1]*(n)
# # D[0] = 0
# # for i in range(1, n):
# #      for j in range(i):
# #          if i-j<= a[j] and D[j]!=-1:
# #              if D[i] == -1 or D[i]>D[j]+1:
# #                  D[i] = D[j]+1
# # print(D[n-1])
# #
# #
# # ##방법 2 어디로 갈 수 있는가
# #
# # # D[0] = 0
# # # for i in range(n-1):
# # #     if D[i] == -1:
# # #         continue
# # #     for j in range(1, a[i]+1):
# # #         if i+j>=n:
# # #             break
# # #         if D[i+j] == -1 or D[i+j]>D[i]+1:
# # #             D[i+j] = D[i]+1
# # #
# # # n= int(input())
# # # a = list(map(int, input().split()))
# # #
# # # D[0]= 0
# # # for i in range(n):
# # #     for j in range(a[i]):
# # #         D[i] =
# import sys
#
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# D = [[-1 for _ in range(n)] for _ in range(n)]
#
#
# def go(i, j):
#     if i == j:
#         return 1
#     elif i + 1 == j:
#         return 1 if a[i] == a[j] else 0
#     if D[i][j] != -1:
#         return D[i][j]
#     if a[i] != a[j]:
#         D[i][j] = 0
#     else:
#         D[i][j] = go(i + 1, j - 1)
#     return D[i][j]
#
# sys.setrecursionlimit(1000000)
# for _ in range(m):
#     u, v = map(int, input().split())
#     print(1 if go(u, v) else 0)
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
D = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
		D[i][i] = True
for j in range(n-1):
	if a[j]==a[j+1]:
		D[j][j+1] = True
for k in range(3, n+1):
	for i in range(0, n-k+1):
		j = i+k-1
		if a[i]==a[j] and D[i+1][j-1]:
			D[i][j] = True
for _ in range(m):
	u, v = map(int, input().split())
	print( 1 if D[u-1][v-1] else 0)