class Node:
    def __init__(self,key,left=None, right=None):
        # self.level =level
        self.key = key
        self.left = left
        self.right= right

k = int(input())
levels = [[] for _ in range(k)]
def inorder(node,level):
    if node==None:
        return
    inorder(node.left,level+1)
    levels[level].append(node.key)
    inorder(node.right,level+1)
order = list(map(int, input().split()))


#완전 이진 트리를 이루고 있다
def makeTree(arr:list, level=0):
    mid = (len(arr)//2)
    levels[level].append(arr[mid])
    if len(arr)==1:
        return
    makeTree(arr[:mid], level+1)
    makeTree(arr[mid+1:], level+1)

makeTree(order)
for level in levels:
    print(*level)

