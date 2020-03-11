def isPalindrome(s):
    i, j = 0, len(s)-1

    while i < j:
        while not s[i].lower().isalnum():
            i += 1
            if not i < j: return True

        while not s[j].lower().isalnum():
            j -= 1
            if not i < j: return True

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(".,"))
print(isPalindrome(" "))
print(isPalindrome("0P"))