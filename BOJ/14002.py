n = int(input())
a = list(map(int, input().split()))
d = [0] * n
v = [-1] * n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
            v[i] = j
ans = max(d)
p = [i for i, x in enumerate(d) if x == ans][0]
print(ans)
res = []
while p != -1:
    res.append(a[p])
    p = v[p]
for num in res:
    print(num, end=" ")


n = int(input())
a = list(map(int, input().split()))
D = [a[i] for i in range(n)]
for i in range(1,n):
    if D[i-1]+a[i] > a[i]:
        D[i] = D[i-1]+a[i]

print(max(D))
