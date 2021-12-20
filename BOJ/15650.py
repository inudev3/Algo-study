M, N = list(map(int, input()))

a = [0] * 10


def go(index, start, n, m):  # 오름차순 추가
    if index == m:
        print(a)
    for i in range(start, n + 1):
        a[index] = i
        go(index + 1, i + 1, n, m)


go(0, 1, N, M)


def go1(index, selected, n, m):
    if selected== m: #선택한 수의 개수가 m개가 됨
        print(a)
        return
    if index > n: #선택할 수가 범위를 벗어남
        return
    a[selected] = index
    go(index+1, selected+1, n, m) #index를 결과에 추가
    a[selected] = 0
    go(index+1, selected, n, m) #추가하는 결과가 전부 끝났으면 츄가하지 않는 결과도 실행함(모든 순열)index를 결과에 추가하지 않음음

go(1, 0, N,M)

