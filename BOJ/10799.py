S = input().split()
stack = []
for char in S:
    if char == '(':
        stack.append(char)
    if char == ')':
