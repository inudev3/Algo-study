from sys import stdin

N, M = map(int, stdin.readline().split())
unseen = set()
unheard = set()
for _ in range(N):
    person = stdin.readline().rstrip()
    unseen.add(person)
for _ in range(M):
    person = stdin.readline().rstrip()
    unheard.add(person)

result = sorted(list(unseen & unheard))
print(len(result))
for person in result:
    print(person)
