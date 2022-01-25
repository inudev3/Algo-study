# s = list(input().rstrip())
#
#
# def go(s, index, lastChar):
#     if index == len(s):
#         return 1
#     if s[index] == 'c':
#         start = ord('a')
#         end = ord('z')
#     else:
#         start = ord('0')
#         end = ord('9')
#     ans = 0
#     for i in range(start, end + 1):
#         if i != lastChar:
#             ans += go(s, index + 1, i)
#     return ans
#
#
# print(go(s, 0, ' '))

a, b, c, x, y = map(int, input().split())
ans = x*a + y*b
for i in range(10001): #2c의 범위
    price = 2*i*c+max(0, x-i)*a+max(0,x-i)*b


n = int(input())
check = [False] * 1001#50으로 4번 골랐을 때의 최대
char = ['I', 'V', 'X', 'L']
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            l = n-i-j-k
            sum = i+5*j+10*k+50*l
            check[sum] = True

ans=0
for i in range(len(check)):
    if check[i]:
        ans+=1
print(ans)



