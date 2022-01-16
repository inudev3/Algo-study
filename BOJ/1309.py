from collections import namedtuple

n = int(input())
mod = 9901

D = [[0]*3 for _ in range(n+1)]
D[1][2] = 1
D[1][0] = 1
D[1][1] = 1
for i in range(2, n+1):
    D[i][0] = D[i-1][1] + D[i-1][2] + D[i-1][0]
    D[i][1] = D[i-1][2] + D[i-1][0]
    D[i][2] = D[i-1][1] + D[i-1][0]


print(sum(D[n]) % mod)
