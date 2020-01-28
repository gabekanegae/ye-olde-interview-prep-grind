def isPalindrome(x):
    if x < 0: return False
    if x < 10: return True
    if x % 10 == 0: return x == 0

    r = 0
    while x > r:
        r = r*10 + x%10 # Push
        x //= 10 # Pop

        if r == x or r == x//10: return True

    return False

print(isPalindrome(1))
print(isPalindrome(21120))
print(isPalindrome(0))
print(isPalindrome(120))
print(isPalindrome(120021))
print(isPalindrome(1203021))
print(isPalindrome(-1203021))