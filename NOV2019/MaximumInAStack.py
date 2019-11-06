#Skill: stack, node
#Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max()
# which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
      class Node:
          def __init__(self, v):
              self.value = v
              self.next = None

      def __init__(self):
        # Fill this in.
        self.stackMemory = None
        self.stackMax = None

      def push(self, val):
        # Fill this in.
        newNode = MaxStack.Node(val)
        newNode.next = self.stackMemory
        self.stackMemory = newNode
        #Stack Max
        if self.stackMax is not None and self.stackMax.value <= val:
            maxValue = MaxStack.Node(val)
            maxValue.next = self.stackMax
            self.stackMax = maxValue
        elif self.stackMax is None:
            self.stackMax = MaxStack.Node(val)

      def pop(self):
        # Fill this in.
        if self.stackMemory is None:
            return self.stackMemory.value
        popNodeValue = self.stackMemory.value
        self.stackMemory = self.stackMemory.next

        if self.stackMax.value == popNodeValue:
            self.stackMax = self.stackMax.next

        return popNodeValue

      def max(self):
        # Fill this in.
        return self.stackMax.value

if __name__ == "__main__":
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print (s.max())
    # 3
    s.pop()
    s.pop()
    print (s.max())
    # 2