def productExceptSelf(nums):
    result = [1 for _ in nums]

    l = 1
    for i in range(len(nums)):
        result[i] *= l
        l *= nums[i]

    r = 1
    for i in reversed(range(len(nums))):
        result[i] *= r
        r *= nums[i]

    return result

print(productExceptSelf([1,2,3,4])) # [24,12,8,6]