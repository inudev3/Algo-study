def redJohn(n):
    # Write your code here
    D = [0] * 41
    D[1] = 1
    D[2] = 1
    D[3] = 1
    D[4] = 2
    if n > 4:
        D[n] = D[n - 1] + D[n - 4]
    x = D[40]
    a = [False, False] + [True for _ in range(x + 1)]
    cnt = 0
    m = int(x ** 0.5) + 1
    for i in range(2, n):
        if a[i]:
            for j in range(2 * i, m+1, i):
                a[j] = False
    for i in a:
        if i is True:
            cnt += 1

    return cnt


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    result = redJohn(n)
    print(result)
