# from collections import defaultdict
# from sys import stdin
#
# cnt = defaultdict(int)
#
# n = int(stdin.readline())

# a = [list(map(int, stdin.readline().split())) for _ in range(N)]
#
#
# def same(x, y, n):
#     for i in range(n):
#         for j in range(n):
#             if a[x + i][y + j] != a[x][y]:
#                 return False
#     return True
#
#
# cnt = [0] * 3


# 분할 정복


def solve(x, y, n):
    if n == 1:
        return 2 * x + y
    else:
        if x < 2 ** (n - 1):
            if y < 2 ** (n - 1):
                return solve(x, y, n - 1)
            else:
                return solve(x, y - 2 ** (n - 1), n-1) + 2 ** (2 * n - 2)
        else:
            if y < 2 ** (n - 1):
                return solve(x-2**(n-1), y, n-1)+ 2**(2*n-1)
            else:
                return solve(x-2**(n-1), y-2**(n-1), n-1) +2**(2*n-2)*3
n,x,y = map(int, input().split())
print(solve(x,y,n))

