#두 수 M,N이 주어졌을 때 x<M, y<N인 자연수 x, y로 연도를 <x,y>와 같이 표현한다고 하자
# 이 때 주어진 <x,y>에 대해 몇 번째 해인지 구하는 문제
M = int(input())
N = int(input())
x,y = list(map(int, input().split()))
#x-1, y-1에 대해 게산하고 나머지 연산을 하는 것이 좋음
x=-1
y=-1
ok = False

for i in range(x, N*M, M):
    if i%N == y:
        print(y+1)
        ok = True
        break
if not ok:
    print(-1)



