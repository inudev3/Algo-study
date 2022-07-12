n = int(input())
nums = list(map(int, input().split()))
a=0
b=0
if n==1:
    print("A")
    exit()
elif n==2:
    if nums[0]==nums[1]:
        print(nums[0])
    else:
        print('A')
    exit()
else:
    if nums[0]==nums[1]:
        print(nums[0])
        exit()
    a = (nums[1]-nums[2])//(nums[0]-nums[1])
    b = nums[1]-nums[0]*a
for i in range(n-1):
    if nums[i+1] != a*nums[i]+b:
        print("B")
        exit()
print(nums[n-1]*a+b)