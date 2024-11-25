import unittest
from binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        """
        Настройка дерева для тестов.
        """
        self.bst = BinarySearchTree()
        for key in [10, 5, 15, 3, 7, 12, 18]:
            self.bst.insert(key)

    def test_insert_and_search(self):
        """
        Тестирование вставки и поиска элементов.
        """
        self.assertTrue(self.bst.search(10))
        self.assertTrue(self.bst.search(7))
        self.assertFalse(self.bst.search(20))

    def test_inorder_traversal(self):
        """
        Тестирование симметричного обхода.
        """
        self.assertEqual(self.bst.inorder_traversal(), [3, 5, 7, 10, 12, 15, 18])

    def test_delete_leaf(self):
        """
        Тестирование удаления листа.
        """
        self.bst.delete(3)
        self.assertFalse(self.bst.search(3))
        self.assertEqual(self.bst.inorder_traversal(), [5, 7, 10, 12, 15, 18])

    def test_delete_node_with_one_child(self):
        """
        Тестирование удаления узла с одним потомком.
        """
        self.bst.delete(12)
        self.assertFalse(self.bst.search(12))
        self.assertEqual(self.bst.inorder_traversal(), [3, 5, 7, 10, 15, 18])

    def test_delete_node_with_two_children(self):
        """
        Тестирование удаления узла с двумя потомками.
        """
        self.bst.delete(10)
        self.assertFalse(self.bst.search(10))
        self.assertEqual(self.bst.inorder_traversal(), [3, 5, 7, 12, 15, 18])

if __name__ == "__main__":
    unittest.main()
