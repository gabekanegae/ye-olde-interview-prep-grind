def numDecodings(s):
    memo = {}

    def rec(i):
        if i == len(s): return 1
        if s[i] == "0": return 0
        if i == len(s)-1: return 1

        if i in memo: return memo[i]

        if (1 <= int(s[i:i+2]) <= 26):
            memo[i] = rec(i+1) + rec(i+2)
        else:
            memo[i] = rec(i+1)

        return memo[i]

    return rec(0)

print("total:", numDecodings("12")) # 2
print("total:", numDecodings("226")) # 3
print("total:", numDecodings("27")) # 1