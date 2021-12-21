##항상 경우의 수가 1억개:1초를 기준으로 그보다 적은지 많은지 판단해야 함

N = int(input())
T = list(range(N+1))
P = list(range(N+1))

for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

ans = 0
def go(day, sum ):
    global ans
    if day == N + 1:
        ans = max(ans, sum)
        return
    if day > N+1:
        return
    go(day+T[day],sum+P[day])
    go(day+1, sum)

go(1, 0)
print(ans)
