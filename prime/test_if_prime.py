"""program to test if_prime function"""
import unittest
from prime import is_prime

class test_if_prime(unittest.TestCase):
    def test_if_number_is_prime(self):
        self.assertEqual(is_prime(2), 2)
    
    def test_non_prime_number(self):
        self.assertFalse(is_prime(4))

    def test_if_number_is_not_interger(self):
        self.assertEquals(int(2.4))

    def test_if_number_is_less_than_one(self):
        self.assertRaises(ValueError)
        
if __name__ == '__main__':
    unittest.main()