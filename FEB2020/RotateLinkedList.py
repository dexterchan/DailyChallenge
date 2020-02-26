
#Given a linked list and a number k, rotate the linked list by k places.

#Here's some starter code and an example:

#Analysis
#iterate each element and find the length of the linked list O(N)
#find the tail node
#calculate the index to fir rotate i=L%k
#Count 0 up to i, find the new head
# append head to tail

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret

def rotate_list(list, k):
    # Fill this in.
    itr = list
    l = 0
    tail = None
    while itr is not None:
        l += 1
        tail = itr
        itr = itr.next

    ptr = k if k < l else k%l
    newhead = list
    prevhead = None
    for i in range (ptr):
        prevhead = newhead
        newhead = newhead.next

    tail.next = list
    prevhead.next = None
    return newhead



if __name__ == "__main__":
    # Order is 1, 2, 3, 4
    llist = Node(1, Node(2, Node(3, Node(4))))

    print(rotate_list(llist, 5))
    # 3412

    llist = Node(1, Node(2, Node(3, Node(4))))
    # Order should now be 3, 4, 1, 2
    print(rotate_list(llist, 2))
    # 3412

