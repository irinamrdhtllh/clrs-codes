from dataclasses import dataclass
from typing import Optional

from queues import Queue


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def pre_order(node: Optional[Node]):
    if node is None:
        return
    print(node.key, end=" ")
    pre_order(node.left)
    pre_order(node.right)


def post_order(node: Optional[Node]):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.key, end=" ")


def in_order(node: Optional[Node]):
    if node is None:
        return
    in_order(node.left)
    print(node.key, end=" ")
    in_order(node.right)


def bfs(root: Node):
    queue = Queue([root])
    while not queue.is_empty():
        node = queue.dequeue()
        print(node.key, end=" ")
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)


if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    node_5.left = node_7
    node_5.right = node_8

    node_6.left = node_9

    pre_order(node_1)
    print()
    post_order(node_1)
    print()
    in_order(node_1)
    print()
    bfs(node_1)
