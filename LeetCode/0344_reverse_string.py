def reverseString(s):
    i, j = 0, len(s)-1

    while i < j:
        s[i], s[j] = s[j], s[i]

        i += 1
        j -= 1

s = list("Hannah")
reverseString(s)
print(s)

s = list("abc")
reverseString(s)
print(s)