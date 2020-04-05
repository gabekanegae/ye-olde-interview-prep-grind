def getNext(n):
    return sum(int(i)**2 for i in str(n))

def isHappy(n): # O(log n) time, O(1) space
    tortoise = getNext(n)
    hare = getNext(getNext(n))

    while tortoise != hare and hare != 1:
        tortoise = getNext(tortoise)
        hare = getNext(getNext(hare))

    return (hare == 1)

def isHappyHash(n): # O(log n) time, O(n) space
    seen = set([n])
    while True:
        n = sum(int(i)**2 for i in str(n))
        if n == 1: return True
        if n in seen: return False
        seen.add(n)

print(isHappy(19)) # True
print(isHappyHash(19)) # True