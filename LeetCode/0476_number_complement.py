def findComplement1(num):
    return int("".join("0" if c == "1" else "1" for c in bin(num)[2:]), 2)

from math import log2

def findComplement2(num):
    n = int(log2(num)) + 1
    mask = (1 << n) - 1
    return mask ^ num

print(findComplement1(5)) # 2
print(findComplement2(5)) # 2