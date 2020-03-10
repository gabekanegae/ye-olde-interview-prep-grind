def hammingWeight(n):
    # return bin(n).count("1")

    count = 0
    while n > 0:
        count += n%2
        n //= 2

    return count

print(hammingWeight(7))