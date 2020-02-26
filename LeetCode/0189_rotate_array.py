def reverse(l, a=None, b=None):
    if a == None: a = 0
    if b == None: b = len(l)

    for i in range((b-a)//2):
        l[a+i], l[b-i-1] = l[b-i-1], l[a+i]

    return l

# O(n) time, O(1) space
def rotate(l, n=1): # Rotate Right
    n %= len(l)

    reverse(l)
    reverse(l, 0, n)
    reverse(l, n, len(l))

l = [1, 2, 3, 4, 5, 6, 7, 8]
rotate(l, 1)
print(l)
rotate(l, 4)
print(l)