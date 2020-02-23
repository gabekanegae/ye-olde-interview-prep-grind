# O(log n) time, O(1) space -- NO EDGE CASES
def search1(nums, target):
    # Binary search for middle index
    l, r = 0, len(nums)
    while l <= r:
        m = (l+r)//2
        if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
            break
        elif nums[m] < nums[m+1]:
            l = m
        elif nums[m] > nums[m+1]:
            r = m

    # nums[:m] is increasing, nums[m:] is decreasing

    if nums[0] <= target <= nums[m]:
        l, r = 0, m # Will search in nums[:m]
    elif nums[m+1] <= target <= nums[-1]:
        l, r = m+1, len(nums) # Will search in nums[m:]
    else:
        return -1

    # Binary search for target
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m
        elif nums[m] > target:
            r = m

    return -1

# O(log n) time, O(1) space
def search2(nums, target):
    if not nums: return -1

    # Binary search for middle index
    l, r = 0, len(nums)
    while l < r:
        m = (l+r)//2
        if (m == 0 or nums[m-1] < nums[m]) and (m == len(nums)-1 or nums[m] > nums[m+1]):
            break
        elif nums[m] < nums[m+1]:
            l = m
        elif nums[m] > nums[m+1]:
            r = m

    # nums[:m] is increasing, nums[m:] is decreasing

    if nums[0] <= target <= nums[m]:
        l, r = 0, m # Will search in nums[:m]
    elif m+1 < len(nums) and nums[m+1] <= target <= nums[-1]:
        l, r = m+1, len(nums) # Will search in nums[m:]
    else:
        return -1

    # Binary search for target
    while l < r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m
        elif nums[m] > target:
            r = m

    return -1

print(search2([4, 5, 6, 7, 0, 1, 2], 0))
print(search2([4, 5, 6, 7, 0, 1, 2], 3))
print(search2([], 4))
print(search2([1], 0))
print(search2([4, 5], 3))
print(search2([4, 5, 3], 3))
print(search2([4, 5, 6, 7], 3))
print(search2([1, 3], 2))