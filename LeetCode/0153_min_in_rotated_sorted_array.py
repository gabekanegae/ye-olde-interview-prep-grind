def findMin(nums):
    n = len(nums)
    if n == 1: return nums[0]
    if nums[0] < nums[n-1]: return nums[0]

    lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo+hi)//2
        print(lo, mid, hi)

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif mid == 0 or nums[mid] > nums[0]:
            lo = mid+1
        elif nums[mid] < nums[0]:
            hi = mid-1

print(findMin([4, 5, 6, 7, 0, 1, 2, 3, 4]))
print(findMin([1]))
print(findMin([4, 5]))
print(findMin([4, 5, 1, 2, 3]))