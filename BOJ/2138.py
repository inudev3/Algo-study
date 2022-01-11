from collections import namedtuple
from sys import stdin

input = stdin.readline
switch = namedtuple('switch', ['success', 'count'])

def change(a, index):
    n = len(a);
    for i in range(index-1, index+2):
        if 0<=i<n:
            a[i] = 1-a[i]

def go(a, goal):
    n = len(a)
    ans =0
    for i in range(n-1):
        if a[i]!= goal[i]:
            change(a, i+1)
            ans+=1
    ok = True
    for i in range(n):
        if a[i]!= goal[i]:
            ok = False
    if ok:
        return switch(True, ans)
    else:
        return switch(False, ans)
n = int(input())
a = list(map(int, list(input().strip())))
goal = list(map(int, list(input().strip())))
b = a[:]
p1 = go(b, goal)
change(a, 0)
p2 = go(a, goal)
if p2.success:
    p2 = switch(p2.success, p2.count+1)
if p1.success and p2.success:
    print(min(p1.count, p2.count))
elif p1.success:
    print(p1.count)
elif p2.success:
    print(p2.count)
else:
    print(-1)













