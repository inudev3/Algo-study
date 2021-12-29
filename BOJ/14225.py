from sys import stdin
N = int(input())
C = [False]*20*100000
S = list(map(int, stdin.readline().split()))

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


