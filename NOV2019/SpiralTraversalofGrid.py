
#You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

#Example:

#grid = [[1,  2,  3,  4,  5],
#        [6,  7,  8,  9,  10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]]

#The clockwise spiral traversal of this array is:

#1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

DONE = -1
class Solution:
    def spiritalMatrix(self, M):
        nrow = len(M)
        ncol = len(M[0])
        result = []
        direction = 0
        lastLen = 0
        start = True
        c = 0
        r = 0
        if (M[r][c] != DONE):
            result.append(M[r][c])
            M[r][c] = DONE
        while start or ( len(result) - lastLen > 0 ) :
            start = False
            lastLen = len (result)
            if direction == 0:
                c, r = self.__right(M, c, r, ncol, nrow, result )
            elif direction == 1:
                c, r = self.__down(M, c, r, ncol, nrow, result)
            elif direction == 2:
                c, r = self.__left(M, c, r, ncol, nrow, result)
            elif direction == 3:
                c, r = self.__up (M, c, r, ncol, nrow, result)
            direction = direction + 1
            direction = direction % 4
        return result


    def __right(self, M, c, r , ncol, nrow, result):
        while c + 1 < ncol and M[r][c + 1] != DONE:
            result.append(M[r][c + 1])
            M[r][c+1] = DONE
            c = c + 1
        return (c, r)
    def __down (self, M, c, r , ncol, nrow, result):

        while r + 1 < nrow and M[r + 1][c] != DONE:
            result.append(M[r + 1][c])
            M[r + 1][c] = DONE
            r = r + 1
        return (c, r)
    def __left (self, M, c, r , ncol, nrow, result):

        while c - 1 >=0 and M[r][c - 1] != DONE:
            result.append(M[r][c - 1])
            M[r][c - 1] = DONE
            c = c - 1
        return (c, r)
    def __up (self, M, c, r , ncol, nrow, result):

        while r - 1 >= 0 and M[r - 1][c] != DONE:
            result.append(M[r - 1][c])
            M[r - 1][c] = DONE
            r = r - 1
        return (c, r)

def matrix_spiral_print(M):
    solu = Solution()
    l = solu.spiritalMatrix(M)
    #print(l)
    return l

if __name__ == "__main__":
    grid = [[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

    l = matrix_spiral_print(grid)
    print (l)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12