import unittest
import palin_int

class TestTest(unittest.TestCase):

	def test_palin(self):
            self.assertEqual(palin_int.Solution.is_palindrome(self, 121), True)
            self.assertEqual(palin_int.Solution.is_palindrome(self, -121), False)
            self.assertEqual(palin_int.Solution.is_palindrome(self, 1231), False)
            self.assertEqual(palin_int.Solution.is_palindrome(self, 0), True)

if __name__ == '__main__':
    unittest.main()		