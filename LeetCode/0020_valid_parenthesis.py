# O(n) time, O(n) space
def isValid(s):
    opens, closes = "({[", ")}]"
    stack = []
    for c in s:
        if c in opens:
            stack.append(c)
        elif c in closes:
            if len(stack) < 1: return False

            popped = stack.pop()
            if popped != opens[closes.index(c)]: return False

    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("((()([])))"))
print(isValid("()])("))
print(isValid("(){}{[}"))