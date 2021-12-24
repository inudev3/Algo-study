import collections

N = int(input())
a = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

order = list(map(int, input().split()))
order = [x - 1 for x in order]
check = [False] * N
parent = [-1] * N
q = collections.deque()
q.append(0)
check[0] = True
m = 1  # 큐의 크기
for i in range(N):
    if not q:
        print(0)
        exit()
    x = q.popleft()
    if x != order[i]:  # 순서가 올바르지 않으면
        print(0)
        exit()
    cnt = 0
    for y in a[x]:
        if not check[y]:
            parent[y] = x
            cnt += 1
    for j in range(cnt):
        if m + j >= N or parent[order[m + j]] != x:
            print(0)
            exit()
        q.append(order[m + j])
        check[order[m + j]] = True
    m += cnt
print(1)
