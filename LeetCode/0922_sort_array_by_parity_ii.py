def sortArrayByParityII(A):
    i, j = 0, 1

    while i < len(A) or j < len(A):
        if A[i]%2 == 1 and A[j]%2 == 0:
            A[i], A[j] = A[j], A[i]
            i += 2
            j += 2

        while i < len(A) and A[i]%2 == i%2: i += 2
        while j < len(A) and A[j]%2 == j%2: j += 2

    return A

print(sortArrayByParityII([2, 3, 1, 1, 4, 0, 0, 4, 3, 3]))