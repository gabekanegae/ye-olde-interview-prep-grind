def searchRange(nums, target):
    start, end = -1, -1

    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2

        if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
            start = mid
            break        
        elif nums[mid] < target:
            lo = mid+1
        elif nums[mid] >= target:
            hi = mid-1

    if start == -1: return [-1, -1]

    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2

        if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
            end = mid
            break
        elif nums[mid] <= target:
            lo = mid+1
        elif nums[mid] > target:
            hi = mid-1

    if end == -1: return [-1, -1]

    return [start, end]

print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([5, 5, 5, 5, 6, 7], 5))
print(searchRange([0, 1, 5, 5, 5, 5], 5))