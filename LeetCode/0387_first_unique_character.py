def firstUniqChar(s):
    seen = dict()
    for c in s:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1

    for i in range(len(s)):
        if seen[s[i]] == 1:
            return i

    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))