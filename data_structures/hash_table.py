from dataclasses import dataclass
from typing import Optional

from data_structures.linked_list import Node, SinglyLinkedList


@dataclass
class Entry:
    key: object
    value: int


class ChainedHashTable:
    table: Optional[SinglyLinkedList]

    def __init__(self, table_capacity=10):
        self.table = table_capacity * [None]
        self.table_capacity = table_capacity

    def insert(self, k: int):
        index = hash(k) % self.table_capacity
        if self.table[index] is None:
            self.table[index] = SinglyLinkedList([k])
        else:
            node = Node(k)
            self.table[index].prepend(node)

    def search(self, k: int):
        index = hash(k) % self.table_capacity
        if self.table[index] is None:
            raise Exception("Key doesn't exist.")
        else:
            return self.table[index].search(k)

    def delete(self, k: int):
        index = hash(k) % self.table_capacity
        if self.table[index] is None:
            raise Exception("Key doesn't exist.")
        else:
            node = self.search(k)
            self.table[index].delete(node)

    def __str__(self):
        string = "{"
        for bucket in self.table:
            if bucket is not None:
                k = bucket.head
                while k != None:
                    if len(string) == 1:
                        string += f"{k.key}"
                    else:
                        string += f", {k.key}"
                    k = k.next
        string += "}"
        return string


if __name__ == "__main__":
    table = ChainedHashTable()
    table.insert(1)
    table.insert(1)
    table.insert(4)
    table.insert(5)
    table.insert(2)
    table.insert(7)
    print(table)

    table.delete(5)
    print(table)

    x = table.search(1)
    print(x)
