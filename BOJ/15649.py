M, N = list(map(int, input()))

check = [False] * 10
a = [0] * 10


def go(index, n, m):
    if index==m:
        print(a)
    for i in range(1, n+1):
        if check[i]:
            continue
        check[i]= True
        a[index] = i
        go(index+1, n, m)
        check[i] = False
go(0, N, M)