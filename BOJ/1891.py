n, a = input().split()
n = int(n)
size = 2 ** n
x, y = go(0, 0, 0, size)
dy, dx = map(int, input().split())
dx = -dx
x += dx
y += dy


def gogo(r, c, size, x, y):  # 좌표에서 사분면 번호로 변환하는 함수
    if size == 1:
        return ''
    m = size // 2
    if x < r + m and y < c + m:
        return '2' + gogo(r, c, m, x, y)
    elif x < r + m and y >= c + m:
        return '1' + gogo(r, c + m, m, x, y)
    elif x >= r + m and y < c + m:
        return '3' + gogo(r + m, c, m, x, y)
    else:
        return '4' + gogo(r + m, c + m, m, x, y)


def go(index, x, y, size):  ##사분면 벊로 좌표 찾는 함수
    if size == 1:
        return (x, y)
    else:
        m = size // 2
        if a[index] == '1':
            return go(index + 1, x, y + m, m)
        elif a[index] == '2':
            return go(index + 1, x, y, m)
        elif a[index] == '3':
            return go(index + 1, x + m, y, m)
        elif a[index] == '4':
            return go(index + 1, x + m, y + m, m)
