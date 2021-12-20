#n개의 동전
#합이 k

n, k = list(map(int, input()))

coins = [int(input()) for _ in range(n)]

cnt =[0] *n

selected=0
ans = []
for i in range(len(coins)):

     k -= coins[i]
     cnt[i]+=1
     for j in range(k, )




def go2(index, selected, n, m):
    if selected == k:
        print(a)
        return
    for i in range(k-selected, 0, -1):
        if i in coins:

    if selected == m:
        print(a)
        return
    if index > n:
        return
    for i in range(m - selected, 0, -1):
        a[index] = i  ##몇번 중복허용할 것인지
        go2(index + 1, selected + i, n, m)
    a[index] = 0
    go2(index + 1, selected, n, m)
