n,m = map(int, input().split())

memory = [0]+list(map(int, input().split()))
cost = [0]+list(map(int, input().split()))
k= sum(cost)
d = [[0] * (k+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(k+1):
        if j-cost[i]>=0:
            d[i][j] = max(d[i-1][j], d[i-1][j-cost[i]]+memory[i])

for i in range(k+1):
    if d[n][i] >= m:
        print(i)
        exit()

