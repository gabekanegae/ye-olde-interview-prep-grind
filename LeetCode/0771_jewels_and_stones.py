def numJewelsInStones(J, S):
    J = set(J)
    return sum(c in J for c in S)

print(numJewelsInStones("aA", "aAAbbbb")) # 3
print(numJewelsInStones("z", "ZZ")) # 0