n, m = map(int, input().split())
a = [0]+list(map(int, input().split()))
c = [0]+list(map(int, input().split()))
D = [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]
result = sum(c)
for i in range(1,n+1):
    byte= a[i]
    cost = c[i]
    for j in range(1, sum(c)+1):
        if j <cost:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j-cost]+byte, D[i-1][j])
        if D[i][j]>=m:
            result = min(result, j)

if m!=0:
    print(result)
else:
    print(0)


