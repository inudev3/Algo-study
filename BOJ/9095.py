T = int(input())


def go(sum, goal):  # 경우의 수 구하기
    if sum > goal:
        return 0
    if sum == goal:
        return 1  # 방법의 수 1개 찾음
    now = 0
    for i in range(1, 4):
        now += go(sum + i, goal)  # 경우의 수 더해줌
    return now


while T:
    N = int(input())
    ans = go(0, 10)
    print(ans)
    T -= 1

# 15989
# 순서만 다른 것은 같은 것으로 취급한다.
# 오름차순만 계산하면 된다.
n = int(input())


def go(sum):
    if sum > n:
        return 0
    if sum == n:
        return 1
    ans = 0
    for k in range(1, 4):
        ans+=go(sum + k )
    return ans
