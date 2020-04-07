def reverseWords(s):
    # return " ".join(s.split()[::-1])

    def reverseSubstring(i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    s = list(" ".join(s.strip().split()))

    start = 0
    for i in range(len(s)+1):
        if i == len(s) or s[i] == " ":
            reverseSubstring(start, i-1)
            start = i+1

    reverseSubstring(0, len(s)-1)

    return "".join(s)

print(reverseWords("the sky is blue")) # "blue is sky the"
print(reverseWords("  hello world!  ")) # "world! hello"
print(reverseWords("a good   example")) # "example good a"