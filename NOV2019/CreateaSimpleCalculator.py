#Skill recursive, array
#Given a mathematical expression with just
# single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.

#Example:
#Input: - ( 3 + ( 2 - 1 ) )
#Output: -4



class Calculator:


    def calculateExpression(self, expression):
        ret = self.__calculateRecursive(expression)

        return ret[0]

    def __calculateRecursive(self, exp):

        opt = None
        result = None
        i = 0

        if exp[0] == "-":
            i = -1
            result = 0

        while(i< len(exp)-2):
            opt = exp[i+1]
            if result is None:
                result = int(exp[i])
            if opt == "+":
                operand, nextPos =  self.__operandHelper(exp[i+2:])
                result = self.__add(result, operand)
                i = i + nextPos
                continue
            elif opt == "-":
                operand, nextPos = self.__operandHelper(exp[i+2:])
                result = self.__substract(result, operand)
                i = i + nextPos
                continue
            elif opt == ")":
                return (result, i+2)
                continue
        return (result, len(exp))

    def __operandHelper(self, exp):
        operand = exp[0]
        if exp[0]=="(" :
            result, nextPos = self.__calculateRecursive(exp[1:])
            return result, nextPos+2
        else:
            return int(exp[0]), 2


    def __add (self, num1 , num2):
        return num1 + num2
    def __substract(self, num1, num2):
        return num1 - num2




def eval(expression):
    exp = expression.replace(" ","")
    calc = Calculator()
    return calc.calculateExpression(exp)


if __name__ == '__main__':
    print(eval('2+(3+5)'))
    print (eval ('2+(3+5)+1') )

    print(eval('2+(3+5+(2-3))+1'))
    print(eval('-2+3'))
    print(eval('-(2+3)'))
    print ( eval('- (3 + ( 2 - 1 ) )') )
# -4