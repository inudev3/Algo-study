from sys import stdin
T = int(stdin.readline())
p = stdin.readline().split()
n = int(stdin.readline())
arr = list(map(int, stdin.readline().strip('[]').split(',')))
stack =[]
for char in p:
    if char == 'R':
        while arr:
            stack.append(arr.pop())

