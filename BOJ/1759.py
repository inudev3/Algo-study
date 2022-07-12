# 3<=L<=C<=15,
# C개의 문자들 중 L개로 이루어진 암호를 구하기
# 암호는 오름차순으로 정렬됨


# 각 알파벳마다 포함될지/ 안될지의 선택여부를 1/0으로 나타낸 순열을 찾는다.
def check(password):
    ja = 0
    mo = 0
    for char in password:
        if char in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(password, i):
    global alpha
    global L
    if len(password) == L:  # 마지막 문자를 포함하고 나서 암호를 만드는 경우를 제외하기 위해서 정답을 확인하는 경우가 먼저 와야 한다.
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(password + alpha[i], i + 1)  # 사용하는 경우와 사용하지 않는 경우를 모두 탐색
    go(password, i + 1)


L, C = map(int, input().split())
alpha = input().split()
alpha.sort()  # 오름차순으로 정렬한 채로 순열조사
go( "", 0)

import sys
from itertools import combinations

def make_code():
    result = []
    for c in list(combinations(alpha, L)):
        if check(c):
            result.append("".join(c))
    return result
