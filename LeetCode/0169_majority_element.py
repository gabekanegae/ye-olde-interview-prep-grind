def majorityElement(nums):
    d = dict()
    for n in nums:
        if n not in d: d[n] = 0
        d[n] += 1

    for k, v in d.items():
        if v > len(nums)//2: return k

print(majorityElement([3,2,3])) # 3
print(majorityElement([2,2,1,1,1,2,2])) # 2