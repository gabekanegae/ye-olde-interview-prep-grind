def findMaxWithBinarySearch(l):
    lo, hi = 0, len(l)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if l[mid-1] < l[mid] > l[mid+1]:
            return l[mid]
        elif l[mid] > l[mid-1]:
            lo = mid+1
        elif l[mid] > l[mid+1]:
            hi = mid-1

    return None

l = [1, 4, 5, 7, 10, 15, 12, 11, 9, 5, 4, 2, 1, 0]
print(findMaxWithBinarySearch(l))