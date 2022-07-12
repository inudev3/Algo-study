
##위상정렬
import collections


def topology(graph, indegree):
    queue = collections.deque()

    for i in range(len(graph)):
        if indegree[i]==0:
            DP[i] = costs[i]
            queue.append(i)
    while queue:
        now = queue.popleft()

        for next in graph[now]:
            indegree[next]-=1
            DP[next] = max(DP[now]+costs[next], DP[next])
            if indegree[next]==0:
                queue.append(next)

T = int(input())
for _ in range(T):
    n, k =map(int, input().split())
    costs = [0]+list(map(int, input().split()))
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    DP = [0 for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b]+=1
    goal = int(input())
    topology(graph,indegree)
    print(DP[goal])

