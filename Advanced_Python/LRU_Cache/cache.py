from __future__ import annotations
from typing import Any, Optional, Tuple
from pydantic import BaseModel


class Node(BaseModel):
    value: str = 0
    prev_node: Optional[Node] = None
    next_node: Optional[Node] = None
    base: Optional[bool] = False

    def append_node(self, node: Node) -> Node:
        node.next_node = self.next_node
        if node.next_node is not None:
            node.next_node.prev_node = node
        node.prev_node = self
        self.next_node = node

        return self

    def next(self) -> Node:
        return self.next_node

    def remove_node(self) -> None:
        if self.base:
            raise "BASE cannot be removed"
        if self.prev_node is None:
            return
        self.prev_node.next_node = self.next_node
        if self.next_node is not None:
            self.next_node.prev_node = self.prev_node
        self.prev_node = None
        self.next_node = None

    def __str__(self) -> str:
        value = self.value
        if self.base:
            value = "BASE"
        if self.next_node is not None:
            return f"{value}->{str(self.next_node)}"
        else:
            return f"{value}"

# class Node():
#     def __init__(self, value:int, prev_node:Node=None, next_node:Node=None) -> None:
#         self.value = value
#         self.prev_node = prev_node
#         self.next_node = next_node


class LRU:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.my_dict = {}
        self.priority_lst: Node = Node(base=True)

    def replace(self, key: str, value: Any):
        (_, node) = self.my_dict[key]
        prev_node: Node = node.prev_node
        new_node: Node = Node(value=key)
        node.remove_node()
        prev_node.append_node(new_node)
        del self.my_dict[key]
        print(f"{key}:{value}")
        self.my_dict[key] = (value, new_node)
        ...

    def put(self, key: str, value: Any):
        if key in self.my_dict:
            self.replace(
                key=key, value=value
            )
            return
        if len(self.my_dict) == self.max_size:
            redundant_node = self.priority_lst.next()
            if redundant_node is not None:
                redundant_node.remove_node()
                del self.my_dict[redundant_node.value]

        node = Node(value=key)
        self.my_dict[key] = (value, node)
        self.priority_lst.append_node(
            node
        )

    def get(self, key: str) -> Any:
        if key not in self.my_dict:
            raise "Not found"
        (value, node) = self.my_dict[key]
        next_node: Node = node.next()
        if next_node is not None:
            node.remove_node()
            next_node.append_node(node=node)
        return value

    def __str__(self) -> str:
        m = ""
        for k, v in self.my_dict.items():
            m = m + f"{{ {k}:{v[0]} }},"
        return f" m:{m} inx:{str(self.priority_lst)}"
