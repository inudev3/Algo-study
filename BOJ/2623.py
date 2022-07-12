import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(m):
    lst = list(map(int, input().split()))
    for j in range(1, lst[0]):
        graph[lst[j]].append(lst[j+1])
        indegree[lst[j+1]]+=1

q = collections.deque()
ans = []
for i in range(1, n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    cur = q.popleft()
    ans.append(cur)
    for next in graph[cur]:
        indegree[next] -=1
        if indegree[next] ==0:
            q.append(next)


if len(ans) !=n:
    print(0)
else:
    print(*ans)