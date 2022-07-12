def solution(n, k, cmd): ##연결리스트
    curr = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == 'C':
            prev, next = table[curr]
            answer[curr] = "X"
            stack.append([prev, curr, next])
            if next is None:
                curr = prev
            else:
                curr = next
            if prev is None:
                table[next][0] = None
            elif next is None:
                table[prev][1] = None
            else:
                table[next][0] = prev
                table[prev][1] = next
        elif c == "Z":
            prev, now, next = stack.pop()
            answer[now] = "O"
            if next is None:
                table[prev][1] = now
            elif prev is None:
                table[next][0] = now
            else:
                table[prev][1] = now
                table[next][0] = now
        else:
            char, num = c.split(" ")
            num = int(num)

            for _ in range(num):
                if char == "D":
                    curr = table[curr][1]
                else:
                    curr = table[curr][0]

    return "".join(answer)


import heapq
def solution(n, k, cmd): ##힙 풀이
    left, right, delete = [],[],[]
    for i in range(n):
        heapq.heappush(right, i)
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))
    for c in cmd:
        if len(c)>1:
            move = int(c.split(" ")[-1])
            if c.startswith("D"):
                for _ in range(move):
                    if right:
                        heapq.heappush(left, -heapq.heappop(right))
            elif c.startswith('U'):
                for _ in range(move):
                    if left:
                        heapq.heappush(right,-heapq.heappop(left))
        elif c=="C":
            delete.append(heapq.heappop(right))
            if not right:
                heapq.heappush(right, -heapq.heappop(left))
        elif c=="Z":
            repair = delete.pop()
            if repair<right[0]:
                heapq.heappush(left,-repair)
            else:
                heapq.heappush(right,repair)
    result=[]
    while left:
        result.append(-heapq.heappop(left))
    while right:
        result.append(heapq.heappop(right))
    result = set(result)
    answer = ["O" if i in result else "X" for i in range(n)]
    return "".join(answer)