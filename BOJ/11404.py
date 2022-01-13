n = int(input())
m = int(input())
INF = 1000000000
a = [[0] * (n+1) for _ in range(n+1)]



for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            a[i][j] = 0
        else:
            a[i][j] = INF


for i in range(m):
    u, v, cost = map(int, input().split())
    if a[u][v]> cost:
        a[u][v] = cost

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i][j]> a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j] == INF:
            a[i][j] = 0
        print(a[i][j], end=' ')
    print()

