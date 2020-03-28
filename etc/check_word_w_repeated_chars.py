def isValid(word):
    dic = set(["hello", "hi", "potato"])
    # print("checking if valid: '{}'".format(word))
    return word in dic

def buildWord(letters, counts):
    return "".join(l*c for l, c in zip(letters, counts))

def checkWord(word):
    def rec(letters, counts, i):
        if isValid(buildWord(letters, counts)): return True
        if i >= len(letters): return False

        if counts[i] == 2:
            countsMin = counts[:]
            countsMin[i] = 1
            return rec(letters, countsMin, i+1) or rec(letters, counts, i+1)
        else:
            return rec(letters, counts, i+1)

    letters = []
    counts = []

    repeats = 1
    for i in range(len(word)):
        if i == len(word)-1 or word[i] != word[i+1]:
            letters.append(word[i])
            counts.append(min(repeats, 2))
            repeats = 1
        else:
            repeats += 1

    return rec(letters, counts, 0)

print(checkWord("hi")) # True
print(checkWord("hiiiiiiiii")) # True
print(checkWord("hhhhhhiiiiiiiii")) # True
print(checkWord("helo")) # False
print(checkWord("hellllloooo")) # True
print(checkWord("heeeeellllo")) # True
print(checkWord("heeeeelloooo")) # True
print(checkWord("potaaaattoooo")) # True
print(checkWord("potaaaattyoooo")) # False