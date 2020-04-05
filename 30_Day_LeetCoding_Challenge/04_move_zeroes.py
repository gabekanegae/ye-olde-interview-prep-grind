def moveZeroes(nums):
    i = 0
    while i < len(nums) and nums[i] != 0:
        i += 1
    j = i+1

    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums) # [1, 3, 12, 0, 0]

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
moveZeroes(nums)
print(nums) # [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]