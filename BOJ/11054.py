from sys import stdin
N = int(input())
A = list(map(int, stdin.readline().split()))
D = [1]*N
D2 = [1]* N
result = [0]*(N)
for i in range(N):
    for j in range(i):
        if A[j]<A[i] and D[j]+1>D[i]:
            D[i] = max(D[i],D[j]+1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[j]< A[i] and D2[j] + 1 > D2[i]:
            D2[i] = D2[j] + 1
for i in range(N):
    result[i] += D[i] + D2[i]-1

print(max(result))