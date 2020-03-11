def toGoatLatin(S):
    vowels = set("aeiou")
    S = list(S)

    goat = []

    wordCount = 0
    i = 0
    while i < len(S):
        if S[i].lower() in vowels:
            while i < len(S) and S[i] != " ":
                goat.append(S[i])
                i += 1
        else:
            first = S[i]
            i += 1
            while i < len(S) and S[i] != " ":
                goat.append(S[i])
                i += 1
            goat.append(first)

        goat += list("ma")
        wordCount += 1
        goat += ["a"*wordCount]
        goat.append(" ")
        i += 1

    return "".join(goat[:-1])

print(toGoatLatin("I speak Goat Latin"))