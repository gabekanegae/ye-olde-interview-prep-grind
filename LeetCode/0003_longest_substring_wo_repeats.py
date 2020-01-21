# Sliding window, O(n^3)
def lengthOfLongestSubstring1(s):
    best = 0
    lo, hi = 0, 0
    while lo < len(s):
        if hi == len(s) or s[hi] in s[lo:hi]:
            lo += 1
            hi = lo
        else:
            hi += 1
            best = max(best, hi-lo)

    return best

# Sliding window, O(n) with O(n) set
def lengthOfLongestSubstring2(s):
    cur = set()
    best = 0
    lo, hi = 0, 0
    while hi < len(s):
        if s[hi] in cur:
            cur.remove(s[lo])
            lo += 1
        else:
            cur.add(s[hi])
            hi += 1
            best = max(best, hi-lo)

    return best

print(lengthOfLongestSubstring2("abcabcbba"))
print(lengthOfLongestSubstring1("abcabcbba"))
print(lengthOfLongestSubstring1("bbbbb"))
print(lengthOfLongestSubstring2("bbbbb"))
print(lengthOfLongestSubstring1(""))
print(lengthOfLongestSubstring2(""))
print(lengthOfLongestSubstring1("abcdefghijklmnopqrstuvwxyz"))
print(lengthOfLongestSubstring2("abcdefghijklmnopqrstuvwxyz"))