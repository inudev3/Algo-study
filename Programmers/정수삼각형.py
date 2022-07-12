def solution(triangle):
    n = len(triangle)
    D = [[0] * n for _ in range(n)]
    D[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            if j > 0:
                D[i][j] = max(D[i - 1][j - 1] + triangle[i][j], D[i][j])
            if j < i:
                D[i][j] = max(D[i - 1][j] + triangle[i][j], D[i][j])
    return max(D[n - 1])
