def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i]+nums[i-1])

    return max(nums)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArray([-2,1])) # 1
print(maxSubArray([-2,-1])) # -1