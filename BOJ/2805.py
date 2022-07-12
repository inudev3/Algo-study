# import sys
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
#
# height = list(map(int, input().split()))
#
#
# # 길이를 설정했을 때 잘린 높이가 m보다 작으면 길이를 낮추고
# # m보다 크면 길이를 높인다
#
# def cut(x):
#     ans = 0
#     for i in range(n):
#         if height[i] - x > 0:
#             ans += height[i] - x
#     return ans >= m
#
#
# left = 0
# right = max(height)
# max = 0
# while left <= right:
#     mid = (left + right) // 2
#     if cut(mid):
#         left = mid + 1
#         if max < mid:
#             max = mid
#     else:
#         right = mid - 1
#
# print(max)
import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input())


def calc(commands, nums):
    reverse = False
    front = 0
    back = 0
    for command in commands:
        if command == 'R':
            reverse = not reverse
        else:
            if reverse:
                back += 1
            else:
                front += 1
    if front + back <= n:
        nums = nums[front:n - back]
        if reverse:
            return '[' + ','.join(nums[::-1]) + ']\n'
        else:
            return '[' + ','.join(nums) + ']\n'
    else:
        return 'error\n'


for i in range(T):
    commands = input().rstrip()
    n = int(input())
    nums = input().rstrip()[1:-1].split(',')
    commands = commands.replace('RR', '')
    print(calc(commands, nums))
