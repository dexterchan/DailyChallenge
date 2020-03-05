

#A maze is a matrix where each cell can either be a 0 or 1. A 0 represents that the cell is empty,
# and a 1 represents a wall that cannot be walked through. You can also only travel either right or down.

#Given a nxm matrix, find the number of ways someone can go from the top left corner to the bottom right corner.
# You can assume the two corners will always be 0.

#Example:
#Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# 0 1 0
# 0 0 1
# 0 0 0
#Output: 2
#The two paths that can only be taken in the above example are: down -> right -> down -> right, and down -> down -> right -> right.

#Here's some starter code:
#Analysis
#By Brutal force, it will cost exponental of time to traverse the whole maze
#There is many overlap calculation inside the brutal force
#We would use memory to "remember" the possible subpath to reduce time complexity to O(N^2)
#while the space cost remains as O(N^2)

#Trick
#navigate a node, follow the rule for possible path
# recursively run the same function
# input current position, maze
# output list of possible path
# function collects listed result from subcall
# we also put the subpath into memory
from collections import deque
import copy

class Mazerunner:

    def paths_through_maze(self, maze):
        Y = len(maze[0])
        X = len(maze)
        Memory = [ [None for y in range(Y)]  for x in range(X)]

        paths = self.__recursiveHelper(0, 0, maze, Memory)

        return len(paths)

    def __recursiveHelper(self, x, y, maze, Memory):
        pathLst = None

        if self.__checkDestination(x, y, maze):
            d = deque()
            d.append(((x,y), "final"))
            return [d]

        pathLst = self.__memoryGetHelper(x, y, Memory)

        if pathLst is not None:
            return pathLst
        else:
            pathLst = []

        directions = self.__findpossibledirection(x, y, maze)
        for direction in directions:
            next, step = direction
            nx, ny = next
            subpaths = self.__recursiveHelper(nx, ny, maze, Memory)
            for s in subpaths:
                s.appendleft(((nx,ny),step))
                pathLst.append(s)
        self.__memoryInsertHelper(x, y, pathLst, Memory)

        return pathLst

    def __memoryInsertHelper(self, nx, ny, pathLst, Memory):
        if Memory[nx][ny] is None:
            Memory[nx][ny] = copy.deepcopy(pathLst)
    def __memoryGetHelper(self,nx, ny, Memory):
        if Memory[nx][ny] is not None:
            return copy.deepcopy(Memory[nx][ny])
        else:
            return None


    def __checkDestination(self, x, y, maze):
        Y = len(maze[0])
        X = len(maze)
        if x == X-1 and y == Y-1:
            return True
        else:
            return False

    def __findpossibledirection(self, x, y, maze):
        Y = len(maze[0])
        X = len(maze)
        res = []
        #check down
        if x+1 < X and maze[x+1][y] != 1:
            res.append(((x+1,y), "down"))
        #check right
        if y+1 < Y and maze[x][y+1] != 1:
            res.append(((x,y+1), "right"))
        return res




def paths_through_maze(maze):
    # Fill this in.
    solu = Mazerunner()
    return solu.paths_through_maze(maze)


if __name__ == "__main__":
    print(paths_through_maze([[0, 0, 0],
                              [0, 0, 1],
                              [0, 0, 0]]))
    # 3

    print(paths_through_maze([[0, 1, 0],
                              [0, 0, 1],
                              [0, 0, 0]]))
    # 2