#Skill : dynamic programming

#A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k,
# we want to figure out after k random moves by a knight,
# the probability that the knight will still be on the chessboard.
# Once the knight leaves the board it cannot move again and will be considered off the board.

#Here's some starter code:
# Analysis
#Probability of x,y,k:
#  path x,y,k still in board/all possible path x,y,k

#  path x,y, k =   path (filter on board ( all possible of next move (x,y) ) , k-1)
#  possible path = all possible of next move (x,y)+ all possible of next move ( path (filter on board ( all possible of next move (x,y) ) , k-1) )
# Brutal force
# Time complexity O((N*N)^k) Space complexity O(1)
# With cache
# Time complexity O(N*N) Space complexity O(N*N*k)

from typing import List, Tuple
class Solution():
    def is_knight_on_board(self, x, y, k, cache={}):
        f, p = self.__path(x, y, k, cache)
        return f/p


    def __path(self, x,y, k, cache)->List[Tuple]:
        if k == 0:
            return 0,0

        if (x,y,k) in cache:
            return cache[(x,y,k)]
        possibleMove = self.__allPossibleMove(x, y)
        filteredMove = self.__filterOnBoard(possibleMove)

        pMove = len(possibleMove)
        fMove = len(filteredMove)
        for (nx, ny) in filteredMove:
            f, p = self.__path(nx, ny, k-1, cache)
            fMove += f
            pMove += p
        cache[(x, y, k)] = (fMove, pMove)

        return fMove, pMove

    def __allPossibleMove(self, x,y):

        possible = []
        possible.append((x+1, y+2))
        possible.append((x+2, y+1))
        possible.append((x+2, y-1))
        possible.append((x+1, y-2))
        possible.append((x-1, y-2))
        possible.append((x-2, y-1))
        possible.append((x-2, y+1))
        possible.append((x-1, y+2))
        return possible

    def __filterOnBoard(self, possiblePt:List[Tuple]) -> List[Tuple]:
        filteredPt = []
        for x,y in possiblePt:
            if (x>=0 and x<8) and (y>=0 and y<8):
                filteredPt.append((x,y))
        return filteredPt




def is_knight_on_board(x, y, k, cache={}):
    # Fill this in.
    solu = Solution()
    return solu.is_knight_on_board(x,y,k,cache)




if __name__=="__main__":
    print (is_knight_on_board(0, 0, 1))
    # 0.25
    print(is_knight_on_board(0, 0, 10))
    # 0.25

    print(is_knight_on_board(3, 3, 1))
    # 1.0