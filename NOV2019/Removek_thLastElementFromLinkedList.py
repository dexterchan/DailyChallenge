# Skill: List traversal
#You are given a singly linked list and an integer k. Return the linked list, removing the k-th last element from the list.

#Try to do it in a single pass and using constant space.

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)




def remove_kth_from_linked_list(head, k):

    cur = head
    lastK = head
    count = 0

    while cur.next is not None:

        if count >= k:
            lastK = lastK.next
        count = count + 1
        cur = cur.next

    if count >= k and lastK.next is not None:
        lastK.next=lastK.next.next
    if count == k-1:
        head = head.next


    return head

if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(head)
    # [1, 2, 3, 4, 5]
    head = remove_kth_from_linked_list(head, 1)
    print(head)
    # [1, 2, 4, 5]
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = remove_kth_from_linked_list(head, 3)
    print(head)

    head = Node(1, Node(2, Node(3)))
    head = remove_kth_from_linked_list(head, 3)
    print(head)