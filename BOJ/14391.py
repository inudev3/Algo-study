#4자리 수 4개를 더하는 것은 더 큰 반례가 존재함
#각 칸에 대해 가로 혹은 세로의 선택을 하는 비트마스크 풀이

N, M = map(int, input().split()) #세로, 가로 순서
a= [list(map(int, list(input()))) for _ in range(N)]
for i in range(1<<(N*M)): #세로는 1 가로는 0
    sum = 0
    for j in range(N): #각행마다 연속된 가로 구하기
        cur = 0
        for k in range(M):
            s = j*M+k #각 칸에 모두 번호를 매긴다.
            if i&(1<<s) == 0: #해당 칸이 가로라면
                cur = cur*10 + a[j][k] #숫자를 한자리씩 더 증가시킴
            else:
                sum += cur # 가로연속이 끝나면 합에 더해줌
                cur = 0
        sum+=cur #가로로 끝났을 경우에는 한번 더 더해줘야 함

    for k in range(M): #각열마다 연속된 세로 구하기
        cur = 0
        for j in range(N):
            s =  j*M+k
            if i &(1<<s) != 0:#해당 칸이 세로라면
                cur = cur*10 +a[j][k]
            else:
                sum+= cur
                cur = 0
        sum+=cur
    ans = max(ans, sum)
print(ans)


