def isBadVersion(version):
    return [False, False, False, True, True][version-1]

def firstBadVersion(n):
    lo, hi = 1, n
    while lo <= hi:
        m = (lo+hi)//2
        if isBadVersion(m):
            if m == 1 or not isBadVersion(m-1):
                return m
            else:
                hi = m-1
        else:
            lo = m+1

print(firstBadVersion(5)) # 4