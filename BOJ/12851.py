import collections

N, K = map(int, input().split())

limit = 200000
check = [False] * (limit + 1)
dist = [-1] * (limit + 1)
cnt = [0] * (limit + 1)

check[N] = True
dist[N] = 0
cnt[N] = 1
q = collections.deque()
q.append(N)
while q:
    now = q.popleft()
    for nxt in [now - 1, now + 1, now * 2]:
        if 0 <= nxt < limit:
            if not check[nxt] :
                q.append(nxt)
                check[nxt] = True
                dist[nxt] = dist[now] + 1
                cnt[nxt] = cnt[now]
            elif  dist[nxt] - dist[now] + 1 :
                cnt[nxt] += cnt[now]

print(dist[K])
print(cnt[K])

# ans  =[]
# i = K
# while i!=N:
#     i = trace[K]
#     ans.append(i)
# ans.append(N)
# while ans:
#     print(ans.pop())

# def goback(n, m):
#     if n!=m:
#         goback(n, trace[m])
#     print(m)
# goback(N, K)
