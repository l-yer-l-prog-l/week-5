nums = list(map(int, input().split()))
alist = []
for i in range(len(nums)):
    if nums[i] > 0:
        alist.append(nums[i])
print(min(alist))
