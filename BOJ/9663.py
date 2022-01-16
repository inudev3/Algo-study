

def check(row, col):
    for i in range(n):
        if i == row:
            continue
        if a[i][col]:
            return False
    x = row - 1
    y = col - 1
    while x >= 0 and y >= 0:  ##한방향으로만 진행
        if a[x][y]:
            return False
        x -= 1
        y -= 1
    x = row - 1
    y = col + 1
    while x >= 0 and y < n:
        if a[x][y]:
            return False
        x -= 1
        y += 1
    return True


# 행 row에 퀸의 위치를 어디에 놓을건지 계산하는 함수:

def calc(row):
    if row == n:  ##끝에 도달하면 방법의 수 1개 추가
        global ans
        ans += 1
        return
    for col in range(n):  ##행에 퀸을 놓을 수 있는 모든 경우의 수 조사
        a[row][col] = True
        if check(row, col):
            calc(row + 1)
        a[row][col] = False

n = int(input())
a = [[False] * n for _ in range(n)]

ans = 0
calc(0)
print(ans)
