class Queue:
    def __init__(self, array, max_length=10):
        self.array = max_length * [0]
        self.head = 0
        self.tail = len(array)
        self.max_length = max_length

        for i, val in enumerate(array):
            self.array[i] = val

    def __str__(self):
        if self.head > self.tail:
            return str(
                self.array[self.head : self.max_length] + self.array[0 : self.tail]
            )
        return str(self.array[self.head : self.tail])

    def enqueue(self, x):
        if (self.head == self.tail + 1) or (
            self.head == 0 and self.tail == self.max_length - 1
        ):
            raise Exception("Overflow")
        self.array[self.tail] = x
        if self.tail == self.max_length - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            raise Exception("Underflow")
        x = self.array[self.head]
        if self.head == self.max_length - 1:
            self.head = 0
        else:
            self.head += 1
        return x


queue = Queue([15, 6, 9, 8, 4])

queue.enqueue(17)
queue.enqueue(3)
queue.enqueue(5)
print(queue)

queue.dequeue()
print(queue)
