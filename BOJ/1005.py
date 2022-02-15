import collections

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    inDegree = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    DP = [0 for _ in range(n+1)]


    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    win = int(input())

    q = collections.deque()
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            q.append(i)
            DP[i] = D[i]

    while q:
        x = q.popleft()
        for next in graph[x]:
            inDegree[next] -= 1
            DP[next] = max(DP[x]+D[next], DP[next])
            if inDegree[next] == 0:
                q.append(next)
    print(DP[win])
# //DAG는 선행관계를 나타내는 데에 사용된다.
# //DAG에서 선후관계에 따라 정렬하는 데에 위상정렬을 사용할 수 있다.
# //그래프의 간선에 선후관계가 있을 때 정점의 순서를 찾는 알고리즘이 위상정렬
