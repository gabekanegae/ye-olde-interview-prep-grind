def reverse(l, a=None, b=None):
    if a == None: a = 0
    if b == None: b = len(l)

    for i in range((b-a)//2):
        l[a+i], l[b-i-1] = l[b-i-1], l[a+i]

    return l

# O(n) time, O(1) space
def rotateRight(l, n=1):
    n %= len(l)

    reverse(l)
    reverse(l, 0, n)
    reverse(l, n, len(l))

# O(n) time, O(1) space
def rotateLeft(l, n=1):
    rotateRight(l, -n) # -n == len(l)-n mod

l = [1, 2, 3, 4, 5, 6, 7, 8]
rotateLeft(l, 1)
print(l)