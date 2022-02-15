n = int(input())
dp = [[0 for _ in range(1024)] for _ in range(10)] * n
MOD = 1e9
for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, n + 1):
    for j in range(10):
        a = (1 << j)
        for k in range(1, 1 << 10):
            if j == 0:
                dp[i][j][k | a] += dp[i - 1][j + 1][k]
            elif j == 9:
                dp[i][j][k | a] += dp[i - 1][j - 1][k]
            else:
                dp[i][j][k | a] += dp[i - 1][j + 1][k] + dp[i - 1][j - 1][k]
            dp[i][j][k | a] %= MOD
sum = 0
for i in range(10):
    sum+=  dp[n][i][1<<10]

print(sum%MOD)
