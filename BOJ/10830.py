n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
def multi(a,b):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
               ans[i][j] += a[i][k] * b[k][j]
            ans[i][j] %=1000
    return ans
def pow(a,b):
    if b==1:
        return a
    if b%2==0:
        tmp = pow(a, b//2)
        return multi(tmp, tmp)
    else:
        tmp = pow(a, b-1)
        return multi(tmp, a)

ans = pow(a,b)
for row in ans:
    for col in row:
        print(col%1000, end=" ")
    print()


