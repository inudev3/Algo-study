n, m = map(int, input().split())
parent = list(range(n + 1))


def Find(x):
    if x != parent[x]:
        parent[x] = Find(parent[x])
    return parent[x]


def Union(x, y):
    a = Find(x)
    b = Find(y)
    if a == b:
        return
    parent[a] = b


graph = [[] for _ in range(m)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[i].extend([c, a, b])

graph.sort()

ans = 0
# MST에서 간선의 개수는 n-1개(최소간선)
# 크루스칼에서는 정렬되어 있는 상태이므로 n-2깨 까지만 유니온하면 최소비용으로 2개의 분리된 트리
##크루스칼은 최소 비용부터 유니온하기 때문
mst = []
for i in range(m):
    cost, a, b = graph[i]
    x = Find(a)
    y = Find(b)
    if x == y:
        continue
    Union(a, b)
    ans += cost
    mst.append([a, b])
    if len(mst) == n - 2:
        break
print(ans)

