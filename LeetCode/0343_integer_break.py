def solve(n):
    best = n-1
    for baseAmt in range(2, n):
        # numbers will be [base+1 [... (plusOneAmt) times], base, [... (baseAmt-plusOneAmt) times]]
        base = n // baseAmt
        plusOneAmt = n - base * baseAmt

        # product of all numbers
        product = base ** (baseAmt - plusOneAmt) * (base + 1) ** plusOneAmt
        if product > best:
            best = product
        else:
            break

    return best

print(solve(2))
print(solve(10))