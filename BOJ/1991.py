from collections import namedtuple

N= int(input())
node = namedtuple('node', ['left', 'right'])

tree = {}

for i in range(N):
    root,left,right =input().split()
    tree[root] = node(left,right)


def preorder(root):
    if root== ".":
        return
    print(root, end="")
    preorder(tree[root].left)
    preorder(tree[root].right)

def inorder(root):
    if root== ".":
        return
    inorder(tree[root].left)
    print(root,end="")
    inorder(tree[root].right)

def postorder(root):
    if root==".":
        return
    postorder(tree[root].left)
    postorder(tree[root].right)
    print(root,end="")

preorder('A')
print()
inorder("A")
print()
postorder("A")