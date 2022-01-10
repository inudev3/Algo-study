import collections

n, m = map(int, input().split())
next = list(range(101))
dist = [-1] * 101

for _ in range(n+m):
    u, v = map(int, input().split())
    next[u] = v

#ㅅㅏ다리와 뱀의 구분은 필요없음
dist[1] = 0 #1번칸
q = collections.deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1,7):
        nx = x+i
        if nx>100:
            continue
        nx = next[nx]
        if dist[nx] != -1:
            dist[nx] = dist[x]+1
            q.append(nx)

print(dist[100])




