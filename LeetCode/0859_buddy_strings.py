def buddyStrings(A, B):
    if len(A) != len(B): return False
    if not A or not B: return False

    if A == B:
        seen = set()
        for a in A:
            if a in seen: return True
            seen.add(a)
        return False

    diff = []
    for a, b in zip(A, B):
        if a != b: diff.append([a, b])

    if len(diff) != 2: return False
    return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]

print(buddyStrings("ab", "ba")) # True
print(buddyStrings("ab", "ab")) # False
print(buddyStrings("aa", "aa")) # True
print(buddyStrings("aaaaaaabc", "aaaaaaacb")) # True
print(buddyStrings("", "aa")) # False