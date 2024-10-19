from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    next: Optional["Node"] = None


class SinglyLinkedList:
    head: Node | None

    def __init__(self, values):
        tail = None
        for i, val in enumerate(values):
            node = Node(key=val, next=None)
            if i == 0:
                self.head = node
                tail = self.head
            else:
                self.insert(node, tail)
                tail = node

    def search(self, key: int):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x

    def prepend(self, x: Node):
        x.next = self.head
        self.head = x

    def insert(self, x: Node, y: Node):
        x.next = y.next
        y.next = x

    def delete(self, x: Node):
        if x == self.head:
            self.head = x.next
        else:
            prev = self.head
            while prev.next != x:
                prev = prev.next
            prev.next = x.next

    def __str__(self):
        string = ""
        x = self.head
        while x != None:
            if x == self.head:
                string += f"{x.key} "
            else:
                string += f"-> {x.key} "
            x = x.next
        return string


if __name__ == "__main__":
    linked_list = SinglyLinkedList([9, 16, 4, 1])
    print(linked_list)

    x = linked_list.search(9)
    print(x)

    linked_list.delete(x)
    print(linked_list)

    x = Node(key=2, next=None)
    linked_list.prepend(x)
    print(linked_list)
