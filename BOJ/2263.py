# 포스트오더의 가장 마지막은 루트
##포스트오더-> 좌->우=>루트
# 인오더=>좌->루트=>우
import sys

input = sys.stdin.readline
write = sys.stdin.write
sys.setrecursionlimit(1000000)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (n + 1)  ## 정점 i의 인오더에서의 위치 저장
for i in range(n):
    position[inorder[i]] = i


def solve(in_start, in_end, post_start, post_end):
    if in_start >= in_end or post_start > post_end:
        return
    root = postorder[post_end]
    write('%d' % root)  # 프리오더 출력
    p = position[root]  # 루트의 인오더에서 위치
    left = p - in_start
    solve(in_start, p - 1, post_start, post_start + left - 1)  # Left tree 프리오더는 루트->좌->우
    solve(p + 1, in_end, post_start + left, post_end - 1)  # Right Tree

solve(0, n-1, 0, n-1)