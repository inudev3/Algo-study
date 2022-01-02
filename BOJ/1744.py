from sys import stdin

input = stdin.readline

n = int(input())
#양수는 큰 수끼리, 음수는 작은수끼리, 1은 묶지 않는 것이 최대, 음수가 홀수가 되어 한개나 남는다면 0과 묶어서 지운다.
s = [int(input()) for _ in range(n)]

plus = []
minus = []
zero = 0
one = 0

for i in range(n):
    if s[i] == 1:
        one+=1
    elif s[i]>0:
        plus.append(s[i])
    elif s[i]<0:
        minus.append(s[i])
    else:
        zero+=1
plus.sort(reverse=True)
minus.sort()
if len(plus)%2==1: #양수의 개수가 홀수라면
    plus.append(1) #마지막 양수와 1을 묶어줌(값이 변하지 않으므로 편의상)
if len(minus)%2 ==1:
    if zero>0:
        minus.append(0) #0의 개수가 1개 이상이면 0과 묶어서 없애줌
    else:
        minus.append(1) #아니면 그냥 1과 묶어서 (값이 동일하므로) 더해줌 -> 편의상 남는 숫자없이 모두 짝지어주는 과정

ans = one #초기값은 1의 개수만큼과 같다.
for i in range(0,len(plus), 2):
    ans+= plus[i] *plus[i+1]
for i in range(0, len(minus), 2):
    ans+= minus[i] * minus[i+1]

