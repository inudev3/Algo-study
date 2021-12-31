# 4가지 방향으로 기울이기
# 앞 방향과 반대방향으로 기울이거나 같은 방향으로 기울이는건 의미가 없다.
from sys import stdin


def gen(k):  # 정수 k를 4진법 수로 변환(4가지 방법의 경우의 선택)
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k & 3)  # 마지막 2비트(4진법으로 1개 자릿수)
        k >>= 2  # 비트 2자리, 4진법 한자리 이동
    return a  # 10자리 4진법 수


def valid(dir):
    l = len(dir)
    for i in range(l - 1):
        if dir[i] == 0 and dir[i + 1] == 1: return False  # 최소방법 수이므로 같은 위치로 돌아오게 되어 앞뒤로 반대방향으로 이동불가
        if dir[i] == 1 and dir[i + 1] == 0: return False
        if dir[i] == 2 and dir[i + 1] == 3: return False
        if dir[i] == 3 and dir[i + 1] == 2: return False
        if dir[i] == dir[i + 1]: return False  # 같은 방향으로 이동불가(제자리가 됨)
    return


def check(a, dir):
    n = len(a)
    m = len(a[0])  ##가로 세로 길이
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'O':
                hx, hy = i, j
            elif a[i][j] == 'R':
                rx, ry = i, j
            elif a[i][j] == 'B':
                bx, by = i, j
    cnt = 0
    for k in dir:
        cnt += 1
        hole1 = hole2 = False
        while True: ##기울이기는 멈출 때까지 이동하므로 이동이 멈출때까지 무한루프해야함
            (move1, reached1) = simulate(a, k, rx, ry)  # (이동여부, 구멍 도달 여부) 리턴함
            (move2, reached2) = simulate(a, k, bx, by)
            if not move1 and not move2: # 이동이 둘다 멈추면 해당 이동 명령 종료
                break
            if reached1: hole1 = True
            if reached2: hole2 = True
        if hole2: return -1 #파란구슬이 구멍에 빠지면 실패
        if hole1: return cnt #파란구슬이 구멍에 빠지는 경우를 제외하고 빨간구슬이 빠질경우에만 횟수 리턴
    return -1 ##구멍에 빠지지 못한 경우 실패

def simulate(a, k, x, y):
    if a[x][y] == '.': return (False, False) #두 구슬이 모두 구멍에 빠져서빈칸이면
    n = len(a)
    m = len(a[0])
    moved = False
    while True:
        nx , ny = x+dx[k], y+dy[k] #k는 4진수
        if a[nx][ny] == '#':
            return (moved, False)
        elif a[nx][ny] == 'R' or a[nx][ny] == 'B':
            return (moved, False)
        elif a[nx][ny] == '.':
            a[nx][ny], a[x][y] = a[x][y], a[nx][ny] #구슬을 해당칸으로 이동
            x = nx
            y = ny
            moved = True
        elif a[nx][ny] == 'O':
            a[x][y] = '.'
            moved = True
            return (moved, True)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
LIMIT = 10
N, M = map(int, stdin.readline())

a = [list(stdin.readline()) for _ in range(N)]
ans = -1
for k in range(1 << (LIMIT * 2)):  # 전체 경우의 수 4^10
    dir = gen(k)
    if valid(dir) is False: continue
    cur = check(a, dir)
    if cur == -1: continue
    if ans == -1 or ans > cur:
        ans = cur
print(ans)

