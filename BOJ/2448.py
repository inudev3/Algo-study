
arr = [[""]* 3072 for _ in range(6143)]

def draw(row, col):
    arr[row][col] = "*"
    arr[row+1][col-1] = '*'
    arr[row+1][col+1] = '*'

    for i in range(5):
        arr[row+2][col-2+i] = '*'

def triangle(len, row, col):
    if len==3:
        draw(row, col)
        return

    triangle(len//2, row, col)
    triangle(len//2, row+len//2, col-len//2)
    triangle(len//2, row+len//2, col+len//2)

n = int(input())
for i in range(n):
    for j in range(2*n-1):
        arr[i][j] = ' '
triangle(n, 0, n-1)#첫줄 가운데점

for i in range(n):
    for j in range(2*n-1):
        print(arr[i][j])
    print()
