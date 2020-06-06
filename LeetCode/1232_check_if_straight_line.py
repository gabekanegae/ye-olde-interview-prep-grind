def checkStraightLine1(coordinates):
    a, b = coordinates[:2]
    p = (b[1]-a[1])*(b[0]-a[0]) # For this purpose, (Y-y)/(X-x) can be (Y-y)*(X-x)

    for a in range(1, len(coordinates)-1):
        a, b = coordinates[a], coordinates[a+1]

        new_p = (b[1]-a[1])*(b[0]-a[0])

        if new_p != p: return False

    return True

# Reduce to nearest point w/ gcd
def checkStraightLine2(coordinates):
    def gcd(a, b):
        while b: a, b = b, a%b
        return a

    def reduce(p):
        g = gcd(p[0], p[1])
        return (p[0]//g, p[1]//g)

    a, b = coordinates[:2]
    p = reduce((b[0]-a[0], b[1]-a[1]))

    for a in range(1, len(coordinates)-1):
        a, b = coordinates[a], coordinates[a+1]

        new_p = reduce((b[0]-a[0], b[1]-a[1]))

        if new_p != p: return False

    return True

print(checkStraightLine1([[0, 0], [0, 1], [0, -1]])) # True
print(checkStraightLine1([[1, -8], [2, -3], [1, 2]])) # False
print(checkStraightLine1([[1, 2], [2, 3], [3, 5]])) # False
print(checkStraightLine1([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])) # False
print(checkStraightLine1([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])) # True

print(checkStraightLine2([[0, 0], [0, 1], [0, -1]])) # True
print(checkStraightLine2([[1, -8], [2, -3], [1, 2]])) # False
print(checkStraightLine2([[1, 2], [2, 3], [3, 5]])) # False
print(checkStraightLine2([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])) # False
print(checkStraightLine2([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])) # True