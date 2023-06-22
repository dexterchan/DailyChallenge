from linkedlist import (DblLinkedList, Node)

def test_insert_linked_list():
    dbl_list:DblLinkedList = DblLinkedList()

    dbl_list.append(1)
    dbl_list.append(2)
    dbl_list.append(3)
    #print(l._head)
    for i,v in enumerate(dbl_list):
        assert v.data == i+1, f"v.data: {v.data} != {i+1}"

    n = dbl_list.find(2)
    assert n.data == 2
    assert n.prev.data == 1
    assert n.next.data == 3

    
    #remove 2
    dbl_list.delete(n)
    assert dbl_list.size() == 2
    assert dbl_list._head.data == 1
    assert dbl_list._tail.data == 3

    #remove 3
    dbl_list.delete(dbl_list._tail)
    assert dbl_list.size() == 1
    assert dbl_list._head.data == 1
    assert dbl_list._tail.data == 1

    

    #remove 1
    dbl_list.delete(dbl_list._head)
    assert dbl_list.size() == 0

    for i in range(1, 5+1):
        dbl_list.append(i)
    assert dbl_list.size() == 5

    for i,v in enumerate(dbl_list):
        assert v.data == i+1, f"v.data: {v.data} != {i+1}"

    n3 = dbl_list.find(3)
    n1 = n3.prev.prev
    assert n3.data == 3
    assert n1.data == 1
    #insert 3 in front of 1
    dbl_list.delete(n3)
    dbl_list.insert(n1, n3)
    print(dbl_list)

    