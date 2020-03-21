#Skill: dynamic programming

#Given a 2d n x m matrix where each cell has a certain amount of change on the floor, your goal is to start from the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1] with the most amount of change. You can only move either left or down.

#Here's some starter code:

#ANalysis
#brutal force, search every possible path.... cost is exponential
# recursively find the possible path...
# the function
# input: from coordinate c1 , next coordinate c2
# output: max change value traveling from c1 to c2
#based on brutal force, apply a cache
# each cache element has two values (right direction value , down direction value)
# first find if cache explored on value....
# if explored, pick up the highest one
# Time cost O(M*N) , space complexity O(M,N)
RIGHT=0
DOWN=1

class Solution():
    def max_change(self, mat):
        X = len(mat)
        Y = len(mat[0])
        cache =[ [ [0,0] for i in range(Y)  ]for j in range(X) ]
        r = self.__runRecursive((0,0), mat, cache)
        return r
    def __runRecursive(self,  next:(int, int), mat, cache) -> int:
        x,y = next
        ch = mat[x][y]
        cachedValue = cache[x][y]

        possiblePath = self.__findPossiblePath(next, mat)
        for p in possiblePath:
            direction  = p[1]
            if cachedValue[direction] == 0:
                newCh = self.__runRecursive( p[0], mat, cache)
                cachedValue[direction] = newCh
        newValue = max(cachedValue[RIGHT], cachedValue[DOWN])
        newValue += ch

        return newValue

    def __findPossiblePath(self, c:(int, int), mat):
        X = len(mat)
        Y = len(mat[0])
        nextPt = []
        #DOWN
        if c[0]+1 < X:
            nextPt.append(  ((c[0]+1,c[1]), DOWN)  )
        if c[1] + 1 < Y:
            nextPt.append( ((c[0], c[1]+1), RIGHT) )
        return nextPt



def max_change(mat):
    # Fill this in.
    solu = Solution()
    return solu.max_change(mat)

mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

if __name__ == "__main__":
    print(max_change(mat))
    # 13