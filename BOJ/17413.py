S = input()

tag = False
stack = []
for char in S:
    if char=="<":
        while stack:
            print(stack.pop())
        tag = True
        print(char)
    elif char ==">":
        tag= False
        print(char)
    elif tag is True:
        print(char)
    else:
        if char== " ":
            while stack:
                print(stack.pop())
                print(char)
        else:
            stack.append(char)
while stack:
    print(stack.pop())
print()