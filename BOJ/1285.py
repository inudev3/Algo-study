from sys import stdin
input = stdin.readline

n = int(input())

def flip(x):
    if x== 'H':
        return 'T'
    else:
        return 'H'
a = [input() for _ in range(n)]
ans = n*n
for state in range(1<<n):
    total = 0
    for j in range(n): #행을 뒤집는 모든 각각의 경우의 수에 대해 해당 열을 검사
        cnt = 0
        for i in range(n):
            cur = a[i][j]
            if (state & (1<<i)): #i번째 행을 뒤집는 경우에는
                cur = flip(cur) #뒤집어준다.
            if cur =='T': # 뒷면이면 세준다.
                cnt+=1
        total += min(cnt, n-cnt) #뒷면의 개수가 작다면 뒤집지 않는 경우를 더해주고 크다면 뒤집는 경우를 더해준다.
    if ans>total:
        ans = total
print(ans)