import sys
from collections import deque
from sys import stdin

input = sys.stdin.readline
print = sys.stdout.write
T = int(input())


def calc(p, arr):
    order = True
    f, b = 0, 0
    for i in p:
        if i == 'R':
            order = not order
        elif i == 'D':
            if order:
                f += 1
            else:
                b += 1

    if f + b <= n:
        arr = arr[f:n - b]
        if not order:
            return '[' + ','.join(arr[::-1]) + ']\n'
        else:
            return '[' + ','.join(arr) + ']\n'
    else:
        return 'Error\n'


for k in range(T):
    print('%d'%k)
    p = input().rstrip()
    n = int(input())
    li = input().rstrip()[1:-1].split(',')
    p = p.replace('RR', '')
    print(calc(p, li))
