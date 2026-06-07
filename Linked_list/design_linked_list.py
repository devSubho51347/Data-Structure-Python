# leetcode - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def _get_node(self, index: int) -> Node:
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr
    def _insert_between(self, val: int, prev_node: Node, next_node: Node) -> None:
        node = Node(val)
        node.prev = prev_node
        node.next = next_node
        prev_node.next = node
        next_node.prev = node
        self.size += 1
    def _delete_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._get_node(index).val
    def addAtHead(self, val: int) -> None:
        self._insert_between(val, self.head, self.head.next)
    def addAtTail(self, val: int) -> None:
        self._insert_between(val, self.tail.prev, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self._insert_between(val, self.tail.prev, self.tail)
        else:
            next_node = self._get_node(index)
            self._insert_between(val, next_node.prev, next_node)
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self._delete_node(self._get_node(index))