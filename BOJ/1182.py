N, S = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, (1 << N)):  # 공집합은 포함안하므로 0은 제외
    s = sum(a[k] for k in range(N) if (i & (1 << k)) > 0)
    if S == s:
        ans += 1
