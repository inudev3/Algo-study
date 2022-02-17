n, s = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = 0



sum = a[0]
ans = n+1
while i <= j and j < n:
    if sum < s:
        j += 1
        if j < n:
            sum += a[j]
    elif sum == s:
        ans = min(j - i + 1, ans)
        j += 1
        if j < n:  # 찾았을 때 r을 증가시켜주면 됨. i가 증가하면 i==j일 때 순서가 바뀌므로
            sum += a[j]
    else:
        ans = min(j - i + 1, ans)
        sum -= a[i]
        i += 1
        if i > j and i < n:
            j = i
            sum = a[i]

if ans>n:
    ans=0
print(ans)
