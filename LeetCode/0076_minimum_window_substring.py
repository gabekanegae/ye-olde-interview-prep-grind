def countChars(s):
    count = [0 for _ in range(256)]
    for c in s:
        count[ord(c)] += 1

    return count

def minWindow(s, t):
    tCount = countChars(t)
    i, j = 0, 0

    sCount = [0 for _ in range(256)]
    best = [None, i, j]
    while i <= j and j < len(s):
        sCount[ord(s[j])] += 1

        while i <= j and all(si>=ti for si, ti in zip(sCount, tCount)):
            if not best[0] or j-i < best[0]:
                best = [j-i, i, j]

            sCount[ord(s[i])] -= 1
            i += 1

        j += 1

    if best[0] == None: return ""

    return s[best[1]:best[2]+1]

print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(minWindow("a", "aa")) # ""