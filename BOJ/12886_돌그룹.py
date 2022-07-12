# 3개 그룹의 합을 N이라고 했을 때,  2 개의 그룹의 개수만 정해진다면 나머지 개수는 N-A-B로 자동으로 결정됨
## 따라서 시간복잡도는 돌의 가능한 개수인 1500^2가 , BFS탐색으로 해결 가능
import sys

sys.setrecursionlimit(1500 * 1500)
check = [[False] * 1501 for _ in range(1501)]
x, y, z = map(int, input().split())
s = x + y + z


def go(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, s - x - y]
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, s - x - y]
                b[i] += a[i]
                b[j] -= a[j]
                go(b[0], b[1])


if s % 3 != 0:
    print(0)
else:
    go(x, y)
    if check[s // 3][s // 3]:
        print(1)
    else:
        print(0)
