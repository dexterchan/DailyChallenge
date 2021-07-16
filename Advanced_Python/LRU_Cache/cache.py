from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class Node(BaseModel):
    value: int = 0
    prev_node: Optional[Node] = None
    next_node: Optional[Node] = None

    def append_node(self, node: Node) -> Node:
        if self.next_node is not None:
            self.prev_node = node

        node.next_node = self.next_node
        node.prev_node = self

        self.next_node = node

        return self

    def next(self) -> Node:
        return self.next_node

    def remove_node(self) -> None:
        self.prev_node = self.next_node
# class Node():
#     def __init__(self, value:int, prev_node:Node=None, next_node:Node=None) -> None:
#         self.value = value
#         self.prev_node = prev_node
#         self.next_node = next_node


class LRU:
    def __init__(self, size: int) -> None:
        self.size = size
        self.my_dict = {}
        self.priority_lst
