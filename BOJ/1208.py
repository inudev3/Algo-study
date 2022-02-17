import bisect
from collections import Counter

n, s = map(int, input().split())
a = list(map(int, input().split()))
m = n // 2  # 뒤
n = n - m  # 앞

x = []
y = []
first = [0] * (1<<n)
for i in range(1 << n):  # n개의 조합의 개수
    for j in range(n):
        if i & (1 << j):
            first[i]+= a[j]
second = [0] * (1<<m)
for i in range(1 << m):  ##조합의 개수
    for j in range(m):  ## 해당 조합의 값만큼 합을 계산해주기
        if i & (1 << j):
           second[i]+=a[j+n]

first.sort()
second.sort()
ans = 0
c = Counter(second)
for num in first:
    if num==s:
        ans+=1
    else:
        ans+= c[s-num]
print(ans)
