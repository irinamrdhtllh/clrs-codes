class Stack:
    def __init__(self, array, max_length=10):
        self.array = max_length * [0]
        self.max_length = max_length

        if len(array) == 0:
            self.top = len(array)
        else:
            self.top = len(array) - 1

        for i, val in enumerate(array):
            self.array[i] = val

    def __str__(self):
        return str(self.array[0 : self.top + 1])

    def empty(self):
        return self.top == 0

    def push(self, x):
        if self.top + 1 == self.max_length:
            raise Exception("Overflow")
        self.top += 1
        self.array[self.top] = x

    def pop(self):
        if self.empty():
            raise Exception("Underflow")
        self.top -= 1
        return self.array[self.top + 1]


stack = Stack(array=[15, 6, 2, 9])

stack.push(17)
stack.push(3)
print(stack)

stack.pop()
print(stack)
