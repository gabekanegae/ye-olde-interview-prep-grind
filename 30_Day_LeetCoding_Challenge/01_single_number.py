def singleNumber(nums):
    counts = dict()
    for n in nums:
        if n not in counts: counts[n] = 0
        counts[n] += 1
    
    for k, v in counts.items():
        if v == 1: return k

print(singleNumber([2, 2, 1])) # 1
print(singleNumber([4, 1, 2, 1, 2])) # 4