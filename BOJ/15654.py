#중복가능, 비내림차순

M,N = list(map(int, input()))
a= [0]*10

def go1(index, start, n, m):
    if index==m:
        print(a)
        return
    for i in range(start, n+1):
        a[index] = i
        go1(index+1, i, n, m)


  ##선택 하지 않는 경우

    for i in range(1, n+1):
        for j in range(1, a[i]+1):
            print(i)