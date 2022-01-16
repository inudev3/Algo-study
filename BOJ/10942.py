import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [[-1] * n for _ in range(n)]  # i번째 부터 j번째 까지 팰린드롬인지 아닌지(1또는 0)


def go(i, j):
    if i == j:  # 길이 1
        return 1
    elif i + 1 == j:  # 길이 2
        if a[i] == a[j]:
            return 1
        else:
            return 0
    if d[i][j] != -1:  ##메모이제이션
        return d[i][j]
    if a[i] != a[j]:
        d[i][j] = 0
    else:
        d[i][j] = go(i + 1, j - 1)  ##현재 글자가 팰린드롬이면 다음 글자 재귀적으로 체크
    return d[i][j]


m = int(input())

for _ in range(m):
    s, e = map(int, input().split())
    print(go(s - 1, e - 1))

for i in range(n):
    d[i][i] = True
for i in range(n - 1):
    if a[i] == a[i + 1]:
        d[i][i + 1] = True  # 2개
for k in range(3, n + 1):  ##수열의 길이 3개이상부터
    for i in range(0, n - k + 1):  ##시작 위치
        j = i + k - 1  ##끝나는 위치
        if a[i] == a[j] and d[i + 1][j - 1]:  ##양끝이 같고 사이가 팰린드롬이면
            d[i][j] = True
