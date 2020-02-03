# O(n^2) time, O(1) space
def maxArea1(heights):
    best = 0
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            area = min(heights[i], heights[j]) * (j-i)
            best = max(area, best)

    return best

# O(n) time, O(1) space
def maxArea2(heights):
    best = 0
    l, r = 0, len(heights)-1

    while l < r:
        area = min(heights[l], heights[r]) * (r-l)
        best = max(area, best)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return best

print(maxArea1([1,8,6,2,5,4,8,3,7]))
print(maxArea2([1,8,6,2,5,4,8,3,7]))