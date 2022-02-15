from sys import stdin
N = int(stdin.readline())
W = list(map(int, stdin.readline()))
def go(w):
    n = len(w)
    if n==2:
        return 0
    ans = 0
    for i in range(1, n-1):
        energy = w[i-1]*w[i+1]
        b = w[:i]+ w[i+1:]
        energy += go(b)

#
# def go(w):
#     n = len(w)
#     if n==2:
#         return 0
#     ans = 0
#     for i in range(1, n-1):#양끝의 구슬은 제외하고 뽑는다.
#         energy = w[i-1]*w[i+1]
#         b = w[:i]+ w[i+1:]
#         energy+= go(b)
#         if ans<energy:
#             ans = energy
#     return ans

def solution(triangle):
    n = len(triangle)
    D = [[0] * i for i in range(1,n+1)]
    D[0][0] = triangle[0][0]
    for i in range(1,n+1):
        for j in range(1,i+1):
            D[i][j] = max(D[i-1][j] , D[i-1][j-1]) + triangle[i][j]
    return max(D[n])
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

n , k = map(int, input().split())
sdf
for _ in range(n):
    w, v = map(int, input().split())