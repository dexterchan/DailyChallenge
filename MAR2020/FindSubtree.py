
#Given 2 binary trees t and s, find if s has an equal subtree in t,
# where the structure and the values are the same. Return True if it exists, otherwise return False.

#Here's some starter code and an example:
#Analysis:
#extract the schema from a tree by BFT
#using recursive function coder
#each node, we code the subtree of the node
#by (value, level, position) position can be root, left, right
#the caller then insert the detail into the list
#each node insert the list into the set
#in return, parent node replicate subtree code list
# and append into its list with level + 1
#function coder
#input : Node, level, set
#output : list of tuple
#Time cost : O(N) Space Cost: O(N)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

class Solution:
    def find_subtree(self, s, t):
        m = set()
        self.__coder(t,0,"root",m)
        m2=set()
        identifier = self.__coder(s, 0, "root", m2)
        hash = self.__hashHelper(identifier)
        return hash in m

    def __coder(self, n:Node, level:int, position:str, m:set):
        if n is None:
            return []
        lSchema = []
        rSchema = []
        if n.left is not None:
            lSchema = self.__coder(n.left, level+1, "left", m)
        if n.right is not None:
            rSchema = self.__coder(n.right, level+1, "right", m)
        mySchema = []
        retSchema = []
        for sch in lSchema:
            mySchema.append((sch[0], sch[1]-level, sch[2]))
            retSchema.append(sch)
        for sch in rSchema:
            mySchema.append((sch[0], sch[1]-level, sch[2]))
            retSchema.append(sch)

        mySchema.append((n.value,0,"root"))
        retSchema.append((n.value,level, position))
        m.add(self.__hashHelper(mySchema))
        return retSchema

    def __hashHelper(self, l):
        h = [ f"{s[0]},{s[1]},{s[2]}" for s in l]
        return ";".join(h)


def find_subtree(s, t):
    # Fill this in.
    solu = Solution()
    return solu.find_subtree(s,t)


if __name__ == "__main__":
    t3 = Node(4, Node(3), Node(2))
    t2 = Node(5, Node(4), Node(-1))
    t = Node(1, t2, t3)

    s = Node(4, Node(3), Node(1))
    print(find_subtree(s, t))

    s = Node(4, Node(3), Node(2))
    """
    Tree t:
        1
       / \
      4   5 
     / \ / \
    3  2 4 -1
    
    Tree s:
      4 
     / \
    3  2 
    """

    print(find_subtree(s, t))
    # True

