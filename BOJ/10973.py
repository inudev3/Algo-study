# 이전순열
# 10972 다음 순열
N = int(input())
A = list(map(int, input().split()))
ans = []


def prev_permutation(N, A):
    i = N - 1
    while i > 0 and A[i] >= A[i - 1]:  # 오름차순인지 검사한다.
        i -= 1
    if i <= 0:
        return False
    j = N - 1
    while A[j] >= A[i - 1]:  # 뒷 숫자들은 이미 오름차순이므로 i-1보다 작은 첫번째 수가 최대값
        j -= 1
    A[i - 1], A[j] = A[j], A[i - 1]
    j = N - 1  # 초기화
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return True


if prev_permutation(N, A) is True:
    print(' '.join(map(str, ans)))
else:
    print(-1)

8, 4, 7, 6, 5, 3
8, 5, 7, 6, 4, 3
