def quicksort(A):
    _quicksort(A, 0, len(A))


def _quicksort(A, p, r):
    if p < r - 1:
        q = partition(A, p, r)
        _quicksort(A, p, q)
        _quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[r - 1]
    A[r - 1] = A[i + 1]
    A[i + 1] = temp

    return i + 1


A = [2, 8, 7, 1, 3, 5, 6, 4]
quicksort(A)
print(A)
