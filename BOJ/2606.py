n = int(input())
m = int(input())
check = [False] * n
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):

    check[start] = True
    for NEXT in graph[start]:
        if check[NEXT] is False:
            dfs(NEXT)


dfs(0)
cnt = [1 for x in check if x is True]
print(sum(cnt)-1)
