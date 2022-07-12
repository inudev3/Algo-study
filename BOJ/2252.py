import heapq

n, m = map(int, input().split())

students = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

q = []
result = []
for _ in range(m):
    x, y = map(int, input().split())
    students[x].append(y)
    indegree[y] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    result.append(cur)
    for next in students[cur]:
        indegree[next]-=1
        if indegree[next]==0:
            q.append(next)

for student in result:
    print(student, " ")
