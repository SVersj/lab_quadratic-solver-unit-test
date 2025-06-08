# test_linked_list.py
import unittest
from linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_append_and_get(self):
        lst = DoublyLinkedList()
        lst.append("a")
        lst.append("b")
        self.assertEqual(lst.get(0), "a")
        self.assertEqual(lst.get(1), "b")

    def test_length(self):
        lst = DoublyLinkedList()
        self.assertEqual(lst.length(), 0)
        lst.append("x")
        lst.append("y")
        self.assertEqual(lst.length(), 2)

    def test_out_of_range(self):
        lst = DoublyLinkedList()
        with self.assertRaises(IndexError):
            lst.get(0)

if __name__ == '__main__':
    unittest.main()
