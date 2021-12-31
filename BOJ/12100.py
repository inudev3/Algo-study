#구슬탈출 문제와 마찬가지로 한 번의 이동에 전부 이동하는 것이 아니라
# 무한루프를 통해 이동이 끝날 때까지 이동해야 한다.
from sys import stdin
input = stdin.readline
dx= [0,0,1,-1]
dy = [1,-1,0,0]
LIMIT = 5
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for k in range(1<<(LIMIT*5)): #4가지 방향을 5번 이동
    dirs = gen(k)
def gen(k):
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k&3) #k의 마지막 2비트
        k>>2
    return a

def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a] # 복사본
    for dir in dirs:
        ok = False
        merged = [[False] * n for _ in range(n)]

        while True:
            ok = False
            if dir==0:
                for i in range(n-2,-1,-1):
                    for j in range(n):
                        if d[i][j] ==0:
                            continue
                        if d[i+1][j] ==0:
                            d[i+1][j] = d[i][j]
                            merged[i+1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i+1][j]== d[i][j]:
                            if not merged[i][j] and not merged[i+1][j]:
                                d[i+1][j] *=2
                                merged[i+1][j] = True
                                d[i][j] = 0
                                ok = True
            if dir==1:
                for i in range(1, n):
                    for j in range(n):
                        if d[i][j] ==0:
                            continue
                        if d[i-1][j]==0:
                            d[i-1][j] = d[i][j]
                            merged[i-1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i-1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i+1]
                                d[i-1][j] *=2
                                merged[i-1][j] = True
                                d[i][j] = 0
                                ok = True
