import math
import copy


def merge_sort(A):
    _merge_sort(A, 0, len(A))


def _merge_sort(A, p, r):
    if p >= r - 1:
        return
    q = math.floor((p + r) / 2)
    _merge_sort(A, p, q)
    _merge_sort(A, q, r)
    merge(A, p, q, r)


def merge(A, p, q, r):
    len_L = q - p
    len_R = r - q
    L = copy.deepcopy(A[p:q])
    R = copy.deepcopy(A[q:r])

    i = 0
    j = 0
    k = p
    while i < len_L and j < len_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len_L:
        A[k] = L[i]
        i += 1
        k += 1
    while j < len_R:
        A[k] = R[j]
        j += 1
        k += 1


A = [5, 2, 4, 6, 1, 3]
merge_sort(A)
print(A)
