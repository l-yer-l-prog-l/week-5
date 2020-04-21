nums = list(map(int, input().split()))
a = 0
b = 1
for i in range(len(nums) - 1):
    if nums[a] < nums[b]:
        print(nums[b], end=' ')
    a += 1
    b += 1
