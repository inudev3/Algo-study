N = int(input())
a = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)


b = list(map(int, input().split()))
b = [x-1 for x in b]
order = [0] *N



for i in range(N):
    order[b[i]] = i
for i in range(N):
    a[i].sort(key=lambda x: order[x])
dfs_order= []

check = [False] * N
def dfs(x):
    if check[x]:
        return
    dfs_order.append(x)
    check[x] = True
    for y in a[x]:
        dfs(y)
ok = True
for i in range(N):
    if dfs_order[i] != b[i]:
        ok = False
print(1 if ok else 0)

for i in ra