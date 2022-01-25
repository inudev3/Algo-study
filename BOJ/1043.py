

parent = [0]*51
party = [0]*51
def find(x):
    if parent[x] ==x:
        return
    x = find(parent[x])
    return x
def union(x,y):
    x = find(x)
    y = find(y)
    parent[y] = x

n, m = map(int, input().split())

tmp = list(map(int, input().split()))
cnt = tmp[0]
know = tmp[1:]

for i in range(1, n+1):
    parent[i] = i

for i in range(m):

D = [0] *(n+1)
for i in range(1, n+1 ):
    D[i] = i ##1로만 더한 최악의 경우로 초기화
    j = 1
    while j**2<=i:
        if D[i] > D[i-j**2]+1:
            D[i] = D[i-j**2]+1
        j+=1
print(D[n])

n, k = map(int, input().split())

D = [[0]*k for _ in range(n)]

for i in range(1, k+1):
    for j in range(n+1):
        for l in range(n+1):
        D[i][j] += D[i-l][j-l]
