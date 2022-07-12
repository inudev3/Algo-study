import collections
import sys

a = list(map(int, input().split()))
a.pop()
n = len(a)
dp = [[[sys.maxsize for _ in range(5)] for _ in range(5)] for _ in range(n)]

def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b-a)%2 == 0:
        return 4
    else:
        return 3

dp[0][0][0] = 0
for i in range(n-1): #마지막 -1 까지
    next = a[i+1]
    for j in range(5): #left
        for k in range(5): #right
            if next!=k:
                dp[i+1][next][k] = min(dp[i+1][next][k], dp[i][j][k]+ move(j, next))
            if next!=j:
                dp[i+1][j][next] = min(dp[i+1][j][next], dp[i][j][k]+move(k, next))

_min = sys.maxsize
for i in range(5):
    for j in range(5):
        _min = min(_min, dp[n-1][i][j])
print(_min)

##top-down
# dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
# def solve(n, l, r):
#     if n>=len(a)-1: return 0
#     cache = dp[n][l][r]
#     if cache != -1:
#         return cache
#     cache = min(solve(n+1, a[n], r)+move(l, a[n]), solve(n+1, l, a[n])+move(r, a[n]))
#     return cache

