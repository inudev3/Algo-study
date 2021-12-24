import collections

N, K = list(map(int, input().split()))
# x->x+1 or x-1 or 2x, 가중치는 시간, 최소비용은 시간
# 정점: 위치 간선: 위치 간의 이동
limit = 200000
check = [False] * (limit+1)
dist = [-1] * (limit+1)
check[N] = True
dist[N] = 0
trace = [-1] *(limit+1)
q = collections.deque()
q.append(N)
while q:
    now = q.popleft()
    for nxt in [now - 1, now + 1, now * 2]:
        if 0 <= nxt < limit and not check[nxt]:
            trace[nxt] = now
            q.append(nxt)
            check[nxt] = True
            dist[nxt] = dist[now] + 1
print(dist[K])

# ans  =[]
# i = K
# while i!=N:
#     i = trace[K]
#     ans.append(i)
# ans.append(N)
# while ans:
#     print(ans.pop())

def goback(n, m):
    if n!=m:
        goback(n, trace[m])
    print(m)
goback(N, K)