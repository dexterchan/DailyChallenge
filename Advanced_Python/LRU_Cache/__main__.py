from .cache import LRU, Node


if __name__ == "__main__":
    ...
    base: Node = Node()
    base.append_node(Node(value=1)).append_node(Node(value=2))
