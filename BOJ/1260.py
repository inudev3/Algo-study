import collections

N,M,V = map(int, input().split())
graph = [[] for _ in range(N)]
checked = [False] * N
for _ in range(M):
    u, v = map(int, input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()
def dfs(start):
    checked[start] = True
    print(start+1, end=" ")
    for next in graph[start]:
        if not checked[next]:
            dfs(next)

dfs(V-1)
for i in range(N):
    checked[i] = False
print()
q = collections.deque()
q.append(V-1)
checked[V-1]= True
while q:
    cur = q.popleft()
    print(cur+1, end=" ")
    for next in graph[cur]:
        if not checked[next]:
            q.append(next)
            checked[next] = True
