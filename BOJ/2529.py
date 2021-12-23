#k개의 부등호에 대해 좌우관계를 만족하는 k+1자리 정수의 최대값과 최소값 출력
n = int(input())
a = list(map(str, input().split()))
check = [False] * 10
ans =[]
def good(x, y, op):
    if op=='<':
        if x>y: return False
    if op=='>':
        if x<y: return False
    return True

def go(index, num):
    if index==n+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index==0 or good(num[index-1], i+'0', a[index-1]): #문자로 바꾸고 이전수랑 비교
            check[i] = True
            go(index+1, num+str(i))
            check[i] = False

go(0, '')
ans.sort()
print(ans[::-1])
print(ans)