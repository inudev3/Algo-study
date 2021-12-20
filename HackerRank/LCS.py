def lcs(a, b):
    x = len(a)
    y = len(b)
    L = [[0] * y for _ in range(x)]
    ans = []
    for i in range(x):
        for j in range(y):
            if x == 0 or y == 0:
                L[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                L[i][j] = 1 + L[i - 1][j - 1]
                ans.append(a[i-1])
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    print(ans)


