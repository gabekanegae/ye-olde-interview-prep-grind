def removeDuplicates(nums):
    i, j = 0, 0

    while j < len(nums):
        if j+1 == len(nums) or nums[j] != nums[j+1]:
            nums[i] = nums[j]
            i += 1
        j += 1

    return i

print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))