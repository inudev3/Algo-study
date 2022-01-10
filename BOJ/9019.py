import collections
import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline
T = int(input())
dx = ['D', 'S','L','R']
def possible(now):
    d = (now*2) % 10000
    s = 9999 if now==0 else now-1
    l = (now%1000) * 10 + now//1000
    r = now//10 + (now%10) * 1000
    return [d,s,l,r]
def go(a,b):
    if a==b: return
    go(a, From[b])
    print(How[b], end='')


for _ in range(T):
    From = [0] * 10001
    How = [''] * 10001
    dist = [-1] * 10001
    a, b = map(int, input().split())
    q = collections.deque()
    q.append(a)
    dist[a] = 0
    while q:
        now = q.popleft()
        for i in range(4):
            next = possible(now)[i]
            if dist[next] == -1:
                q.append(next)
                dist[next] = dist[now]+1
                From[next] = now
                How[next] = dx[i]
    go(a,b)
    print()

