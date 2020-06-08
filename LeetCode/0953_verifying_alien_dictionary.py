def isAlienSorted(words, order):
    order = {e: i for i, e in enumerate(order)}

    for i in range(len(words)-1):
        a, b = words[i], words[i+1]

        diff = False
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                diff = True
                
                if order[a[i]] > order[b[i]]:
                    return False
                
                break

        if not diff and len(a) > len(b):
            return False

    return True

print(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
print(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")) # False
print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")) # False
print(isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz")) # True