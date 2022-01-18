string = input().rstrip()
exp = input().rstrip()


n = len(string)
m= len(exp)

last = exp[-1]
stack = []
for char in string:
    stack.append(char)
    if char == last and "".join(stack[-m:])==exp:
        del stack[-m:]

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
