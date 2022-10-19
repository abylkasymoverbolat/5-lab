nums = []
while True:
    num = int(input("выводите число: "))
    if num == 0:
        break
    else:
        nums.append(num)
nums = sorted(nums, reverse=True)
for c in nums:
    print(c)