# 조건에 따라 간선이 나뉜다면(유무가 다르다면)
# 조건에 따라 서로 다른 정점임
# 따라서 이럴 때는 map으로 묶어서 (V, 조건)
# 식으로 정점의 조건을 나눠줘야함 2차원으로
# (s,c)-> (s,s)(복사) (s+c,c)(붙여넣기), (s-1,c)(삭제)
import collections

S = int(input())
limit = 1001
d = [[-1] * limit for _ in range(limit)]  # 이모티콘의 개수마다 클립보드의 개수 limit개의 상태를 각각 가짐

q = collections.deque()
q.append((1, 0))
d[1][0] = 0
while q:
    s, c = q.popleft()
    if d[s][s] == -1:  # 복사가 가능할 경우
        d[s][s] = d[s][c] + 1
        q.append((s, s))
    if d[s + c][c] == -1 and s + c < S:
        d[s + c][c] = d[s][c] + 1
        q.append((s + c, c))
    if s >= 1 and d[s - 1][c] == -1:
        d[s - 1][c] = d[s][c] + 1
        q.append((s - 1, c))
ans = 1
for i in range(S):
    if d[S][i] != -1:
        if ans == -1 or ans > d[S][i]:
            ans = d[S][i]
print(ans)
