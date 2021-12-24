import sys

sys.setrecursionlimit(1000000)

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    color = [0] * n
    for _ in range(m):
        u, v = map(int, sys.stdin.eadline().split())
        a[u - 1].append(v - 1)
        a[v - 1].append(u - 1)


    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:  # 방문안했으면 0, 1에서 방문할 경우는 2, 2에서 방문할 경우는 3이므로
                dfs(y, 3 - c)  # 서로 반대의 정점을 3-c로 표현 가능


    ans = True
    for i in range(n):
        if color[i] == 0:
            dfs(i, 1)  # 그룹 1로 dfs 시작
    for i in range(n):
        for j in a[i]:
            if color[i] == color[j]:
                ans = False
    print('YES' if ans else 'NO')
