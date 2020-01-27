def isPalindrome(s):
    return s == s[::-1]

# O(n^3) time, O(1) space
def longestPalindrome1(s):
    start, end = 0, 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                if len(s[i:j+1]) > end-start:
                    start, end = i, j+1

    return s[start:end]

# O(n^2) time, O(1) space
def longestPalindrome2(s):
    def expand(s, l, r):
        cl, cr = l, r
        while cl >= 0 and cr < len(s) and s[cl] == s[cr]:
            cl, cr = cl-1, cr+1
        return cr-cl-1

    start, end = 0, 0
    for i in range(len(s)):
        pad = max(expand(s, i, i), expand(s, i, i+1))
        if pad > end-start:
            start = i-((pad-1)//2)
            end = i+(pad//2)

    return s[start:end+1]

print(longestPalindrome1("babadcccccd"))
print(longestPalindrome2("babadcccccd"))
print(longestPalindrome1("cbbd"))
print(longestPalindrome2("cbbd"))
print(longestPalindrome1("abcba"))
print(longestPalindrome2("abcba"))