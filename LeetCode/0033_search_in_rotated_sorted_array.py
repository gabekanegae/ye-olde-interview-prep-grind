def search(nums, target):
    def binarySearch(lo, hi):
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid-1
        return -1

    n = len(nums)

    if n == 0:
        return -1
    elif n == 1:
        return 0 if nums[0] == target else -1

    if nums[0] < nums[n-1]:
        mid = 0
    else:
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2

            if mid == 0 or nums[mid] > nums[mid+1]:
                mid = mid+1
                break
            elif nums[mid] > nums[0]:
                lo = mid+1
            elif nums[mid] < nums[0]:
                hi = mid-1

    index = mid

    if nums[index] == target:
        return index
    elif index == 0:
        return binarySearch(0, n-1)
    elif target < nums[0]:
        return binarySearch(index+1, len(nums)-1)
    else:
        return binarySearch(0, index-1)

print(search([4, 5, 6, 7, 0, 1, 2, 3, 4], 3))
print(search([1], 0))
print(search([4, 5], 3))
print(search([3, 1], 1))
print(search([1, 3], 3))
print(search([4, 5, 1, 2, 3], 1))
print(search([4, 5, 3], 3))
print(search([4, 5, 6, 7], 3))
print(search([1, 3], 2))