allowed = set("abcdefghijklmnopqrstuvwxyz0123456789")

def isPalindrome(s):
    s = s.lower()

    i, j = 0, len(s)-1

    while i < j:
        if s[i] not in allowed:
            i += 1
        if s[j] not in allowed:
            j -= 1

        if s[i] in allowed and s[j] in allowed:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

    return True

print(isPalindrome("Socorram-me, subi no onibus em marrocos!!!")) # True
print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False
print(isPalindrome(".,")) # True
print(isPalindrome(" ")) # True
print(isPalindrome("0P")) # False