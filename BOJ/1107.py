

def possible(c): ##숫자버튼을 누르는 횟수
    if c==0: #0인 경우 예외처리
        if broken[0]:
            return 0
        else:
            return 1
    len = 0
    while c>0:
        if broken[c%10]: #가장 마지막수에 대해서 고장난 버튼인지 검사, 모든 자릿수에 대해 검사함
            return 0
        c //= 10
        len+=1
    return len
#숫자버튼을 먼저 눌러야 하며, +나 -중 하나만 연속해서 눌러야 함.
#0<=N<=500000
#이동하려는 채널이 500000이기 때문에, 최악의 경우에 정답은 1000000백
limit = 1000000
N= int(input())
M = int(input())
broken = [False] * 10

for  _ in range(M):
    for k in map(int, input().split()):
        broken[k] = True
ans = abs(N - 100)  # 초기값은 100으로 설정(100에서 최소임)
for i in range(1000000):
    c = i
    len = possible(c)
    if len>0:
        press = abs(c-N) #+ - 버튼 누르는 횟수계산
        if ans> len+press:
            ans = len+press
print(ans)



