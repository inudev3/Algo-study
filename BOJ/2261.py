from collections import namedtuple

n=int(input())

ax = [Point(*map(int, input().split())) for _ in range(n)]
ay = ax[:]

a.sort()
Point= namedtuple('Point', ['x', 'y'])


def dist(p1:Point, p2:Point):
    return (p1.x-p2.x)**2 + (p1.y-p2.y)**2
def closest(a, start, end):
    n=end-start+1
    if n<=3:
        return brute_force(a,start,end)
    mid = (start+end)//2
    mid_p =
    left = closest(a,start,mid)
    right = closest(a, mid+1, end)
    ans = min(left, right)
    b = []
    for i in range(start, end+1):
        d = a[i].x - a[mid].x
        if (d*d < ans):
            b.append(a[i])



