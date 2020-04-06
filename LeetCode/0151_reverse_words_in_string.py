def reverseWords(s):
    # return " ".join(s.split()[::-1])

    def reverseString(s, a, b):
        i, j = a, b
        while i < j:
            s[a], s[b] = s[b], s[a]
            i += 1
            j -= 1

        return "".join(s[a:b+1])

    s = list(s)
    cur = []

    i = 0
    start = None
    for i in range(len(s)):
        if not start and s[i] == " ": continue
        if not start:
            start = i
        else:
            cur.append(reverseString(s, start, i))
            start = None

    return " ".join(cur)

print(reverseWords("the sky is blue")) # "blue is sky the"
print(reverseWords("  hello world!  ")) # "world! hello"
print(reverseWords("a good   example")) # "example good a"