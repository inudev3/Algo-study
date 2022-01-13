# n = int(input())
# m = int(input())
# check = [False] * n
# graph = [[] for _ in range(n)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     graph[u].append(v)
#     graph[v].append(u)
#
#
# def dfs(start):
#
#     check[start] = True
#     for NEXT in graph[start]:
#         if check[NEXT] is False:
#             dfs(NEXT)
#
#
# dfs(0)
# cnt = [1 for x in check if x is True]
# print(sum(cnt)-1)

##유니온 파인드

n = int(input())
parent = list(range(n+1))
m = int(input())
def find(x):
    if x== parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[y] = x
for _ in range(m):
    x, y = map(int, input().split())
    union(x,y)
ans = 0
for i in range(2, n+1):
    if find(1) == find(i):
       ans+=1
print(ans)
