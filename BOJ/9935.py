string = input().rstrip()
exp = input().rstrip()



lastChar = exp[-1]
stack = []
length = len(exp)

for char in string:
    stack.append(char)
    if char==lastChar and ''.join(stack[-length:]) == exp:
        for _ in range(len(exp)):
            stack.pop()

answer = ''.join(stack)
