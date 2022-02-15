from sys import stdin
N = int(input())
C = [False]*2000000 ##가능한 수 체크
S = list(map(int, stdin.readline().split()))

for i in range(1<<N):#N크기의 순열에 대해 가능한 모든 부분 순열
    sum=0
    for j in range(N):
        if(i & 1<<j): #j번째 수가 i에 포함되는지 확인
            sum+=S[j]
        C[sum] = True #가능한 수 체크
for i in range(N): #합은 자연수(음이 아닌 정수) 이므로
    if S[i] is False:
        print(i)

def go(index, sum):
    if index==N:
        C[sum] = True
    go(index+1, sum+S[index])
    go(index+1, sum)
i=0
while True:
    if C[i] is True:
       print(i)
       break


