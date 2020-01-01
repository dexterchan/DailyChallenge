
#Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.

#Note: be sure that pop() and top() handle being called on an empty stack.

#Analysis
# To archive push and pop at constant, we need linked list as base
# there should be a pointer to record the last element of stack....
# Then in LIFO or getting top element, we can archieve O(1)
# For getting min, we would have a min pointer to compare every element going in and check if element < min pointer
# if yes, we update min pointer
# for min update during pop, it is tricky
# if min value is not equal to pop value, cost is still constant
# if min value is equal to pop value, cost is N to update the min value

class LinkedList:
    def __init__(self, ele, prev=None, next=None):
        self.value = ele
        self.next = next
        self.prev = prev


class minStack(object):
    def __init__(self):
        # Fill this in.
        self.linkedList = None
        self.minPointer = None
        self.topItem = None

    def push(self, x):
        # Fill this in.
        if self.linkedList is None:
            self.linkedList = LinkedList(x)
            self.topItem = self.linkedList
            self.minPointer = self.linkedList
            return
        self.topItem.next = LinkedList(x)
        self.topItem.next.prev = self.topItem
        self.topItem = self.topItem.next
        if self.minPointer.value > self.topItem.value:
            self.minPointer = self.topItem
        return

    def pop(self):
        # Fill this in.
        if self.topItem is None:
            return None
        value = self.topItem.value
        if self.topItem == self.linkedList:
            self.linkedList = None
            self.minPointer = None
            self.topItem = None
            return value

        popItem = self.topItem
        prevItem = self.topItem.prev
        if prevItem is not None:
            prevItem.next = None
        self.topItem = prevItem

        if self.minPointer == popItem:
            #Update minPointer again
            self.__updateMinPointer()

        return value

    def __updateMinPointer(self):
        cur = self.linkedList
        self.minPointer = cur
        while cur != None:
            if cur.value < self.minPointer.value:
                self.minPointer = cur
            cur = cur.next



    def top(self):
        # Fill this in.
        if self.topItem is not None:
            return self.topItem.value
        else:
            return None

    def getMin(self):
        # Fill this in.
        if self.minPointer is not None:
            return self.minPointer.value
        else:
            return None

if __name__ == "__main__":
    x = minStack()
    x.push(-2)
    x.push(0)
    x.push(-3)
    print(x.getMin())
    # -3
    x.pop()
    print(x.top())
    # 0
    print(x.getMin())
    # -2
    x.pop()
    print(x.getMin())

    print ("Pop last item {}".format(x.pop()))
    print ("No item:"+ str(x.getMin() is None))

    x.push(0)
    print(x.getMin())
