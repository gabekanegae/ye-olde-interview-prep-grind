def myAtoi(s):
    if not s: return 0

    num = 0
    sign = 1

    i = 0
    while i < len(s) and s[i] == " ": i += 1

    if i == len(s): return 0

    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == "+":
        i += 1

    while i < len(s):
        if s[i] not in "0123456789": break

        num *= 10
        num += ord(s[i])-ord("0")

        i += 1

    ans = num*sign
    if ans < -2**31: return -2**31
    if ans > 2**31-1: return 2**31-1
    return ans

print(myAtoi("4193 with words")) # 4193
print(myAtoi("     -42")) # -42
print(myAtoi("-91283472332")) # -2147483648
print(myAtoi("      -11919730356x"))