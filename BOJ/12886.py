#(A,B)를 정점으로하고, c의 개수는 n-a-b로 유추한다.
# a==b==n-a-b 일 때 정답
import sys

a,b,c = map(int, input().split())
sys.setrecursionlimit(1500**2)
check = [[False] * 1501 for _ in range(1501)
x,y,z = map(int, input().split())
s= x+y+z

def go(x,y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x. y. s-x-y]
    for i in range(3):
        for j in range(3):
            if a[i]<a[j]:
                b = [x,y, s-x-y]
                b[i]+= a[i]
                b[j]-= a[i]
                go(b[0], b[1])




if s%3!=0:
    print(0)
else:
    go(x,y)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)

