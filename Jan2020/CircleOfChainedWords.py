#SKill: linked List
#Difficulty : Easy
#Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

#Given a list of words, determine if there is a way to 'chain' all the words in a circle.

#Example:
#Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
#Output: True
#Explanation:
#The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

#Here's a start:

#Analysis:
# begin with a linked list
# each node represents a word
# For each node, each first character register with address of the node in map register "head"
# each last character register with address of the node in map register "tail"
# for first node, it puts first character "e" into head map e-> first
# it puts last character "s" into tail map s -> first
#
# for second node, it search in tail to link to, if not found, register "k" into head map k-> second
# then search in head to link to, if not found, register "t" into tail map
# ...
# for third node, it search in tail to link to, if not found, register "a" into head map a-> third
# then search in head to link to, it is found , tail link to first, remove head map e-> first
#
# for fourth node, it search in tail to link to , yes, found, first link to head, remove tail map s->first
# then search in head to link to, it is found, tail link to second, remove head map k->second
# until end of array
# in the end, check if circle linked list
# iterate the linked list for N+1 times, if it reach the first node at N+1.... it is circle, otherwise it is not a circle
# MVP ... assume mp repeated character in head and tail....
# next, the head, tail map should contain linked list for repeated character..... <--- defaultdict would help
# Time cost : O(N)
# Time to create linked list : O(N)
# Time to check circular queue: O(N)
# Space cost: O(N)
# Space for linked List : O(N)


from collections import defaultdict
from collections import deque

class Node:
    def __init__(self, word, next=None):
        self.value = word
        self.next = next

class Solution():
    def chainedWords(self, words):
        l = len(words)
        headMap = defaultdict(deque)
        tailMap = defaultdict(deque)

        #Create the linked list
        baseNode = Node(words[0])
        self.__registerHeadMap(headMap, baseNode)
        self.__registerTailMap(tailMap, baseNode)

        for i in range(1, l):
            w = words[i]
            node = Node(w)
            firstCh = w[0]
            lastCh = w[-1]
            if len(tailMap[firstCh]) == 0:
                self.__registerHeadMap(headMap, node)
            else:
                parentNode = tailMap[firstCh].popleft()
                parentNode.next = node

            if len(headMap[lastCh]) == 0:
                self.__registerTailMap(tailMap, node)
            else:
                childNode = headMap[lastCh].popleft()
                node.next = childNode

        #Check circular
        cnt = 1
        isCircular = False
        nextNode = baseNode.next
        while nextNode is not None and cnt <= l:
            cnt += 1
            if nextNode == baseNode:
                isCircular = True
                break
            nextNode = nextNode.next

        cmp = baseNode == nextNode
        return isCircular and cnt==l+1

    def __registerHeadMap(self, headMap, node):
        headMap[node.value[0]].append(node)
    def __registerTailMap(self, tailMap, node):
        tailMap[node.value[-1]].append(node)

def chainedWords(words):
    # Fill this in.
    solu = Solution()
    return solu.chainedWords(words)

if __name__ == "__main__":
    print(chainedWords(['apple', 'area', 'eggs', 'snack', 'karat', 'tuna']))

    print (chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
    # True

