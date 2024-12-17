def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i, len(A)):
            if A[min_index] > A[j]:
                min_index = j
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp


A = [5, 2, 4, 6, 1, 3]
selection_sort(A)
print(A)
