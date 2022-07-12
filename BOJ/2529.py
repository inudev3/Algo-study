import itertools

k= int(input())
eq = input().split()
big = [9-i for i in range(k+1)]
small = [i for i in range(k+1)]
def check(arr, eq):
    for i in range(len(eq)):
        if eq[i]=="<" and arr[i]>=arr[i+1]:
            return False
        if eq[i]==">" and arr[i]<=arr[i+1]:
            return False
    return True

def next_permutation(arr):
    n = len(arr)
    if n<2:return False
    i = n-2
    while i>=0 and arr[i]>=arr[i+1]:i-=1
    if i<0: return False
    j = i+1
    k= n-1

    while arr[i]>=arr[k]: k-=1
    arr[i],arr[k] = arr[k],arr[i]
    arr[j:] = arr[:j-1:-1]
    return arr
def prev_permutation(arr):
    n= len(arr)
    if n<2: return False
    i= n-2
    while i>=0 and arr[i]<=arr[i+1]:i-=1
    if i<0:return False
    j=i+1
    k=n-1
    while arr[i] <= arr[k]: k -= 1
    arr[i], arr[k] = arr[k], arr[i]
    arr[j:] = arr[:j - 1:-1]
    return arr


while True:
    if check(big, eq):
        print(''.join(map(str,big)))
        break
    if not prev_permutation(big):
        break
while True:
    if check(small, eq):
        print(''.join(map(str,small)))
        break
    if not next_permutation(small):
        break