
#Given a linked list, swap the position of the 1st and 2nd node, then swap the position of the 3rd and 4th node etc.

#Here's some starter code:
#Time complexity: O(N), space complexity:O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(llist):
    # Fill this in.
    head = llist
    curPtr = head

    prehead = head
    while curPtr is not None and curPtr.next is not None:
        orgPtr = curPtr
        curPtr = curPtr.next
        if orgPtr == head:
            head = curPtr
        else:
            prehead.next = curPtr
        curPtr.next, orgPtr.next = orgPtr , curPtr.next
        curPtr = orgPtr.next
        prehead = orgPtr


    return head





if __name__ == "__main__":


    llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(swap_every_two(llist))
    # 2, (1, (4, (3, (5, (None)))))

    llist = Node(1, Node(2))
    print(swap_every_two(llist))