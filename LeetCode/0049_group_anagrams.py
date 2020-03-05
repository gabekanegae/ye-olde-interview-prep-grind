def getCount(s):
    ct = [0 for _ in range(26)]
    for c in s:
        ct[ord(c) - ord("a")] += 1

    return ",".join([str(c) for c in ct])

def groupAnagrams(strs):
    groups = dict()

    for s in strs:
        ct = getCount(s)
        if ct not in groups:
            groups[ct] = []
        groups[ct].append(s)

    return groups.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))