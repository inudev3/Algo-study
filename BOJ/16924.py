
n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
check =[[False] * m for _ in range(n)]
ans= []
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            l=0
            for k in range(1, min(n,m)):
                if i+k<n and i-k>=0 and j+k<m and j-k>=0:
                    if a[i+k][j] == a[i-k][j] == a[i][j+k]== a[i][j-k] == '*':
                        l=k
                    else:
                        break
                else:
                    break
            if l>0:
                ans.append((i+1, j+1, l))
                check[i][j] = True
                for k in range(l):
                    check[i+k][j] = True
                    check[i-k][j]= True
                    check[i][j-k]= True
                    check[i][j+k]= True

for i in range(n):
    for j in range(m):
        if a[i][j] == '*' and not check[i][j]:
            print(-1)
            exit()
for i in ans:
    x, y, len = i
    print(x, end=' ')
    print(y, end=' ')
    print(len, end= ' ')
