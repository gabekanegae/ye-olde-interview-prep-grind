def containsNearbyDuplicate(nums, k):
    window = set()
    for i in range(len(nums)):
        if nums[i] in window: return True
        window.add(nums[i])
        if len(window) > k:
            window.remove(nums[i-k])

    return False

print(containsNearbyDuplicate([1, 2, 3, 1], 3)) # True
print(containsNearbyDuplicate([1, 0, 1, 1], 2)) # True
print(containsNearbyDuplicate([1, 0, 1, 1], 1)) # True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)) # False