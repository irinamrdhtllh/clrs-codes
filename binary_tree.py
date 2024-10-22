from dataclasses import dataclass
from typing import Optional

from queues import Queue


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinaryTree:
    def __init__(self, values):
        i = 0
        self.root = Node(values[i])
        i += 1
        queue = Queue([self.root])
        while not queue.is_empty():
            node = queue.dequeue()
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.enqueue(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.enqueue(node.right)
            i += 1

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node: Optional[Node]):
        if node is None:
            return
        print(node.key, end=" ")
        self._pre_order(node.left)
        self._pre_order(node.right)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, node: Optional[Node]):
        if node is None:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.key, end=" ")

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node: Optional[Node]):
        if node is None:
            return
        self._in_order(node.left)
        print(node.key, end=" ")
        self._in_order(node.right)

    def bfs(self):
        queue = Queue([self.root])
        while not queue.is_empty():
            node = queue.dequeue()
            print(node.key, end=" ")
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)


if __name__ == "__main__":
    tree = BinaryTree([1, 7, 9, 2, 6, None, 9, None, None, 5, 11, 5])

    tree.pre_order()
    print()
    tree.post_order()
    print()
    tree.in_order()
    print()
    tree.bfs()
