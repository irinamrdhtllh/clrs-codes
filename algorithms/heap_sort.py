class Heap:
    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)

    def __getitem__(self, i):
        return self.array[i]

    def __setitem__(self, i, value):
        self.array[i] = value

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


def heap_sort(A: Heap):
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        A.heap_size = A.heap_size - 1
        max_heapify(A, 0)


def build_max_heap(A: Heap):
    n = (A.heap_size - 1) // 2
    for i in range(n, -1, -1):
        max_heapify(A, i)


def max_heapify(A: Heap, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = 0

    if l < A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < A.heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest)


A = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
heap_sort(A)
print(A)
