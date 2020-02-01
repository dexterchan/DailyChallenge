
#Design a Tic-Tac-Toe game played between two players on an n x n grid.
#A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid.
# A player who succeeds in placing n of their marks in a horizontal, diagonal, or vertical row wins the game.
# Once a winning condition is reached, the game ends and no more moves are allowed.
# Below is an example game which ends in a winning condition:

#Given n = 3, assume that player 1 is "X" and player 2 is "O"
#board = TicTacToe(3);

#board.move(0, 0, 1); -> Returns 0 (no one wins)
#|X| | |
#| | | |    // Player 1 makes a move at (0, 0).
#| | | |

#board.move(0, 2, 2); -> Returns 0 (no one wins)
#|X| |O|
#| | | |    // Player 2 makes a move at (0, 2).
#| | | |

#board.move(2, 2, 1); -> Returns 0 (no one wins)
#|X| |O|
#| | | |    // Player 1 makes a move at (2, 2).
#| | |X|

#board.move(1, 1, 2); -> Returns 0 (no one wins)
#|X| |O|
#| |O| |    // Player 2 makes a move at (1, 1).
#| | |X|

#board.move(2, 0, 1); -> Returns 0 (no one wins)
#|X| |O|
#| |O| |    // Player 1 makes a move at (2, 0).
#|X| |X|

#board.move(1, 0, 2); -> Returns 0 (no one wins)
#|X| |O|
#|O|O| |    // Player 2 makes a move at (1, 0).
#|X| |X|

#board.move(2, 1, 1); -> Returns 1 (player 1 wins)
#|X| |O|
#|O|O| |    // Player 1 makes a move at (2, 1).
#|X|X|X|

#Here's a starting point:

class InvalidMoveException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
class FinishException (Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
class TicTacToe():
    def __init__(self, n):
        # Fill this in.
        self.M = [ [' ' for i in range(n)] for i in range(n)]
        self.dim = n
        self.lastPlayer= None
        self.finish = False

    def move(self, row, col, player):
        # Fill this in.
        try:
            if not self.checkValid(row, col, player):
                raise InvalidMoveException("Invalid move")
        except FinishException as err:
            print(err)
            return str(self)

        if self.checkWin(row, col, player):
            print("Winner is %d"%(player))
            self.finish = True
        print (str(self))
        return str(self)

    def checkValid(self, row, col, player):
        if self.finish:
            raise FinishException("Game finished")
        if self.M[row][col] != " ":
            return False
        if player == self.lastPlayer:
            return False
        return True

    def checkWin(self, row, col, player):
        self.M[row][col] = player
        cnt = 0
        #Check horizonal
        for j in range(self.dim):
            if self.M[row][j] == player:
                cnt += 1

        if cnt == self.dim:
            return True
        cnt = 0
        for i in range(self.dim):
            if self.M[i][col] == player:
                cnt += 1

        if cnt == self.dim:
            return True
        cnt = 0
        for i in range(self.dim):
            if self.M[i][i] == player:
                cnt += 1

        if cnt == self.dim:
            return True
        cnt = 0
        for i in range(self.dim):
            if self.M[i][self.dim-i-1] == player:
                cnt += 1

        if cnt == self.dim:
            return True
        cnt = 0
        return False

    def __str__(self):
        s = []
        for i in range(self.dim):
            s.append("|")
            for j in range(self.dim):
                s.append (str(self.M[i][j]))
                s.append("|")
            s.append("\n")
        return "".join(s)



if __name__ == "__main__":
    board = TicTacToe(3)
    board.move(0, 0, 1)
    board.move(0, 2, 2)
    board.move(2, 2, 1)
    board.move(1, 1, 2)
    board.move(2, 0, 1)
    board.move(1, 0, 2)
    print(board.move(2, 1, 1))