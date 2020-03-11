def scoreOfParentheses(S):
    total = 0

    cur = 0
    for i in range(len(S)):
        if S[i] == "(":
            cur += 1
        elif S[i] == ")":
            cur -= 1
            if S[i-1] == "(":
                total += 2**cur

    return total

print(scoreOfParentheses("()")) # 1
print(scoreOfParentheses("()()")) # 2
print(scoreOfParentheses("((()))")) # 4
print(scoreOfParentheses("(()(()))")) # 6
print(scoreOfParentheses("(((()))()())")) # 12