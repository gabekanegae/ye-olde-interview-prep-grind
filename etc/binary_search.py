def binarySearch(l, x):
    lo, hi = 0, len(l)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if l[mid] == x:
            return mid
        elif l[mid] < x:
            lo = mid+1
        elif l[mid] > x:
            hi = mid-1

    return None

l = [1, 4, 5, 7, 10, 15, 34, 65, 85, 104, 159, 197, 201, 230, 259, 267]
print(binarySearch(l, 15))