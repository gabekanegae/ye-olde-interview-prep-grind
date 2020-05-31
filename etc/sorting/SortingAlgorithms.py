def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            # Check when two side-to-side elements should be swapped
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

def insertionSort(array):
    for i in range(1, len(array)):
        cur = array[i]

        # Bring element back along the sorted portion
        k = i
        while k > 0 and cur < array[k-1]:
            array[k] = array[k-1]
            k -= 1

        array[k] = cur

def selectionSort(array):
    for i in range(len(array)): 
        k = i

        # Find minimum element from the unsorted portion
        for j in range(i+1, len(array)):
            if array[k] > array[j]:
                k = j

        array[i], array[k] = array[k], array[i]

def mergeSort(array):
    if len(array) < 2: return array

    mid = len(array)//2

    leftArray = mergeSort(array[:mid])
    rightArray = mergeSort(array[mid:])

    i, j, k = 0, 0, 0

    # Grab minimum between the two halves
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    # Grab leftovers from any of the halves
    while i < len(leftArray):
        array[k] = leftArray[i]
        i += 1
        k += 1
    while j < len(rightArray):
        array[k] = rightArray[j]
        j += 1
        k += 1

    return array

def quickSort(array, startl=0, startr=0):
    if startr == 0: startr = len(array)-1

    if len(array) < 2: return

    # Grab middle element as pivot
    pivot = array[(startl+startr)//2]
    l, r = startl, startr

    # Bring elements smaller than pivot to the left, and bigger to the right
    while l <= r:
        # Find two elements that should be in opposite sides
        while array[l] < pivot:
            l += 1
        while array[r] > pivot:
            r -= 1

        if l <= r:
            array[l], array[r] = array[r], array[l]

            l += 1
            r -= 1

    # New pivot location
    pivot = l

    # Left call (if there are elements to the left of pivot)
    if startl < pivot-1:
        quickSort(array, startl, pivot-1)

    # Right call (if there are elements to the right of pivot)
    if pivot < startr:
        quickSort(array, pivot, startr)