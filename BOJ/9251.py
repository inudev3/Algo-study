a = input().rstrip()
b = input().rstrip()
n = len(a)
m = len(b)
D = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            D[i + 1][j + 1] = D[i][j] + 1
        else:
            D[i + 1][j + 1] = max(D[i + 1][j], D[i][j + 1])

print(D[n][m])

a = " " + a
b = " " + b

v = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i]==b[j]:
            D[i][j] = D[i-1][j-1]+1
            v[i][j] = 1
        else:
            if D[i][j-1] < D[i-1][j]:
                D[i][j] = D[i-1][j]
                v[i][j] = 2
            else:
                D[i][j] = D[i][j-1]
                v[i][j] =3
ans = ""
while n>0 and m>0:
    if v[n][m] == 1:
       ans+= a[n]
       n-=1
       m-=1
    elif v[n][m]==2:
        n-=1
    else:
        m-=1
print(D[n][m])
if D[n][m]!=0:
    print(ans[::-1])

for i in range(1, n+1):
    for j in range(1,m+1):
        if a[i]==b[j]:
            D[i][j] = D[i-1][j-1]+1
        else:
            D[i][j] = 0



