# 사이클을 찾을 땐 DFS, 정점에서의 거리를 찾을 땐 BFS
# 이전 정점과 다른 정점 방문하는데 이전에 방문했던 정점을 방문한다면 그것은 사이클의 시작점임
# 순환선에 포함된 모든 정점으로부터 BFS를 수행하여
from collections import deque

N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

dist = [0] * (N + 1)
check = [0] * (N + 1)  # 1:visited, 2:cycle


def go(x, p):
    # -2: found cycle which is not included
    # -1: not found cycle
    # 0~n-1: found cycle
    if check[x] == 1:
        return x #사이클의 시작점을 리턴한다.
    check[x] = 1
    for y in adj[x]:
        if y == p:
            continue
        res = go(y, x)  # 다음 정점
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2
            if x == res: #현재 정점이 사이클의 시작정점과 같다면 현재부터는 사이클에 포함되지 않음
                return -2
            else: #아니라면 사이클
                return res
            # return res는 사이클이고, return -2 는 사이클을 찾았으나 미포함인 것  return -1은 사이클을 못찾은 것
    return -1

go(0,-1)
q = deque()
dist = [-1] *N
for i in range(N):
    if check[i] == 2: #사이클에서 BFS탐색 시작
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = -1
while q:
    x = q.popleft()
    for y in adj[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x]+1

print( *dist, sep=' ')