#k개의 수중에서 6개를 고르는 문제

#선택한 6개를 1, 선택하지않은 나머지 k-6개를 0이라고 한다면

# 이 수를 가지고 로또를 만들 수 있는 방법은
# k! / 6! *(k-6)! (순서 상관 없음)
from sys import stdin

while True:
    n, *a = list(map(int, stdin.readline().split()))
    if n==0:
        break
    go(a, 0, [])

def go(a, index, lotto):
    if index==len(a):
        return
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return
    go(a, index+1, lotto+a[index])
    go(a, index+1, lotto)



