from unittest import TestCase
from user import User

class TestUser(TestCase):
    """
    class for testing User class
    """
    def test_Calories(self):
        """
        Test get_Calories method
        """
        u1 = User('Marie', 'woman', 56, 177, 26, 'medium')
        self.assertEqual(u1.get_Calories(), 2132)

    def test_Water(self):
        """
        Test get_Water method
        """
        u1 = User('Marie', 'woman', 56, 177, 26, 'medium')
        self.assertEqual(u1.get_Water(), 1680)

    def test_init(self):
        """
        Test init of class
        """
        u1 = User('Marie', 'woman', 56, 177, 26, 'medium')
        self.assertEqual(u1.name, 'Marie')
        self.assertEqual(u1.gender, 'woman')
        self.assertEqual(u1.age, 26)
        self.assertEqual(u1.weight, 56)
        self.assertEqual(u1.height, 177)
        self.assertEqual(u1.physical, 1.55)



