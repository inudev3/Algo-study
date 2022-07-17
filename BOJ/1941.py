import collections
import heapq
import sys

arr = [input() for i in range(5)]

prin = [[0 for i in range(5)] for j in range(5)]

diry = [1,-1,0,0]
dirx = [0,0,1,-1]

visit = [[0 for i in range(5)] for j in range(5)]
ans = 0
p = []


def check(s):
    global visit
    y = s // 5
    x = s % 5

    for i in range(4):
        ty = y + diry[i]
        tx = x + dirx[i]

        if ty >= 0 and ty < 5 and tx >= 0 and tx < 5:
            if visit[ty][tx] == 0:
                if (ty * 5 + tx) in p:
                    visit[ty][tx] = 1
                    check((ty * 5 + tx))
