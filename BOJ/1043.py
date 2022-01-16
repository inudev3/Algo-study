

parent = [0]*51

def find(x):
    if parent[x] ==x:
        return
    x = find(parent[x])
    return x
def union(x,y):
    x = find(X)
    y = find(y)
    parent[y] = x

n, m = map(int, input().split())

know = list(map(int, input().split()))
cnt = know[0]
know[0] = 0
for i in range(1, n+1):
    parent[i] = i

for i in range(m):


