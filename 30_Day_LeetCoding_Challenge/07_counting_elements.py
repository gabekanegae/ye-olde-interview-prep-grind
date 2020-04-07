def countElements(arr):
    elements = set(arr)

    total = 0
    for n in arr:
        if n+1 in elements:
            total += 1

    return total

print(countElements([1, 2, 3])) # 2
print(countElements([1, 1, 3, 3, 5, 5, 7, 7])) # 0
print(countElements([1, 3, 2, 3, 5, 0])) # 3
print(countElements([1, 1, 2, 2])) # 2