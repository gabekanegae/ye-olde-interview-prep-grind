def wordBreak(s, wordDict):
    wordDict = set(wordDict)

    validUpToIndex = [False for _ in range(len(s)+1)]
    validUpToIndex[0] = True

    for i in range(1, len(s)+1):
        for j in range(0, i):
            # breaking into s[:j] and s[j:i]
            if validUpToIndex[j] and s[j:i] in wordDict:
                validUpToIndex[i] = True
                break

    return validUpToIndex[-1]

print(wordBreak("catsanddog", ["cats", "and", "dog", "sand", "cat"]))