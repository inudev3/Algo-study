import heapq
n, m = map(int, input().split())
problem = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

q = []
result = []
for _ in range(m):
    x, y = map(int, input().split())
    problem[x].append(y)
    indegree[y]+=1

for  i in range(1, n+1):
    if indegree[i]==0:
        heapq.heappush(q, i)
while q:
    first = heapq.heappop(q)
    result.append(first)
    for next in problem[first]:
        indegree[next]-=1
        if indegree[next]==0:
            heapq.heappush(q, next)

for i in result:
    print(i, end=" ")
