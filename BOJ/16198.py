from sys import stdin
N = int(stdin.readline())
W = list(map(int, stdin.readline()))

def go(w):
    n = len(w)
    if n==2:
        return 0
    ans = 0
    for i in range(1, n-1):#양끝의 구슬은 제외하고 뽑는다.
        energy = w[i-1]*w[i+1]
        b = w[:i]+ w[i+1:]
        energy+= go(b)
        if ans<energy:
            ans = energy
    return ans