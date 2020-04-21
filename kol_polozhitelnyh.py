nums = list(map(int, input().split()))
count = 0
for number in nums:
    if number > 0:
        count += 1
print(count)
