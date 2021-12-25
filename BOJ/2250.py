# 인오더의 순서로 열방향을 탐색할 수 있다.
# 트리의 입력을 받을 때는 부모의 수를 카운터해서
# 부모의 수가 0인 노드가 root가 된다. 번호 1번이 루트가 아님
import sys

sys.setrecursionlimit(10000000)
class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.depth = 0
        self.order = 0


def inorder(node, depth):
    global order
    if node == -1:  ## 자식이 없는 리프 노드
        return
    inorder(a[node].left, depth + 1)
    a[node].depth = depth
    order+=1
    a[node].order = order
    inorder(a[node].right, depth + 1)


order = 0
N = int(input())
limit = 10001
a = [Node() for _ in range(limit)]
cnt = [0] * limit
posMin = [0] * limit  # 각 깊이에서 인오더 순서의 최소값과 최대값을 각각 저장
posMax = [0] * limit
for _ in range(N):
    i, left, right = map(int, input().split())
    a[i].left, a[i].right = left, right
    if left != -1: cnt[left] += 1
    if right != -1: cnt[right] += 1
root = 0
for i in range(1, N + 1):
    if cnt[i] == 0:
        root = i  # 부모가 없는 노드가 루트
inorder(root, 1)
maxDepth = 0

for i in range(1, N + 1):
    depth = a[i].depth
    order = a[i].order
    if posMin[depth] == 0:  # 해당깊이의 다른 노드의 순서가 정의되어 있지 않으면
        posMin[depth] = order  # 해당노드의 순서를 최소값으로 한다.
    else:
        posMin[depth] = min(posMin[depth], order)
    posMax[depth] = max(posMax[depth], order)
    maxDepth = max(maxDepth, depth)

ans = 0
ans_level = 0
for i in range(1, maxDepth + 1):
    if ans < posMax[i] - posMin[i] + 1:
        ans = posMax[i] - posMin[i] + 1
        ans_level = i
print(ans_level, end=" ")
print(ans)
