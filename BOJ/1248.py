N = int(input())
Sign = list(map(str, input().split()))
ans = []

def go(index):
    if index==n:
        return ok()

    if Sign[index][index] ==0:
        ans[index] = 0
