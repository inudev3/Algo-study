import sys
from collections import namedtuple

input = sys.stdin.readline
n = int(input())
Meeting = namedtuple('Meeting', ['begin', 'end'])
a = [Meeting(*map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: (x.end, x.begin))

cnt = 1
last = a[0]
for i in range(1, n):
    if a[i].begin >= last.end:
        cnt += 1
        last = a[i]
print(cnt)








