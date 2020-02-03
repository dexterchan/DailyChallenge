import unittest
from FEB2020.ReverseaDirectedGraph import reverse_graph, Node as RDNode
from FEB2020.CompareVersionNumbers import Solution as CmpVersionNumber
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
