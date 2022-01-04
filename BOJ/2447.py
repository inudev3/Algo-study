n = int(input())

STAR = "*"
BLANK = " "
a = [[BLANK] * n for _ in range(n)]


def go(x, y, n, color):
    if color == BLANK: ##먼저 가운데에 공백을 만든 다음
        for i in range(x, x + n):
            for j in range(y, y + n):
                a[i][j] = BLANK
    else: # 나머지 채우는 부분들은 사이즈를 분할하면서 재귀적으로 공백을 추가하도록 한다.
        if n == 1:
            a[x][y] = STAR
        else:
            newColor = STAR
            m = n // 3
            for i in range(3):  ##3등분 해서 나눠그린다.
                for j in range(3):
                    if i == 1 and j == 1:
                        newColor = BLANK
                    else:
                        newColor = STAR
                    go(x + m * i, y + m * j, m, newColor)
