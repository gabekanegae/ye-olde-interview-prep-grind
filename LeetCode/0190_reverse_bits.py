def reverseBits(n):
    result = 0
    for _ in range(32):
        result *= 2
        result += n%2
        n //= 2

    return result

print(reverseBits(43261596)) # 964176192