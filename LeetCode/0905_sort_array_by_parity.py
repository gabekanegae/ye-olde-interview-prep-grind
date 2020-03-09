def sortArrayByParity(A):
    i, j = 0, len(A)-1

    while i <= j:
        if A[i] % 2 == 1 and A[j] % 2 == 0: # odd, even
            A[i], A[j] = A[j], A[i]

        if A[i] % 2 == 0: i += 1
        if A[j] % 2 == 1: j -= 1

    return A

print(sortArrayByParity([3, 1, 2, 4]))