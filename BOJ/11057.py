
n = int(input())
D = [[0]*10 for _ in range(1001)]
mod = 10007
for i in range(10):
    D[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        for k in range(j+1):
            D[i][j] += D[i-1][k]
            D[i][j] %= mod

print(sum(D[n]) % mod)