import unittest
import lca

class TestLca(unittest.TestCase):

    def test_node4_5(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 4, 5).key, 2)

    def test_node6_2(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 6, 2).key, 1)

    def test_node_none(self):
        self.assertEqual(lca.lowestCommonAncestor(None, 4, 5), None)

    def test_node1_5(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 1, 5).key, 1)

    def test_node_same(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 1, 1).key, 1)

    def test_node2_3(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 2, 3).key, 1)

    def test_node6_7(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 6, 7).key, 3)

    def test_node_fake(self):
        self.assertEqual(lca.lowestCommonAncestor(lca.tree, 8, 8), None)


if __name__ == '__main__':
    unittest.main()