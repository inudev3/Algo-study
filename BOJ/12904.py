from sys import stdin
input = stdin.readline
s = list(input().rstrip())
t = list(input().rstrip())
while len(t)>len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
if s==t:
    print(1)
else:
    print(0)

while len(t)>=len(s):
    if t[-1]=='A':
        t.pop()
    else:
        t.pop()
        t.reverse()
if s==t:
    print(1)
else:
    print(0)