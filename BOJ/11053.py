from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))

D = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            D[i] = max(D[i], D[j]+1)

print(max(D))

D2 = [1]*n
for i in range(n,-1,-1):
    for j in range(i,n):
        if arr[i]>arr[j]:
            D2[i] = max(D[i], D[j]+1)

ans = [0] * n
for i in range(n):
    ans[i] = D[i]+D2[i]-1

print(max(ans))