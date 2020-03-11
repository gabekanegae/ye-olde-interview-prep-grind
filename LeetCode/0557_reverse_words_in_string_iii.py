def reverseWords(s):
    def reverseSubstring(i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    s = list(s)

    start = 0
    for i in range(len(s)):
        if s[i] == " ":
            reverseSubstring(start, i-1)
            start = i+1
    
    reverseSubstring(start, len(s)-1)

    return "".join(s)

print(reverseWords("Let's take LeetCode contest"))