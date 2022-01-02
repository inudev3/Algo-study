
a = input().split('-')
num = []
for i in a:
    cnt=0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n-= num[i]
print(n)

s= input()
num = []
sign = []
minus = False
cur = 0
sign.append(1)#첫번째 수는 부호가 없으므로 양수로 넣어준다
for i in range(len(s)):
    if s[i] == '+' or s[i] =='-':
        if s[i]=='+':
            sign.append(1)
        else:
            sign.append(-1)
        num.append(cur)
        cur=0
    else:
        cur = cur*10 + ord(s[i])-ord('0') #자릿수 더해주
num.append(cur) #가장 마지막 수는 부호가 없으므로 직접 넣어줘야 함
ans = 0
for i in range(len(num)):
    if sign[i] ==-1:
        minus = True
    if minus :
        ans -= num[i]
    else:
        ans+= num[i]

print(ans)