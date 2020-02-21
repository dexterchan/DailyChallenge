import unittest
from FEB2020.ReverseaDirectedGraph import reverse_graph, Node as RDNode
from FEB2020.CompareVersionNumbers import Solution as CmpVersionNumber
from FEB2020.SpreadsheetColumnTitle import Solution as SpreadSheetColumnTitle
from FEB2020.GenerateAllIPAddresses import ip_addresses
from FEB2020.Printatreelevel_by_levelwithline_breaks import Node as PNode
from FEB2020.PalindromeIntegers import is_palindrome
from FEB2020.StayingOnChessBoard import is_knight_on_board
from FEB2020.Kaprekar_Constant import num_kaprekar_iterations
from FEB2020.CitySkyline import generate_skyline
from FEB2020.NumberofCousins import Solution as NumberOfCousins, Node as CNode
from FEB2020.Unicode8Validator import utf8_validator
from FEB2020.zigzagBinaryTree import zigzag_order, Node as ZNode

class Feb2020Suite(unittest.TestCase):
    def test_reverse_graph(self):
        a = RDNode('a')
        b = RDNode('b')
        c = RDNode('c')

        a.adjacent += [b, c]
        b.adjacent += [c]

        graph = {
            a.value: a,
            b.value: b,
            c.value: c,
        }
        newGraph = reverse_graph(graph)
        self.assertEqual(0, len(newGraph['a'].adjacent))
        self.assertEqual(['a'], (newGraph['b'].adjacent))
        self.assertEqual(['a','b'], (newGraph['c'].adjacent))

    def test_CmpVersionNumber(self):
        version1 = "01.00000.001"
        version2 = "1"
        self.assertEqual(1, CmpVersionNumber().compareVersion(version1, version2))
        # 1

        version1 = "1.0.0"
        version2 = "1"
        self.assertEqual(0, CmpVersionNumber().compareVersion(version1, version2))

        version1 = "01.00000.001"
        version2 = "1.000001"
        self.assertEqual(-1, CmpVersionNumber().compareVersion(version1, version2))

    def test_SpreadSheetColumnTitle(self):
        self.assertEqual("AY", SpreadSheetColumnTitle().convertToTitle(51))
        input1 = 1
        input2 = 456976
        input3 = 28
        self.assertEqual("A", SpreadSheetColumnTitle().convertToTitle(input1))
        # A
        self.assertEqual("YYYZ", SpreadSheetColumnTitle().convertToTitle(input2))
        # YYYZ
        self.assertEqual("AB", SpreadSheetColumnTitle().convertToTitle(input3))
        # AB
    def test_ip_addresses(self):
        self.assertEqual(['159.255.101.3', '159.255.10.13'].sort(),ip_addresses('1592551013').sort())
        # ['159.255.101.3', '159.255.10.13']

    def test_Printatreelevel_by_levelwithline_breaks(self):
        tree = PNode('a')
        tree.left = PNode('b')
        tree.right = PNode('c')
        tree.left.left = PNode('d')
        tree.left.right = PNode('e')
        tree.right.left = PNode('f')
        tree.right.right = PNode('g')
        self.assertEqual("a\nbc\ndefg", str(tree))

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome(1234322))
        # False

        self.assertTrue(is_palindrome(1234321))
        # True

        self.assertFalse(is_palindrome(12))
        # False

        self.assertTrue(is_palindrome(121))
        # True

    def test_is_knight_on_board(self):
        self.assertAlmostEqual(0.25, is_knight_on_board(0, 0, 1),5)
        self.assertAlmostEqual(1.0, is_knight_on_board(4, 4, 1), 2)
        self.assertAlmostEqual(0.75, is_knight_on_board(4, 4, 10), 2)

    def test_num_kaprekar_iterations(self):
        self.assertEqual(3, num_kaprekar_iterations(123))
        self.assertEqual(7, num_kaprekar_iterations(4560))

    def test_generate_skyline(self):
        self.assertEqual([(2, 3), (4, 5), (7, 3), (9, 0)], generate_skyline([(2, 8, 3), (4, 6, 5)]))

    def test_NumberOfCousins(self):
        #     1
        #    / \
        #   2   3
        #  / \   \
        # 4   6   5
        root = CNode(1)
        root.left = CNode(2)
        root.left.left = CNode(4)
        root.left.right = CNode(6)
        root.right = CNode(3)
        root.right.right = CNode(5)

        self.assertEqual([4,6],NumberOfCousins().list_cousins(root, 5))
        # [4, 6]

        #     1
        #    /  \
        #   2    3
        #  / \   / \
        # 4   6 7   5
        root = CNode(1)
        root.left = CNode(2)
        root.left.left = CNode(4)
        root.left.right = CNode(6)
        root.right = CNode(3)
        root.right.right = CNode(5)
        root.right.left = CNode(7)

        self.assertEqual([4,6],NumberOfCousins().list_cousins(root, 5))

    def test_utf8_validator(self):
        self.assertTrue(utf8_validator([0b11000000, 0b10000000, 0b00000001]))
        # True

        self.assertFalse(utf8_validator([0b11000000, 0b00000000]))
        # False

        self.assertTrue(utf8_validator([0b11000000, 0b10000000]))
        # True
        self.assertTrue(utf8_validator([0b00000000]))
        # True
        self.assertFalse(utf8_validator([0b00000000, 0b10000000]))
        # False

    def test_zigzag_order(self):
        n4 = ZNode(4)
        n5 = ZNode(5)
        n6 = ZNode(6)
        n7 = ZNode(7)
        n2 = ZNode(2, n4, n5)
        n3 = ZNode(3, n6, n7)
        n1 = ZNode(1, n2, n3)

        self.assertEqual([1, 3, 2, 4, 5, 6, 7], zigzag_order(n1))
        # [1, 3, 2, 4, 5, 6, 7]

        n15 = ZNode(15)
        n14 = ZNode(14)
        n13 = ZNode(13)
        n12 = ZNode(12)
        n11 = ZNode(11)
        n10 = ZNode(10)
        n9 = ZNode(9)
        n8 = ZNode(8)
        n4 = ZNode(4, n8, n9)
        n5 = ZNode(5, n10, n11)
        n6 = ZNode(6, n12, n13)
        n7 = ZNode(7, n14, n15)
        n2 = ZNode(2, n4, n5)
        n3 = ZNode(3, n6, n7)
        n1 = ZNode(1, n2, n3)

        self.assertEqual([1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8], zigzag_order(n1))
        # [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8]
