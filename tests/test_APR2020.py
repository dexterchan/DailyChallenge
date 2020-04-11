import unittest
from APR2020.RemoveOneLayerofParenthesis import remove_outermost_parenthesis
from APR2020.IndexofLargerNextNumber import larger_number


class Apr2020Suite(unittest.TestCase):
    def test_remove_outermost_parenthesis(self):
        self.assertEqual("()()",remove_outermost_parenthesis('(()())'))
        # ()()

        self.assertEqual("()",remove_outermost_parenthesis('(())()'))
        # ()

        self.assertEqual("",remove_outermost_parenthesis('()()()'))
        # ' '

    def test_larger_number(self):
        self.assertEqual([2, 2, 3, 4, -1, -1], larger_number([3, 2, 5, 6, 9, 8]))