def lengthOfLIS(nums):
    if not nums: return 0

    memo = [1 for n in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                memo[i] = max(memo[i], memo[j]+1)

    return max(memo)

print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # 4