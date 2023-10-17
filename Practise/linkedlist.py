from __future__ import annotations
import io

class DblLinkedList:
    def __init__(self) -> None:
        self._head:Node = None
        self._tail:Node = None
        self._cur:Node = None
        pass

    def __len__(self) -> int:
        return self.size()
    
    def __repr__(self) -> str:
        return str(self._head)
    
    def __iter__(self) -> Node:
        _cur = self._head
        while _cur is not None:
            yield _cur
            _cur = _cur.next

    # def __iter__(self) -> Node:
    #     self._cur = self._head
    #     return self
    
    # def __next__(self) -> Node:
    #     if self._cur is None:
    #         raise StopIteration
        
    #     cur = self._cur
    #     self._cur = self._cur.next
    #     return cur
    
    def append(self, data) -> Node:
        if self._head is None:
            self._head = Node(data)
            self._tail = self._head
            return self._head
        else:
            tail_node, is_last = self._tail.append(Node(data))
            assert is_last
            self._tail = tail_node
            return tail_node
    
    def insert(self, node:Node, new_node:Node) -> Node:
        inserted_node, is_first = node.insert(new_node)
        if is_first:
            self._head = inserted_node
        return new_node

    def delete(self, node:Node) -> Node:
        last_node, is_first, is_last = node.delete()
        if is_first:
            self._head = last_node
        if is_last:
            self._tail = last_node
        node.prev=None
        node.next=None
        return last_node
    
    def find(self, value) -> Node:
        return self._head.find(value)
    
    def size(self) -> int:
        i:int = -1
        for i, _ in enumerate(self):
            pass
        return i+1
    
    pass


class Node:    
    def __init__(self, data):
        self.data = data
        self.next:Node = None
        self.prev:Node = None
    
    def __repr__(self) -> str:
        n:Node = self
        str_io = io.BytesIO()
        while n is not None:
            str_io.write(f"{n.data},".encode("utf-8"))
            n = n.next    
        return str_io.getvalue().decode("utf-8")
    
    def insert(self, new_node:Node) ->tuple[Node, bool] :
        new_node.next = self
        new_node.prev = self.prev
        is_first:bool = self.prev is None
        #check if it is first element
        if not is_first:
            self.prev.next = new_node
            
        self.prev = new_node
        return new_node, is_first
        
    def delete(self) -> tuple[Node, bool, bool]:
        #check if it is first element
        is_first = self.prev is None
        is_last = self.next is None
        last_node:Node = None
        if is_first:
            if not is_last:
                self.next.prev = None
            last_node = self.next
        else:
            self.prev.next = self.next
            last_node = self.prev

        #check if it is not last element
        if not is_last:
            self.next.prev = self.prev
        
        return last_node, is_first, is_last
    
    def append(self, new_node:Node) -> tuple[Node, bool]:
        is_last = self.next is None
        new_node.next = self.next
        new_node.prev = self
        if self.next is not None:
            self.next.prev = new_node
        self.next = new_node
        return new_node, is_last

    def find(self, value) -> Node:
        n:Node = self
        while n is not None:
            if n.data == value:
                return n
            n = n.next
        return None

if __name__ == "__main__":
    lead:Node = None
    a_node = Node("a")
    lead = a_node

    b_node, is_first = a_node.insert(Node("b"))
    print(b_node, is_first)
    lead = b_node if is_first else lead


    c_node, is_first = b_node.insert(Node("c"))
    print(c_node, is_first)
    lead = c_node if is_first else lead

    d_node, is_first = b_node.insert(Node("d"))
    print(d_node, is_first)
    lead = d_node if is_first else lead

    print(lead)

    d_node.delete()
    print(lead)

    f_node = lead.find("b")
    print(f_node.prev.data)

    new_node, is_first, is_last = f_node.delete()
    lead = new_node if is_first else lead
    print(lead)

    g_node, is_last = c_node.append(Node("g"))
    print(lead, is_last)
    # print(g_node.prev.data)
    # print(g_node.next.data)
    # print(g_node.next.prev.data)
    # for element in lead:
    #     print(element.data)

    

