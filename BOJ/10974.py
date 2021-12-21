
N = int(input())
A =  [0] * N

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

for i in range(N):
    A[i] = i+1
for j in range(N):
    print(A[j])
while next_permutation(N, A):
    for j in range(N):
        print(A[j])