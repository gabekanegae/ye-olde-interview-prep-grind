def frequencySort(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1

    d = [(-v, k) for k, v in d.items()]
    d.sort()

    s = []
    for k, v in d:
        s += [v]*(-k)

    return "".join(s)

print(frequencySort("tree")) # eert
print(frequencySort("cccaaa")) # cccaaa
print(frequencySort("Aabb")) # "bbAa"