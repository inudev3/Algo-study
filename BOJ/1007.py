import sys
import math
import itertools

input = sys.stdin.readline
T = int(input())
results = []
for _ in range(T):
    n = int(input())
    coords = []
    xsum = 0
    ysum = 0
    for _ in range(n):
        x, y, = map(int, input().split())
        xsum += x
        ysum += y
        coords.append([x,y])
        comb = itertools.combinations(coords, n//2)
    n//2
    브루트

