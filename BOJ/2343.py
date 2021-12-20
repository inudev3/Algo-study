# 순서가 바뀌면 안됨
from sys import stdin

N, M = map(int, stdin.readline().split())

lessons = list(map(int, stdin.readline().split()))

low = -1

for i in range(len(lessons)):
    low = max(low, lessons[i])  # 최소크기
Sum = sum(lessons)

high = Sum  # 최대크기

while low <= high:
    cnt = 0
    tmp = 0
    mid = (low + high) // 2
    for i in range(N):
        if tmp + lessons[i] > mid:  # 중간값과 비교
            tmp = 0
            cnt += 1
        tmp += lessons[i]
    if tmp != 0:
        cnt += 1
    if cnt <= M:
        high = mid - 1
    else:
        low = mid + 1
print(low)
