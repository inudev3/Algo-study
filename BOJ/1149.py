from collections import namedtuple

n = int(input())

RGB = namedtuple('RGB', ['red', 'green', 'blue'])

a = [RGB(0,0,0)]+ [RGB(*map(int, input().split())) for _ in range(n)]


D = [[0] *3 for _ in range(n+1)]

D[0] = [0,0,0]
for i in range(1, n+1):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + a[i].red
    D[i][1] = min(D[i - 1][0], D[i - 1][2]) + a[i].green
    D[i][2] = min(D[i - 1][0], D[i - 1][1]) + a[i].blue
print(min(D[n]))

