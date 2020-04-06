def moveZeroes(nums):
    lastNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZero], nums[i] = nums[i], nums[lastNonZero]
            lastNonZero += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums) # [1, 3, 12, 0, 0]

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
moveZeroes(nums)
print(nums) # [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]