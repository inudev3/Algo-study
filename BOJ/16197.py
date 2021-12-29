from sys import stdin

N, M = map(int, stdin.readline().split())
a = [list(stdin.readline()) for _ in range(N)]
x1 = y1 = x2 = y2 = -1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    for j in range(M):
        if a[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            a[i][j] = '.'  # 두동전의 좌표를 계산하고 빈칸으로 만들어줌(이동 가능하니까)


def go(cnt, x1, y1, x2, y2):
    # 불가능한 경우: 두 동전 모두 떨어진 경우
    # 정답: 두 동전 중 하나만 떨어진 경우
    fall1 = fall2 = False
    if cnt == 11:
        return -1
    if x1 >= N or x1 < 0 or y1 < 0 or y1 >= M: fall1 = True
    if x2 >= N or x2 < 0 or y2 < 0 or y2 >= M: fall2 = True
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return cnt
    ans = -1
    for k in range(4):
        nx1, ny1= x1 + dx[k], y1 + dy[k]
        nx2, ny2 = x2 + dx[k], y2 + dy[k]
        if 0 <= nx1 < N and 0 <= ny1 < M and a[nx1][ny1] == '#':  # 벽인 경우 제자리
            nx1, ny1 = x1, y1
        if 0 <= nx2 < N and 0 <= ny2 < M and a[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        tmp = go(cnt + 1, nx1, ny1, nx2, ny2)
        if tmp == -1:  # 불가능하면 건너뛰고
            continue
        if ans == -1 or ans > tmp:  # 가능하면 최소값 저장
            ans = tmp
    return ans  # 최소값을 리턴


##벽의 정보를 다 넘기지 않고 동전의 위치만 함수의 인자로 넘겨 이동을 재귀로 확인한다.
print(go(0, x1, y1, x2, y2))
