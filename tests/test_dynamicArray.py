from unittest import TestCase
from calorie_tracker.ADT import DynamicArray

class TestDynamicArray(TestCase):
    """
    class for testing ADT
    """
    def test_lenght(self):
        """
        Tests the lenghth
        """
        D = DynamicArray()
        D.add('orange')
        D.add('appple')
        self.assertEqual(len(D), 2)

    def test_init(self):
        """
        Tests init of class
        """
        D = DynamicArray()
        D.add('pasta')
        self.assertEqual(D._size, 1)
        self.assertEqual(D._capacity, 1)
        D.add('pizza')
        self.assertEqual(D._size, 2)
        self.assertEqual(D._capacity, 2)


    def test_delete(self):
        """
        Test delete method
        """
        D = DynamicArray()
        D.add('fish')
        D.add('meat')
        self.assertEqual(D.delete_item('g'), "value not found")
        self.assertIsNone(D.delete_item('fish'), None)

    def test_str(self):
        """
        Test str method
        """
        D = DynamicArray()
        D.add('apple')
        self.assertEqual(str(D), 'apple ')

    def test_add(self):
        """
        Test add method
        """
        D = DynamicArray()
        self.assertEqual(D.add('d'), None)


    def test_getitem(self):
        """
        Test getitem method
        """
        D = DynamicArray()
        D.add(56)
        self.assertEqual(D[0], 56)

    def test_chagesize(self):
        """
        Test change size method
        """
        D = DynamicArray()
        D.add(12)
        self.assertEqual(D._changesize(2), None)
        self.assertEqual(D._capacity, 2)



