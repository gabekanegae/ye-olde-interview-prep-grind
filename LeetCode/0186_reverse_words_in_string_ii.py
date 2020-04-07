def reverseWords(s):
    # return " ".join(s.split()[::-1])

    def reverseSubstring(i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    start = 0
    for i in range(len(s)+1):
        if i == len(s) or s[i] == " ":
            reverseSubstring(start, i-1)
            start = i+1

    reverseSubstring(0, len(s)-1)

s = list("the sky is blue")
reverseWords(s)
print(s) # "blue is sky the"

s = list("hello world!")
reverseWords(s)
print(s) # "world! hello"

s = list("a good example")
reverseWords(s)
print(s) # "example good a"