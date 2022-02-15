n = int(input())
a = list(map(int, input().split()))
goal = a[-1]
D = [[0]*21 for _ in range(n-1)]
D[0][a[0]] =1
#0은 플러스 1은 마이너스

for i in range(n-1):
    for j in range(21):
        if j-a[i]>=0:
            D[i][j] += D[i-1][j-a[i]]
        if j+a[i]<=20:
            D[i][j] += D[i-1][j+a[i]]
print(D[n-2][goal]