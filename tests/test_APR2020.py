import unittest
from APR2020.RemoveOneLayerofParenthesis import remove_outermost_parenthesis


class Apr2020Suite(unittest.TestCase):
    def test_remove_outermost_parenthesis(self):
        self.assertEqual("()()",remove_outermost_parenthesis('(()())'))
        # ()()

        self.assertEqual("()",remove_outermost_parenthesis('(())()'))
        # ()

        self.assertEqual("",remove_outermost_parenthesis('()()()'))
        # ' '