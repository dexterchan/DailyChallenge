
#Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

#Here's a starting point:

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.toggle = True
    def __resolveMasterSlave(self):
        if self.toggle:
            return self.s1, self.s2
        else:
            return self.s2, self.s1
    def enqueue(self, val):
        master, slave = self.__resolveMasterSlave()
        master.append(val)

    def dequeue(self):
        master, slave = self.__resolveMasterSlave()
        while len(master)!=0:
            slave.append(master.pop())
        v = slave.pop()
        while len (slave)!=0:
            master.append(slave.pop())
        return v


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())
    # 1 2 3