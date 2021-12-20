from sys import stdin


def check(candies):
    n = len(candies)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candies[i][j] == candies[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt: ans = cnt
        cnt = 1
        for j in range(1, n):
            if candies[j][i] == candies[j][i - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt: ans = cnt
    return ans


def checkSwapped(candies, i, j, row):
    n = len(candies)
    ans = 1
    for k in range(1, n):

        cnt  =1
        if row is True:
            if candies[i][k] == candies[i][k - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        else:
            if candies[k][j] == candies[k-1][j]:
                cnt+=1
            else:
                cnt = 1
            if ans<cnt:
                ans = cnt
    for k in range(n):
        if row is True:
            if j+1<n:
                candies[k][j] == candies[k+1][j]






N = int(input())

candies = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = check(candies)
row = True
for i in range(N):
    for j in range(N):
        cnt = 1
        if i + 1 < N:
            cnt = checkSwapped(candies, i, j, row)
            if ans<cnt: ans= cnt
        if j + 1 < N:
            row = False
            cnat = checkSwapped(candies, i, j , row)
            if ans < cnt: ans = cnt

print(ans)
