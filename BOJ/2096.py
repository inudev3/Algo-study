n = int(input())
INF = 900001
a = [list(map(int, input().split())) for _ in range(n)]
D = a[0]
d = a[0]
for i in range(1, n):
    D = [max(D[0], D[1]) + a[i][0], max(D[0], D[1], D[2]) + a[i][1], max(D[1], D[2]) + a[i][2]]
    d = [min(d[0], d[1]) + a[i][0], min(d[0], d[1], d[2]) + a[i][1], min(d[1], d[2]) + a[i][2]]



 print(max(D), min(d))
