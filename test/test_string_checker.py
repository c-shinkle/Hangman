import unittest
from src import string_checker

class StringCheckerTests(unittest.TestCase):
  def test_check_if_letter_is_in_word(self):
    containsLetter = string_checker.check("Christian", "C")
    self.assertEqual(containsLetter, True)

if __name__ == '__main__':
    unittest.main()