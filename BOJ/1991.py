from collections import namedtuple

N= int(input())
a = [list(map(int, input().split())) for _ in range(N)]
tree = namedtuple('tree', ['left', 'right'])
a = [list(*map(tree))]
def preorder(n):
    if n== -1:
        return
    print(n)
    preorder(a[n].left)
    preorder(a[n].right)

def inorder(n):
    if n==-1:
        return
    inorder(a[n].left)
    print(n)
    inorder(a[n].right)

def postorder(n):
    if n==1:
        return
    postorder(a[n].left)
    postorder(a[n].right)
    print(n)

