#케빈 베이컨
#BFS로 최소거리를 기록 후 모든 정점에 대한 최소거리 합
#합 중 최소 출력
import collections
def bfs(i):
    dist = [0] *(N+1)
    check = [False] * (N+1)
    q = collections.deque()
    q.append(i)
    check[i] = True
    while q:
        x = q.popleft()
        for next in graph[x]:
            if not check[next]:
                q.append(next)
                check[next] = True
                dist[next] = dist[x] + 1
    return sum(dist)

N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans  = 0
result = []
for i in range(1, N+1):
    ans = bfs(i)
    result.append(ans)

print(result.index(min(result))+1)


