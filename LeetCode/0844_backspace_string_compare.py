def backspaceCompare1(s, t):
    def build(s):
        sr = []
        for c in s:
            if c == "#":
                try: sr.pop()
                except: pass
            else:
                sr.append(c)

        return "".join(sr)
    
    return build(s) == build(t)

def backspaceCompare2(s, t):
    i, iDel = len(s)-1, 0
    j, jDel = len(t)-1, 0

    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == "#":
                iDel += 1
                i -= 1
            elif iDel > 0:
                iDel -= 1
                i -= 1
            else:
                break

        while j >= 0:
            if t[j] == "#":
                jDel += 1
                j -= 1
            elif jDel > 0:
                jDel -= 1
                j -= 1
            else:
                break

        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1

    return True

print(backspaceCompare1("ab#c", "ad#c")) # True
print(backspaceCompare2("ab#c", "ad#c")) # True
print(backspaceCompare1("ab##", "c#d#")) # True
print(backspaceCompare2("ab##", "c#d#")) # True
print(backspaceCompare1("a##c", "#a#c")) # True
print(backspaceCompare2("a##c", "#a#c")) # True
print(backspaceCompare1("a#c", "b")) # False
print(backspaceCompare2("a#c", "b")) # False