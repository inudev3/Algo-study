import sys

input = sys.stdin.readline
n = int(input())
a = [0] * (n+1)
for i in range(1, n+1):
    a[i] = int(input())

D= [[0]*3 for _ in range(n+1)] #마시지 않았거나, 1번 연속해서 마셨거나, 2번 연속해서 마셨거나

D[1][1] = a[1]

if n>=2:
    D[2][2] = a[1]+ a[2]
    D[2][1] = a[2]
    D[2][0] = a[1]
for i in range(3, n+1):
    D[i][0] = max(D[i-1])
    D[i][1] = max(D[i-2]) + a[i]
    D[i][2] = max(D[i-3])+a[i]+a[i-1]

print(max(D[n]))