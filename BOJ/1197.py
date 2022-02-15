v,e = map(int, input().split())
graph = [[] for _ in range(e)]
parent = list(range(v+1))
for i in range(e):
    a,b,c = map(int, input().split())
    graph[i].extend([c,a,b])
graph.sort(key=lambda x:x[0]) ##비용으로 정렬
def Find(x):
    if x==parent[x]:
        return x
    parent[x] = Find(parent[x])
    return parent[x]
def Union(x,y):
    x = Find(x)
    y = Find(y)
    if x==y:
        return
    parent[x] = y
ans = 0
for i in range(e):
    cost,a,b = graph[i]
    x = Find(a)
    y = Find(b)
    if x!=y:
        Union(x,y)
        ans+=cost
print(ans)
