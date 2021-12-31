from collections import namedtuple
from sys import stdin

input = stdin.readline
switch = namedtuple('switch', ['success', 'count'])

def change(a, index):
    for i in range(index - 1, index + 2):
        if 0 <= i < N:
            a[i] = 1 - a[i]


def go(a, goal):

    n = len(a)
    ans = 0
    for i in range(n - 1):
        if a[i] != goal[i]:
            change(a, i + 1)
            ans += 1
    if a == goal:
        return switch(True, ans)
    else:
        return switch(False, ans)


n = int(input())
a = list(map(int, list(input().rstrip())))
goal = list(map(int, list(input().rstrip())))
b = a[:]  # 복사
p1 = go(a, goal)  # 0번 스위치를 누르지 않은 채로 그리디로 스위치를 눌러가보기
change(a, 0)  # 0번 스위치 누르고
p2 = go(a, goal)
if p2.success:
    p2 = switch(p2.success, p2.count + 1)  #0번을 누른 횟수를 포함시켜줌
if p1.success and p2.success:
    print(min(p1.count, p2.count))
elif p1.success:
    print(p1.count)
elif p2.success:
    print(p2.count)
else:
    print(-1)





