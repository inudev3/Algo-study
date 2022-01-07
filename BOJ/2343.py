# 순서가 바뀌면 안됨

# 그룹의 합의 최대값의 최소값을 구하는 문제
# 이분탐색으로 구할 수 있다.
# 블루레이의 개수가 M보다 작으면 크기를 줄이고, M보다 크다면 크기를 키운다.
# 블루레이 크기의 최소값: 레슨 한개 크기의 최대값

from sys import stdin

input = stdin.readline
n, m = map(int, input().split())

lessons = list(map(int, input().split()))


def go(lessons, m, x):
    cnt = 1
    tmp = 0
    for i in range(n):
        if tmp + lessons[i] > x:
            cnt += 1
            tmp = lessons[i]
        else:
            tmp += lessons[i]
    return cnt <= m


left = max(lessons)
right = sum(lessons)  # 최대크기
ans = 0
while left <= right:
    mid = (left + right) // 2
    if go(lessons, m, mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
