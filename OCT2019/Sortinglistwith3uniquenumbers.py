#Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

#Example 1:
#Input: [3, 3, 2, 1, 3, 2, 1]
#Output: [1, 1, 2, 2, 3, 3, 3]
class List:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

def debug (nums):
    currentNode = nums
    while currentNode != None:
        print(currentNode.val, end=',')
        currentNode = currentNode.next
    print("\n")
def sortNums(nums):
  # Fill this in.
    head = None
    last = None
    currentNode = None
    for inx, x in enumerate(nums):
        if(inx == 0 ):
            head = List(x)
            currentNode = head
        else:
            currentNode.next = List(x)
            currentNode.next.prev = currentNode
            currentNode = currentNode.next
        if (inx == len(nums)-1):
            last = currentNode

    currentNode = head
    count = 0
    while (count<len(nums) and currentNode.next != None):
        count = count + 1
        if(currentNode.val==2):
            currentNode=currentNode.next
            #debug(head)
        elif(currentNode.val==1):
            if(head == currentNode):
                currentNode = currentNode.next
            else:
                tmpNode=currentNode.next
                if (currentNode.prev != None):
                    currentNode.prev.next=currentNode.next
                currentNode.next.prev=currentNode.prev
                head.prev=currentNode
                currentNode.prev=None
                currentNode.next=head
                head=currentNode
                currentNode=tmpNode
                #debug(head)
        else:

            tmpNode = currentNode.next
            if(head == currentNode):
                    head = currentNode.next
            if(currentNode.prev != None):
                    currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            last.next = currentNode
            currentNode.prev=last
            currentNode.next = None
            last = currentNode
            currentNode = tmpNode
            #debug(head)

    result = []
    currentNode = head
    while currentNode != None:
        result.append(currentNode.val)
        currentNode = currentNode.next


    return result

if __name__ == "__main__":
    N =  sortNums([3, 3, 2, 1, 3, 2, 1])
    #N = sortNums([ 2, 1, 3, 2, 1])
    print (N)
    # [1, 1, 2, 2, 3, 3, 3]