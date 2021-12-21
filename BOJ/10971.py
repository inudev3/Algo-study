# 외판원 순회2

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
A = list(range(N))



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
        i += 1
        j -= 1
    return True


ans = 2147483647

while True: #다시돌아오기 때문에 첫자리를 고정해놓고 N-1에 대해서만 순열을 구해도 됨
    #if A[0]!=1: break # 마찬가지로 첫째자리를 고정하는 방법
    s = 0
    ok = True
    for i in range(N - 1):
        if W[A[i]][A[i + 1]] == 0:
            ok = False
            break
        else:
            s += W[A[i]][A[i + 1]]
    if ok and W[A[-1]][A[0]] != 0:
        s += W[A[-1]][A[0]]
        ans = min(ans, s)
    if not next_permutation(N, A):
        break
    if A[0]!= 0:
        break
print(ans)
