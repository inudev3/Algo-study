T = int(input())

def go( sum, goal): # 경우의 수 구하기
    if sum>goal:
        return 0
    if sum==goal:
        return 1 #방법의 수 1개 찾음
    now = 0
    for i in range(1, 4):
        now += go(sum+i, goal) # 경우의 수 더해줌
    return now

while T:
    N = int(input())
    ans = go(0, 10)
    print(ans)
    T-=1