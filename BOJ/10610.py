#3의 배수는 모든 자리수의 합이 3의 배수이면 3의 배수이다.

#따라서 입력받은 수의 모든자릿수의 합이 3의배수이면 숫자를 섞어도 3의 배수임다

# 내림차순으로 뒷자리가 0이 되면 무조건 30의 배수가 되므로

# 우선 숫자의 합 3의 배수인지 확인, 숫자 중에 0이 존재하는 지 확인 후 내림차순 정렬하면 됨

from sys import stdin
input = stdin.readline

s = int(input().rstrip())
sum=0
for char in s:
    sum+= ord(char)-ord('0')
s.sort()
if s[0]==0 and sum%3==0:
    s = reversed(s)
    print(s)
else:
    print(-1)
