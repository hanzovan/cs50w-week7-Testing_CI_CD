import unittest
from prime import is_prime

class Tests(unittest.TestCase):
    def test_1(self):
        """ Check that 1 is not prime """
        self.assertFalse(is_prime(1))

    def test_2(self):
        """ Check that 2 is prime """
        self.assertTrue(is_prime(2))

    def test_5(self):
        """ Check that 5 is prime """
        self.assertTrue(is_prime(5))

    def test_9(self):
        """ Check that 9 is prime """
        self.assertFalse(is_prime(9))

    def test_17(self):
        """ Check that 17 is prime """
        self.assertTrue(is_prime(17))

    def test_25(self):
        """ Check that 25 is not prime """
        self.assertFalse(is_prime(25))

    def test_37(self):
        """ Check that 37 is prime """
        self.assertTrue(is_prime(37))

    def test_49(self):
        """ Check that 49 is not prime """
        self.assertFalse(is_prime(49))


if __name__=='__main__':
    unittest.main()