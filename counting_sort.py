def counting_sort(A):
    n = len(A)
    k = max(A)

    B = [0] * n
    C = [0] * (k + 1)

    for j in range(n):
        C[A[j]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B


A = [2, 5, 3, 0, 2, 3, 0, 3]
B = counting_sort(A)
print(B)
