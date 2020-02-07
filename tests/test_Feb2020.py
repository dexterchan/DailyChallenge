import unittest
from FEB2020.ReverseaDirectedGraph import reverse_graph, Node as RDNode
from FEB2020.CompareVersionNumbers import Solution as CmpVersionNumber
from FEB2020.SpreadsheetColumnTitle import Solution as SpreadSheetColumnTitle
from FEB2020.GenerateAllIPAddresses import ip_addresses
from FEB2020.Printatreelevel_by_levelwithline_breaks import Node as PNode
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