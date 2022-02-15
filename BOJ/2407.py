##파스칼의 삼각형

n, m = map(int, input().split())

dp = [[0]*(101) for _ in range(101)]

for i in range(1,101):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])