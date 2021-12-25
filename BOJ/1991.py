N= int(input())
a = [list(map(int, input().split())) for _ in range(N)]
def preorder(n):
    if n== -1:
        return
    print(n)
    preorder(a[n].left)
    preorder(a[n].right)