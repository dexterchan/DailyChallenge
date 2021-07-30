from .cache import LRU, Node


def test_nodes():
    base: Node = Node(base=True)
    node1: Node = Node(value=1)
    node2: Node = Node(value=2)
    node3: Node = Node(value=3)
    node4: Node = Node(value=4)
    base.append_node(node1) \
        .append_node(node2) \
        .append_node(node3)
    # Full path
    print(base)

    # Remove 2
    node2.remove_node()
    print(base)

    # Remove 3
    node3.remove_node()
    print(base)

    # Remove 1
    node1.remove_node()
    print(base)

    base.append_node(node1) \
        .append_node(node2) \
        .append_node(node3)
    print(base)

    # Remove 3 down the list
    next_node = node3.next_node
    node3.remove_node()
    if next_node is not None:
        next_node.append_node(node3)
    print(base)

    # Remove 2
    node2.remove_node()
    print(base)

    # append 4
    base.append_node(node4)
    print(base)

    next_node = node4.next_node
    node4.remove_node()
    if next_node is not None:
        next_node.append_node(node4)
    print(base)


if __name__ == "__main__":
    lru = LRU(max_size=3)
    lru.put(
        key="a", value="apple"
    )
    lru.put(
        key="b", value="banana"
    )
    print(lru)

    v = lru.get("a")
    assert v == "apple"
    print(lru)

    v = lru.get("b")
    assert v == "banana"
    print(lru)

    lru.put(
        key="m", value="melon"
    )
    print(lru)

    lru.put(
        key="k", value="kiwi"
    )
    print(lru)

    v = lru.get("k")
    v = lru.get("k")
    v = lru.get("k")
    v = lru.get("k")
    v = lru.get("k")
    v = lru.get("k")
    print(lru)
    lru.get("b")
    lru.get("a")
    lru.put("b", "Beetroot")
    print(lru)

    lru.put("c", "cherry")
    print(lru)
