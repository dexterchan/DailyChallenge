
#LRU cache is a cache data structure that has limited space,
# and once there are more items in the cache than available space,
# it will preempt the least recently used item. What counts as recently used is any item a key has 'get' or 'put' called on it.

#Implement an LRU cache class with the 2 functions 'put' and 'get'.
# 'put' should place a value mapped to a certain key, and preempt items if needed.
# 'get' should return the value for a given key if it exists in the cache, and return None if it doesn't exist.

#Here's some examples and some starter code.
#Analysis
#a LRU cache
# Get in O(N)
# Put in O(1)

#Cache is a linked list of node
#LRUCache, contain the size , head and tail of the linked list
# it pre-initialize the linked list of size N
#it
#when insert, insert to the end
#when get, search for the key in linked list, O(N), insert the node up one level

BLANK = (None, None)
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key

class LRUCache:
    def __init__(self, space):
        # Fill this in.
        self.__cache = [ None ] * space
        for i in range(space):
            self.__cache[i] = Node(None, None)
        self.size = 0
        self.MaxSize = space

    def get(self, key):
        # Fill this in.
        inx = 0
        foundValue = None
        for inx in range(self.size):
            if self.__cache[inx].key == key:
                foundValue = self.__cache[inx].value
                break

        if foundValue is not None and inx > 0:
            preInx = inx - 1
            tmpKey = self.__cache[preInx].key
            tmpValue = self.__cache[preInx].value
            self.__cache[preInx].key = self.__cache[inx].key
            self.__cache[preInx].value = self.__cache[inx].value
            self.__cache[inx].key = tmpKey
            self.__cache[inx].value = tmpValue

        return foundValue


    def put(self, key, value):
        inx = self.size
        if inx == self.MaxSize:
            inx -= 1
        self.__cache[inx].key = key
        self.__cache[inx].value = value
        if self.size < self.MaxSize:
            self.size += 1


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(3, 3)
    cache.put(4, 4)
    print(cache.get(3))
    # 3
    print(cache.get(2))
    # None
    cache.put(2, 2)
    print(cache.get(4))
    # None (pre-empted by 2)
    print(cache.get(3))
    # 3

    print(cache.get(2))
    #2
    cache.put(5,5)
    print(cache.get(3))
    #None

    print ("next")
    cache = LRUCache(3)
    cache.put(3, 3)
    cache.put(4, 4)
    cache.put(2,2)
    print(cache.get(2))
    #2
    print(cache.get(2))
    #2
    print(cache.get(4))
    #4
    cache.put(10,10)
    print(cache.get(3))
    #None

