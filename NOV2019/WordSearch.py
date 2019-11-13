#skills: array traversal
#You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix.
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

#Example:

#[['F', 'A', 'C', 'I'],
# ['O', 'B', 'Q', 'P'],
# ['A', 'N', 'O', 'B'],
# ['M', 'A', 'S', 'S']]

#Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.
class Solution:
    def findWord(self, matrix, word):
        numrow = len(matrix)
        numcol = len(matrix[0])
        wordlen = len(word)
        for i in range(0, numrow):
            for j in range(0, numcol):
                chkL2R = self.__checkL2R(i, j, matrix, word, numrow, numcol)
                chkU2D = self.__checkU2D(i, j, matrix, word, numrow, numcol)
                if(chkL2R or chkU2D):
                    return True
        return False

    def __checkL2R(self, x, y, matrix, word, numrow, numcol):
        #check if reach boundary
        element = []
        if(y+len(word)>numcol):
            return False
        for i in range(len(word)):
            element.append(matrix[x][y+i])
        strRef = "".join(element)
        if(strRef == word):
            return True
        else:
            return False

    def __checkU2D(self, x, y, matrix, word, numrow, numcol):
        # check if reach boundary
        element = []
        if (x + len(word) > numrow):
            return False
        for i in range(len(word)):
            element.append(matrix[x+i][y])
        strRef = "".join(element)
        if (strRef == word):
            return True
        else:
            return False


def word_search(matrix, word):
    solu = Solution()
    return solu.findWord(matrix, word)



if __name__ == "__main__":
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]
    print (word_search(matrix, 'FOAM') )
    # True
    print(word_search(matrix, 'BSl'))