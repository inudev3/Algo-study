def bit(num):
    return 1 << num


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one = one * (len(answers) // len(one)) + one[:len(answers) % len(one)]
    two = two * (len(answers) // len(two)) + two[:len(answers) % len(two)]
    three = three * (len(answers) // len(three)) + three[:len(answers) % len(three)]
    res = [0, 0, 0]
    print(one, two, three)
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            res[0] += 1
        if answers[i] == two[i % 8]:
            res[1] += 1
        if answers[i] == three[i % 10]:
            res[2] += 1

    res.sort()
    Max = max(res)
    ans = []
    if Max == res[0]:
        ans.append(1)
    if Max == res[1]:
        ans.append(2)
    if Max == res[2]:
        ans.append(3)
    return res



