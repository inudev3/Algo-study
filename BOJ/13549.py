# 순간이동의 가중치가 0
# 매 단계마다 거리별로 큐를 따로 나눈 뒤에 BFS가 종료될 때 이를 합치면
# 가중치가 0인 경우에도 구할 수 있다(가중치가 0이여도 BFS 가능)

# 2가지 방법
# 1. 가중치의 가짓수만큼의 큐를 생성해서 가중치별로 큐에 인큐한 다음, 하나의 큐가 전부 pop되면 다음 큐로 변경하고 다음큐를 새로 만드는 방법
# 2. 덱을사용하는 방법. 하나의 덱을 만들고, 가중치 크기의 순서대로 작은건 appendleft, 큰건 append하면 가중치의 순서대로 큐가 정렬되므 하나의 큐만 사용가능
# 파이썬에서는 덱과 큐가 같다.
import collections

N, K = map(int, input().split())

# 덱 1개
limit = 200000
dist = [-1] * limit
check = [False] * limit
q = collections.deque()
q.append(N)
dist[N] = 0
while q:
    now = q.popleft()
    if now * 2 < limit and check[now * 2] is False:
        q.appendleft(now*2)
        check[now*2] = True
        dist[now * 2] = dist[now]
    for nxt in [now - 1, now + 1]:
        if 0 <= nxt < limit and check[nxt] is False:
            q.append(nxt)
            check[nxt] = True
            dist[nxt] = dist[now] + 1
print(dist[K])

##다음 큐로 옮기는 방법
# next_queue =collections.deque()
#
# while q:
#     now = q.popleft()
#     if now*2<limit and check[now*2] is False:
#         q.append(now*2)
#         dist[now*2] = dist[now]
#         check[now*2] = True
#     for nxt in [now+1, now-1]:
#         if 0<=nxt<limit and check[nxt] is False:
#             next_queue.append(nxt)
#             dist[nxt] = dist[now] +1
#             check[nxt] = True
#     if not q:
#         q = next_queue
#         next_queue = collections.deque()
# print(dist[K])
