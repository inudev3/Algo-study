import sys


input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))

# 이분 분할
m = n // 2
n = n - m
first = [0] * (1 << n)  # 왼쪽 subset
for i in range(1 << n):
    for k in range(n):
        if (i & (i << k)) > 0:  # k번째 수가 subset에 포함되어 있으면
            first[i] += a[k]

second = [0] * (1 << m)
for i in range(1 << m):
    for k in range(m):
        if (i & (i << k)) > 0:
            second[i] += a[n + k]

first.sort()  ##오름차순 정렬
second.sort(reverse=True)  ##내림차순 정렬

n = (1 << n)  # first 길이
m = (1 << m)  # second 길이
i = 0
j = 0
ans = 0
while i < n and j < m:
    if first[i] + second[j] == s:
        c1 = 1  # 수의 개수 카운트
        c2 = 1
        i += 1
        j += 1
        while i < n and first[i] == first[i - 1]:
            c1 += 1
            i += 1
        while j < m and second[j] == second[j - 1]:
            c2 += 1
            j += 1
        ans += c1 * c2
    elif first[i] + second[j] > s:
        j += 1
    else:
        i += 1
if s == 0:  ##s가 0인 경우에는 공집합의 경우만 하나 빼주면 된다.
    ans -= 1

print(ans)
