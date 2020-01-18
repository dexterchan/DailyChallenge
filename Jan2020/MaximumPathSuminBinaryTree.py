# Tree traversal, Dynamic programming
# Difficulty: Medium
#You are given the root of a binary tree. Find the path between 2 nodes that
# maximizes the sum of all the nodes in the path, and return the sum.
# The path does not necessarily need to go through the root.

#Analysis
#It is a simplified path search problem: only one path between 2 nodes
#Get all the path distance between nodes and fill in into matrix:
# 1) Traverse the tree element by element by depth first search
#    Start from Node A, traverse to left child B:
#    Put Node A in position lst, also register Node A to map : M[node A] = index of position lst
#    traverse to child B, store path A-B: (A,B) into pathList, register node B in position lst, register Node B to M[nodeB] = index of position lst
#    similar for right child using depth first search until finish
# 2) setup 2D array D: size of position lst X size of position lst
#    initialize all value = MAX negative value
#    initialize D[k,k] = node value of position[k]
#    initialize path list:
#        for each path, calculate distance e.g. A,B = node value A+ node value B
#        save the dist(A,B) into D[ M[node A], M[node B] ] = dist(A,B)
#        save the dist(B,A) into D[ M[node B], M[node A] ] = dist(B,A)
#        Put path(A,B) in the pathQueue
#    process path Queue
#         1)popleft A,B = path
#         2)explore from A, all pt C dist AC != MAX negative value, if D[M[nodeC], M[node B]] = MAX negative value,
#         then update D[M[node C], M[node B] ] = dist(A,B) + dist(A,C)-A.val
#         then update D[M[node B], M[node C] ] = dist(A,B) + dist(A,C)-A.val
#         save dist(C,B) in path Queue
#         3) loop pathQueue
# 3) Find the max value in D
# Time complexity O(N^2), space complexity O(N^2)
from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
NOTFOUND = -(1<<31)
class Solution:
    def maxPathSum(self, root):
        pathList = []
        positionLst = []
        M = {}
        self.__DFS(root, pathList, positionLst, M)

        D, pathQ = self.__setupMap(pathList, positionLst, M)
        #print(D)
        D = self.__processPathQueue(pathQ, D,positionLst, M)

        #print (D)
        p = list(map (lambda x: x.val,positionLst))
        #print (p)
        return max([max(x) for x in D])

    def __processPathQueue(self, pathQ, D,positionLst, M):

        while len(pathQ)>0:
            A, B = pathQ.popleft()
            #explore A
            inxA = M[A]
            inxB = M[B]
            possiblePt = D[inxA]
            for j in range(len(possiblePt)):
                if j == inxA:
                    continue
                if j == inxB:
                    continue
                if possiblePt[j] != NOTFOUND:
                    #find point C
                    C=positionLst[j]
                    if D[j][inxB] == NOTFOUND:
                        newDist = D[inxA][inxB] + possiblePt[j] - A.val
                        D[j][inxB] = newDist
                        D[inxB][j] = newDist
                        pathQ.append((positionLst[j], B))

        return D
    def __setupMap(self, pathList, positionLst, M):
        l = len(positionLst)
        pathQ = deque()
        D = [[NOTFOUND for x in range(l)] for y in range(l)]
        for i in range(l):
            D[i][i] = positionLst[i].val

        for path in pathList:
            pathQ.append(path)
            A,B = path
            iA = M[A]
            iB = M[B]
            dist = A.val + B.val
            D[iA][iB] = dist
            D[iB][iA] = dist


        return D, pathQ
    def __DFS(self, root, pathList, positionLst, M):
        if root is None:
            return
        M[root] = len(positionLst)
        positionLst.append(root)
        if root.left is not None:
            pathList.append((root, root.left))
            self.__DFS(root.left, pathList, positionLst, M)
        if root.right is not None:
            pathList.append((root, root.right))
            self.__DFS(root.right, pathList, positionLst, M)

def maxPathSum(root):
    # Fill this in.
    solu = Solution()
    return solu.maxPathSum(root)
# (* denotes the max path)

if __name__ == "__main__":
    #       *10
    #       /  \
    #     *2   *10
    #     / \     \
    #   20  *100    25

    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(100)
    root.right.right = Node(25)

    print(maxPathSum(root))
    # 147

    #       *10
    #       /  \
    #     *2   *10
    #     / \     \
    #   *20  1    -25
    #             /  \
    #            3    4
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    print (maxPathSum(root))
    # 42


    #       *10
    #       /  \
    #     -2   *10
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(10)
    print(maxPathSum(root))
    # 20


