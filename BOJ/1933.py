import sys
from collections import namedtuple

input = sys.stdin.readline
Building = namedtuple('Building', ['left', 'height', 'right'])
Pair = namedtuple('Pair', ['x', 'height'])

n = int(input())
a = [Building(*map(int, input().split())) for _ in range(n)]
a.sort()
def append(ans:[Pair], p:Pair): #
    if ans:
        if ans[-1].height == p.height:
            return ##높이가 같으면 추가 하지 않음
        if ans[-1].x == p.x:
            ans[-1] = Pair(ans[-1].x, p.height)
            return
    ans += [p]

def merge(l:[Pair],r:[Pair]):
    ans=[]
    h1 = 0
    h2 = 0
    i=j=0
    while i<len(l) and j<len(r):
        u = l[i]
        v = r[j]
        if u.x<v.x:
            x = u.x
            h1 = u.height
            h = max(h1,h2)
            append(ans, Pair(x,h))
            i+=1
        else:
            x=v.x
            h2 = v.height
            h = max(h1,h2)
            append(ans, Pair(x,h))
            j+=1
    while i<len(l):
        ans.append(l[i])
        i+=1
    while j<len(j):
        ans.append(r[j])
        j+=1
def go(a:[Building], start, end):#분할정복(머지소트)로 나눈 뒤 합친다.
    if start==end: #빌딩 1개
        return [
            Pair(a[start].left, a[start].height),
            Pair(a[start].right, 0)
        ]
    mid = (start+end)//2
    l = go(a, start, mid)
    r = go(a, mid+1, end)
    return merge(l,r)

go(a, 0, n)