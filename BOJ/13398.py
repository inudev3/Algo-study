n = int(input())
a = list(map(int, input().split()))
D = [0]*(n+1) # 끝나는 최대 연속합
D2 = [0]*(n+1) #시작하 최대연속합
for i in range(n):
    D[i] = a[i]
    D[i] = max(D[i-1]+a[i],a[i])

for i in range(n-1, -1, -1):
    D2[i] = a[i]
    D2[i] = max(D2[i+1]+a[i], a[i])
ans = max(D)
for i in range(1, n-1):
    if D[i-1]+D2[i+1] > ans:
        ans = D[i-1]+D2[i+1]
print(ans)

