n, m = map(int, input().split())
a = [[0]*(m+1)]+[[0]+list(map(int, input().split())) for _ in range(n)] ##m+1, n+1맞추기(1부터 n,m까지)
D = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        D[i][j] = max(D[i-1][j], D[i][j-1], D[i-1][j-1]) + a[i][j]

print(D[n][m])

##방법 2
D[1][1] = a[1][1]
for i in range(1, n+1):
    for j in range(1, m+1):
        if j+1<=m:
            D[i][j+1] = max(D[i][j+1], D[i][j]+a[i][j+1])
        if i+1<=n:
            D[i+1][j] = max(D[i+1][j], D[i][j]+a[i+1][j])
        if i+1<=1 and j+1<=m:
            D[i+1][j] = max(D[i+1][j+1], D[i][j] + a[i+1][j+1])

print(D[n][m])
##방법1과 방법2의 D는 항상 같은 값이다.(점화식의 정의가 같음)
#방법 3. 항상 양수이기 때문에 대각선 방법은 사용하지 않아도 무관함

for i in range(1, n+1):
    for j in range(1, m+1):
        D[i][j] = max(D[i-1][j], D[i][j-1])+ a[i][j]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j+1<=m:
            D[i][j+1] = max(D[i][j+1], D[i][j]+a[i][j+1])
        if i+1<=n:
            D[i+1][j] = max(D[i+1][j], D[i][j]+a[i+1][j])

#방법 4. Top-Down 재귀 방식
D = [[-1]*(m+1) for _ in range(n+1)]
def go(i:int, j:int):
    if i<1 or j<1:
        return 0
    if D[i][j]>=0:
        return D[i][j] #top-down방식 메모이제이션
    D[i][j] = max(go(i-1, j), go(i, j-1)) + a[i][j]
    return D[i][j]

print(go(n,m))
#방법 5.
D = [[-1]*(m+1) for _ in range(n+1)]
def go(i:int, j:int): ## (n,m)에서 (1,1)로 가는 경우로 점화식의 의미를 바꿈
    if i>n or j>m:
        return 0
    if D[i][j]>=0:
        return D[i][j] #top-down방식 메모이제이션
    D[i][j] = max(go(i+1, j), go(i, j+1)) + a[i][j]
    return D[i][j]
print(D[n][m])
