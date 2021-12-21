# 차이를 최대로

def calculate(A):
    ans = 0
    for i in range(len(A) - 1):
        ans += abs(A[i] - A[i + 1])
    return ans

def next_permutation(N, A):
    i = N - 1
    while i > 0 and A[i] <= A[i - 1]:
        i -= 1
    if i <= 0:
        return False
    j = N - 1
    while A[j] <= A[i - 1]:
        j -= 1
    A[i - 1], A[j] = A[j], A[i - 1]
    j = N - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i+=1
        j-=1
    return True


N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A)

ans = calculate(A)
while next_permutation(N, A):
    temp = calculate(A)
    ans = max(temp, ans)
print(ans)
