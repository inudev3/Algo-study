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

k = int(input())
eq = input().split()
small = [0] * (k+1)
big = [0] * (k+1)
for i in range(k+1):
    small[i] = i
    big[i] = 9-i


def next_permutation(N, A):
    ans = []
    i = N - 1
    while i > 0 and A[i] <= A[i - 1]:  # 내림차순인지 검사한다.
        i -= 1
    if i <= 0:
        return False
    j = N - 1
    while A[j] <= A[i - 1]:  # 뒷 숫자들은 이미 내림차순이므로 i-1보다 큰 첫번째 수가 최소값
        j -= 1
    A[i - 1], A[j] = A[j], A[i - 1]
    j = N-1
    while i<j:
        A[i], A[j] = A[j], A[i]
        i+=1
        j-=1
    return True

def prev_permutation(N, a):
    ans  =[]
    i = N-1
    while i>0 and A[i]>=A[i-1]: #오름차순인지 검사
        i -=1
    if i<=0:
        return False
    j = N-1
    while A[i]>= A[i-1]:
        j-=1
    A[i-1], A[j] = A[j] = A[i-1]
    j = N - 1  # 초기화
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return True
def check(perm, a):
    for i in range(len(a)):
        if a[i] == '<' and perm[i] > perm[i+1]:
            return False
        if a[i] == '>' and perm[i] <perm[i+1]:
            return False
    return True
while True:
    if check(small, eq):
        break
    if